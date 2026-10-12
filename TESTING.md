# Scaffold and Vercel integration test

This repository contains both skill sources and generated examples:

| Path | Role | Vercel project |
| --- | --- | --- |
| `mobile/` | SwiftUI iOS 17+ counter app | Native; not deployed to Vercel |
| `landing/` | iOS companion landing page | `agent-dev-tools-ios-landing` |
| `web/` | React/Next.js app with `/api/health` | `agent-dev-tools-web` |

The web app includes an interactive counter and an API check. The mobile landing page includes an illustrative app preview and a link to the Swift source; it does not claim an App Store release.

Run `npm ci`, `npm run lint`, `npm run typecheck`, and `npm run build` inside each web folder. Start either app with `npm run start -- --hostname 127.0.0.1`, then verify the page. For `web/`, also request `/api/health` and use the Check server API button.

For native validation, follow `Scaffolding/scaffold-app/references/mobile.md`, using the app and scheme name `AgentDevDemo`. The bundle identifier is `com.pleyva.agentdevdemo`; configure signing and distribution details before releasing. Native compilation and simulator tests require macOS/Xcode and are not verified on Linux.

Both Vercel projects connect to this GitHub repository with different Root Directory settings (`landing` and `web`), using `main` for production and issue branches for previews. Preserve the test branch after merging.
