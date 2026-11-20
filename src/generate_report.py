"""generate_report.py — Génère le PDF du rapport P3 — Fuites sociales (doxing).

Contenu : corrélations (Sites), fuites HIBP (breaches), métadonnées (GPS, appareil photo), PDF de type Rssi.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def build_markdown(data: dict) -> str:
    username = data.get("username", "testuser123")
    uc = data.get("username_correlator", {"platforms": [], "total": 0})
    bc = data.get("breach_checker", {"email": username + "@example.com", "breaches": [], "status": "n/a"})
    ms = data.get("metadata_scanner", {"scanned_paths": [], "results": {}})

    lines = [
        "# P3 — Fuites sociales (doxing) — Outil de détection",
        "",
        f"- **Identifiant analysé** : `{username}` (générique — aucun compte réel, selon ethique P3)",
        f"- **Délai évaluation** : {data.get('run_at', '-')}",
        f"- **Résultat** : {uc.get('total', 0)} plateformes corrélées, breaches : {bc.get('breaches', [])}",
        "",
        "## 1. Corrélations d'identités numériques (Sherlock)",
        "",
    ]
    for p in uc.get("platforms", [])[:20]:
        lines.append(f"- **{p}**")
    if not uc.get("platforms"):
        lines.append("- *(aucune plateforme détectée — username introuvable ou compte Protecté — voir note S3)*")

    lines += [
        "",
        "## 2. Fuites de données (Have I Been Pwned)",
        "",
        f"- Email test : `{bc.get('email', 'n/a')}` → status {bc.get('status')}",
        *( [f"- Breaches détectées : {bc.get('breaches')}" ] if bc.get("breaches") else ["- Aucune breach détectée (404 ou absence de données publics)"] ),
        "",
        "## 3. Analyse des métadonnées (exiftool)",
        "",
    ]
    for path, res in ms.get("results", {}).items():
        if not isinstance(res, dict):
            continue
        gps = res.get("gps")
        lines.append(f"- `{path}` → GPS: {gps if gps else 'aucun (aucune donnée GPS exposée)'}")

    lines += [
        "",
        "## 4. Notes éthiques et solutions",
        "- identifiant générique — username 'testuser123' — outils de recherche dans alertes anonymes.",
        "- L'ANPDP notifiée si email/username diffusés en clair dans ce dossier (interdit P3 — anonymisation dans tous les outputs).",
        "- Filtres : utiliser des identifiers automatiques (pattern a-z0-9, prefixes 'z' pour anonymisation).",
        "- Alternative sociale: double-profil public/profil d'anonymisation (pattern public-first-pseudo).",
        "",
        "## 5. Exécutions à montrer au prof :",
        "- `python -m doxing_fuites_main --username testuser123 --save-json outputs/results.json`",
        "- `python -m generate_report --json outputs/results.json --pdf outputs/rapport-p3.pdf`",
    ]
    return "\n".join(lines)


def build_pdf(markdown: str, out_path: Path) -> None:
    from reportlab.lib.pagesizes import LETTER
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

    def esc(t: str) -> str:
        return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(str(out_path), pagesize=LETTER, topMargin=0.5 * inch, bottomMargin=0.5 * inch, leftMargin=0.75 * inch, rightMargin=0.75 * inch)
    styles = getSampleStyleSheet()
    story = []
    for line in markdown.split("\n"):
        if not line.strip():
            story.append(Spacer(1, 6))
            continue
        if line.startswith("# "):
            story.append(Paragraph(esc(line[2:]), styles["h1"]))
        elif line.startswith("## "):
            story.append(Paragraph(esc(line[3:]), styles["h2"]))
        else:
            story.append(Paragraph(esc(line), styles["Normal"]))
    doc.build(story)
    print(f"[OK] PDF écrit : {out_path} ({out_path.stat().st_size} octets)")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="generate_report", description="Génère le rapport P3 — Fuites sociales")
    ap.add_argument("--json", type=Path, default=None, help="Fichier JSON du résultat")
    ap.add_argument("--pdf", type=Path, default=Path("outputs/rapport-p3.pdf"), help="Chemin du PDF")
    args = ap.parse_args(argv)
    data = json.loads(args.json.read_text(encoding="utf-8")) if args.json else {"app": "aegis-p3-doxing-fuites", "run_at": "-", "username": "n/a", "username_correlator": {"total": 0, "platforms": []}, "breach_checker": {"email": "n/a", "breaches": [], "status": "n/a"}, "metadata_scanner": {"scanned_paths": [], "results": {}}}
    md = build_markdown(data)
    args.pdf.parent.mkdir(parents=True, exist_ok=True)
    (args.pdf.parent / "report.md").write_text(md, encoding="utf-8")
    build_pdf(md, args.pdf)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
