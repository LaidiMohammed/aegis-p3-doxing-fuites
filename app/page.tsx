import Console from "@/components/Console";
import Reveal from "@/components/Reveal";

const MODULES = [
  ["01", "username_correlator", "sherlock CLI (local) → comptes associés à un identifiant générique."],
  ["02", "breach_checker", "Have I Been Pwned API v3 → listes des fuites connues pour un email de test."],
  ["03", "metadata_scanner", "exiftool → métadonnées GPS / appareil sur fichiers locaux factices."],
  ["04", "doxing_audit", "Orchestration complète — 7 tests mocks réussis."],
];

export default function Page() {
  return (
    <main className="min-h-screen bg-paper">
      <nav className="sticky top-0 z-40 border-b border-coal/20 bg-paper/95 backdrop-blur">
        <div className="mx-auto flex max-w-7xl items-center justify-between px-5 py-4">
          <a href="#top" className="flex items-center gap-3">
            <span className="grid h-9 w-9 place-items-center bg-coal font-mono text-xs font-bold text-paper">P3</span>
            <span className="coord text-coal/70">DOSSIER · FUITES SOCIALES</span>
          </a>
          <div className="hidden gap-7 md:flex">
            {[["#modules","Modules"],["#audit","Audit"],["#demo","Démo"],["#ethique","Éthique"]].map(([h,l])=><a key={h} href={h} className="coord text-coal/55 hover:text-red">{l}</a>)}
          </div>
          <a href="https://github.com/LaidiMohammed/aegis-p3-doxing-fuites" target="_blank" rel="noreferrer" className="border border-coal/40 px-3 py-1.5 font-mono text-[11px] hover:bg-coal hover:text-paper">GitHub ↗</a>
        </div>
      </nav>

      <div className="overflow-hidden border-b border-coal/20 bg-coal py-2 text-paper">
        <div className="tick-track coord">
          {Array.from({length:2}).map((_,k)=><span key={k} className="flex shrink-0 gap-10 px-5"><span>ANONYMISÉ</span><span>▮</span><span>IDENTIFIANT GÉNÉRIQUE</span><span>▮</span><span>7 TESTS MOCKS</span><span>▮</span><span>0 GPU · 0 CLOUD</span><span>▮</span></span>)}
        </div>
      </div>

      <section id="top" className="mx-auto grid max-w-7xl gap-12 px-5 py-16 lg:grid-cols-[1fr_1fr] lg:items-center lg:py-20">
        <div>
          <Reveal><div className="mb-5 flex items-center gap-3"><span className="h-px w-12 bg-red"/><span className="coord text-red">Fiche technique · P3</span></div></Reveal>
          <Reveal delay={70}><h1 className="typed text-5xl font-bold leading-[1.05] sm:text-6xl">Fuites<br/><span className="text-red">sociales</span><br/>&amp; doxing</h1></Reveal>
          <Reveal delay={140}><p className="mt-6 max-w-xl text-base leading-relaxed text-coal/75">Corrélation d'identités numériques et détection de fuites de données — sur des <b className="text-coal">cibles libres et génériques</b>, entièrement anonymisé.</p></Reveal>
          <Reveal delay={210}><div className="mt-7 flex flex-wrap gap-3"><a href="#audit" className="bg-coal px-6 py-3 font-mono text-xs font-bold uppercase tracking-widest text-paper hover:bg-red">Ouvrir le dossier ↓</a><a href="#modules" className="border border-coal/50 px-6 py-3 font-mono text-xs uppercase tracking-widest hover:border-red hover:text-red">Les modules</a></div></Reveal>
          <Reveal delay={280}><div className="mt-10 flex flex-wrap gap-8 border-t border-coal/20 pt-6">{[["04","modules"],["07","tests mocks"],["1","rapport PDF"],["00","compte réel"]].map(([n,l])=><div key={l}><div className="typed text-2xl font-bold">{n}</div><div className="coord text-coal/45">{l}</div></div>)}</div></Reveal>
        </div>
        <Reveal delay={120}><Console /></Reveal>
      </section>

      <section id="modules" className="mx-auto max-w-7xl px-5 py-14">
        <Reveal><span className="coord text-red">01 / Modules</span><h2 className="typed mt-2 text-4xl font-bold sm:text-5xl">Quatre outils, un audit</h2></Reveal>
        <div className="mt-8 grid gap-x-10 gap-y-6 md:grid-cols-2">
          {MODULES.map(([n,t,d],i)=>(
            <Reveal key={n} delay={i*70}><div className="file-paper h-full p-6 pl-10">
              <div className="flex items-baseline justify-between"><span className="typed text-3xl text-red">{n}</span><span className="coord text-coal/50">{t}</span></div>
              <p className="mt-3 font-mono text-sm leading-relaxed text-coal/75">{d}</p>
            </div></Reveal>
          ))}
        </div>
      </section>

      <section id="audit" className="mx-auto max-w-7xl px-5 py-14">
        <Reveal><span className="coord text-red">02 /Architecture</span><h2 className="typed mt-2 text-4xl font-bold sm:text-5xl">Pipeline d'audit</h2></Reveal>
        <div className="mt-8 grid gap-6 lg:grid-cols-2">
          <Reveal><div className="file-paper p-7 pl-10">
            <pre className="whitespace-pre-wrap font-mono text-xs leading-loose text-coal/80">
{`doxing_audit(username, email):
  username_correlator(username)   # sherlock
  breach_checker(email)           # HIBP v3
  metadata_scanner()              # exiftool
  → { app, username, ...results }`}
            </pre>
          </div></Reveal>
          <Reveal delay={100}><div className="border-l-2 border-red pl-6">
            <span className="coord text-red">Sortie structurée</span>
            <p className="mt-3 font-mono text-sm text-coal/75">&#123; app, username, username_correlator, breach_checker, metadata_scanner &#125;</p>
            <div className="my-6 h-px bg-coal/20" />
            <p className="font-mono text-sm leading-relaxed text-coal/70">Toutes les entrées/sorties réseau et subprocess sont <b>mockables</b> dans les tests (patch requests / subprocess).</p>
          </div></Reveal>
        </div>
      </section>

      <section id="demo" className="mx-auto max-w-7xl px-5 py-14">
        <Reveal><span className="coord text-red">03 / Démonstration</span><h2 className="typed mt-2 text-4xl font-bold sm:text-5xl">Commandes</h2></Reveal>
        <div className="mt-8 space-y-2 font-mono text-[12px]">
          {["python -m src.doxing_fuites_main --username testuser123 --save-json outputs/results.json --json","python -m src.generate_report --json outputs/results.json --pdf outputs/rapport-p3.pdf"].map(c=><div key={c} className="border-l-2 border-red bg-white/50 px-4 py-3 text-coal"><span className="text-red">$</span> {c}</div>)}
        </div>
      </section>

      <section id="ethique" className="mx-auto max-w-7xl px-5 py-14">
        <Reveal><span className="coord text-red">04 / Éthique</span><h2 className="typed mt-2 text-4xl font-bold sm:text-5xl">Règle P3</h2></Reveal>
        <div className="mt-6 file-paper p-7 pl-10 max-w-3xl">
          <p className="typed text-lg leading-relaxed">Identifiant générique — <span className="redact">aucun compte réel</span> — Smoke uniquement. Aucune donnée personnelle n'est collectée ni exposée ; les résultats sont anonymisés.</p>
        </div>
      </section>

      <footer className="border-t-2 border-coal bg-coal text-paper">
        <div className="mx-auto flex max-w-7xl flex-wrap items-center justify-between gap-6 px-5 py-10">
          <div><div className="typed text-2xl font-bold">P3 <span className="text-red">/ FUITES SOCIALES</span></div><div className="coord mt-1 text-paper/50">Master 1 PFE · Laidi Mohammed · 2026</div></div>
          <div className="flex gap-5 font-mono text-xs text-paper/70"><a href="https://github.com/LaidiMohammed/aegis-p3-doxing-fuites" target="_blank" rel="noreferrer" className="hover:text-red">GitHub ↗</a><a href="https://aegis-p3-doxing-fuites.vercel.app" className="hover:text-red">Vercel ↗</a></div>
        </div>
      </footer>
    </main>
  );
}
