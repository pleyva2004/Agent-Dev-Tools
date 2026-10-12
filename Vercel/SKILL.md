---
name: vercel
description: Connect a GitHub repository to Vercel, configure its web root and environments, and verify preview and production deployments. Use for deploying a full stack application's web frontend or a mobile application's landing page, including monorepo Git integration and deployment troubleshooting.
---

# Vercel repository connection

## 1. Inspect and choose the deployment surface

- Read repository instructions, package manifests, lockfiles, existing deployment configuration, and the requested issue.
- Identify the GitHub repository, Vercel account/team, existing project, production branch, framework, web root, and backend API URL. Reuse known values; ask only for missing choices that block connection.
- Apply the following routing rule:

  | Application | Deploy to Vercel | Keep outside this flow |
  | --- | --- | --- |
  | Full stack web app | Existing web frontend, commonly `web/` | Separate backend services, databases, workers, and infrastructure |
  | Mobile app | Web landing page, commonly `web/` | Native iOS/Android application build and store distribution |

- Preserve existing framework route handlers when they are part of the web app. Do not migrate a separate backend merely to connect the frontend.
- For mobile repositories without a web surface, create a small landing page in `web/` using the existing web stack when available. Include the app purpose, screenshots/assets if supplied, support contact, and real store links if available. Omit fabricated download links. Keep native source outside the Vercel root.
- Keep this repository's `Vercel/` folder as the skill itself; do not select it as a deployment root.

## 2. Prepare the web project

- Create an issue branch under the applicable lowercase `feature/`, `docs/`, or `hotfix/` prefix.
- Install dependencies with the repository's package manager and lockfile. Run its existing lint, typecheck, test, and production build commands where relevant.
- Use framework detection first. Override build/install/output settings only when the project needs them; do not force static export or an output directory on Next.js.
- For an external backend, configure an environment-specific API URL. Use preview/test services for previews and the production endpoint for production. Verify HTTPS, allowed origins, authentication redirects, and cookie behavior against the deployed frontend.
- Keep tokens and backend credentials server-side. Treat client-exposed environment variables as public, including `NEXT_PUBLIC_*` and `VITE_*` values. Commit only placeholder variable names in `.env.example`; ignore local environment files and `.vercel/` state.

## 3. Connect the repository

- Read [Git connection workflow](references/git-connection.md) for exact dashboard steps, optional CLI linking, and troubleshooting.
- Use available Vercel/GitHub connectors first. Use the dashboard when no suitable connector exists; use CLI only with established access and the correct project/team.
- Complete preparation before connecting: importing a repository can trigger the first deployment. Continue within the user's deployment authorization; if the request only asks for a plan or skill, document the flow without connecting an account or deploying.
- Configure Root Directory to the selected frontend or landing page, environments before deployment, and the production branch to the repository's intended branch.

## 4. Verify and hand off

- Check deployment status, build logs, and the deployed commit SHA. Open the preview URL and verify page rendering, assets, deep links, and the main user action.
- For web apps, verify an API-backed flow against the selected environment. For mobile landing pages, verify responsive layout and all published links.
- Confirm Git integration by observing the intended branch push or PR deployment. Distinguish a local CLI link from the Git connection; neither a successful local build nor a manual upload proves automatic Git deployments.
- When production deployment is authorized, merge through the repository's PR workflow, verify the production URL/commit, and preserve the issue branch. Respect required reviews and checks.
- Report repository, Vercel project/team, root directory, branch, preview/production URLs, checks, and unresolved blockers. Report secrets by name only. Do not claim connection or deployment succeeded without evidence.
