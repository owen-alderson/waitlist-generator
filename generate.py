#!/usr/bin/env python3
"""
waitlist-generator — generate a deployable waitlist landing page from the command line.

Usage:
  python3 generate.py

You'll be prompted for:
  - Startup name
  - Tagline (one-liner)
  - 3 value proposition bullets
  - CTA button text
  - Optional: accent color, logo emoji

Output: index.html — ready to push to GitHub Pages.
"""

import sys
from pathlib import Path
from datetime import datetime


TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{name} — {tagline}</title>
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

    :root {{
      --accent: {accent};
      --bg: #0a0a0f;
      --surface: #13131a;
      --border: #1e1e2e;
      --text: #f0f0f5;
      --subtext: #8888aa;
    }}

    body {{
      background: var(--bg);
      color: var(--text);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }}

    /* ── Nav ── */
    nav {{
      padding: 20px 40px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--border);
    }}
    .logo {{ font-size: 1.1rem; font-weight: 700; letter-spacing: -.02em; }}
    .logo span {{ color: var(--accent); }}
    .nav-tag {{
      font-size: .75rem; font-weight: 600;
      background: color-mix(in srgb, var(--accent) 15%, transparent);
      color: var(--accent);
      border: 1px solid color-mix(in srgb, var(--accent) 30%, transparent);
      padding: 4px 12px; border-radius: 999px;
    }}

    /* ── Hero ── */
    .hero {{
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      padding: 80px 24px 60px;
    }}

    .badge {{
      display: inline-flex; align-items: center; gap: 6px;
      font-size: .8rem; font-weight: 600;
      color: var(--accent);
      background: color-mix(in srgb, var(--accent) 10%, transparent);
      border: 1px solid color-mix(in srgb, var(--accent) 25%, transparent);
      padding: 5px 14px; border-radius: 999px;
      margin-bottom: 28px;
    }}

    h1 {{
      font-size: clamp(2.2rem, 6vw, 4rem);
      font-weight: 800;
      letter-spacing: -.04em;
      line-height: 1.1;
      max-width: 700px;
      margin-bottom: 20px;
    }}
    h1 em {{
      font-style: normal;
      background: linear-gradient(135deg, var(--accent), color-mix(in srgb, var(--accent) 60%, white));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }}

    .tagline {{
      font-size: 1.15rem;
      color: var(--subtext);
      max-width: 520px;
      line-height: 1.6;
      margin-bottom: 48px;
    }}

    /* ── Form ── */
    .form-wrap {{
      display: flex;
      gap: 10px;
      max-width: 460px;
      width: 100%;
      margin-bottom: 16px;
      flex-wrap: wrap;
      justify-content: center;
    }}

    .form-wrap input {{
      flex: 1;
      min-width: 220px;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 10px;
      color: var(--text);
      padding: 13px 16px;
      font-size: .95rem;
      outline: none;
      transition: border-color .15s;
    }}
    .form-wrap input:focus {{ border-color: var(--accent); }}
    .form-wrap input::placeholder {{ color: var(--subtext); }}

    .cta-btn {{
      background: var(--accent);
      color: #fff;
      border: none;
      border-radius: 10px;
      padding: 13px 24px;
      font-size: .95rem;
      font-weight: 700;
      cursor: pointer;
      transition: opacity .15s, transform .1s;
      white-space: nowrap;
    }}
    .cta-btn:hover {{ opacity: .9; transform: translateY(-1px); }}
    .cta-btn:active {{ transform: translateY(0); }}

    .form-note {{
      font-size: .8rem;
      color: var(--subtext);
      margin-bottom: 64px;
    }}

    /* ── Value props ── */
    .props {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
      max-width: 720px;
      width: 100%;
    }}
    @media (max-width: 600px) {{ .props {{ grid-template-columns: 1fr; }} }}

    .prop {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 20px;
      text-align: left;
    }}
    .prop-icon {{
      font-size: 1.4rem;
      margin-bottom: 10px;
    }}
    .prop-title {{
      font-size: .9rem;
      font-weight: 700;
      margin-bottom: 6px;
    }}
    .prop-desc {{
      font-size: .82rem;
      color: var(--subtext);
      line-height: 1.5;
    }}

    /* ── Footer ── */
    footer {{
      padding: 20px 40px;
      border-top: 1px solid var(--border);
      font-size: .8rem;
      color: var(--subtext);
      text-align: center;
    }}

    /* ── Success state ── */
    .success {{
      display: none;
      flex-direction: column;
      align-items: center;
      gap: 8px;
      padding: 16px 24px;
      background: color-mix(in srgb, var(--accent) 10%, transparent);
      border: 1px solid color-mix(in srgb, var(--accent) 30%, transparent);
      border-radius: 12px;
      margin-bottom: 64px;
      max-width: 400px;
      text-align: center;
    }}
    .success .check {{ font-size: 1.8rem; }}
    .success p {{ font-size: .9rem; color: var(--subtext); }}
    .success strong {{ color: var(--text); }}
  </style>
</head>
<body>

  <nav>
    <div class="logo">{emoji} <span>{name}</span></div>
    <div class="nav-tag">Early Access</div>
  </nav>

  <main class="hero">
    <div class="badge">✦ Now accepting early members</div>

    <h1>{h1}</h1>
    <p class="tagline">{tagline}</p>

    <div class="form-wrap" id="form-wrap">
      <input type="email" id="email-input" placeholder="Enter your email" />
      <button class="cta-btn" onclick="handleSubmit()">{cta}</button>
    </div>

    <div class="success" id="success-box">
      <div class="check">✓</div>
      <p><strong>You're on the list.</strong><br />We'll be in touch when access opens.</p>
    </div>

    <p class="form-note" id="form-note">No spam. Unsubscribe anytime.</p>

    <div class="props">
      {props_html}
    </div>
  </main>

  <footer>
    © {year} {name} &nbsp;·&nbsp; Built with <a href="https://github.com/owen-alderson/waitlist-generator" style="color:var(--accent);text-decoration:none">waitlist-generator</a>
  </footer>

  <script>
    function handleSubmit() {{
      const email = document.getElementById('email-input').value.trim();
      if (!email || !email.includes('@')) {{
        document.getElementById('email-input').style.borderColor = '#f87171';
        return;
      }}
      document.getElementById('form-wrap').style.display = 'none';
      document.getElementById('form-note').style.display = 'none';
      const box = document.getElementById('success-box');
      box.style.display = 'flex';
      // Log to console so you can wire up a real backend later
      console.log('Waitlist signup:', email);
    }}
    document.getElementById('email-input').addEventListener('keydown', e => {{
      if (e.key === 'Enter') handleSubmit();
    }});
  </script>

</body>
</html>
"""

PROP_TEMPLATE = """\
      <div class="prop">
        <div class="prop-icon">{icon}</div>
        <div class="prop-title">{title}</div>
        <div class="prop-desc">{desc}</div>
      </div>"""

PROP_ICONS = ["⚡", "🎯", "🔒", "🌍", "✦", "→"]
DEFAULT_ACCENT = "#4f8ef7"


def prompt(label: str, default: str = "") -> str:
    hint = f" [{default}]" if default else ""
    val = input(f"  {label}{hint}: ").strip()
    return val or default


def parse_prop(text: str) -> tuple[str, str]:
    """Split 'Title: description' or just return as title with empty desc."""
    if ":" in text:
        title, _, desc = text.partition(":")
        return title.strip(), desc.strip()
    return text.strip(), ""


def build_h1(name: str, tagline: str) -> str:
    """Generate a simple styled headline."""
    words = tagline.split()
    if len(words) <= 5:
        return f"<em>{tagline}</em>"
    # Italicize the last 2-3 words
    split = max(len(words) - 3, len(words) // 2)
    plain = " ".join(words[:split])
    em = " ".join(words[split:])
    return f"{plain} <em>{em}</em>"


def generate(
    name: str,
    tagline: str,
    props: list[str],
    cta: str,
    accent: str,
    emoji: str,
    output_path: Path,
):
    props_html = ""
    for i, prop in enumerate(props[:3]):
        title, desc = parse_prop(prop)
        props_html += PROP_TEMPLATE.format(
            icon=PROP_ICONS[i], title=title, desc=desc or title
        )

    html = TEMPLATE.format(
        name=name,
        tagline=tagline,
        h1=build_h1(name, tagline),
        cta=cta,
        accent=accent,
        emoji=emoji,
        props_html=props_html,
        year=datetime.now().year,
    )

    output_path.write_text(html, encoding="utf-8")


def main():
    print("\n  ✦  Waitlist Page Generator\n")
    print("  Answer a few questions — your page will be ready in seconds.\n")

    name    = prompt("Startup name", "Tidepool")
    tagline = prompt("One-liner tagline", "Shared field notes for small research teams")
    cta     = prompt("CTA button text", "Request Access")
    accent  = prompt("Accent color (hex)", DEFAULT_ACCENT)
    emoji   = prompt("Logo emoji", "✦")

    print("\n  Value propositions (format: 'Title: short description')\n")
    props = []
    for i in range(1, 4):
        p = prompt(f"  Prop {i}", f"Feature {i}: A key benefit of your product")
        props.append(p)

    output = Path("index.html")
    generate(
        name=name, tagline=tagline, props=props,
        cta=cta, accent=accent, emoji=emoji,
        output_path=output,
    )

    print(f"\n  ✓  Generated: {output.resolve()}")
    print(f"  →  Open in browser: open index.html")
    print(f"  →  Deploy: push to GitHub Pages\n")


if __name__ == "__main__":
    main()
