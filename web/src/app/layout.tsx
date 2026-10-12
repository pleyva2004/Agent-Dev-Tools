import type { Metadata } from "next";
import "./globals.css";
export const metadata: Metadata = {"title": "Agent Dev Tools | Web demo", "description": "A React and Next.js scaffold with a working server API."};
export default function RootLayout({ children }: Readonly<{children: React.ReactNode}>) {return <html lang="en"><body>{children}</body></html>;}
