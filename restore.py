#!/usr/bin/env python3
"""
Run this script from the root of the QC_Article_Part1 repo to restore the
full article and add the hero teaser.

Usage:
  git fetch --all
  python3 restore.py
  git add index.html
  git commit -m "fix: restore full article with hero teaser and blog link"
  git push
  git rm restore.py && git commit -m "chore: remove restore script" && git push
"""
import subprocess, sys

# Get original file from git history (before bad edits)
ORIGINAL_COMMIT = "d85b292f061978c95c021c3eabcff292a164d44d"

result = subprocess.run(
    ["git", "show", f"{ORIGINAL_COMMIT}:index.html"],
    capture_output=True, text=True
)
if result.returncode != 0:
    print("ERROR: Could not get original file from git history")
    print(result.stderr)
    sys.exit(1)

html = result.stdout
print(f"Original size: {len(html)} chars")

# 1 — Add hero-note CSS
old_css = '.hero-sub { font-size: 17px; font-weight: 300; color: rgba(249,246,241,.6); max-width: 620px; line-height: 1.6; margin-bottom: 40px; font-style: italic; }'
new_css = old_css + """
    .hero-note { font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; letter-spacing: 0.08em; color: rgba(240,235,226,0.55); margin-top: -24px; margin-bottom: 32px; }
    .hero-note a { color: var(--accent); text-decoration: none; border-bottom: 1px solid rgba(184,146,42,0.4); }
    .hero-note a:hover { border-bottom-color: var(--accent); }"""
html = html.replace(old_css, new_css, 1)

# 2 — Replace hero-sub content
old_para = '    <p class="hero-sub">From superposition and entanglement to climate models and energy systems: why quantum computing is uniquely suited to solving the most complex problems humanity has ever faced.</p>'
new_para = (
    '    <p class="hero-sub">Quantum computing might sound like just another geeky buzzword \u2014 '
    'but in reality, it could be the most consequential technological breakthrough of all time. '
    'Far more than a faster classical computer, it operates on entirely different physical principles \u2014 '
    "ones that could crack problems today's most powerful machines would take longer than the age of the "
    "universe to solve. This article explores how these extraordinary properties are tailor-made to tackle "
    "humanity's most pressing challenges: from accelerating drug discovery to modelling climate systems "
    'and transforming clean energy.</p>\n'
    '    <p class="hero-note">This article is also available on my personal '
    '<a href="https://medium.com/@oliverinderwildi" target="_blank" rel="noopener">blog</a>.</p>'
)
html = html.replace(old_para, new_para, 1)

print(f"Modified size: {len(html)} chars")
print(f"Teaser inserted: {'geeky buzzword' in html}")
print(f"Blog link inserted: {'hero-note' in html}")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("\nDone! Now run:")
print("  git add index.html")
print("  git commit -m 'fix: restore full article with hero teaser and blog link'")
print("  git push")
