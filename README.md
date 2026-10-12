# Agent-Dev-Tools

A workspace for developing tools for AI agents.

## Project status

This repository is in its initial setup stage. It currently contains this README; application code, dependencies, and runnable tools have not been added yet. Setup, usage, and test instructions will be documented as implementations are introduced.

## Getting started

Install Git, then clone the repository:

```bash
git clone https://github.com/pleyva2004/Agent-Dev-Tools.git
cd Agent-Dev-Tools
```

Review the [issues](https://github.com/pleyva2004/Agent-Dev-Tools/issues) for requested work and project discussions.

## Contributing

1. Choose an existing issue or open one describing the proposed change and expected outcome.
2. Create a branch from the latest `main`, using a descriptive name based on the issue:

   ```bash
   git switch main
   git pull --ff-only origin main
   git switch -c <issue-name>
   ```

3. Make focused changes and update relevant documentation. For code changes, run the applicable checks and document the results.
4. Commit and push your branch:

   ```bash
   git add <changed-files>
   git commit -m "Describe the change"
   git push -u origin <issue-name>
   ```

5. Open a pull request targeting `main`. Explain the change, describe validation, and reference the issue with `Closes #<issue-number>` when the work fully resolves it.

## Questions and feedback

Use [GitHub Issues](https://github.com/pleyva2004/Agent-Dev-Tools/issues) to report problems, propose tools, or ask questions. Include relevant context, reproduction steps when applicable, and the expected behavior.
