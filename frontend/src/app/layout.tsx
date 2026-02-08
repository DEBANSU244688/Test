import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Career Path Optimizer",
  description: "Resume-to-Job Matcher & Skill Gap Analyzer"
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
