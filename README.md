# Agent-Dev-Tools

Reusable agent skills for scaffolding apps and connecting web projects to Vercel.

## Skills

| Skill | Purpose | Entry point |
| --- | --- | --- |
| Scaffold App | Generate a SwiftUI iOS app or a React full stack Next.js app | [Scaffolding/scaffold-app/SKILL.md](Scaffolding/scaffold-app/SKILL.md) |
| Vercel Git Connection | Connect and verify a web app or mobile landing page deployment | [Vercel/SKILL.md](Vercel/SKILL.md) |

These are repository-hosted skill sources, not automatically installed personal skills. Read the relevant `SKILL.md` and its selected references before using it.

## Scaffold an app

Clone this repository, then point the generator at an existing target repository:

```bash
git clone https://github.com/pleyva2004/Agent-Dev-Tools.git
cd Agent-Dev-Tools
python Scaffolding/scaffold-app/scripts/scaffold.py web --repo /absolute/target-repo
# Or choose native iOS:
python Scaffolding/scaffold-app/scripts/scaffold.py mobile --repo /absolute/target-repo --name StarterApp --bundle-id com.example.starterapp
```

Use Python 3.10+; web generation also needs Node/npm and registry access. Build iOS on macOS with Xcode and XcodeGen. The generator creates `web/` or `mobile/`, refuses existing destinations, and preserves target repository root files. Follow [web verification](Scaffolding/scaffold-app/references/web.md) or [mobile verification](Scaffolding/scaffold-app/references/mobile.md) after generation. Commit generated web lockfiles and never commit secrets or build output.

For Vercel, read [Vercel/SKILL.md](Vercel/SKILL.md). Use the generated `web/` as the deployment Root Directory; native Swift apps require Apple's distribution tooling. Scaffolding alone does not deploy an app.

## Contributing

Follow [instruction.md](instruction.md): read the issue and comments, branch from the latest `main` using `feature/`, `docs/`, or `hotfix/` plus a lowercase issue-title slug, implement and verify, commit, and open a PR with `Closes #<issue-number>`. Merge after required checks pass and preserve the issue branch.

Check generator changes with:

```bash
python -m unittest discover -s Scaffolding/scaffold-app/scripts/tests -v
```

Use [GitHub Issues](https://github.com/pleyva2004/Agent-Dev-Tools/issues) for problems and proposed tools.

## Integration test examples

See [TESTING.md](TESTING.md) for the generated SwiftUI app (`mobile/`), its Vercel landing page (`landing/`), and the React full stack demo (`web/`).
