# Weekly Updates Outlook

Generate professional weekly leadership update emails from CSV files directly into Outlook drafts.

## Why this exists

Weekly leadership updates often require repetitive manual formatting, consolidation and rewriting.

This project automates the preparation step while keeping the final email under human control.

CSV in → Outlook draft out.

## Architecture

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
