import type { Metadata } from "next";
import { Special_Elite, IBM_Plex_Mono, Inter } from "next/font/google";
const displayFont = Special_Elite({ subsets: ["latin"], weight: ["400"], variable: "--font-display", display: "swap" });
const monoFont = IBM_Plex_Mono({ subsets: ["latin"], weight: ["400", "600"], variable: "--font-mono", display: "swap" });
const sansFont = Inter({ subsets: ["latin"], weight: ["400", "500"], variable: "--font-sans", display: "swap" });
import "./globals.css";
export const metadata: Metadata = {
  title: "P3 / DOSSIER — Détection de fuites sociales (doxing)",
  description: "P3 — Corrélation d'identités numériques et fuites de données sur identifiants génériques. Anonymisé, local, éthique.",
};
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return <html lang="fr" className={`${displayFont.variable} ${monoFont.variable} ${sansFont.variable}`}><body>{children}</body></html>;
}
