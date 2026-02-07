import type { Config } from "tailwindcss";

const config: Config = {
  darkMode: ["class"],
  content: ["./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        primary: "#00ADB5",
        background: "#0F172A",
        surface: "#1E293B",
        accent: "#38BDF8",
        success: "#22C55E",
        warning: "#FACC15",
        danger: "#F43F5E"
      }
    }
  },
  plugins: []
};

export default config;
