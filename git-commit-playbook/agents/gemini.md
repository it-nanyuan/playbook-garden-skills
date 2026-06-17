# Git Commit Playbook for Gemini

Use these instructions when generating a commit message from repository changes.

## Workflow

1. Inspect the actual Git changes before writing.
2. Use the diff to infer the main purpose of the commit.
3. If multiple unrelated themes are present, recommend separate commits.
4. If the user has not approved a commit yet, only provide a draft.

## Output Contract

Produce the commit message using this format:

```text
<type>: <one-line summary>

1. <specific change 1>
2. <specific change 2>
3. <specific change 3>
```

## Allowed Prefixes

Use exactly one of:

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

## Message Quality

- The title should explain the main change area and result.
- The numbered body should list concrete code, workflow, UI, config, or test changes.
- Avoid vague wording such as "update code" or "optimize logic".
- If the repository setup includes `.gitignore` changes, include that explicitly in the body.
