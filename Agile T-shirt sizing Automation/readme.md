# Agile T-Shirt Sizing & Effort Estimation with Jev

Automating **Agile T-shirt sizing** of tickets using [Jev](https://typesafe.ai/jev), a **System one model** designed for fast, intuitive, structured decision-making.

The goal is to explore whether Jev can be used for fast, consistent **effort and complexity estimation** before escalating uncertain cases to a larger LLM.

---

## What is Jev?

Jev is a **System one model** designed for fast, intuitive decision-making.

Unlike generative LLMs that generate text token-by-token, Jev works with a small set of structured primitives and returns bounded outputs. This allows it to behave more like a **line of code** for certain decisions: provide state and structured questions, and get a structured result.

### Key characteristics

- **System one thinking** — designed for fast, intuitive decisions rather than lengthy reasoning or text generation.
- **Bounded outputs** — Jev works within the choices and score ranges defined by the developer. It cannot generate an option or score outside those defined boundaries.
- **Three primitives only:**
  - **Choice** — select from a predefined set of options.
  - **Noul** — return a probability between 0 and 1. *Noul is essentially a new term for a probability-style output.*
  - **Score** — evaluate something against a defined scoring range.
- **No open-ended text generation** — Jev returns structured outputs rather than generating another piece of text.
- **Confidence-aware** — probability outputs can be used as a confidence signal. Low-confidence results can be escalated to another, more capable model.
- **Parallel structured questions** — multiple structured questions can be answered within a single request, replacing sequential generation with parallel generation where applicable.
- **Low latency** — Jev claims response times of **<500 ms** for its primitives. This experiment will validate the practical end-to-end latency for ticket sizing.
- **Consistency** — Noul outputs are intended to provide consistent probability-style assessments. This experiment will evaluate how well that holds against real ticket data.

In simple terms:

```text
State + Questions + type: Choice / Score / Noul → Output
```

For example:

```text
State:
  Ticket information

Questions:
  complexity → Score
  effort     → Score
  uncertainty → Score
  size       → Choice

Output:
  complexity → 3
  effort     → 4
  uncertainty → 2
  size        → M
```

---

# Use Case

## Agile T-Shirt Sizing & Effort Estimation

In Agile teams, tickets are often assigned a T-shirt size based on factors such as:

- Estimated effort
- Technical complexity
- Uncertainty
- Dependencies
- Number of systems/components affected
- Overall scope of the work

The typical output is:

```text
XS → S → M → L → XL
```

Today, this usually requires a human to read the ticket, assess its complexity and expected effort, and assign a size.

This experiment explores whether Jev can automate this **initial estimation step**.

---

# Why This Is a Good system one Use Case

T-shirt sizing has a **small, predefined output space**.

The system does not need to generate an explanation or invent a new category. It needs to evaluate the ticket against defined criteria and select one of:

```text
XS / S / M / L / XL
```

This makes it a potentially good fit for Jev's system one approach.

The intended flow is:

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

The objective is to determine whether Jev can provide a **fast, consistent first-pass estimate**, while uncertain cases can be escalated to a larger LLM or a human.

---

# Inputs

The `tickets/` directory contains ticket information used by the experiment.

```text
tickets/
├── ticket-001.md
├── ticket-002.md
└── ticket-003.md
```
