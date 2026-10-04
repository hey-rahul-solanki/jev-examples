# Agile T-Shirt Sizing & Effort Estimation with Jev

Automating **Agile T-shirt sizing** of tickets using [Jev](https://typesafe.ai/jev), a lightweight decision-oriented approach based on structured questions and bounded outputs.

The goal is to explore whether Jev can be used for fast, consistent **effort and complexity estimation** before escalating uncertain cases to a larger LLM.

---

## Use Case

### Agile T-Shirt Sizing & Effort Estimation

In Agile teams, tickets are often assigned a T-shirt size based on factors such as:

- Estimated effort
- Technical complexity
- Uncertainty
- Dependencies
- Number of systems/components affected
- Overall scope of the work

The typical output is:

`XS → S → M → L → XL`

Today, this can require a human to read the ticket, assess its complexity, and assign a size.

This experiment explores whether Jev can automate this initial assessment.

---

## Why Jev?

T-shirt sizing is a good fit for a decision-oriented model because the output space is small and well-defined.

Instead of asking an LLM to generate an explanation and then extract a size, we can define a constrained decision:

```text
State + Questions + type: Choice / Score / Noul → Output
```

For example:

```text
Ticket
  ↓
Jev
  ├── Effort
  ├── Complexity
  ├── Uncertainty
  ↓
T-Shirt Size
```

The objective is not to replace human estimation immediately, but to investigate whether Jev can provide a **fast and consistent first-pass estimation**.

---

## Inputs

The `inputs/` directory contains ticket information used by the experiment.

Example:

```text
inputs/
├── ticket-001.json
├── ticket-002.json
└── ticket-003.json
```

Each ticket can contain information such as:

- Ticket ID
- Title
- Description
- Acceptance criteria
- Technical context
- Dependencies
- Other information available in the ticket

The exact state provided to Jev can be refined as the experiment progresses.

---

## Jev Decision

The initial experiment can evaluate several dimensions of a ticket:

### Effort

How much work is expected to complete the ticket?

### Complexity

How technically complex is the work?

### Uncertainty

How much ambiguity or unknown work exists?

These inputs can then be used to determine the final T-shirt size.

Example:

```text
Effort       → 3
Complexity   → 2
Uncertainty  → 1

T-Shirt Size → S
Confidence   → 91%
```

> **Confidence** is used in the results for readability. Jev's underlying output may be represented as a probability; here it is interpreted as the model's confidence in the selected decision.

---

## Project Structure

```text
agile-tshirt-sizing/
│
├── inputs/
│   ├── ticket-001.json
│   ├── ticket-002.json
│   └── ticket-003.json
│
├── results/
│   └── jev_t_shirt_sizing_results.csv
│
└── jev_t_shirt_sizing_automation.py
```

### `inputs/`

Contains the ticket information used as input to Jev.

### `jev_t_shirt_sizing_automation.py`

Runs the Jev-based sizing process and produces structured results.

### `results/`

Contains human-readable experiment results.

CSV is used initially because it makes the results easy to inspect, filter, compare, and analyze.

---

## Results

The results CSV can contain fields such as:

| Field | Description |
|---|---|
| `ticket_id` | Ticket identifier |
| `title` | Ticket title/summary |
| `effort` | Estimated effort |
| `complexity` | Estimated complexity |
| `uncertainty` | Estimated uncertainty |
| `tshirt_size` | Final T-shirt size |
| `confidence` | Confidence in the selected size |

Example:

```text
ticket_id,title,effort,complexity,uncertainty,tshirt_size,confidence
TKT-001,