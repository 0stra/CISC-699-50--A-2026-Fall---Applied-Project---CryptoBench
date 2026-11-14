"""Draws the three new evidence figures used in the Assignment 11 thesis draft.
Every fact drawn here comes from analysis/results/claims_register_2026-11-05.md,
docs/ISSUE_LOG.md and docs/PROCEDURE_NOTES.md. Run: python3 figures_thesis_source.py
Written by Claude (AI assistant) on 14 November 2026."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
plt.rcParams['font.family'] = 'DejaVu Sans'
INK, GREY, BLUE, AMB, GRN, RED = '#1f2933', '#6b7280', '#3b5ba9', '#b7791f', '#2f7d5b', '#b03a2e'
TINT = {'met': '#e3f0e8', 'part': '#fdf0d5', 'not': '#fbe7e4', 'todo': '#eceef1'}
EDGE = {'met': GRN, 'part': AMB, 'not': RED, 'todo': GREY}

def box(ax, x, y, w, h, text, kind, fs=7.6, bold=False):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.01,rounding_size=0.012',
                                fc=TINT[kind], ec=EDGE[kind], lw=1.3))
    ax.text(x + 0.012, y + h / 2, text, va='center', ha='left', fontsize=fs, color=INK,
            fontweight='bold' if bold else 'normal', linespacing=1.25)

# ---------- Figure: gate status ----------
gates = [
 ('Reference inventory: two independent passes agree on every item', 'not', 'NOT MET',
  'Passes disagreed on 39 lines; reconciled by my own rules; supervisor has not confirmed (ISSUE-09)'),
 ('Known positive, Semgrep', 'part', 'MET, ONE RULE',
  'Checks A, D and F: each of four rules fires on a known case; same-shape control for one rule'),
 ('Known negative, Semgrep', 'part', 'MET, ONE FILE',
  'Check C: 0 findings on StringUtils.java (425 lines, no cryptography)'),
 ('Run reproducibility, Semgrep', 'part', 'MET, SMALL',
  'Checks A to E repeated on two machines and two versions; check F one run'),
 ('Independent human re-run of the written steps', 'todo', 'NOT DONE',
  'Only an AI agent (low independence) and my own self-check; no other person has run it'),
 ('Sonar Cryptography Plugin: known positive and negative', 'todo', 'NOT STARTED',
  'Plugin and SonarQube not installed (ISSUE-01); fallback Rule 1 applies'),
 ('TLS scanner: validation and any scan', 'todo', 'NOT STARTED',
  'No written authorisation on file; nothing scanned (RISK-05)'),
 ('Sample set of 15 to 25 assets selected', 'todo', 'NOT STARTED',
  'One file used, chosen by convenience; fallback Rule 3 (feasibility case study)'),
 ('Scoring reproducibility and effort logging', 'todo', 'NOT STARTED',
  'No scored result exists; analysis/scored/ is empty'),
]
fig, ax = plt.subplots(figsize=(7.4, 5.0), dpi=220)
ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis('off')
n = len(gates); top = 0.955; rh = 0.093; gap = 0.0085
for i, (name, kind, tag, why) in enumerate(gates):
    y = top - (i + 1) * rh - i * gap
    ax.add_patch(FancyBboxPatch((0.005, y), 0.99, rh, boxstyle='round,pad=0.004,rounding_size=0.012',
                                fc=TINT[kind], ec=EDGE[kind], lw=1.2))
    ax.text(0.02, y + rh * 0.68, name, fontsize=7.8, fontweight='bold', color=INK, va='center')
    ax.text(0.02, y + rh * 0.29, why, fontsize=6.7, color=GREY, va='center')
    ax.text(0.985, y + rh / 2, tag, fontsize=7.6, fontweight='bold', color=EDGE[kind], va='center', ha='right')
ax.text(0.005, 0.985, 'Gates set in advance (Assignments 03 and 04) and where each one stands on 5 November 2026',
        fontsize=8.2, fontweight='bold', color=INK, va='center')
fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
fig.savefig('figure_4_gate_status_2026-11-14.png'); plt.close(fig)

# ---------- Figure: claims to records ----------
claims = [('K1', 'Procedure runs end to end on public inputs', ['R1', 'R2', 'P3', 'P4'], 'Survived with limits'),
          ('K2', 'Planned ruleset returned HTTP 404', ['P1'], 'Provisional'),
          ('K3', 'Rule fires on its own test file (line 15)', ['R2', 'P3'], 'Survived with limits'),
          ('K4', 'Zero on Md5Crypt.java: coverage gap', ['R2', 'P3', 'R3', 'P6', 'P7'], 'Provisional'),
          ('K5', 'No false positive on a no-crypto file', ['P4'], 'Survived with limits'),
          ('K6', 'Checks A to C repeat on 2 machines', ['R2', 'P3', 'P4'], 'Survived with limits'),
          ('K7', 'Template hand edit needs three checks', ['TC2'], 'Survived with limits'),
          ('K8', 'Chained form found, variable form missed', ['R3', 'P6'], 'Survived with limits'),
          ('K9', 'Other 3 rules: fire on tests, 0 on file', ['P7'], 'Survived (single run)')]
cols = [('R1', 'Claude'), ('R2', 'Claude'), ('R3', 'Claude'), ('P1', 'typed by Claude Code'),
        ('P3', 'me'), ('P4', 'me'), ('P6', 'me'), ('P7', 'me'), ('TC2', 'me')]
fig, ax = plt.subplots(figsize=(7.4, 4.3), dpi=220)
ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis('off')
x0, cw = 0.43, 0.043
for j, (c, who) in enumerate(cols):
    xc = x0 + j * cw + cw / 2
    ax.text(xc, 0.945, c, ha='center', fontsize=7.6, fontweight='bold', color=INK)
    ax.text(xc, 0.905, 'Claude' if who == 'Claude' else ('Claude\nCode' if 'Code' in who else 'me'),
            ha='center', va='top', fontsize=5.8, color=BLUE if who != 'me' else AMB, linespacing=1.0)
ax.text(0.99, 0.945, 'Status', ha='right', fontsize=7.6, fontweight='bold', color=INK)
rh = 0.0925
for i, (k, txt, recs, st) in enumerate(claims):
    y = 0.80 - i * rh
    prov = st == 'Provisional'
    ax.add_patch(FancyBboxPatch((0.003, y - 0.004), 0.994, rh - 0.012, boxstyle='round,pad=0.002,rounding_size=0.01',
                                fc=TINT['part'] if prov else '#f5f7f6', ec='none'))
    ax.text(0.012, y + rh * 0.38, k, fontsize=7.8, fontweight='bold', color=INK, va='center')
    ax.text(0.060, y + rh * 0.38, txt, fontsize=6.6, color=INK, va='center')
    for j, (c, who) in enumerate(cols):
        xc = x0 + j * cw + cw / 2
        if c in recs:
            ax.plot(xc, y + rh * 0.38, 'o', ms=6.2, color=BLUE if who != 'me' else AMB)
        else:
            ax.plot(xc, y + rh * 0.38, '.', ms=2.5, color='#c3c8cf')
    ax.text(0.99, y + rh * 0.38, st, ha='right', fontsize=6.8, fontweight='bold',
            color=AMB if prov else GRN, va='center')
fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
fig.savefig('figure_5_claim_record_map_2026-11-14.png'); plt.close(fig)

# ---------- Figure: classification of the zero ----------
fig, ax = plt.subplots(figsize=(7.4, 4.6), dpi=220)
ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis('off')
box(ax, 0.22, 0.88, 0.56, 0.09, 'Check B: four official rules report 0 findings on Md5Crypt.java\n(the file creates MD5 digests at lines 259, 275, 312)', 'part', 7.6, True)
box(ax, 0.02, 0.66, 0.46, 0.15, 'Step 1. Does each rule fire on a known case?\nYes. Checks A, D (line 6) and F: each rule fires\non its own test file or control.\nSo "non-functional" is ruled out for these rules.', 'met', 7.0)
box(ax, 0.52, 0.66, 0.46, 0.15, 'Step 2. Is the tool silent on a file with no cryptography?\nYes. Check C: StringUtils.java, 0 findings, twice.\nSo the zero is not simply silence on everything.', 'met', 7.0)
box(ax, 0.02, 0.28, 0.46, 0.27, 'use-of-md5-digest-utils: COVERAGE GAP (shape)\nThe call is in the file, stored in a variable.\nThe rule matches the chained form only.\nControl: line 6 found, lines 10 to 12 not (check D).\nA second shape also missed:\nDigestUtils.java line 469 (check E).\nClaims K8, L8', 'part', 7.0)
box(ax, 0.52, 0.28, 0.46, 0.27, 'use-of-md5, md5-used-as-password, weak-random:\nNO MATCHING CALL IN THE FILE\nMd5Crypt.java has no getInstance call, and\nRandom appears only as a type.\nEach rule fires on its own test file\n(3, 1 and 3 findings; check F).\nClaim K9', 'part', 7.0)
box(ax, 0.02, 0.03, 0.96, 0.17, 'Reading. For the benchmark, every zero here is a miss against the reference inventory, whatever its cause,\nbecause the inventory records MD5 use in any form. The two causes differ: a shape gap in one rule, and no target for three.\nThe explanation is provisional (K4): it rests on my reading of the rule patterns, which I have not yet re-checked.', 'not', 6.9)
ax.text(0.5, 0.605, 'Both controls pass, so the zero needs a cause. Cause found rule by rule:', ha='center', fontsize=7.0, color=GREY, style='italic')
for (x1, y1, x2, y2) in [(0.5, 0.88, 0.25, 0.81), (0.5, 0.88, 0.75, 0.81), (0.25, 0.585, 0.25, 0.55), (0.75, 0.585, 0.75, 0.55), (0.25, 0.28, 0.25, 0.20), (0.75, 0.28, 0.75, 0.20)]:
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle='-|>', color=GREY, lw=1.2))
fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
fig.savefig('figure_6_zero_classification_2026-11-14.png'); plt.close(fig)
print('ok')
