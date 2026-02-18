# Hookstest

A minimal repo for experimenting with Git hook behavior. Use it as a sandbox to verify when hooks run and what data they receive.

## What This Is
- A tiny Git repository for testing hook scripts.
- A safe place to prototype and iterate on hook logic.
- Not a production project.

## Quick Start
1. Clone the repo.
2. Add a hook script under `.git/hooks/` (hooks are local to your clone).
3. Make a change, then run the Git action that should trigger the hook.

## Example: `pre-commit` Hook
Create a simple hook that blocks commits containing the word `WIP`:

```bash
cat <<'HOOK' > .git/hooks/pre-commit
#!/usr/bin/env bash
if git diff --cached --name-only | xargs -I{} grep -n "WIP" {} >/dev/null 2>&1; then
  echo "Commit blocked: remove WIP before committing."
  exit 1
fi
HOOK

chmod +x .git/hooks/pre-commit
```

Now try committing a file containing `WIP` to see the hook in action.

## Tips
- Hooks are not committed with the repo by default.
- To share hooks across teammates, consider a `scripts/` directory and a setup script that installs hooks into `.git/hooks/`.

## Contributing
Open an issue or submit a PR if you have improvements or additional hook examples.
