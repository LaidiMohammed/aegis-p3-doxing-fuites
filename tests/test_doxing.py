"""Tests unitaires — P3 Doxing / fuites sociales (mocks — no shell).

- username_correlator : mock subprocess.Popen — returns JSON platforms
- breach_checker : mock requests.get — returns breaches
- metadata_scanner : mock subprocess.run — returns exiftool output
- doxing_audit : stucture clé bien formée
- generate_report : md + pdf
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src import doxing_fuites_main as m
from src import generate_report as rep


class FakePopen:
    def __init__(self, out_raw: str):
        self._out = out_raw

    def communicate(self, timeout=None):
        return self._out, ""

    def __enter__(self): return self
    def __exit__(self, *a): pass


def fake_req(status=404, breaches=None):
    return SimpleNamespace(status_code=status, json=lambda: (breaches or []))


def test_username_correlator_mock():
    with patch.object(m.subprocess, "Popen", return_value=FakePopen('["aegis.xyz","tweet.com"]')):
        out = m.username_correlator("testuser123")
    assert out["username"] == "testuser123" and len(out["platforms"]) == 2 and out["total"] == 2


def test_breach_checker_404():
    with patch.object(m.requests, "get", return_value=fake_req(404)):
        out = m.breach_checker("test@example.com")
    assert out["status"] == 404 and out["breaches"] == []


def test_breach_checker_found():
    with patch.object(m.requests, "get", return_value=fake_req(200, [{"Name": "Adobe"}])):
        out = m.breach_checker("test@example.com")
    assert out["status"] == 200 and out["breaches"] == ["Adobe"]


def test_metadata_scanner_mock():
    fake_run = MagicMock()
    fake_run.stdout = json.dumps([{"GPSLatitude": 36.7378, "GPSLongitude": 3.0742}])
    with patch.object(m.subprocess, "run", return_value=fake_run):
        out = m.metadata_scanner(["./sample_docs/photo.jpg"])
    assert out["results"]["./sample_docs/photo.jpg"]["gps"] == {"lat": 36.7378, "long": 3.0742}


def test_doxing_audit_structure():
    with patch.object(m, "username_correlator", return_value={"username": "u", "platforms": [], "total": 0}), \
         patch.object(m, "breach_checker", return_value={"email": "e", "breaches": [], "status": 404}), \
         patch.object(m, "metadata_scanner", return_value={"scanned_paths": [], "results": {}}):
        out = m.doxing_audit("testuser123", "e@x.com")
    assert set(out.keys()) == {"app", "username", "username_correlator", "breach_checker", "metadata_scanner"}


def test_generate_report_files(tmp_path):
    data = {"app": "aegis-p3-doxing-fuites", "username": "testuser123",
            "username_correlator": {"username": "testuser123", "platforms": ["aegis.xyz", "tweet.com"], "total": 2},
            "breach_checker": {"email": "e@x.com", "breaches": ["Adobe"], "status": 200},
            "metadata_scanner": {"scanned_paths": ["./sample_docs/photo.jpg"],
                                 "results": {"./sample_docs/photo.jpg": {"metadata": [], "gps": {"lat": 36.7, "long": 3.07}}}}}
    md = rep.build_markdown(data)
    assert "testuser123" in md and "aegis.xyz" in md
    out = tmp_path / "r.pdf"
    rep.build_pdf(md, out)
    assert out.exists() and out.stat().st_size > 500


def test_main_smoke():
    assert m.main([]) == 0


if __name__ == "__main__":
    pytest.main([__file__, "-q"])
