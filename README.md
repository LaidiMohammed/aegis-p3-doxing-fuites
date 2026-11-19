# AEGIS — P3 — Détection de fuites sociales (doxing)

[![Vercel](https://img.shields.io/badge/Vercel-aegis-p3--blue?logo=vercel)](https://aegis-p3-doxing-fuites.vercel.app)
[![Tests](https://img.shields.io/badge/Tests-passing-brightgreen)]

Détection de fuites sociales (doxing) — PFE P13 style AEGIS (Master 1 Sécurité informatique).

## Infos rapides

| Élément | Valeur |
|---|---|
| **GitHub** | https://github.com/LaidiMohammed/aegis-p3-doxing-fuites |
| **Vercel** | https://aegis-p3-doxing-fuites.vercel.app |
| **Stacks** | PyGithub, requests, exiftool CLI |
| **Type** | pg |
| **Ethique** | Labo local, anti-GPU, anti-cloud, stand-alone |

## Install

```bash
pip install -r requirements.txt
make install  # (venv)
```

## Smoke & tests (démo à la prof)

```bash
make smoke   # ou: scripts/run_smoke.sh
make test
```

## Fonctions à exécuter à la démo

Voir [`docs/ETHICS.md`](docs/ETHICS.md), [`docs/SPEC.md`](docs/SPEC.md).
