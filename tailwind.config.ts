import type { Config } from "tailwindcss";
const config: Config = {
  content: ["./app/**/*.{js,ts,jsx,tsx,mdx}", "./components/**/*.{js,ts,jsx,tsx,mdx}"],
  theme: {
    extend: {
      colors: { paper: "#efece4", coal: "#111111", red: "#c0392b", fog: "#8b8b8b" },
      fontFamily: {
        display: ["Special Elite", "Courier New", "monospace"],
        mono: ["IBM Plex Mono", "Consolas", "monospace"],
        sans: ["Inter", "Arial", "sans-serif"],
      },
    },
  },
  plugins: [],
};
export default config;
