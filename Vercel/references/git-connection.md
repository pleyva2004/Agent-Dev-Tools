# Git connection workflow

## Dashboard: recommended for initial connection

1. Open the Vercel dashboard and select the intended account/team.
2. Choose **Add New → Project** and import the GitHub repository. If it is missing, inspect the Vercel GitHub App's repository access and organization authorization. Grant only the repository access needed for the task.
3. Reuse an existing project when appropriate: inspect **Settings → Git** before creating a duplicate or replacing an existing connection.
4. Set the project name, framework preset, and **Root Directory** to the actual web package (for example `web/`). In a monorepo, create a Vercel project per independently deployed web surface, not per native app.
5. Inspect the framework's inferred install/build/output settings. Match the repository's package manager, lockfile, and Node requirements. Enable access to files outside the root only when shared workspace dependencies require it.
6. Add required environment variables to their intended Development, Preview, and Production environments. Use separate API URLs where needed. Changes affect subsequent deployments; redeploy to apply new values.
7. Select **Deploy** after configuration is ready. Record the deployment result and source commit, then inspect Git settings and the intended production branch.
8. Push the issue branch or update its PR and verify the resulting preview deployment. Merge only after the repository's required checks and preview validation pass, when production changes are within scope.

## CLI: optional, with an authenticated account

Verify the installed CLI with `vercel --version` and `vercel whoami`. Use its current official documentation before relying on flags. Select the intended team/project interactively rather than accepting defaults blindly.

For a single web project, run from its checked-out app directory:

```bash
vercel link
vercel git connect
```

`vercel link` associates local files with a Vercel project; `vercel git connect` associates that project with a Git repository found through local Git remotes. Inspect `git remote -v` locally to choose the intended remote, and do not expose embedded credentials. Verify the resulting repository association in project Git settings. Linking alone does not enable automatic Git deployments.

For monorepos already imported with Git integration, run from the **repository root**:

```bash
vercel link --repo
```

This links existing projects across the repository. Do not run the single-project sequence blindly in a monorepo subdirectory or assume this command creates the initial Git integration. Prefer dashboard import for the initial monorepo setup. Keep `.vercel/` and pulled environment files out of commits.

Use Git-triggered deployments as the default; avoid adding a second GitHub Actions deployment path unless the repository requires custom CI deployment.

## Troubleshooting

| Symptom | Inspect and resolve |
| --- | --- |
| Repository not listed | Correct GitHub account, Vercel team, GitHub App repository permissions, and organization access |
| Build fails | First meaningful error in logs, root directory, manifest scripts, lockfile, runtime version, and required variables |
| Home page works but deep links fail | Framework preset and routing configuration; add a SPA fallback only for a stack that needs it |
| API requests fail | Environment API URL, HTTPS, CORS allowed origins, cookies, auth callbacks, and backend reachability |
| Preview push produces no deployment | Git connection, branch settings, ignored/skipped builds, author permissions, and fork authorization |
| CLI works but Git pushes do not deploy | Separate local linking from Git provider integration and inspect project Git settings |
| Preview works but production fails | Production variable values, selected branch, backend endpoint, and deployed source SHA |

## Official sources

Verified 2026-10-12. Recheck these pages when applying the skill because dashboard labels and CLI behavior can change.

- [Git integration](https://vercel.com/docs/git)
- [GitHub integration and permissions](https://vercel.com/docs/git/vercel-for-github)
- [Monorepo project roots and linking](https://vercel.com/docs/monorepos)
- [Build configuration](https://vercel.com/docs/builds/configure-a-build)
- [Environment variables](https://vercel.com/docs/environment-variables)
- [Deployment environments](https://vercel.com/docs/deployments/environments)
- [CLI local linking](https://vercel.com/docs/cli/link)
- [CLI Git connection](https://vercel.com/docs/cli/git)
