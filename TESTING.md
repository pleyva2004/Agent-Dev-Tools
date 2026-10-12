# Scaffold and Vercel integration test

This branch contains both skill sources and generated examples:

| Path | Role | Intended Vercel project |
| --- | --- | --- |
| `mobile/` | SwiftUI iOS 17+ counter app | Native; not deployed to Vercel |
| `landing/` | iOS companion landing page | `agent-dev-tools-ios-landing` |
| `web/` | React/Next.js app with `/api/health` | `agent-dev-tools-web` |

The web app includes an interactive counter and an API check. The mobile landing page includes an illustrative app preview and a link to the Swift source; it does not claim an App Store release. Its source links target main and will resolve after this PR is merged.

## Verified locally

- Both web projects: ESLint, TypeScript, and production builds passed.
- Both local pages returned HTTP 200 with expected content.
- The web health endpoint returned HTTP 200 and `{"status":"ok","service":"web"}`.
- Browser interaction checks remain unverified because the runtime could not download Chromium.
- Native compilation and simulator tests remain unverified because macOS/Xcode are unavailable.

Run `npm ci`, `npm run lint`, `npm run typecheck`, and `npm run build` inside each web folder. Start either app with `npm run start -- --hostname 127.0.0.1`, then verify the page. For `web/`, also request `/api/health` and use the Check server API button.

For native validation, follow `Scaffolding/scaffold-app/references/mobile.md`, using the app and scheme name `AgentDevDemo`. The bundle identifier is `com.pleyva.agentdevdemo`; configure signing and distribution details before releasing.

## Vercel connection status

The intended setup is two Vercel projects connected to this GitHub repository, with separate Root Directory settings (`landing` and `web`), `main` for production, and issue branches for previews. Automatic Git deployment is not verified.

The `agent-dev-tools-web` project was created, but it has no verified deployment. Creation/linking of the landing project failed because Vercel requires the GitHub integration. Deployment to the reported `pleyva2004s-projects` scope returned HTTP 403 (not authorized). The ChatGPT Vercel connection needs appropriate access to that project scope, and Vercel's GitHub integration must be authorized for this repository.

Keep the PR open until the connection and live deployments can be verified. Preserve `feature/test-mobile-and-web-vercel` after merging.
