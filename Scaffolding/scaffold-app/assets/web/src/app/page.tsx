import Link from "next/link";

export default function Home() {
  return (
    <main className="container">
      <h1>Your app starts here</h1>
      <p>React UI, typed server routes, and room for your first feature.</p>
      <Link href="/api/health">Check the API health endpoint</Link>
    </main>
  );
}
