import type { Metadata } from "next";
import "./globals.css";
export const metadata: Metadata = {
  title: "P3 / DOSSIER — Détection de fuites sociales (doxing)",
  description: "P3 — Corrélation d'identités numériques et fuites de données sur identifiants génériques. Anonymisé, local, éthique.",
};
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return <html lang="fr"><body>{children}</body></html>;
}
