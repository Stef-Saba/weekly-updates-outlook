Generate leadership-ready Outlook update emails from structured CSV delivery updates.

## Problem

Weekly leadership updates often require teams to manually transform detailed delivery information into concise communication.

The information already exists, but the process of filtering, prioritising and formatting updates is repetitive and inconsistent.

This project explores how simple automation and configurable rules can help bridge the gap between execution data and leadership communication.

## Solution

This tool:
- reads structured CSV updates
- applies classification logic
- generates an Outlook-compatible HTML email
- creates a draft for human review before sending

The goal is not to replace judgement, but to reduce repetitive formatting work.

## Architecture

CSV Delivery Updates
        |
        v
Update Processing Engine
        |
        +----------------+
        |                |
        v                v
   [MAJOR] tag      [ADOPTION] tag
        |                |
        v                v
Leadership        Adoption &
Awareness         Achievements

        |
        v

HTML Email Generator

        |
        v

Outlook Draft Creation

        |
        v

Human Review → Send

## Update Classification Logic

### [MAJOR]
Used for updates requiring leadership awareness, visibility or escalation.

### [ADOPTION]
Used to highlight adoption, usage or business impact.

### Completed updates
Used to maintain visibility of delivery progress.

## Getting Started

1. Prepare your CSV file.
2. Add update tags where relevant.
3. Run the generator.
4. Review the generated Outlook draft.
5. Adjust and send.

## Feedback

This is an early version and feedback is welcome.

If you work with delivery updates, project reporting or leadership communication, I would love feedback on:
- workflow improvements
- additional automation opportunities
- alternative use cases

Please open an issue with your suggestions.

## Roadmap

- Gmail-compatible version
- configurable templates
- additional email platforms
- more flexible classification rules# Weekly Updates Outlook

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
