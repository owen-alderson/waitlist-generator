# waitlist-generator

Generate a deployable waitlist landing page in under 60 seconds. Answer a few prompts — get a clean, dark-themed HTML page ready to push to GitHub Pages.

No dependencies. No frameworks. Pure Python + HTML/CSS.

## Usage

```bash
python3 generate.py
```

Answer the prompts:

```
  Startup name [Acme]: Acme
  One-liner tagline: Shared field notes for small research teams
  CTA button text [Request Access]: Request Access
  Accent color (hex) [#4f8ef7]: #c9a84c
  Logo emoji [✦]: ✦

  Value propositions (format: 'Title: short description')
  Prop 1: Shared notebooks: Every note, photo and sample in one place
  Prop 2: Works offline: Record in the field, sync when you're back
  Prop 3: Built for teams: Invite your whole lab on the free plan

  ✓  Generated: /path/to/index.html
  →  Open in browser: open index.html
  →  Deploy: push to GitHub Pages
```

## Output

A single `index.html` file with:
- Gradient headline with accent color
- Email capture form with input validation
- 3 value proposition cards
- Success state on signup (console-logs the email — wire up a backend when ready)
- Fully responsive

## Deploy to GitHub Pages

```bash
# In a new repo or existing one:
git add index.html
git commit -m "Add waitlist page"
git push

# Enable Pages: Settings → Pages → Deploy from branch → main → / (root)
```

Your page is live at `https://yourusername.github.io/repo-name`.

## Example

See [`example/index.html`](example/index.html) for an Acme-branded demo page (gold accent, dark theme).

## No dependencies

```bash
# Nothing to install — just run:
python3 generate.py
```

Requires Python 3.6+.
