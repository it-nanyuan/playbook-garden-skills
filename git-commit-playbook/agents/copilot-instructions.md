# Git Commit Playbook for GitHub Copilot

Apply these rules when asked to draft or refine a commit message.

## Workflow

- Inspect `git status` and relevant diffs before writing.
- Summarize only the changes actually present.
- Reuse the user's confirmed commit message language when known.
- If the language is unclear, ask once whether the commit message should be in Chinese or English.
- Recommend splitting the commit if unrelated work is mixed together.
- If the user wants a draft only, do not run `git commit`.

## Commit Message Format

```text
<type>: <one-line summary>

1. <specific change 1>
2. <specific change 2>
3. <specific change 3>
```

## Required Prefixes

Choose one:

- `feat:`
- `fix:`
- `refactor:`
- `docs:`
- `style:`
- `test:`
- `build:`
- `ci:`
- `chore:`
- `perf:`
- `revert:`

## Quality Standard

- The title must be concise but specific.
- The numbered items must be concrete and easy to review.
- Keep the whole message in the language selected by the user.
- Mention `.gitignore` updates explicitly when present.
- Avoid vague statements like "misc changes" or "code cleanup" unless the diff truly cannot support anything more specific.
