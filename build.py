import json
import os
import html
from urllib.parse import quote_plus

SITE_URL = "https://thread.faultcodewiki.com"
MAIN_SITE_URL = "https://faultcodewiki.com"
AMAZON_TAG = "faultcodewiki-20"
DIST_DIR = "dist"


def amazon_url(query: str) -> str:
    return f"https://www.amazon.com/s?k={quote_plus(query)}&tag={AMAZON_TAG}"


CSS_CONTENT = """
:root {
  --bg: #f8fafc;
  --card: #ffffff;
  --text: #0f172a;
  --muted: #475569;
  --border: #cbd5e1;
  --primary: #1d4ed8;
  --primary-dark: #1e40af;
  --primary-soft: #eff6ff;
  --warn-bg: #fffbeb;
  --warn-border: #f59e0b;
  --warn-text: #92400e;
  --danger-bg: #fef2f2;
  --danger-border: #ef4444;
  --danger-text: #991b1b;
  --ok-bg: #f0fdf4;
  --ok-border: #22c55e;
  --ok-text: #166534;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  background: var(--bg);
  color: var(--text);
  line-height: 1.6;
  font-size: 16px;
}
a { color: var(--primary); text-decoration: none; }
a:hover { text-decoration: underline; }
.container { max-width: 920px; margin: 0 auto; padding: 0 16px; }
header {
  background: #0f172a;
  color: #ffffff;
  padding: 14px 0;
  border-bottom: 3px solid var(--primary);
}
.nav-wrap {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 10px;
}
.brand { font-weight: 800; font-size: 1.15rem; color: #ffffff; letter-spacing: -0.3px; }
.brand span { color: #60a5fa; }
.nav-links { display: flex; gap: 14px; font-size: 0.9rem; }
.nav-links a { color: #cbd5e1; }
.nav-links a:hover { color: #ffffff; text-decoration: none; }
.ref-banner {
  background: #e2e8f0;
  color: #334155;
  font-size: 0.82rem;
  text-align: center;
  padding: 7px 12px;
  border-bottom: 1px solid var(--border);
}
.hero { padding: 26px 0 16px; }
.hero h1 {
  font-size: 1.75rem;
  line-height: 1.25;
  letter-spacing: -0.5px;
  margin-bottom: 10px;
}
.hero p { color: var(--muted); font-size: 1rem; margin-bottom: 14px; }
.mistake-box {
  background: var(--warn-bg);
  border-left: 4px solid var(--warn-border);
  color: var(--warn-text);
  padding: 12px 14px;
  border-radius: 6px;
  font-size: 0.92rem;
  margin-bottom: 20px;
}
.card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 20px;
  margin-bottom: 22px;
  box-shadow: 0 1px 3px rgba(15, 23, 42, 0.05);
}
.section-label {
  font-size: 0.82rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: var(--muted);
  margin-bottom: 8px;
  display: block;
}
.preset-row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 18px;
}
.preset-btn {
  background: var(--primary-soft);
  border: 1px solid #bfdbfe;
  color: var(--primary-dark);
  padding: 8px 12px;
  border-radius: 8px;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  min-height: 40px;
}
.preset-btn:hover, .preset-btn.active {
  background: var(--primary);
  color: #ffffff;
  border-color: var(--primary);
}
.form-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
  margin-bottom: 16px;
}
.form-group { display: flex; flex-direction: column; gap: 6px; }
.form-group.full { grid-column: 1 / -1; }
label { font-weight: 600; font-size: 0.94rem; }
select {
  width: 100%;
  min-height: 48px;
  padding: 10px 12px;
  font-size: 16px;
  border: 1px solid #94a3b8;
  border-radius: 8px;
  background: #ffffff;
  color: var(--text);
  font-weight: 600;
}
.sys-tabs { display: flex; gap: 8px; margin-bottom: 14px; }
.sys-tab {
  flex: 1;
  min-height: 44px;
  border: 1px solid var(--border);
  background: #f1f5f9;
  color: var(--text);
  font-weight: 700;
  border-radius: 8px;
  cursor: pointer;
  font-size: 0.95rem;
}
.sys-tab.active {
  background: #0f172a;
  color: #ffffff;
  border-color: #0f172a;
}
.result-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 8px;
  border-bottom: 1px solid #e2e8f0;
  padding-bottom: 12px;
  margin-bottom: 16px;
}
.result-title { font-size: 1.25rem; font-weight: 800; }
.series-badge {
  background: #e2e8f0;
  color: #1e293b;
  padding: 4px 10px;
  border-radius: 999px;
  font-size: 0.82rem;
  font-weight: 700;
}
.drill-grid {
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  gap: 14px;
  margin-bottom: 16px;
}
.primary-drill-box {
  background: var(--primary-soft);
  border: 2px solid var(--primary);
  border-radius: 10px;
  padding: 16px;
}
.primary-drill-val {
  font-size: 1.9rem;
  font-weight: 900;
  color: var(--primary-dark);
  line-height: 1.15;
  margin: 4px 0 6px;
}
.sub-conv { font-size: 0.95rem; color: #1e3a8a; font-weight: 600; }
.compare-box {
  background: #f8fafc;
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 14px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 10px;
}
.dont-use {
  background: var(--danger-bg);
  border: 1px solid #fca5a5;
  color: var(--danger-text);
  padding: 8px 10px;
  border-radius: 6px;
  font-size: 0.86rem;
  font-weight: 600;
}
.alert-stack { display: flex; flex-direction: column; gap: 10px; margin-bottom: 16px; }
.alert-item {
  padding: 11px 14px;
  border-radius: 8px;
  font-size: 0.92rem;
}
.alert-pitch { background: var(--warn-bg); border: 1px solid #fcd34d; color: var(--warn-text); }
.alert-chuck { background: var(--danger-bg); border: 1px solid #f87171; color: var(--danger-text); font-weight: 600; }
.alert-method { background: var(--ok-bg); border: 1px solid #86efac; color: var(--ok-text); }
.depth-box {
  background: #f1f5f9;
  border-radius: 8px;
  padding: 13px 15px;
  margin-bottom: 18px;
  font-size: 0.93rem;
}
.depth-nums {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  margin-top: 6px;
  font-weight: 700;
  color: #0f172a;
}
.amz-section {
  border-top: 2px dashed var(--border);
  padding-top: 18px;
  margin-top: 16px;
}
.amz-main-card {
  background: #ffffff;
  border: 2px solid #0f172a;
  border-radius: 10px;
  padding: 16px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 14px;
  margin-bottom: 14px;
}
.amz-main-info h3 { font-size: 1.05rem; margin-bottom: 4px; }
.amz-main-info p { font-size: 0.88rem; color: var(--muted); }
.amz-btn-primary {
  background: #f59e0b;
  color: #0f172a;
  font-weight: 800;
  padding: 12px 18px;
  border-radius: 8px;
  white-space: nowrap;
  font-size: 0.95rem;
  display: inline-block;
  text-align: center;
}
.amz-btn-primary:hover { background: #d97706; text-decoration: none; }
.checklist-wrap {
  background: #f8fafc;
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 12px 14px;
}
.checklist-title {
  font-size: 0.86rem;
  font-weight: 700;
  color: var(--muted);
  margin-bottom: 8px;
}
.checklist-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 10px;
  padding: 8px 0;
  border-top: 1px solid #e2e8f0;
  font-size: 0.9rem;
}
.checklist-item:first-of-type { border-top: none; }
.amz-link-sub {
  font-weight: 700;
  font-size: 0.86rem;
  white-space: nowrap;
  padding: 6px 10px;
  border: 1px solid var(--border);
  border-radius: 6px;
  background: #ffffff;
}
.amz-disclosure {
  font-size: 0.78rem;
  color: var(--muted);
  margin-top: 10px;
}
.disclaimer-box {
  background: #f1f5f9;
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 14px;
  font-size: 0.82rem;
  color: #475569;
  margin-top: 18px;
}
.table-scroll { overflow-x: auto; -webkit-overflow-scrolling: touch; }
table { width: 100%; border-collapse: collapse; font-size: 0.9rem; min-width: 600px; }
th, td { padding: 10px 12px; border-bottom: 1px solid #e2e8f0; text-align: left; }
th { background: #f1f5f9; font-weight: 700; color: #1e293b; }
tr:hover td { background: #f8fafc; }
.faq-item { margin-bottom: 16px; padding-bottom: 14px; border-bottom: 1px solid #e2e8f0; }
.faq-item:last-child { border-bottom: none; margin-bottom: 0; padding-bottom: 0; }
.faq-item h3 { font-size: 1.02rem; margin-bottom: 6px; }
.faq-item p { color: var(--muted); font-size: 0.94rem; }
footer {
  background: #0f172a;
  color: #94a3b8;
  padding: 28px 0;
  margin-top: 36px;
  font-size: 0.85rem;
}
.footer-links { display: flex; flex-wrap: wrap; gap: 16px; margin-bottom: 12px; }
.footer-links a { color: #cbd5e1; }
@media (max-width: 700px) {
  .hero h1 { font-size: 1.42rem; }
  .form-grid, .drill-grid { grid-template-columns: 1fr; }
  .amz-main-card, .checklist-item { flex-direction: column; align-items: stretch; }
  .amz-btn-primary, .amz-link-sub { text-align: center; width: 100%; }
}
"""

DISCLAIMER_HTML = """
<div class="disclaimer-box">
  <strong>Disclaimer &amp; Trademark Notice:</strong> Calculations, drill bit sizes, and hole depths are general reference estimates modeled on standard STI (Screw Thread Insert) tolerances for informational purposes only. Always verify exact drill bit sizes, hole depths, and repair eligibility against your specific insert kit's printed instructions and the OEM service manual—especially on safety-critical automotive, engine, cylinder head, brake, steering, or structural components. The site operator assumes no liability for damaged castings, failed repairs, property damage, or injury. Heli-Coil&reg;, Time-Sert&reg;, and Big-Sert&reg; are registered trademarks of their respective owners; this website is an independent technical reference tool and is not affiliated with, sponsored by, or endorsed by any trademark owner.
</div>
"""


def render_layout(title: str, description: str, canonical_path: str, body_html: str, extra_head: str = "") -> str:
    canonical_url = f"{SITE_URL}{canonical_path}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(description)}">
  <link rel="canonical" href="{canonical_url}">
  <link rel="stylesheet" href="/assets/style.css">
  {extra_head}
</head>
<body>
  <header>
    <div class="container nav-wrap">
      <a href="/" class="brand">Thread<span>.FaultCodeWiki</span></a>
      <nav class="nav-links">
        <a href="/">Calculator</a>
        <a href="/#master-chart">STI Drill Chart</a>
        <a href="/about/">About</a>
        <a href="/disclaimer/">Disclaimer</a>
      </nav>
    </div>
  </header>
  <div class="ref-banner">
    Independent STI Thread Repair Reference Estimate &mdash; Always verify against your specific insert kit manual before drilling.
  </div>
  <main class="container">
    {body_html}
  </main>
  <footer>
    <div class="container">
      <div class="footer-links">
        <a href="/">Thread Repair Calculator</a>
        <a href="/about/">About Us</a>
        <a href="/disclaimer/">Legal Disclaimer</a>
        <a href="/privacy/">Privacy Policy</a>
        <a href="/terms/">Terms of Service</a>
        <a href="{MAIN_SITE_URL}">FaultCodeWiki Main</a>
      </div>
      <p>&copy; 2026 Thread.FaultCodeWiki.com &mdash; Independent Technical Reference. As an Amazon Associate, we earn from qualifying purchases.</p>
    </div>
  </footer>
</body>
</html>
"""


def build_home(threads: list) -> str:
    threads_json_inline = json.dumps(threads)

    rows_html = []
    for t in threads:
        chuck_flag = "1/2\" Reduced Shank Req." if t["over_half_inch_chuck"] else "Fits Standard 3/8\"-1/2\" Drill"
        rows_html.append(f"""
        <tr>
          <td><a href="/specs/{t['id']}/"><strong>{html.escape(t['label'])}</strong></a></td>
          <td><strong>{html.escape(t['sti_drill_primary'])}</strong></td>
          <td>{t['sti_drill_inch_dec']:.4f}&quot; / {t['sti_drill_mm']} mm</td>
          <td>{html.escape(t['standard_tap_drill'])}</td>
          <td>{html.escape(chuck_flag)}</td>
        </tr>""")

    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": "Can I use a standard tap drill chart for a wire thread insert (Heli-Coil style)?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "No. Wire thread inserts require an oversized STI (Screw Thread Insert) tap and a larger drill bit than standard bolt tapping. Using a standard tap drill hole will bind or snap an STI tap."
                }
            },
            {
                "@type": "Question",
                "name": "What drill bit size is needed for an M10x1.25 vs M10x1.5 thread repair?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Both M10x1.25 and M10x1.5 wire thread inserts typically use a 13/32 inch (approx. 10.3 mm to 10.4 mm) drill bit, but their STI taps are NOT interchangeable. Always verify thread pitch with a pitch gauge before tapping."
                }
            },
            {
                "@type": "Question",
                "name": "What should I do if a wire thread insert pulls out a second time?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Never stack wire coils inside each other. If a standard wire insert fails or the hole is wallowed out, step up to an externally oversized solid bushing system (such as a Big-Sert style insert) after checking casting wall thickness."
                }
            }
        ]
    }
    extra_head = f'<script type="application/ld+json">{json.dumps(faq_schema)}</script>'

    body = f"""
    <section class="hero">
      <h1>Check Before You Drill &mdash; Match Stripped Thread Repair Sizes in Seconds.</h1>
      <p>No more zooming into blurry PDF charts with greasy hands. Instant STI drill bit sizes, inch/mm shop conversions, blind-hole depths, and pitch warnings modeled on standard thread insert specs.</p>
      <div class="mistake-box">
        <strong>&#9888;&#65039; #1 Garage Mistake:</strong> Never use a standard tap drill chart for wire thread inserts&mdash;STI holes must be drilled larger. Always confirm thread pitch (e.g., M10&times;1.25 vs. M10&times;1.5) before touching aluminum or cast iron.
      </div>
    </section>

    <section class="card" aria-label="Stripped Thread Repair Calculator">
      <span class="section-label">Quick Garage Presets (1-Tap)</span>
      <div class="preset-row" id="presetRow">
        <button type="button" class="preset-btn" data-id="m6x1-0">M6 &times; 1.0</button>
        <button type="button" class="preset-btn" data-id="m8x1-25">M8 &times; 1.25</button>
        <button type="button" class="preset-btn active" data-id="m10x1-25">M10 &times; 1.25 (JIS)</button>
        <button type="button" class="preset-btn" data-id="m14x1-5">M14 &times; 1.5 (Drain Plug)</button>
        <button type="button" class="preset-btn" data-id="1-4-20-unc">1/4-20 UNC</button>
        <button type="button" class="preset-btn" data-id="3-8-16-unc">3/8-16 UNC</button>
      </div>

      <div class="sys-tabs">
        <button type="button" class="sys-tab active" id="tabAll" onclick="setSystemFilter('all')">All Sizes (Metric + SAE)</button>
        <button type="button" class="sys-tab" id="tabMetric" onclick="setSystemFilter('metric')">Metric (mm)</button>
        <button type="button" class="sys-tab" id="tabSae" onclick="setSystemFilter('sae')">SAE / Inch</button>
      </div>

      <div class="form-grid">
        <div class="form-group full">
          <label for="threadSelect">1. Stripped Bolt / Thread Size</label>
          <select id="threadSelect" onchange="updateCalculator()"></select>
        </div>
        <div class="form-group">
          <label for="lengthSelect">2. Insert Length (Blind Hole Depth)</label>
          <select id="lengthSelect" onchange="updateCalculator()">
            <option value="1.0">1.0D &mdash; Shallow Boss / Thin Plate</option>
            <option value="1.5" selected>1.5D &mdash; Standard Repair (Most Common)</option>
            <option value="2.0">2.0D &mdash; Deep / Soft Aluminum Casting</option>
          </select>
        </div>
        <div class="form-group">
          <label for="situationSelect">3. Repair Condition &amp; Application</label>
          <select id="situationSelect" onchange="updateCalculator()">
            <option value="standard" selected>First-Time Repair (General Bracket / Cover)</option>
            <option value="heavy">Oil Drain Pan / Spark Plug / High Torque</option>
            <option value="failed">2nd Attempt (Previous Insert Pulled Out)</option>
          </select>
        </div>
      </div>

      <div id="resultArea">
        <div class="result-header">
          <div>
            <div class="result-title" id="resTitle">M10 &times; 1.25 Thread Repair Specs</div>
            <div style="font-size:0.88rem;color:#475569;" id="resUses"></div>
          </div>
          <span class="series-badge" id="resSeries">Metric Fine</span>
        </div>

        <div class="drill-grid">
          <div class="primary-drill-box">
            <span class="section-label" style="color:#1e40af;">Recommended STI Drill Bit</span>
            <div class="primary-drill-val" id="resPrimaryDrill">13/32&quot;</div>
            <div class="sub-conv" id="resDecimalConv">0.4062&quot; &bull; 10.3 mm</div>
            <div style="font-size:0.85rem;color:#334155;margin-top:8px;" id="resAltDrill"></div>
          </div>
          <div class="compare-box">
            <div class="dont-use" id="resDontUse">
              &#10060; DO NOT use standard tap drill (8.8 mm) &mdash; hole will be too small for STI tap!
            </div>
            <div style="font-size:0.87rem;color:#334155;" id="resProNote"></div>
            <div><a href="/specs/m10x1-25/" id="resDetailLink" style="font-size:0.86rem;font-weight:700;">View full printable spec page &rarr;</a></div>
          </div>
        </div>

        <div class="alert-stack" id="alertStack"></div>

        <div class="depth-box">
          <strong>Blind Hole Minimum Drill Depth (Includes Tap Chamfer &amp; Tang Clearance):</strong>
          <div class="depth-nums">
            <span id="depthInsert">Insert Length: 15.0 mm (0.59&quot;)</span>
            <span id="depthMinDrill">Min. Hole Depth: 20.0 mm (0.79&quot;)</span>
          </div>
          <p style="font-size:0.82rem;color:#475569;margin-top:6px;">
            Tip: Wrap a piece of painter's tape around your drill bit at the minimum depth mark so you never drill into a coolant or oil passage. Break the installation tang only after seating the coil 1/4 to 1/2 turn below the flush surface.
          </p>
        </div>

        <div class="amz-section">
          <div class="amz-main-card">
            <div class="amz-main-info">
              <h3 id="amzMainTitle">Matching All-in-One Thread Repair Kit</h3>
              <p id="amzMainDesc">Includes matched STI drill bit, STI tap, installation mandrel, and stainless inserts in one box so sizes cannot mismatch.</p>
            </div>
            <a href="#" target="_blank" rel="nofollow sponsored noopener" class="amz-btn-primary" id="amzMainBtn">Check Current Price on Amazon</a>
          </div>

          <div class="checklist-wrap">
            <div class="checklist-title">Optional Project Checklist (Skip what you already have)</div>
            <div class="checklist-item">
              <span id="amzOpt1Label">1. Metric &amp; SAE Thread Pitch Gauge + Tap Cutting Fluid</span>
              <a href="#" target="_blank" rel="nofollow sponsored noopener" class="amz-link-sub" id="amzOpt1Btn">Check Current Price</a>
            </div>
            <div class="checklist-item">
              <span id="amzOpt2Label">2. Heavy-Duty Solid Bushing Alternative (For Oil Pans &amp; High Load)</span>
              <a href="#" target="_blank" rel="nofollow sponsored noopener" class="amz-link-sub" id="amzOpt2Btn">Check Current Price</a>
            </div>
          </div>
          <p class="amz-disclosure">
            Affiliate links: As an Amazon Associate, we earn from qualifying purchases at no extra cost to you. Always confirm final drill bit sizes against your kit manual before installation.
          </p>
        </div>

        {DISCLAIMER_HTML}
      </div>
    </section>

    <section class="card" id="master-chart">
      <h2 style="margin-bottom:8px;font-size:1.3rem;">Master STI Thread Repair Drill Chart (Metric &amp; SAE)</h2>
      <p style="color:#475569;font-size:0.92rem;margin-bottom:14px;">Click any thread size below to open its full blind-hole depth guide and compatibility notes.</p>
      <div class="table-scroll">
        <table>
          <thead>
            <tr>
              <th>Thread Size</th>
              <th>STI Drill Bit</th>
              <th>Decimal / mm</th>
              <th>Std. Tap Drill (Do Not Use)</th>
              <th>Drill Chuck Note</th>
            </tr>
          </thead>
          <tbody>
            {''.join(rows_html)}
          </tbody>
        </table>
      </div>
    </section>

    <section class="card">
      <h2 style="margin-bottom:14px;font-size:1.3rem;">Frequently Asked Questions</h2>
      <div class="faq-item">
        <h3>Why can't I use a normal tap drill chart for a stripped thread insert?</h3>
        <p>Standard tap drills cut threads directly for the original bolt diameter. Wire thread inserts and solid bushings sit between the bolt and the parent metal, so they require a dedicated oversized STI (Screw Thread Insert) tap and larger drill hole.</p>
      </div>
      <div class="faq-item">
        <h3>When should I choose a solid bushing (Time-Sert style) over a wire spring coil?</h3>
        <p>Standard stainless wire inserts work great on valve covers, brackets, and general blind holes. For aluminum oil drain pans, cylinder head spark plug ports, or bolts removed repeatedly under high torque, a flanged solid bushing prevents backing out and seals better.</p>
      </div>
      <div class="faq-item">
        <h3>What if my drill chuck only opens to 1/2 inch (13 mm)?</h3>
        <p>Repairs on M14, M16, 1/2-13, and 5/8-11 require STI drill bits larger than 0.500 inch. Either choose an all-in-one repair kit with a stepped shank or order a 1/2-inch reduced-shank (Silver &amp; Deming) drill bit.</p>
      </div>
    </section>

    <script>
      const THREADS = {threads_json_inline};
      const AMZ_TAG = "{AMAZON_TAG}";
      let currentSystem = "all";
      let selectedId = "m10x1-25";

      function makeAmzUrl(q) {{
        return "https://www.amazon.com/s?k=" + encodeURIComponent(q) + "&tag=" + AMZ_TAG;
      }}

      function setSystemFilter(sys) {{
        currentSystem = sys;
        document.getElementById("tabAll").classList.toggle("active", sys === "all");
        document.getElementById("tabMetric").classList.toggle("active", sys === "metric");
        document.getElementById("tabSae").classList.toggle("active", sys === "sae");
        populateDropdown();
      }}

      function populateDropdown() {{
        const sel = document.getElementById("threadSelect");
        const filtered = THREADS.filter(t => currentSystem === "all" || t.system === currentSystem);
        sel.innerHTML = "";
        let found = false;
        filtered.forEach(t => {{
          const opt = document.createElement("option");
          opt.value = t.id;
          opt.textContent = t.label + " — " + t.series + " (STI Drill: " + t.sti_drill_primary + ")";
          if (t.id === selectedId) {{
            opt.selected = true;
            found = true;
          }}
          sel.appendChild(opt);
        }});
        if (!found && filtered.length > 0) {{
          selectedId = filtered[0].id;
          sel.value = selectedId;
        }}
        updateCalculator();
      }}

      function updateCalculator() {{
        const sel = document.getElementById("threadSelect");
        if (sel.value) selectedId = sel.value;
        const item = THREADS.find(t => t.id === selectedId) || THREADS[0];
        const mult = parseFloat(document.getElementById("lengthSelect").value || "1.5");
        const sit = document.getElementById("situationSelect").value;

        document.querySelectorAll(".preset-btn").forEach(btn => {{
          btn.classList.toggle("active", btn.getAttribute("data-id") === item.id);
        }});

        document.getElementById("resTitle").textContent = item.label + " Thread Repair Specs";
        document.getElementById("resSeries").textContent = item.series;
        document.getElementById("resUses").textContent = "Common applications: " + item.common_uses;
        document.getElementById("resPrimaryDrill").textContent = item.sti_drill_primary;
        document.getElementById("resDecimalConv").textContent = item.sti_drill_inch_dec.toFixed(4) + '"  •  ' + item.sti_drill_mm + " mm";
        document.getElementById("resAltDrill").textContent = "Shop / Tolerance Alternative: " + item.alt_drill;
        document.getElementById("resDontUse").textContent = "❌ DO NOT use standard tap drill (" + item.standard_tap_drill + ") — too small for STI tap!";
        document.getElementById("resProNote").textContent = "Mechanic Note: " + item.pro_note;
        document.getElementById("resDetailLink").href = "/specs/" + item.id + "/";

        const insMm = item.diameter_mm * mult;
        const minHoleMm = insMm + (item.pitch_mm * 4.0);
        const insIn = insMm / 25.4;
        const minHoleIn = minHoleMm / 25.4;
        document.getElementById("depthInsert").textContent = "Insert Length (" + mult.toFixed(1) + "D): " + insMm.toFixed(1) + ' mm (' + insIn.toFixed(2) + '")';
        document.getElementById("depthMinDrill").textContent = "Min. Blind Hole Depth: " + minHoleMm.toFixed(1) + ' mm (' + minHoleIn.toFixed(2) + '")';

        const stack = document.getElementById("alertStack");
        let alertsHtml = '<div class="alert-item alert-pitch"><strong>⚠️ Pitch Verification:</strong> ' + item.pitch_warning + '</div>';
        if (item.over_half_inch_chuck) {{
          alertsHtml += '<div class="alert-item alert-chuck">🚨 <strong>1/2" (13 mm) Drill Chuck Alert:</strong> This STI bit exceeds standard cordless drill capacity. Use a 1/2" reduced-shank bit or an all-in-one kit with a stepped shank.</div>';
        }}
        if (sit === "heavy") {{
          alertsHtml += '<div class="alert-item alert-method"><strong>🔧 Recommended Method (High Load / Drain Pan / Plug):</strong> Consider a flanged <strong>Solid Thread Bushing</strong> (Time-Sert style) instead of an open spring coil to prevent oil/gas leaks and insert back-out.</div>';
        }} else if (sit === "failed") {{
          alertsHtml += '<div class="alert-item alert-method"><strong>🔧 Recommended Method (2nd Attempt / Pulled-Out Coil):</strong> Do NOT stack wire inserts! Step up to an externally <strong>Oversized Solid Bushing</strong> (Big-Sert style) after confirming adequate casting wall thickness around the boss.</div>';
        }}
        stack.innerHTML = alertsHtml;

        const mainTitle = document.getElementById("amzMainTitle");
        const mainDesc = document.getElementById("amzMainDesc");
        const mainBtn = document.getElementById("amzMainBtn");
        const opt1Label = document.getElementById("amzOpt1Label");
        const opt1Btn = document.getElementById("amzOpt1Btn");
        const opt2Label = document.getElementById("amzOpt2Label");
        const opt2Btn = document.getElementById("amzOpt2Btn");

        if (sit === "standard") {{
          mainTitle.textContent = item.label + " All-in-One Wire Thread Repair Kit";
          mainDesc.textContent = "Matched STI drill bit, STI tap, installation tool, and stainless inserts in one box.";
          mainBtn.href = makeAmzUrl(item.amazon_kit_query);
          opt2Label.textContent = "2. Heavy-Duty Solid Bushing Kit (" + item.label + " Upgrade Option)";
          opt2Btn.href = makeAmzUrl(item.solid_insert_query);
        }} else if (sit === "heavy") {{
          mainTitle.textContent = item.label + " Solid Bushing / Heavy-Duty Repair Kit";
          mainDesc.textContent = "Flanged solid insert system ideal for drain pans, spark plugs, and high-torque castings.";
          mainBtn.href = makeAmzUrl(item.solid_insert_query);
          opt2Label.textContent = "2. Standard " + item.label + " Wire Insert Kit (Budget Alternative)";
          opt2Btn.href = makeAmzUrl(item.amazon_kit_query);
        }} else {{
          mainTitle.textContent = item.label + " Oversized Solid Thread Repair Kit (2nd-Attempt Fix)";
          mainDesc.textContent = "Externally oversized wall bushing designed to salvage previously failed wire-insert holes.";
          mainBtn.href = makeAmzUrl(item.label + " oversized thread repair kit");
          opt2Label.textContent = "2. High-Temp Threadlocker (Red 2620 / Sleeve Retainer)";
          opt2Btn.href = makeAmzUrl("high temperature sleeve retainer threadlocker");
        }}

        if (item.over_half_inch_chuck) {{
          opt1Label.textContent = "1. 1/2-Inch Reduced-Shank Drill Bit (" + item.sti_drill_primary + ") + Cutting Fluid";
          opt1Btn.href = makeAmzUrl(item.sti_drill_primary + " reduced shank drill bit");
        }} else {{
          opt1Label.textContent = "1. Metric & SAE Thread Pitch Gauge + Tap Cutting Fluid";
          opt1Btn.href = makeAmzUrl("metric sae thread pitch gauge cutting fluid");
        }}
      }}

      document.querySelectorAll(".preset-btn").forEach(btn => {{
        btn.addEventListener("click", () => {{
          selectedId = btn.getAttribute("data-id");
          if (currentSystem !== "all") {{
            setSystemFilter("all");
          }} else {{
            document.getElementById("threadSelect").value = selectedId;
            updateCalculator();
          }}
        }});
      }});

      populateDropdown();
    </script>
    """
    return render_layout(
        title="Stripped Thread Repair & STI Drill Bit Size Calculator | Thread.FaultCodeWiki",
        description="Instant STI thread repair drill bit calculator for Metric and SAE bolts. Compare inch/mm bit conversions, blind hole depths, and pitch warnings before drilling.",
        canonical_path="/",
        body_html=body,
        extra_head=extra_head
    )


def build_spec_page(t: dict) -> str:
    d_mm = t["diameter_mm"]
    p_mm = t["pitch_mm"]
    depth_rows = []
    for mult, label in [(1.0, "1.0D (Shallow)"), (1.5, "1.5D (Standard)"), (2.0, "2.0D (Deep / Soft Alloy)")]:
        ins_mm = d_mm * mult
        hole_mm = ins_mm + (p_mm * 4.0)
        depth_rows.append(f"""
        <tr>
          <td><strong>{label}</strong></td>
          <td>{ins_mm:.1f} mm ({ins_mm/25.4:.2f}&quot;)</td>
          <td><strong>{hole_mm:.1f} mm ({hole_mm/25.4:.2f}&quot;)</strong></td>
        </tr>""")

    chuck_html = ""
    if t["over_half_inch_chuck"]:
        chuck_html = """
        <div class="alert-item alert-chuck" style="margin-bottom:14px;">
          &#128680; <strong>1/2&quot; (13 mm) Drill Chuck Warning:</strong> This STI drill diameter exceeds standard 1/2-inch hand drill chucks. Order a 1/2-inch reduced-shank drill bit or an all-in-one kit featuring a reduced shank.
        </div>"""

    opt1_q = f"{t['sti_drill_primary']} reduced shank drill bit" if t["over_half_inch_chuck"] else "metric sae thread pitch gauge"
    opt1_txt = f"1. Reduced-Shank {t['sti_drill_primary']} Drill Bit" if t["over_half_inch_chuck"] else "1. Metric & SAE Thread Pitch Gauge (Verify Pitch First)"

    body = f"""
    <section class="hero">
      <p style="font-size:0.88rem;margin-bottom:6px;"><a href="/">&larr; Back to Interactive Thread Repair Calculator</a></p>
      <h1>{html.escape(t['label'])} Thread Repair Drill Bit Size &amp; STI Tap Specs</h1>
      <p>Reference STI drill diameter, shop fractional/metric conversions, and minimum blind-hole depth chart for repairing stripped <strong>{html.escape(t['label'])}</strong> ({html.escape(t['series'])}) internal threads.</p>
    </section>

    <section class="card">
      <div class="drill-grid">
        <div class="primary-drill-box">
          <span class="section-label" style="color:#1e40af;">Recommended STI Drill Bit</span>
          <div class="primary-drill-val">{html.escape(t['sti_drill_primary'])}</div>
          <div class="sub-conv">{t['sti_drill_inch_dec']:.4f}&quot; &bull; {t['sti_drill_mm']} mm</div>
          <p style="font-size:0.86rem;color:#334155;margin-top:8px;"><strong>Shop Alternative:</strong> {html.escape(t['alt_drill'])}</p>
        </div>
        <div class="compare-box">
          <div class="dont-use">
            &#10060; Do NOT use standard {html.escape(t['label'])} tap drill ({html.escape(t['standard_tap_drill'])}) &mdash; STI repair taps require a larger hole!
          </div>
          <p style="font-size:0.88rem;color:#334155;"><strong>Common Applications:</strong> {html.escape(t['common_uses'])}</p>
        </div>
      </div>

      <div class="alert-item alert-pitch" style="margin-bottom:14px;">
        <strong>&#9888;&#65039; Pitch Mistake Warning:</strong> {html.escape(t['pitch_warning'])}
      </div>
      {chuck_html}
      <div class="alert-item alert-method" style="margin-bottom:18px;">
        <strong>Mechanic Field Note:</strong> {html.escape(t['pro_note'])}
      </div>

      <h2 style="font-size:1.15rem;margin-bottom:8px;">{html.escape(t['label'])} Minimum Blind Hole Drill Depth Chart</h2>
      <p style="font-size:0.88rem;color:#475569;margin-bottom:10px;">Includes 4 pitches of bottom clearance for STI tap starter chamfer and clean tang break-off.</p>
      <div class="table-scroll" style="margin-bottom:18px;">
        <table>
          <thead>
            <tr>
              <th>Insert Length Class</th>
              <th>Installed Coil Length</th>
              <th>Min. Blind Hole Drill Depth</th>
            </tr>
          </thead>
          <tbody>
            {''.join(depth_rows)}
          </tbody>
        </table>
      </div>

      <div class="amz-section">
        <div class="amz-main-card">
          <div class="amz-main-info">
            <h3>{html.escape(t['label'])} All-in-One Thread Repair Kit</h3>
            <p>Includes matched STI drill bit, STI tap, installation mandrel, and stainless steel inserts.</p>
          </div>
          <a href="{amazon_url(t['amazon_kit_query'])}" target="_blank" rel="nofollow sponsored noopener" class="amz-btn-primary">Check Current Price on Amazon</a>
        </div>

        <div class="checklist-wrap">
          <div class="checklist-title">Optional Project Checklist (Skip what you already have)</div>
          <div class="checklist-item">
            <span>{html.escape(opt1_txt)}</span>
            <a href="{amazon_url(opt1_q)}" target="_blank" rel="nofollow sponsored noopener" class="amz-link-sub">Check Current Price</a>
          </div>
          <div class="checklist-item">
            <span>2. {html.escape(t['label'])} Solid Bushing / Heavy-Duty Upgrade Kit</span>
            <a href="{amazon_url(t['solid_insert_query'])}" target="_blank" rel="nofollow sponsored noopener" class="amz-link-sub">Check Current Price</a>
          </div>
        </div>
        <p class="amz-disclosure">Affiliate links: As an Amazon Associate, we earn from qualifying purchases. Always verify drill size against your kit's printed chart before drilling.</p>
      </div>

      {DISCLAIMER_HTML}
    </section>
    """
    return render_layout(
        title=f"{t['label']} Thread Repair Drill Bit Size (STI Chart & Depth) | Thread.FaultCodeWiki",
        description=f"Find the exact STI drill bit size ({t['sti_drill_primary']} / {t['sti_drill_mm']} mm), blind hole depth, and pitch warnings for {t['label']} stripped thread repair.",
        canonical_path=f"/specs/{t['id']}/",
        body_html=body
    )


def build_policy_pages() -> dict:
    pages = {}
    pages["about"] = render_layout(
        title="About Thread.FaultCodeWiki | Independent Thread Repair Reference",
        description="Learn how Thread.FaultCodeWiki helps DIYers and mechanics match STI drill bit sizes and avoid costly stripped thread repair mistakes.",
        canonical_path="/about/",
        body_html="""
        <section class="hero"><h1>About Thread.FaultCodeWiki</h1></section>
        <section class="card">
          <p style="margin-bottom:12px;"><strong>Thread.FaultCodeWiki.com</strong> is a specialized engineering reference division of FaultCodeWiki built for home garage DIYers, automotive technicians, and maintenance machinists across North America.</p>
          <p style="margin-bottom:12px;">Most stripped-thread mistakes happen when someone misreads a tiny PDF chart on a phone screen, confuses a standard tap drill with an oversized STI (Screw Thread Insert) drill bit, or mixes up fine and coarse pitches such as M10&times;1.25 and M10&times;1.5.</p>
          <p style="margin-bottom:12px;">Our mobile-first calculator organizes standard Unified (UNC/UNF) and Metric STI reference tolerances into fast, clear shop cards complete with fractional-to-millimeter conversions, 1/2-inch drill chuck warnings, and blind-hole clearance estimates.</p>
          <h2 style="font-size:1.15rem;margin:18px 0 8px;">Contact</h2>
          <p>For technical feedback or corrections, please reach out via our main portal at <a href="https://faultcodewiki.com">FaultCodeWiki.com</a>.</p>
        </section>
        """
    )
    pages["disclaimer"] = render_layout(
        title="Legal Disclaimer & Trademark Notice | Thread.FaultCodeWiki",
        description="Legal disclaimer, safety notice, affiliate disclosure, and trademark statement for Thread.FaultCodeWiki.com.",
        canonical_path="/disclaimer/",
        body_html=f"""
        <section class="hero"><h1>Legal Disclaimer &amp; Trademark Notice</h1></section>
        <section class="card">
          <h2 style="font-size:1.15rem;margin-bottom:8px;">1. Informational Reference Only</h2>
          <p style="margin-bottom:14px;">All drill bit sizes, decimal conversions, tap clearances, and repair suggestions on Thread.FaultCodeWiki.com are provided strictly as general reference estimates modeled on published STI (Screw Thread Insert) standards. Different insert manufacturers and specialty kits (such as thin-wall, solid bushing, or piloted spark plug systems) may require proprietary drill and tap dimensions. Always follow the printed instructions included inside your specific thread repair kit.</p>
          <h2 style="font-size:1.15rem;margin-bottom:8px;">2. Safety-Critical Automotive &amp; Structural Components</h2>
          <p style="margin-bottom:14px;">Some OEM vehicle and equipment manufacturers prohibit thread inserts in safety-critical assemblies such as brake calipers, steering knuckles, suspension mounts, wheel hubs, or cylinder head bolts. Always consult the official OEM service manual and a qualified professional mechanic or machinist before attempting any repair.</p>
          <h2 style="font-size:1.15rem;margin-bottom:8px;">3. Trademark Notice (Nominative Fair Use)</h2>
          <p style="margin-bottom:14px;">Heli-Coil&reg;, Time-Sert&reg;, Big-Sert&reg;, and Sav-A-Thread&reg; are registered trademarks of their respective owners. Thread.FaultCodeWiki.com is an independent reference website and is not affiliated with, endorsed by, or sponsored by Stanley Black &amp; Decker, Time Fastener Company, or any other manufacturer.</p>
          <h2 style="font-size:1.15rem;margin-bottom:8px;">4. Affiliate Disclosure</h2>
          <p>Thread.FaultCodeWiki.com participates in the Amazon Services LLC Associates Program. As an Amazon Associate, we earn from qualifying purchases when users click outbound product links, at zero additional cost to the buyer.</p>
          {DISCLAIMER_HTML}
        </section>
        """
    )
    pages["privacy"] = render_layout(
        title="Privacy Policy | Thread.FaultCodeWiki",
        description="Privacy policy, cookie usage, Google AdSense, and Amazon Associates disclosure for Thread.FaultCodeWiki.com.",
        canonical_path="/privacy/",
        body_html="""
        <section class="hero"><h1>Privacy Policy</h1></section>
        <section class="card">
          <p style="margin-bottom:12px;">Effective Date: November 2026</p>
          <p style="margin-bottom:12px;">Thread.FaultCodeWiki.com respects visitor privacy. Our thread repair calculator runs directly in your browser and does not require account registration or personal data submission.</p>
          <h2 style="font-size:1.15rem;margin:16px 0 8px;">Cookies &amp; Advertising</h2>
          <p style="margin-bottom:12px;">Third-party vendors, including Google (Google AdSense / Google Analytics), may use cookies to serve ads or measure traffic based on a user's prior visits to this website or other websites. Users may opt out of personalized advertising by visiting Google Ads Settings.</p>
          <h2 style="font-size:1.15rem;margin:16px 0 8px;">Outbound Affiliate Links</h2>
          <p>When you click an outbound Amazon link, Amazon may place a standard affiliate cookie to track qualifying purchases in accordance with Amazon's own Privacy Notice.</p>
        </section>
        """
    )
    pages["terms"] = render_layout(
        title="Terms of Service | Thread.FaultCodeWiki",
        description="Terms of use and limitation of liability for Thread.FaultCodeWiki.com.",
        canonical_path="/terms/",
        body_html="""
        <section class="hero"><h1>Terms of Service</h1></section>
        <section class="card">
          <p style="margin-bottom:12px;">By accessing and using Thread.FaultCodeWiki.com, you agree that all calculators, charts, and technical notes are provided "AS IS" without warranties of any kind, either express or implied.</p>
          <p style="margin-bottom:12px;">You assume sole responsibility for verifying fastener thread pitch, parent metal wall thickness, blind hole depth, and OEM repair eligibility before drilling or tapping any workpiece. Under no circumstances shall the site operator be liable for direct, indirect, or consequential damages resulting from the use of this website.</p>
        </section>
        """
    )
    return pages


def write_file(rel_path: str, content: str):
    full_path = os.path.join(DIST_DIR, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")


def main():
    with open("threads.json", "r", encoding="utf-8") as f:
        threads = json.load(f)

    write_file("assets/style.css", CSS_CONTENT)
    write_file("index.html", build_home(threads))

    urls = [f"{SITE_URL}/"]
    for t in threads:
        write_file(f"specs/{t['id']}/index.html", build_spec_page(t))
        urls.append(f"{SITE_URL}/specs/{t['id']}/")

    for slug, html_doc in build_policy_pages().items():
        write_file(f"{slug}/index.html", html_doc)
        urls.append(f"{SITE_URL}/{slug}/")

    sitemap_items = "\n".join([f"  <url><loc>{u}</loc></url>" for u in urls])
    sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{sitemap_items}
</urlset>"""
    write_file("sitemap.xml", sitemap_xml)

    robots_txt = f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n"
    write_file("robots.txt", robots_txt)
    print(f"Build complete: generated {len(urls)} pages in {DIST_DIR}/")


if __name__ == "__main__":
    main()
