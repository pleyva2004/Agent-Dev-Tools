export function healthStatus() {
  return { status: "ok", service: "web" } as const;
}
