---
name: scaffold-app
description: Scaffold a repository for a native SwiftUI iOS mobile app or a React full stack web app using Next.js, with source structure, configuration, and build verification. Use when asked to initialize an app, choose mobile versus web scaffolding, or create a reusable starting code skeleton. Preserve existing app code and do not deploy as part of scaffolding.
---

# Scaffold an app

## Choose and inspect

1. Read the target repository's `instruction.md`, `AGENTS.md`, manifests, and existing app directories. Apply its issue workflow, lowercase branch prefixes, and branch retention.
2. Choose **mobile** for native iOS/Swift requirements; choose **web** for browser/React requirements. Ask one platform question only if the request does not determine it. Use both only when requested, generating separate `mobile/` and `web/` directories.
3. Use SwiftUI with feature-oriented views, an observable main-actor presentation model, and separately testable domain models for mobile. Use Next.js App Router with TypeScript, server components, and route handlers for React full stack web. Treat these as practical defaults, not universal best architectures.
4. Read [references/mobile.md](references/mobile.md) or [references/web.md](references/web.md). Resolve `scripts/` and `assets/` relative to this skill directory, regardless of the current working directory.

## Generate

Run Python 3.10+ with an existing absolute repository path:

```bash
python <skill-directory>/scripts/scaffold.py mobile --repo /absolute/repo --name StarterApp --bundle-id com.example.starterapp
python <skill-directory>/scripts/scaffold.py web --repo /absolute/repo
```

Generate only the selected platform. Optionally use `--app-dir my-app` for a different single lowercase directory name. Set a real reverse-DNS bundle identifier for mobile before distribution. The web generator uses the exact `create-next-app` version recorded in the script and writes it to `scaffold.json`; explicitly supply `--next-version X.Y.Z` after checking official release compatibility when upgrading. Commit the generated lockfile so installs are reproducible.

The script stages generation inside the target repository, refuses every existing app destination (including symlinks and empty directories), and leaves root files alone. For an existing app, adapt it deliberately rather than running the generator over it. Inspect generated agent instructions before implementing features. Do not copy `node_modules`, generated Xcode projects, or build output into this skill.

## Extend and verify

- Implement one small vertical slice through the chosen source structure. Keep private environment variables on the server. Add runtime validation and authorization to new API inputs; the initial read-only health endpoint needs no secrets or persistence.
- Add a database, authentication, networking, or alternate backend only when requirements demand it. Do not represent the health endpoint as a database-backed application.
- Run the selected platform's reference checks, inspect the diff, and report which checks ran. A successful Python generation is not evidence of an iOS build or a web production build.
- For mobile plus a marketing site, scaffold a separate `web/` Next.js app and pass that directory to the repository's Vercel skill. Vercel hosts web assets/API routes; distribute native iOS builds through Apple's toolchain.
- Complete the repository's commit/PR/merge workflow when authorized. Preserve the issue branch. Do not deploy or publish an app merely because its skeleton was requested.

For changes to this skill's generator, run `python -m unittest discover -s <skill-directory>/scripts/tests -v` and validate its frontmatter with the skill-creator validator.
