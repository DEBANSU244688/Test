"use client";

import { useEffect, useState } from "react";

export function ThemeToggle() {
  const [darkMode, setDarkMode] = useState(true);

  useEffect(() => {
    document.documentElement.classList.toggle("dark", darkMode);
  }, [darkMode]);

  return (
    <button
      className="rounded-md border border-accent px-3 py-1 text-sm hover:bg-surface"
      onClick={() => setDarkMode((prev) => !prev)}
      type="button"
    >
      {darkMode ? "Switch to Light" : "Switch to Dark"}
    </button>
  );
}
