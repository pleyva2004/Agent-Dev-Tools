import type { Metadata } from "next";
import "./globals.css";
export const metadata: Metadata = {"title": "Agent Dev Demo | iOS", "description": "A SwiftUI iOS starter, with its landing page hosted on Vercel."};
export default function RootLayout({ children }: Readonly<{children: React.ReactNode}>) {return <html lang="en"><body>{children}</body></html>;}
