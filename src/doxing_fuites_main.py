"""Module principal — P3 Détection de fuites sociales (doxing) — AEGIS.

Où la extraction :
  - correlation d'identités numériques (Sherlock)
  - verification de fuites de données (Have I Been Pwned)
  - analyse de métadonnées locales (exiftool, vision 2D datetimes...)

Règle éthique (P3) : identifiant générique — aucun compte réel — Smoke uniquement.
"""
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Any

import requests  # module-level (mockable dans les tests)

USER_AGENT = "aegis-p3-doxing-fuites/1.0.0 (+https://aegis-p3-doxing-fuites.vercel.app)"


def username_correlator(username: str = "testuser123", timeout: int = 8) -> dict[str, Any]:
    """Returns comptes où SHERLOCK trouve le username."""
    out: list[str] = []
    try:
        with subprocess.Popen(["sherlock", username, "--print-found", "--json"],
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=timeout) as p:
            out_raw, _ = p.communicate(timeout=timeout)
        try:
            out = json.loads(out_raw or "[]")
        except Exception:
            out = [x.strip() for x in out_raw.split() if x.strip()]
    except Exception:  # noqa: BLE001
        pass
    return {"username": username, "platforms": out[:20], "total": len(out)}


def breach_checker(email: str = "testuser123@example.com", timeout: int = 8) -> dict[str, Any]:
    """Have I Been Pwned — /api/v3/breachedaccount/{email} — returns list of breaches."""
    try:
        r = requests.get(f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}",
                         headers={"User-Agent": USER_AGENT}, timeout=timeout)
        if r.status_code == 404:
            return {"email": email, "breaches": [], "status": 404, "note": "not_found"}
        if r.status_code == 200:
            return {"email": email, "breaches": [b["Name"] for b in r.json()], "status": r.status_code}
        return {"email": email, "breaches": [], "status": r.status_code, "error": "http_error"}
    except Exception as e:  # noqa: BLE001
        return {"email": email, "breaches": [], "status": "error", "error": str(e)}


def metadata_scanner(paths: list[str] | None = None, timeout: int = 8) -> dict[str, Any]:
    """Scanne les métadonnées via exiftool — GPS, avis appareil photo, outils précis."""
    found: dict[str, Any] = {}
    try:
        # On suppose les fichiers dans ./sample_docs (créés par generate_traffic)
        # On exécute une commande exiftool locale et on parse le JSON (mock local dans les tests)
        for p in (paths or ["./sample_docs/photo.jpg"]):
            r = subprocess.run(["exiftool", "-j", p], capture_output=True, text=True, timeout=timeout)
            try:
                data = json.loads(r.stdout)
            except Exception:
                data = []
            gps = None
            for d in data:
                if d.get("GPSLatitude") and d.get("GPSLongitude"):
                    gps = {"lat": d["GPSLatitude"], "long": d["GPSLongitude"]}
            found[p] = {"metadata": data[:20], "gps": gps}
    except Exception as e:  # noqa: BLE001
        found["error"] = str(e)
        found.setdefault("./sample_docs/photo.jpg", {}).setdefault("gps", None)
    return {"scanned_paths": (paths or ["./sample_docs/photo.jpg"]), "results": found}


def doxing_audit(username: str = "testuser123", email: str = "testuser123@example.com") -> dict[str, Any]:
    return {
        "app": "aegis-p3-doxing-fuites",
        "username": username,
        "username_correlator": username_correlator(username),
        "breach_checker": breach_checker(email),
        "metadata_scanner": metadata_scanner(),
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="doxing_fuites", description="Détection de fuites sociales — P3")
    ap.add_argument("--username", default="testuser123")
    ap.add_argument("--email", default="testuser123@example.com")
    ap.add_argument("--save-json", default=None)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    out = doxing_audit(args.username, args.email)
    if args.save_json:
        p = Path(args.save_json)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"[OK] écriture : {p}")
    if args.json:
        import sys
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        print(json.dumps(out, indent=2, ensure_ascii=False))
    else:
        gps_info = out['metadata_scanner']['results'].get('./sample_docs/photo.jpg', {}).get('gps', 'n/a')
        print(f"[SUMMARY] username={args.username} breaches={out['breach_checker']['breaches'][:5]} gps={gps_info}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
