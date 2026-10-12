# Scaffold and Vercel integration test

| Path | Role | Vercel project |
| --- | --- | --- |
| `mobile/` | SwiftUI iOS 17+ counter app | Native; not deployed to Vercel |
| `landing/` | iOS companion landing page | `agent-dev-tools-ios-landing` |
| `web/` | React/Next.js app with `/api/health` | `agent-dev-tools-web` |

## Verified results

- Both web projects passed ESLint, TypeScript, and production builds locally.
- Both production pages returned HTTP 200 with expected content on October 12, 2026.
- React API: HTTP 200 and `{"status":"ok","service":"web"}`.
- Vercel reported both production deployments as READY.
- React deployment source: Git, branch `feature/test-mobile-and-web-vercel`, commit `763deb8f6c84fd1061e00f6fccd5e95d3ca99df4`.
- Landing deployment: source-file upload from the same app source; automated Git deployment is not verified.
- Browser interaction checks remain unverified because Chromium could not be downloaded.
- Native compilation and simulator tests remain unverified because macOS/Xcode are unavailable.

Live pages:

- [React app](https://agent-dev-tools-web.vercel.app)
- [Swift iOS companion landing page](https://agent-dev-tools-ios-landing.vercel.app)
- [React health API](https://agent-dev-tools-web.vercel.app/api/health)

The web demo uses local counter state and a read-only server API; it has no persistence or authentication. The landing page contains an illustrative native preview and a source link, without claiming an App Store release.

## Local and native checks

Run `npm ci`, `npm run lint`, `npm run typecheck`, and `npm run build` inside each web folder. Start with `npm run start -- --hostname 127.0.0.1`, verify the page, and use the web demo's counter and Check server API button.

For native validation, follow `Scaffolding/scaffold-app/references/mobile.md`, using the app and scheme name `AgentDevDemo`. The bundle identifier is `com.pleyva.agentdevdemo`; configure signing before distribution.

## Remaining Git integration setup

Use separate Vercel Root Directories (`landing` and `web`) for the two projects. The React app has a verified Git-sourced deployment. Linking the landing project through the connector still returns a GitHub integration authorization error; source upload allowed its live deployment, but does not enable automatic builds on push.

Connect the landing project to `pleyva2004/Agent-Dev-Tools` in Vercel's Git settings and configure the intended production branch. Verify automatic preview and production deployments before treating the connection workflow as fully tested.

Preserve `feature/test-mobile-and-web-vercel` after merging.
