from pathlib import Path
import csv
import json

from typesafe_sdk import Score, TypeSafeClient


BASE_DIR = Path(__file__).parent
INPUT_DIR = BASE_DIR / "inputs"
RULES_FILE = BASE_DIR / "ticket_scoring_rules.json"
RESULTS_DIR = BASE_DIR / "results"
RESULTS_FILE = RESULTS_DIR / "ticket_scoring_results.csv"


def load_scoring_rules():
    """Load reusable Jev scoring questions."""
    with RULES_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)["questions"]


def load_tickets():
    """Load all Markdown tickets from the inputs directory."""
    return sorted(INPUT_DIR.glob("*.md"))


def main():
    questions_config = load_scoring_rules()
    ticket_files = load_tickets()

    if not ticket_files:
        raise RuntimeError(f"No .md files found in {INPUT_DIR}")

    client = TypeSafeClient()

    results = []

    for ticket_file in ticket_files:
        print(f"Scoring: {ticket_file.name}")

        # The entire Markdown ticket becomes Jev's state.
        ticket = ticket_file.read_text(encoding="utf-8")

        # Convert JSON question definitions into Jev SDK primitives.
        questions = {
            name: Score(
                instructions=config["instructions"],
                criteria=config["criteria"],
            )
            for name, config in questions_config.items()
        }

        response = client.system_one(
            state=ticket,
            questions=questions,
        )

        answers = response.answers

        results.append(
            {
                "ticket_id": ticket_file.stem,
                "effort": answers["effort"].score,
                "effort_confidence": answers["effort"].confidence,
                "complexity": answers["complexity"].score,
                "complexity_confidence": answers["complexity"].confidence,
                "uncertainty": answers["uncertainty"].score,
                "uncertainty_confidence": answers["uncertainty"].confidence,
            }
        )

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    with RESULTS_FILE.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as f:
        writer = csv.DictWriter(
            f,
            fieldnames=results[0].keys(),
        )

        writer.writeheader()
        writer.writerows(results)

    print(f"\nResults written to: {RESULTS_FILE}")


if __name__ == "__main__":
    main()