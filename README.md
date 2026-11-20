# AEGIS — P3 — Fuites sociales (doxing)

P3 — **Outil de détection de fuites sociales (doxing)** (PFE P13 style AEGIS).

## Objectif

Corrélation d'identités numériques et fuites de données (doxing), sur des cibles libres/génériques.

## Architecture

```
AEGIS P3 (doxing-fuites)
├── src/
│   ├── doxing_fuites_main.py    # CLI — username_correlator / breach_checker / metadata_scanner / doxing_audit
│   └── generate_report.py       # PDF via reportlab
└── tests/
    └── test_doxing.py           # 7 tests mocks — pass
```

## Fonctions — démo à la prof

```bash
python -m src.doxing_fuites_main --username testuser123 --save-json outputs/results.json --json
python -m src.generate_report --json outputs/results.json --pdf outputs/rapport-p3.pdf
```

- `username_correlator` : sherlock CLI (local — mock dans tests) — comptes associés.
- `breach_checker` : Have I Been Pwned API (mock dans tests).
- `metadata_scanner` : exiftool (mock dans tests).
- `doxing_audit` : cette commande complète (7 tests pass).

## Install

```bash
pip install -r requirements.txt
```

## Sites

- **GitHub** : https://github.com/LaidiMohammed/aegis-p3-doxing-fuites
- **Vercel** : https://aegis-p3-doxing-fuites.vercel.app

## Éthique

- identifiant générique (testuser123@example.com), pas de compte réel — Smoke uniquement.
- Aucune fuite diffuse (anonymisation dans outputs — voir audit éthique P3).

See `docs/ETHICS.md`.
