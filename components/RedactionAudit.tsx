"use client";
import { useState } from "react";

const MODULES = [
  { fn: "username_correlator", out: "platforms: 12 comptes corrélés", redact: "GitHub · Twitter · Reddit" },
  { fn: "breach_checker", out: "breaches: 3 fuites détectées", redact: "LinkedIn · Adobe · Dropbox" },
  { fn: "metadata_scanner", out: "EXIF GPS present: true", redact: "48.85°N / 2.35°E" },
];

export default function RedactionAudit() {
  const [run, setRun] = useState(false);
  return (
    <div className="file-paper p-6 pl-10">
      <div className="flex items-start justify-between gap-3">
        <div>
          <span className="coord text-red">dossier · audit P3</span>
          <h3 className="typed mt-1 text-2xl">doxing_audit()</h3>
        </div>
        <span className="stamp text-xs">anonymisé</span>
      </div>

      <div className="my-5 border-t border-coal/20" />

      <div className="space-y-4 font-mono text-[12.5px]">
        <div><span className="text-red">$</span> python -m src.doxing_fuites_main --username <span className="redact">testuser123</span></div>
        {MODULES.map((m, i) => (
          <div key={m.fn} className="border-l-2 border-coal/25 pl-4">
            <div className="text-coal/70">{m.fn}</div>
            {run ? (
              <div className="mt-1">
                <div className="text-coal">{m.out}</div>
                <div className="mt-1"><span className="redact">{m.redact}</span></div>
              </div>
            ) : (
              <div className="mt-1 text-fog">— en attente —</div>
            )}
          </div>
        ))}
      </div>

      <div className="scanbar mt-4" style={{ width: run ? "100%" : 0 }} />

      <div className="mt-4 border-t border-coal/20 pt-3 font-mono text-[11px] text-coal/55">
        {run ? "[SUMMARY] username=test█████ breaches=[████] gps=████ · 7/7 tests mocks" : "cible générique · aucun compte réel · données anonymisées"}
      </div>

      <button
        onClick={() => setRun(!run)}
        className="mt-5 w-full border-2 border-coal bg-coal px-5 py-3 font-mono text-xs font-bold uppercase tracking-widest text-paper transition hover:bg-red hover:border-red"
      >
        {run ? "↺ Fermer le dossier" : "◆ Exécuter l'audit"}
      </button>
    </div>
  );
}
