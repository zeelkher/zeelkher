"""Generates the SVG assets used by README.md.
Run:  python scripts/gen_assets.py
Change ACCENT to re-theme the whole profile in one place."""
import pathlib

OUT = pathlib.Path(__file__).resolve().parent.parent / "assets"
OUT.mkdir(parents=True, exist_ok=True)

FONT = "'JetBrains Mono','Fira Code','Cascadia Code','SF Mono',Menlo,Consolas,'Liberation Mono','Courier New',monospace"
BG, PANEL = "#0D0D0D", "#0D1117"
ACCENT = "#00D1B2"           # teal accent (Akshat's uses red #E53935)
WHITE, GREY, DIM, LINE = "#F4F4F4", "#8B9097", "#5C6168", "#222831"


def write(name, svg):
    p = OUT / name
    p.write_text(svg.strip() + "\n", encoding="utf-8", newline="\n")
    print("wrote", p.name, len(svg), "bytes")


def banner():
    W, H = 1280, 320
    widths = [3, 1, 5, 2, 1, 6, 2, 1, 3, 4, 1, 2, 6, 1, 3, 2, 1, 5, 1, 2, 4, 1, 3, 6, 2, 1, 3, 2]
    x, bars = 1000, []
    for i, w in enumerate(widths):
        if i % 6 == 2:
            fill, op = ACCENT, ".9"
        elif i % 4 == 0:
            fill, op = "#4A4F57", "1"
        else:
            fill, op = "#2A2E34", "1"
        bars.append(f'<rect x="{x}" y="122" width="{w}" height="52" fill="{fill}" opacity="{op}"/>')
        x += w + 4
    sq = []
    for r in range(3):
        for c in range(3):
            fill = ACCENT if (r + c) % 2 == 0 else "#2A2E34"
            sq.append(f'<rect x="{1204 + c * 14}" y="{122 + r * 14}" width="8" height="8" fill="{fill}"/>')
    barcode = "\n".join(bars)
    squares = "\n".join(sq)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">
<title id="t">ZEEL KHER — SOFTWARE · SYSTEMS · EXPERIMENTS</title>
<desc id="d">Hero banner: dark textured background, teal accent marks, monospace type.</desc>
<style>
.mono{{font-family:{FONT}}}
.name{{font-size:92px;font-weight:800;letter-spacing:3px;fill:{WHITE}}}
.ghost{{font-size:92px;font-weight:800;letter-spacing:3px;fill:{ACCENT};opacity:.4}}
.sub{{font-size:22px;font-weight:700;letter-spacing:6px;fill:{ACCENT}}}
.meta{{font-size:13px;font-weight:500;letter-spacing:2px;fill:{GREY}}}
.tiny{{font-size:11px;letter-spacing:2px;fill:{DIM}}}
.cursor{{animation:blink 1.1s steps(1) infinite}}
.sweep{{animation:sweep 7s linear infinite}}
@keyframes blink{{0%,49%{{opacity:1}}50%,100%{{opacity:0}}}}
@keyframes sweep{{0%{{transform:translateY(-10px)}}100%{{transform:translateY({H + 10}px)}}}}
@media (prefers-reduced-motion:reduce){{.cursor,.sweep{{animation:none}}}}
</style>
<defs>
<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#191919" stroke-width="1"/></pattern>
<pattern id="scan" width="3" height="3" patternUnits="userSpaceOnUse"><rect width="3" height="1" fill="#000" opacity=".22"/></pattern>
<pattern id="hatch" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="1" height="8" fill="{ACCENT}" opacity=".25"/></pattern>
<filter id="noise" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="7" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/><feComponentTransfer><feFuncA type="linear" slope=".07"/></feComponentTransfer></filter>
<radialGradient id="glow" cx=".2" cy=".55" r=".55"><stop offset="0" stop-color="{ACCENT}" stop-opacity=".14"/><stop offset="1" stop-color="{ACCENT}" stop-opacity="0"/></radialGradient>
<linearGradient id="sweepg" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="{ACCENT}" stop-opacity="0"/><stop offset=".5" stop-color="{ACCENT}" stop-opacity=".16"/><stop offset="1" stop-color="{ACCENT}" stop-opacity="0"/></linearGradient>
</defs>
<rect width="{W}" height="{H}" fill="{BG}"/>
<rect width="{W}" height="{H}" fill="url(#grid)"/>
<rect width="{W}" height="{H}" fill="url(#glow)"/>
<rect width="{W}" height="{H}" filter="url(#noise)"/>
<rect x="940" y="228" width="316" height="44" fill="url(#hatch)"/>
<rect width="{W}" height="{H}" fill="url(#scan)"/>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" fill="none" stroke="#222222"/>
<rect x="0" y="0" width="460" height="3" fill="{ACCENT}"/>
<rect x="820" y="{H - 3}" width="460" height="3" fill="{ACCENT}"/>
<path d="M22 46V22h24M1234 22h24v24M22 274v24h24M1234 298h24v-24" fill="none" stroke="{ACCENT}" stroke-width="2"/>
<path d="M640 34v12M634 40h12M640 274v12M634 280h12M900 154v12M894 160h12" stroke="#3A3A3A" stroke-width="1"/>
<rect x="58" y="34" width="8" height="8" fill="{ACCENT}"/>
<text x="76" y="42" class="mono meta">FILE 000 // OPERATION: ITERATE</text>
<text x="1210" y="42" text-anchor="end" class="mono meta">INDEPENDENT MIND // CONTINUOUS ITERATIONS</text>
<rect x="1218" y="34" width="8" height="8" fill="{ACCENT}"/>
<rect x="58" y="284" width="8" height="8" fill="{ACCENT}"/><rect x="70" y="284" width="8" height="8" fill="{ACCENT}" opacity=".55"/><rect x="82" y="284" width="8" height="8" fill="{ACCENT}" opacity=".25"/>
<text x="100" y="292" class="mono tiny">SYS.STATUS: ONLINE</text>
<text x="1210" y="292" text-anchor="end" class="mono tiny">LAB LOG // 2026</text>
<rect x="96" y="108" width="6" height="128" fill="{ACCENT}"/>
<text x="116" y="180" class="mono ghost" transform="translate(-3 2)">ZEEL KHER</text>
<text x="116" y="180" class="mono name">ZEEL KHER</text>
<text x="118" y="226" class="mono sub">SOFTWARE · SYSTEMS · EXPERIMENTS<tspan class="cursor">_</tspan></text>
{barcode}
<text x="1000" y="198" class="mono tiny">0D0D0D // {ACCENT} // F4F4F4</text>
{squares}
<rect class="sweep" x="1" y="0" width="{W - 2}" height="10" fill="url(#sweepg)"/>
</svg>'''
    write("banner.svg", svg)


def section(num, label, slug, total=5):
    W, H = 900, 64
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="// {num} {label}">
<title>// {num} {label}</title>
<style>
.mono{{font-family:{FONT}}}
.h{{font-size:22px;font-weight:700;letter-spacing:3px;fill:{ACCENT}}}
.tag{{font-size:12px;letter-spacing:2px;fill:{DIM}}}
</style>
<defs>
<pattern id="scan" width="3" height="3" patternUnits="userSpaceOnUse"><rect width="3" height="1" fill="#000" opacity=".2"/></pattern>
<linearGradient id="ul" x1="0" x2="1" y1="0" y2="0"><stop offset="0" stop-color="{ACCENT}"/><stop offset=".3" stop-color="{ACCENT}" stop-opacity=".45"/><stop offset="1" stop-color="{ACCENT}" stop-opacity="0"/></linearGradient>
</defs>
<rect width="{W}" height="{H}" fill="{PANEL}"/>
<rect width="{W}" height="{H}" fill="url(#scan)"/>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" fill="none" stroke="{LINE}"/>
<rect x="0" y="0" width="5" height="{H}" fill="{ACCENT}"/>
<rect x="24" y="26" width="10" height="10" fill="{ACCENT}"/>
<text x="48" y="39" class="mono h">// {num} {label}</text>
<rect x="0" y="{H - 2}" width="{W}" height="2" fill="url(#ul)"/>
<text x="852" y="37" text-anchor="end" class="mono tag">SECTION {num} / {total:02d}</text>
<rect x="866" y="24" width="7" height="7" fill="{ACCENT}"/><rect x="866" y="34" width="7" height="7" fill="{ACCENT}" opacity=".5"/><rect x="876" y="24" width="7" height="7" fill="{ACCENT}" opacity=".5"/><rect x="876" y="34" width="7" height="7" fill="{ACCENT}" opacity=".2"/>
</svg>'''
    write(f"section-{num}-{slug}.svg", svg)


def tags():
    W, H = 560, 44
    words = ["BUILD", "LEARN", "ITERATE", "SHIP"]
    bw, bh, gap = 112, 36, 24
    x, parts = 20, []
    for i, w in enumerate(words):
        parts.append(f'<rect x="{x + .5}" y="4.5" width="{bw - 1}" height="{bh - 1}" fill="{PANEL}" stroke="{ACCENT}" stroke-width="1.5"/>')
        parts.append(f'<rect x="{x + 6}" y="10" width="4" height="4" fill="{ACCENT}"/>')
        parts.append(f'<text x="{x + bw / 2}" y="27" text-anchor="middle" class="mono t">{w}</text>')
        if i < len(words) - 1:
            parts.append(f'<rect x="{x + bw + gap / 2 - 2.5}" y="{4 + bh / 2 - 2.5}" width="5" height="5" fill="{ACCENT}" opacity=".7"/>')
        x += bw + gap
    body = "\n".join(parts)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="BUILD • LEARN • ITERATE • SHIP">
<title>BUILD • LEARN • ITERATE • SHIP</title>
<style>
.mono{{font-family:{FONT}}}
.t{{font-size:13px;font-weight:700;letter-spacing:3px;fill:{WHITE}}}
</style>
{body}
</svg>'''
    write("tags-about.svg", svg)


def footer():
    W, H = 1280, 72
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="BUILD · LEARN · DEBUG · REPEAT">
<title>BUILD · LEARN · DEBUG · REPEAT</title>
<style>
.mono{{font-family:{FONT}}}
.motto{{font-size:20px;font-weight:700;letter-spacing:6px}}
.a{{fill:#B4B9C0}}
.b{{fill:{ACCENT}}}
.tiny{{font-size:11px;letter-spacing:2px;fill:{DIM}}}
</style>
<defs>
<pattern id="scan" width="3" height="3" patternUnits="userSpaceOnUse"><rect width="3" height="1" fill="#000" opacity=".22"/></pattern>
<linearGradient id="top" x1="0" x2="1" y1="0" y2="0"><stop offset="0" stop-color="{ACCENT}" stop-opacity="0"/><stop offset=".5" stop-color="{ACCENT}"/><stop offset="1" stop-color="{ACCENT}" stop-opacity="0"/></linearGradient>
</defs>
<rect width="{W}" height="{H}" fill="{BG}"/>
<rect width="{W}" height="{H}" fill="url(#scan)"/>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" fill="none" stroke="#222222"/>
<rect x="0" y="0" width="{W}" height="2" fill="url(#top)"/>
<rect x="820" y="{H - 2}" width="460" height="2" fill="{ACCENT}"/>
<rect x="24" y="32" width="8" height="8" fill="{ACCENT}"/><rect x="36" y="32" width="8" height="8" fill="{ACCENT}" opacity=".55"/><rect x="48" y="32" width="8" height="8" fill="{ACCENT}" opacity=".25"/>
<text x="68" y="40" class="mono tiny">ZEEL.KHER</text>
<text x="{W // 2}" y="43" text-anchor="middle" class="mono motto"><tspan class="a">BUILD · LEARN · DEBUG ·</tspan><tspan class="b" dx="14">REPEAT</tspan></text>
<text x="1256" y="40" text-anchor="end" class="mono tiny">// END OF FILE</text>
</svg>'''
    write("footer.svg", svg)


banner()
section("01", "ABOUT ME", "about")
section("02", "TECH STACK", "tech-stack")
section("03", "SELECTED PROJECTS", "projects")
section("04", "GITHUB ACTIVITY", "github-stats")
section("05", "LET'S CONNECT", "connect")
tags()
footer()
