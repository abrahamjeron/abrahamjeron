#!/usr/bin/env python3
"""Generates assets/neofetch.svg - dark-blue terminal panel for the profile README."""
from html import escape

ART = [
    "░█▀█░█▀▄░█▀▄░█▀█░█░█░█▀█░█▄█",
    "░█▀█░█▀▄░█▀▄░█▀█░█▀█░█▀█░█░█",
    "░▀░▀░▀▀░░▀░▀░▀░▀░▀░▀░▀░▀░▀░▀",
    "",
    "░░░░░▀▀█░█▀▀░█▀▄░█▀█░█▀█░░░░",
    "░░░░░░░█░█▀▀░█▀▄░█░█░█░█░░░░",
    "░░░░░▀▀░░▀▀▀░▀░▀░▀▀▀░▀░▀░░░░",
]

# (key, value) | ("--",) blank | ("##", title)
ROWS = [
    ("##", "abraham@jeron"),
    ("OS", "Arch Linux · Ubuntu 22.04"),
    ("Uptime", "3 years building for the web"),
    ("Host", "Coimbatore, India"),
    ("School", "Kalvium · BCA, University of Mysore"),
    ("Kernel", "Software Engineer"),
    ("Editor", "VS Code · Neovim"),
    ("--",),
    ("##", "Stack"),
    ("Languages", "TypeScript, JavaScript, Python, SQL"),
    ("AI.Systems", "LangChain, Genkit, Claude SDK, RAG"),
    ("Frontend", "React, Next.js, Tailwind"),
    ("Backend", "Node.js, Express, Prisma"),
    ("Databases", "PostgreSQL, MongoDB, Firebase"),
    ("Cloud", "Google Cloud Platform, Firebase"),
    ("--",),
    ("##", "Interests"),
    ("Building", "Agentic systems, LLM tooling, RAG"),
    ("Open.Source", "Samagra X · C4GT squads"),
    ("Offline", "UI/UX design, chess, hackathons"),
]

BG, PANEL, CYAN, VIOLET, MAGENTA, TEXT, DIM = (
    "#0A0E27", "#101A3D", "#00D9FF", "#7B61FF", "#FF4B91", "#C9D6FF", "#3B4A80",
)

FS = 13.0
CW = FS * 0.6                      # monospace advance
COLS = 58                          # dotted-leader field width in chars
X_ART, X_INFO, Y0, LH = 44, 300, 132, 19.5

parts = []
add = parts.append

add(f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="{Y0 + len(ROWS)*LH + 78}"
     viewBox="0 0 900 {Y0 + len(ROWS)*LH + 78}" role="img" aria-label="abraham@jeron neofetch">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#070B1E"/><stop offset="100%" stop-color="{BG}"/>
    </linearGradient>
    <linearGradient id="ink" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{CYAN}"/><stop offset="100%" stop-color="{VIOLET}"/>
    </linearGradient>
    <filter id="glow" x="-25%" y="-25%" width="150%" height="150%">
      <feGaussianBlur stdDeviation="2.6" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <pattern id="grid" width="26" height="26" patternUnits="userSpaceOnUse">
      <path d="M26 0H0V26" fill="none" stroke="{CYAN}" stroke-width="0.5" stroke-opacity="0.06"/>
    </pattern>
    <clipPath id="win"><rect x="10" y="10" width="880" height="{Y0 + len(ROWS)*LH + 56}" rx="12"/></clipPath>
  </defs>
  <g clip-path="url(#win)">
    <rect x="10" y="10" width="880" height="{Y0 + len(ROWS)*LH + 56}" fill="url(#bg)"/>
    <rect x="10" y="10" width="880" height="{Y0 + len(ROWS)*LH + 56}" fill="url(#grid)"/>
    <rect x="10" y="10" width="880" height="38" fill="{PANEL}"/>
  </g>
  <rect x="10" y="10" width="880" height="{Y0 + len(ROWS)*LH + 56}" rx="12" fill="none" stroke="#1E2A5A" stroke-width="1.5"/>
  <line x1="10" y1="48" x2="890" y2="48" stroke="#1E2A5A" stroke-width="1.5"/>
  <circle cx="34" cy="29" r="6" fill="#FF5F57"/><circle cx="54" cy="29" r="6" fill="#FEBC2E"/><circle cx="74" cy="29" r="6" fill="#28C840"/>
  <text x="450" y="34" text-anchor="middle" font-family="ui-monospace,'JetBrains Mono','DejaVu Sans Mono',monospace"
        font-size="12.5" fill="{DIM}">abraham@jeron: ~</text>''')

# prompt
add(f'''
  <text x="44" y="82" font-family="ui-monospace,'JetBrains Mono','DejaVu Sans Mono',monospace" font-size="13.5">
    <tspan fill="{CYAN}">abraham@jeron</tspan><tspan fill="{TEXT}">:</tspan><tspan fill="{VIOLET}">~</tspan><tspan fill="{TEXT}">$ neofetch</tspan>
  </text>''')

# ASCII monogram
add(f'''
  <g font-family="'DejaVu Sans Mono',ui-monospace,monospace" font-size="14.5" fill="url(#ink)"
     filter="url(#glow)" xml:space="preserve">''')
for i, line in enumerate(ART):
    add(f'    <text x="{X_ART}" y="{Y0 + 46 + i*15}">{escape(line)}</text>')
add("  </g>")

# info column
add(f'''
  <g font-family="ui-monospace,'JetBrains Mono','DejaVu Sans Mono',monospace" font-size="{FS}" xml:space="preserve">''')
y = Y0
for row in ROWS:
    if row[0] == "--":
        y += LH
        continue
    if row[0] == "##":
        add(f'    <text x="{X_INFO}" y="{y}" fill="{CYAN}" font-weight="600">{escape(row[1])}</text>')
        add(f'    <line x1="{X_INFO}" y1="{y+7}" x2="856" y2="{y+7}" stroke="#1E2A5A" stroke-width="1"/>')
        y += LH + 4
        continue
    key, val = row
    label = key + ":"
    dots = max(2, COLS - len(label) - len(val))
    add(
        f'    <text x="{X_INFO}" y="{y}">'
        f'<tspan fill="{VIOLET}">{escape(label)}</tspan>'
        f'<tspan fill="{DIM}"> {"." * dots} </tspan>'
        f'<tspan fill="{TEXT}">{escape(val)}</tspan></text>'
    )
    y += LH
add("  </g>")

# closing prompt + cursor
cy_ = Y0 + len(ROWS) * LH + 30
add(f'''
  <text x="44" y="{cy_}" font-family="ui-monospace,'JetBrains Mono','DejaVu Sans Mono',monospace" font-size="13.5">
    <tspan fill="{CYAN}">abraham@jeron</tspan><tspan fill="{TEXT}">:</tspan><tspan fill="{VIOLET}">~</tspan><tspan fill="{TEXT}">$ </tspan>
  </text>
  <rect x="182" y="{cy_-11}" width="8" height="14" fill="{MAGENTA}">
    <animate attributeName="opacity" values="1;1;0;0" dur="1.1s" repeatCount="indefinite"/>
  </rect>
</svg>''')

open("assets/neofetch.svg", "w").write("\n".join(parts))
print("wrote assets/neofetch.svg")
