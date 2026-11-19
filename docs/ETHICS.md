# ETHICS — P3 — Détection de fuites sociales (doxing) (AEGIS)

Engagements éthiques du projet — stand-alone, labo local, GPU refused, anti-cloud.

- **Cible** : [AEGIS Détection de fuites sociales (doxing)](https://github.com/LaidiMohammed/aegis-p3-doxing-fuites)
- **Périmètre** : [AEGIS Détection de fuites sociales (doxing)](https://aegis-p3-doxing-fuites.vercel.app) — smoke + fonctions CLI.
- **GPU refused** : implementation uniquement CPU/pure Python.
- **Données locales** : sources acceptées : labo local (localhost, Juice Shop, DVWA, etc.).
- **Smoke au prof** : cmds à exécuter — voir README/scripts/run_smoke.sh.
- **Smoke clé de validation** : voir `smoke()` dans `src/doxing-fuites_main.py` — doit retourner `{"ok": true, ...}`.
- **Site statique Vercel** : disponible pour la démo statique (smoke uniquement).

See SPEC.md (avec use cases + tableaux attendus).
