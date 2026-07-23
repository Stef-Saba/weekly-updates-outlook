# Weekly Updates Outlook

Generate professional weekly leadership update emails from CSV files directly into Outlook drafts.

## Why this exists

Weekly leadership updates often require repetitive manual formatting, consolidation and rewriting.

This project automates the preparation step while keeping the final email under human control.

CSV in → Outlook draft out.

## Architecture 

The project follows a simple automation pipeline:

```text
                         USER
                          |
                          v
              Weekly Updates CSV File
                          |
                          v
        +--------------------------------+
        |                                |
        |     CSV Processing Engine      |
        |                                |
        | - Reads structured updates     |
        | - Extracts statuses            |
        | - Evaluates update content     |
        |                                |
        +--------------------------------+
                          |
                          v
        +--------------------------------+
        |                                |
        |       Classification Logic     |
        |                                |
        |  [MAJOR]                       |
        |      |                         |
        |      v                         |
        | Leadership Awareness           |
        |                                |
        |  [ADOPTION]                    |
        |      |                         |
        |      v                         |
        | Highlights & Achievements      |
        |                                |
        |  Status = ✅                   |
        |      |                         |
        |      v                         |
        | Leadership Visibility          |
        |                                |
        +--------------------------------+
                          |
                          v
        +--------------------------------+
        |                                |
        |       HTML Email Generator     |
        |                                |
        | - Builds email structure       |
        | - Applies email-safe HTML      |
        |                                |
        +--------------------------------+
                          |
                          v
                 Outlook Draft
                          |
                          v
              Review → Edit → Send

Then also add the project file architecture:

```markdown
## Project structure

```text
weekly-updates-outlook

├── sample_weekly_updates.csv
│       Input delivery updates
│
├── generate_update.py
│       Processing engine
│       Classification rules
│       HTML generation
│
├── outlook_sender.py
│       Outlook draft creation
│
└── README.md
        Documentation

## Update logic

The generator applies transparent rules to classify updates.

### [MAJOR]

Updates containing `[MAJOR]` are elevated into Leadership Awareness.

Used for:
- important milestones
- critical decisions
- significant delivery updates

### [ADOPTION]

Updates containing `[ADOPTION]` are added to Highlights & Achievements.

Used for:
- adoption milestones
- engagement improvements
- successful rollouts

### Completed items

Items with status ✅ are surfaced because completed milestones are relevant for leadership visibility.

## Why use rules?

The current version intentionally uses simple, transparent logic:

- easy to understand
- easy to modify
- predictable output
- no external AI dependency

## Feedback

Have ideas or found issues?

Please open a GitHub Issue.

## FAQ

### Can I change the rules?

Yes. The logic is contained in `generate_update.py`.

### Can this support Gmail?

A Gmail version can reuse the same processing logic with a different email delivery component.
