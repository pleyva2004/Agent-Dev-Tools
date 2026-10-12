# React full stack web scaffold

## Layout and prerequisites

Use an installed supported Node LTS release satisfying Next.js requirements (currently Node >=20.9), npm/npx, and registry access. Check the exact selected generator's requirements before upgrading. The generator delegates package versions, TypeScript, ESLint, and framework configuration to official `create-next-app`, then overlays a small font-download-free starting page and API:

```text
web/
  src/app/layout.tsx           HTML shell and metadata
  src/app/page.tsx             Server-rendered home page
  src/app/api/health/route.ts   GET /api/health
  src/lib/health.ts            Shared service function
  .env.example                Environment conventions
  package.json                dev/build/start/lint/typecheck
  package-lock.json           Resolved dependency versions
  scaffold.json               Generator provenance
```

Retain the official generated configuration and ignore rules. Add feature modules beneath `src/features/<feature>/` when there is real feature code; add server-only data access beneath `src/lib/server/` with the `server-only` boundary when needed. Use client components only for browser state/events and preserve server boundaries. Put API handlers in `src/app/api/<resource>/route.ts`; validate untrusted inputs and keep long-running jobs separate from request handlers.

## Run and check

From `web/`, run:

```bash
npm ci
npm run lint
npm run typecheck
npm run build
npm run start
```

In another terminal, request `http://localhost:3000/` and `http://localhost:3000/api/health`. Expect an HTML page and JSON `{"status":"ok","service":"web"}` with HTTP 200. Stop the server after checking. Use `npm run dev` for iteration. Commit source, framework configs, `scaffold.json`, and `package-lock.json`; exclude `node_modules/`, `.next/`, and secrets. Ensure `.env.example` is tracked explicitly if the generated `.gitignore` ignores `.env*`.

Set Vercel's project Root Directory to `web` and its framework to Next.js when deploying through the separate Vercel skill. This app contains framework API routes; it does not require a separate Express process. Verify the framework's current hosting configuration instead of forcing static export, which would exclude server routes.

## Official sources

Checked October 12, 2026:

- [Next.js installation and supported runtime](https://nextjs.org/docs/app/getting-started/installation)
- [create-next-app flags](https://nextjs.org/docs/app/api-reference/cli/create-next-app)
- [Route handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route)
- [Server and client components](https://nextjs.org/docs/app/getting-started/server-and-client-components)

Recheck these sources before version changes. A registry/network failure blocks generation; fix access or provide a known-compatible local generator, and do not claim a generated app exists.
