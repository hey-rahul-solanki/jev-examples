from pathlib import Path
import csv
import json

from typesafe_sdk import Choice, TypeSafeClient


BASE_DIR = Path(__file__).parent

INPUT_DIR = BASE_DIR / "inputs"
RULES_FILE = BASE_DIR / "sizing_rules.json"
SCORING_RESULTS_FILE = BASE_DIR / "results" / "ticket_scoring_results.csv"
FINAL_RESULTS_FILE = BASE_DIR / "results" / "final_ticket_sizing.csv"


def load_sizing_rules():
    """Load the T-shirt sizing Choice configuration."""
    with RULES_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)["question"]


def extract_ticket_title(ticket_file):
    """Extract the first Markdown heading as the ticket title."""
    for line in ticket_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()

        if line.startswith("#"):
            return line.lstrip("#").strip()

    return ticket_file.stem


def load_scoring_results():
    """Load Stage 1 scoring results from CSV."""
    with SCORING_RESULTS_FILE.open("r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def build_state(row):
    """Build the state that Jev will use for T-shirt sizing."""
    return f"""
Ticket ID: {row["ticket_id"]}

Effort score: {row["effort"]}/5
Effort confidence: {row["effort_confidence"]}

Complexity score: {row["complexity"]}/5
Complexity confidence: {row["complexity_confidence"]}

Uncertainty score: {row["uncertainty"]}/5
Uncertainty confidence: {row["uncertainty_confidence"]}
""".strip()


def main():
    sizing_config = load_sizing_rules()
    scoring_results = load_scoring_results()

    if not scoring_results:
        raise RuntimeError(
            f"No scoring results found in {SCORING_RESULTS_FILE}"
        )

    client = TypeSafeClient()

    final_results = []

    for row in scoring_results:
        ticket_id = row["ticket_id"]

        ticket_file = INPUT_DIR / f"{ticket_id}.md"

        if not ticket_file.exists():
            raise FileNotFoundError(
                f"Ticket file not found: {ticket_file}"
            )

        ticket_title = extract_ticket_title(ticket_file)

        state = build_state(row)

        question = Choice(
            instructions=sizing_config["instructions"],
            criteria=sizing_config["criteria"],
        )

        response = client.system_one(
            state=state,
            questions={
                "size": question
            },
        )

        answer = response.answers["size"]

        final_results.append({
            "ticket_id": ticket_id,
            "ticket_title": ticket_title,
            "effort": row["effort"],
            "complexity": row["complexity"],
            "uncertainty": row["uncertainty"],
            "size": answer.choice,
            "size_confidence": answer.confidence,
        })

        print(
            f"{ticket_id}: "
            f"{answer.choice} "
            f"(confidence={answer.confidence:.2f})"
        )

    FINAL_RESULTS_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with FINAL_RESULTS_FILE.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as f:
        fieldnames = [
            "ticket_id",
            "ticket_title",
            "effort",
            "complexity",
            "uncertainty",
            "size",
            "size_confidence",
        ]

        writer = csv.DictWriter(
            f,
            fieldnames=fieldnames,
        )

        writer.writeheader()
        writer.writerows(final_results)

    print(
        f"\nFinal results written to: "
        f"{FINAL_RESULTS_FILE}"
    )


if __name__ == "__main__":
    main()