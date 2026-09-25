"""Generate the animated SVG assets used by the profile README.

Run from the repository root:

    python3 assets/generate.py

The generated SVGs are committed so GitHub can render the profile without a
build step. Edit PROFILE_LINES or the palette below to update the content.
"""

import random
from html import escape
from pathlib import Path


OUT = Path(__file__).parent

# Deep-ocean palette: calm, technical and high-contrast on GitHub dark mode.
BG = "#07111f"
BG_2 = "#0b1b2b"
BORDER = "#17354a"
FG = "#d8f3ff"
MUTED = "#a8c2d1"
COMMENT = "#58768a"
BLUE = "#5cc8ff"
CYAN = "#8be9fd"
GREEN = "#73e2a7"
PURPLE = "#a78bfa"
RED = "#ff6b81"
YELLOW = "#ffd166"
SANS = "'Segoe UI', 'Helvetica Neue', Ubuntu, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'DejaVu Sans Mono', monospace"


def hero() -> str:
    """Return the animated profile header."""
    rng = random.Random(2105)
    particles = []
    for _ in range(48):
        x, y = rng.uniform(10, 990), rng.uniform(10, 270)
        radius = rng.choice([0.7, 0.9, 1.1, 1.4, 1.8])
        duration = rng.uniform(2.4, 5.2)
        delay = rng.uniform(0, 4)
        particles.append(
            f'<circle class="particle" cx="{x:.0f}" cy="{y:.0f}" r="{radius}" '
            f'style="animation-duration:{duration:.1f}s;animation-delay:{delay:.1f}s"/>'
        )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="280" viewBox="0 0 1000 280" role="img" aria-label="Nguyễn Đức Mạnh — AI Engineer · Agentic AI · Computer Vision">
  <style>
    .particle {{ fill: {FG}; animation: pulse 3.2s ease-in-out infinite both; }}
    .orb-a {{ animation: drift-a 15s ease-in-out infinite alternate; }}
    .orb-b {{ animation: drift-b 18s ease-in-out infinite alternate; }}
    .name {{ font: 800 70px {SANS}; letter-spacing: .5px; stroke-width: 1.3; stroke-dasharray: 1100;
             animation: draw 2.5s ease-out both, fill-in 1s ease 1.4s both; }}
    .rule {{ transform-box: fill-box; transform-origin: center; animation: grow 1.1s cubic-bezier(.2,.8,.2,1) 1.9s both; }}
    .role {{ font: 500 21px {SANS}; letter-spacing: 1.4px; fill: {MUTED}; animation: rise 1s ease 2.2s both; }}
    .dot {{ fill: {GREEN}; }}
    @keyframes pulse {{ 0%, 100% {{ opacity: .12 }} 50% {{ opacity: .9 }} }}
    @keyframes drift-a {{ from {{ transform: translate(-70px, -5px) }} to {{ transform: translate(130px, 20px) }} }}
    @keyframes drift-b {{ from {{ transform: translate(90px, 15px) }} to {{ transform: translate(-120px, -20px) }} }}
    @keyframes draw {{ from {{ stroke-dashoffset: 1100 }} to {{ stroke-dashoffset: 0 }} }}
    @keyframes fill-in {{ from {{ fill-opacity: 0 }} to {{ fill-opacity: 1 }} }}
    @keyframes grow {{ from {{ transform: scaleX(0); opacity: 0 }} to {{ transform: scaleX(1); opacity: 1 }} }}
    @keyframes rise {{ from {{ opacity: 0; transform: translateY(12px) }} to {{ opacity: 1; transform: translateY(0) }} }}
    @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
  </style>
  <defs>
    <clipPath id="card"><rect width="1000" height="280" rx="18"/></clipPath>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{BG}"/><stop offset="1" stop-color="{BG_2}"/>
    </linearGradient>
    <linearGradient id="shine" x1="0" y1="0" x2="520" y2="0" gradientUnits="userSpaceOnUse" spreadMethod="repeat">
      <stop offset="0" stop-color="{BLUE}"/><stop offset=".35" stop-color="{CYAN}"/>
      <stop offset=".7" stop-color="{GREEN}"/><stop offset="1" stop-color="{BLUE}"/>
      <animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="520 0" dur="5.5s" repeatCount="indefinite"/>
    </linearGradient>
    <linearGradient id="rule" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{BLUE}" stop-opacity="0"/><stop offset=".5" stop-color="{GREEN}"/>
      <stop offset="1" stop-color="{BLUE}" stop-opacity="0"/>
    </linearGradient>
    <filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="48"/></filter>
    <filter id="glow" x="-10%" y="-40%" width="120%" height="180%">
      <feGaussianBlur stdDeviation="6" result="blurred"/>
      <feMerge><feMergeNode in="blurred"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <g clip-path="url(#card)">
    <rect width="1000" height="280" fill="url(#bg)"/>
    <ellipse class="orb-a" cx="280" cy="90" rx="270" ry="90" fill="{BLUE}" opacity=".2" filter="url(#blur)"/>
    <ellipse class="orb-b" cx="750" cy="205" rx="285" ry="82" fill="{GREEN}" opacity=".15" filter="url(#blur)"/>
    {''.join(particles)}
  </g>
  <rect x=".5" y=".5" width="999" height="279" rx="18" fill="none" stroke="{BORDER}"/>
  <text class="name" x="500" y="140" text-anchor="middle" fill="url(#shine)" stroke="url(#shine)" filter="url(#glow)">Nguyễn Đức Mạnh</text>
  <rect class="rule" x="355" y="162" width="290" height="2" rx="1" fill="url(#rule)"/>
  <text class="role" x="500" y="204" text-anchor="middle">AI Engineer <tspan class="dot">·</tspan> Agentic AI <tspan class="dot">·</tspan> Computer Vision</text>
</svg>
"""


# (kind, payload): command lines are typed one character at a time; output
# lines appear together. Keeping this data separate makes the asset easy to
# personalize later.
PROFILE_LINES = [
    ("cmd", "whoami"),
    ("out", [(FG, "Nguyễn Đức Mạnh"), (COMMENT, " — "), (MUTED, "AI Engineer · Ha Noi, Viet Nam")]),
    ("cmd", "cat profile.yml"),
    ("kv", ("education", "Information Technology · AI specialization")),
    ("kv", ("focus    ", "Agent systems · Computer vision · ML products")),
    ("kv", ("strengths", "Python · FastAPI · PyTorch · Docker")),
    ("kv", ("building ", "Agent Orchestrator · rPPG Heart Rate")),
    ("kv", ("mindset  ", "End-to-end · measurable · production-minded")),
    ("cmd", "echo $MOTTO"),
    ("out", [(YELLOW, '"Build it. Measure it. Make it useful."')]),
]


def terminal() -> str:
    """Return an animated terminal that introduces the profile."""
    type_speed = 0.068
    after_command = 0.4
    after_output = 0.2
    hold = 6.0
    line_height = 28
    x_origin = 28
    y_origin = 82
    height = y_origin + line_height * len(PROFILE_LINES) + 44

    now = 0.8
    timeline = []
    for kind, payload in PROFILE_LINES:
        if kind == "cmd":
            chars = [now + index * type_speed for index in range(len(payload))]
            timeline.append((now, chars))
            now += len(payload) * type_speed + after_command
        else:
            timeline.append((now, None))
            now += after_output

    final_prompt_at = now + 0.2
    cycle = final_prompt_at + hold

    def show(at: float) -> str:
        key = at / cycle
        return (
            f'<animate attributeName="visibility" values="hidden;visible;hidden" '
            f'keyTimes="0;{key:.4f};0.985" dur="{cycle:.2f}s" calcMode="discrete" repeatCount="indefinite"/>'
        )

    prompt = (
        f'<tspan fill="{GREEN}">manh</tspan><tspan fill="{COMMENT}"> in </tspan>'
        f'<tspan fill="{BLUE}">~</tspan><tspan fill="{PURPLE}"> ❯ </tspan>'
    )
    lines = []
    for index, ((kind, payload), (at, char_times)) in enumerate(zip(PROFILE_LINES, timeline)):
        y = y_origin + index * line_height
        if kind == "cmd":
            typed = "".join(
                f'<tspan fill="{FG}">{escape(char)}{show(char_at)}</tspan>'
                for char, char_at in zip(payload, char_times)
            )
            lines.append(f'<text x="{x_origin}" y="{y}">{prompt}{typed}{show(at)}</text>')
        elif kind == "kv":
            key, value = payload
            body = (
                f'<tspan fill="{CYAN}" xml:space="preserve">  {escape(key)}</tspan>'
                f'<tspan fill="{COMMENT}"> : </tspan><tspan fill="{MUTED}">{escape(value)}</tspan>'
            )
            lines.append(f'<text x="{x_origin}" y="{y}" xml:space="preserve">{body}{show(at)}</text>')
        else:
            body = "".join(f'<tspan fill="{color}">{escape(text)}</tspan>' for color, text in payload)
            lines.append(f'<text x="{x_origin}" y="{y}" xml:space="preserve">  {body}{show(at)}</text>')

    final_y = y_origin + len(PROFILE_LINES) * line_height
    cursor = (
        f'<tspan fill="{FG}">█<animate attributeName="fill-opacity" values="1;0" dur="1.1s" '
        f'calcMode="discrete" repeatCount="indefinite"/></tspan>'
    )
    lines.append(f'<text x="{x_origin}" y="{final_y}">{prompt}{cursor}{show(final_prompt_at)}</text>')

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="900" height="{height}" viewBox="0 0 900 {height}" role="img" aria-label="Terminal profile for Nguyễn Đức Mạnh">
  <defs>
    <linearGradient id="edge" x1="0" y1="0" x2="900" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="{BLUE}"/><stop offset=".5" stop-color="{GREEN}"/><stop offset="1" stop-color="{CYAN}"/>
      <animateTransform attributeName="gradientTransform" type="rotate" values="0 450 {height / 2};360 450 {height / 2}" dur="9s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <rect x="1" y="1" width="898" height="{height - 2}" rx="14" fill="{BG}" stroke="url(#edge)" stroke-width="1.5" stroke-opacity=".8"/>
  <path d="M1 15 a14 14 0 0 1 14 -14 H885 a14 14 0 0 1 14 14 V40 H1 Z" fill="{BG_2}"/>
  <line x1="1" y1="40" x2="899" y2="40" stroke="{BORDER}"/>
  <circle cx="24" cy="21" r="6" fill="{RED}"/><circle cx="44" cy="21" r="6" fill="{YELLOW}"/><circle cx="64" cy="21" r="6" fill="{GREEN}"/>
  <text x="450" y="26" text-anchor="middle" fill="{COMMENT}" font-family="{SANS}" font-size="13">manh@ngducmanh21 — zsh</text>
  <g font-family="{MONO}" font-size="16">
    {' '.join(lines)}
  </g>
</svg>
"""


def divider() -> str:
    """Return an animated comet divider."""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="14" viewBox="0 0 1000 14" role="img" aria-label="">
  <style>
    .comet {{ animation: fly 4.8s cubic-bezier(.45,0,.55,1) infinite; }}
    @keyframes fly {{ from {{ transform: translateX(-240px) }} to {{ transform: translateX(1000px) }} }}
    @media (prefers-reduced-motion: reduce) {{ .comet {{ animation: none; opacity: 0 }} }}
  </style>
  <defs>
    <linearGradient id="base" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{BORDER}" stop-opacity="0"/><stop offset=".5" stop-color="{BORDER}"/><stop offset="1" stop-color="{BORDER}" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="tail" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{BLUE}" stop-opacity="0"/><stop offset=".82" stop-color="{CYAN}"/><stop offset="1" stop-color="{GREEN}"/>
    </linearGradient>
    <filter id="glow" x="-20%" y="-300%" width="140%" height="700%"><feGaussianBlur stdDeviation="2.5"/></filter>
  </defs>
  <rect y="6.5" width="1000" height="1" fill="url(#base)"/>
  <g class="comet">
    <rect y="5" width="220" height="4" rx="2" fill="url(#tail)" filter="url(#glow)"/>
    <rect y="6" width="220" height="2" rx="1" fill="url(#tail)"/>
  </g>
</svg>
"""


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for filename, builder in {
        "hero.svg": hero,
        "terminal.svg": terminal,
        "divider.svg": divider,
    }.items():
        target = OUT / filename
        target.write_text(builder(), encoding="utf-8")
        print(f"wrote {target}")
