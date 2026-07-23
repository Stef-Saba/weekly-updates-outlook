# Weekly Updates Outlook

Generate leadership-ready Outlook update emails from structured CSV delivery updates.

## Problem

Weekly leadership updates often require teams to manually transform detailed delivery information into concise communication.

The information already exists, but the process of filtering, prioritising, formatting and rewriting updates is repetitive and inconsistent.

For Technical Program Managers and delivery teams, the challenge is not collecting updates. The challenge is turning execution details into clear leadership communication.

This project explores how simple automation and configurable rules can help bridge the gap between execution data and leadership updates.

## Solution

Weekly Updates Outlook transforms structured CSV delivery updates into a leadership-ready Outlook draft.

Workflow:

CSV updates → Processing engine → Classification logic → HTML email generation → Outlook draft → Human review

The objective is not to replace judgement or decision-making.

The objective is to automate repetitive preparation work while keeping the final communication under human control.

## Architecture

The project follows a simple automation pipeline.

                         USER
                          |
                          v
              Weekly Updates CSV File
                          |
                          v
        +--------------------------------+
        |     CSV Processing Engine      |
        |                                |
        | - Reads structured updates     |
        | - Extracts statuses            |
        | - Evaluates update content     |
        +--------------------------------+
                          |
                          v
        +--------------------------------+
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
        |  Completed items               |
        |      |                         |
        |      v                         |
        | Leadership Visibility          |
        +--------------------------------+
                          |
                          v
        +--------------------------------+
        |       HTML Email Generator     |
        |                                |
        | - Builds email structure       |
        | - Applies email-safe HTML      |
        +--------------------------------+
                          |
                          v

                 Outlook Draft
                          |
                          v

              Review → Edit → Send

## Update Classification Logic

The generator applies transparent rules to classify updates.

The purpose of these rules is not to automate leadership judgement. The purpose is to consistently surface information that is usually important for leadership audiences.

## [MAJOR]

Updates containing `[MAJOR]` are elevated into Leadership Awareness.

Used for:

- Important milestones
- Critical decisions
- Significant delivery updates
- Risks or changes requiring visibility

Rationale:

Leadership teams need visibility into events that may affect priorities, timelines, decisions or delivery outcomes.

## [ADOPTION]

Updates containing `[ADOPTION]` are added to Highlights & Achievements.

Used for:

- Adoption milestones
- Engagement improvements
- Successful rollouts
- Business impact updates

Rationale:

Delivery success is not only measured by completion. Adoption demonstrates whether delivered capabilities are creating value.

## Completed Updates

Completed items are surfaced because delivery milestones provide useful leadership visibility.

Rationale:

Leadership communication should show both future priorities and evidence of execution progress.

## Why Use Rules?

The current version intentionally uses simple, transparent logic instead of external AI dependency.

This approach is:

- Easy to understand
- Easy to modify
- Predictable
- Adaptable to different team workflows

The goal is to automate repetitive communication preparation, not automate leadership judgement.

## Getting Started

1. Prepare your CSV delivery updates.
2. Add tags where relevant:
   - `[MAJOR]`
   - `[ADOPTION]`
3. Run the generator.
4. Review the generated Outlook draft.
5. Edit if required and send.

## Feedback

This is an early version and feedback is welcome.

If you work with delivery updates, project reporting or leadership communication, I would love feedback on:

- Classification approaches
- Reporting workflows
- Automation opportunities
- Alternative use cases

Please open a GitHub Issue with suggestions, improvements or problems encountered.

## FAQ

### Can I change the classification rules?

Yes.

The classification logic is contained in `generate_update.py` and can be adapted to different reporting workflows.

### Does this replace human review?

No.

The tool creates a draft to reduce preparation effort. The final communication remains with the user.

### Can this support Gmail?

Yes.

A Gmail version can reuse the same processing logic with a different email delivery component.

### Why not use AI for classification?

The current version focuses on transparent, predictable rules that users can understand and modify.

AI-based enhancements could be explored in future versions.

## Roadmap

- Gmail-compatible version
- Configurable templates
- Additional email platforms
- More flexible classification rules
- Additional reporting formats


