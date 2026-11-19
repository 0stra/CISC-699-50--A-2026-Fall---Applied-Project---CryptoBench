"""Draws the three evidence figures used in the Assignment 12 thesis (gate status, claim-to-record map,
classification of the zero), updated from figures_thesis_source.py (14 November).
Every fact drawn here comes from analysis/results/claims_register_2026-11-19.md, docs/ISSUE_LOG.md,
docs/INVENTORY_FREEZE_RECORD.md and docs/K4_RULE_ANALYSIS_2026-11-19.md. Run: python3 figures_a12_source.py
Written by Claude (AI assistant) on 19 November 2026."""
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
 ('Reference inventory: two independent passes agree on every item', 'not', 'CANDIDATE, NOT FROZEN',
  'v1: 10 items, 53 lines, valid CycloneDX 1.6, hashed; not independent; no second reader (ISSUE-09)'),
 ('Known positive, Semgrep', 'part', 'MET, ONE RULE',
  'Checks A, D and F: each of four rules fires on a known case; 12 one-feature variants for one rule'),
 ('Known negative, Semgrep', 'part', 'MET, ONE FILE',
  'Check C: 0 findings on StringUtils.java (425 lines, no cryptography)'),
 ('Run reproducibility, Semgrep', 'part', 'MET, BY ME ONLY',
  'Checks A to F on three Semgrep versions incl. a fresh container (P8); variants run by Claude only'),
 ('Independent human re-run of the written steps', 'todo', 'NOT DONE',
  'Requested from a person; nothing received. Fresh-container re-run (P8) is mine, not independent (ISSUE-11)'),
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
ax.text(0.005, 0.985, 'Gates set in advance (Assignments 03 and 04) and where each one stands on 19 November 2026',
        fontsize=8.2, fontweight='bold', color=INK, va='center')
fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
fig.savefig('figure_7_gate_status_2026-11-19.png'); plt.close(fig)

# ---------- Figure: claims to records ----------
claims = [('K1', 'Procedure runs end to end on public inputs', ['R1', 'R2', 'P3', 'P4', 'P8'], 'Survived with limits'),
          ('K2', 'Planned ruleset returned HTTP 404', ['P1'], 'Provisional'),
          ('K3', 'Rule fires on its own test file (line 15)', ['R2', 'P3', 'P8'], 'Survived with limits'),
          ('K4', 'Zero on Md5Crypt.java: coverage gap', ['R2', 'P3', 'R3', 'R4', 'P6', 'P7', 'P8'], 'Provisional (stronger)'),
          ('K5', 'No false positive on a no-crypto file', ['P4', 'P8'], 'Survived with limits'),
          ('K6', 'Checks A to C repeat on 3 environments', ['R2', 'P3', 'P4', 'P8'], 'Survived with limits'),
          ('K7', 'Template hand edit needs three checks', ['TC2'], 'Survived with limits'),
          ('K8', 'Chained form found, variable form missed', ['R3', 'R4', 'P6', 'P8'], 'Survived with limits'),
          ('K9', 'Other 3 rules: fire on tests, 0 on file', ['P7', 'P8'], 'Survived (2 runs, mine)')]
cols = [('R1', 'Claude'), ('R2', 'Claude'), ('R3', 'Claude'), ('R4', 'Claude'), ('P1', 'typed by Claude Code'),
        ('P3', 'me'), ('P4', 'me'), ('P6', 'me'), ('P7', 'me'), ('P8', 'me'), ('TC2', 'me')]
fig, ax = plt.subplots(figsize=(7.4, 4.3), dpi=220)
ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis('off')
x0, cw = 0.43, 0.034
for j, (c, who) in enumerate(cols):
    xc = x0 + j * cw + cw / 2
    ax.text(xc, 0.945, c, ha='center', fontsize=7.6, fontweight='bold', color=INK)
    ax.text(xc, 0.905, 'AI' if who == 'Claude' else ('AI\ncode' if 'Code' in who else 'me'),
            ha='center', va='top', fontsize=5.8, color=BLUE if who != 'me' else AMB, linespacing=1.0)
ax.text(0.99, 0.945, 'Status', ha='right', fontsize=7.6, fontweight='bold', color=INK)
rh = 0.0925
for i, (k, txt, recs, st) in enumerate(claims):
    y = 0.80 - i * rh
    prov = st.startswith('Provisional')
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
fig.savefig('figure_8_claim_record_map_2026-11-19.png'); plt.close(fig)

# ---------- Figure: classification of the zero ----------
fig, ax = plt.subplots(figsize=(7.4, 4.6), dpi=220)
ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis('off')
box(ax, 0.22, 0.88, 0.56, 0.09, 'Check B: four official rules report 0 findings on Md5Crypt.java\n(the file creates MD5 digests at lines 259, 275, 312)', 'part', 7.6, True)
box(ax, 0.02, 0.66, 0.46, 0.15, 'Step 1. Does each rule fire on a known case?\nYes. Checks A, D (line 6) and F: each rule fires\non its own test file or control.\nSo "non-functional" is ruled out for these rules.', 'met', 7.0)
box(ax, 0.52, 0.66, 0.46, 0.15, 'Step 2. Is the tool silent on a file with no cryptography?\nYes. Check C: StringUtils.java, 0 findings, twice.\nSo the zero is not simply silence on everything.', 'met', 7.0)
box(ax, 0.02, 0.28, 0.46, 0.27, 'use-of-md5-digest-utils: COVERAGE GAP (shape)\nRule needs DigestUtils.getMd5Digest().digest(...)\nas one chained expression. The file stores the\ndigest in a variable (lines 259, 275, 312).\nCheck D: line 6 found, lines 10 to 12 not.\n12 variants (R4): variable, unprefixed (line 469\nshape) and qualified forms missed. K4, K8, L8', 'part', 7.0)
box(ax, 0.52, 0.28, 0.46, 0.27, 'use-of-md5, md5-used-as-password, weak-random:\nNO MATCHING CALL IN THE FILE\nMd5Crypt.java has no getInstance call, and\nRandom appears only as a type.\nEach rule fires on its own test file\n(3, 1 and 3 findings; check F).\nClaim K9', 'part', 7.0)
box(ax, 0.02, 0.03, 0.96, 0.17, 'Reading. Three conclusions are kept apart. (1) The scanner ran: supported. (2) One pattern did not match: supported by the rule text\nand 12 variants; I have not yet read the rule myself or re-run them. (3) The inventory holds an item that was not reported: not established,\nbecause the inventory is a candidate and not frozen. K4 therefore stays provisional.', 'not', 6.9)
ax.text(0.5, 0.605, 'Both controls pass, so the zero needs a cause. Cause found rule by rule:', ha='center', fontsize=7.0, color=GREY, style='italic')
for (x1, y1, x2, y2) in [(0.5, 0.88, 0.25, 0.81), (0.5, 0.88, 0.75, 0.81), (0.25, 0.585, 0.25, 0.55), (0.75, 0.585, 0.75, 0.55), (0.25, 0.28, 0.25, 0.20), (0.75, 0.28, 0.75, 0.20)]:
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle='-|>', color=GREY, lw=1.2))
fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
fig.savefig('figure_9_zero_classification_2026-11-19.png'); plt.close(fig)
print('ok')

# ---------- Figure: twelve K4 variants (added 19 November 2026) ----------
variants = [
 ('V00', 'chained baseline', 'match', 'match'),
 ('V01', 'variable form (lines 259, 275, 312)', 'no match', 'no match'),
 ('V02', 'unprefixed call (DigestUtils.java 469)', 'no match', 'no match'),
 ('V03', 'fully qualified receiver', 'no match*', 'no match'),
 ('V04', 'sha512 method, chained', 'no match', 'no match'),
 ('V05', 'chained digest() without arguments', 'match', 'match'),
 ('V06', 'chained update, not digest', 'no match', 'no match'),
 ('V07', 'chained across three lines', 'match', 'match'),
 ('V08', 'creation call in parentheses', 'match*', 'match'),
 ('V09', 'md5() helper', 'no match', 'no match'),
 ('V10', 'md5Hex() helper', 'no match', 'no match'),
 ('V11', 'chained result assigned', 'match', 'match'),
]
fig, ax = plt.subplots(figsize=(7.4, 4.9)); ax.set_xlim(0, 1.1); ax.set_ylim(0, 1); ax.axis('off')
ax.text(0.0, 0.975, 'Twelve one-feature variants of the call that use-of-md5-digest-utils targets', fontsize=9.5, fontweight='bold', color=INK, va='top')
ax.text(0.0, 0.925, 'Expected (committed before the run) versus observed (R4, Semgrep 1.186.0, one run each). * = predicted with uncertainty.', fontsize=7.2, color=GREY, va='top')
for x, h in ((0.0, 'File'), (0.12, 'Feature changed'), (0.64, 'Expected'), (0.82, 'Observed')):
    ax.text(x, 0.865, h, fontsize=7.8, fontweight='bold', color=INK)
n = len(variants); top = 0.83; step = 0.066
for k, (v, feat, exp, obs) in enumerate(variants):
    y = top - k * step
    kind = 'met' if obs.startswith('match') else 'todo'
    ax.add_patch(FancyBboxPatch((0.0, y - 0.045), 1.1, 0.055, boxstyle='round,pad=0.002,rounding_size=0.008', fc=TINT[kind], ec='none'))
    ax.text(0.01, y - 0.018, v, fontsize=7.6, color=INK, va='center')
    ax.text(0.12, y - 0.018, feat, fontsize=7.6, color=INK, va='center')
    ax.text(0.64, y - 0.018, exp, fontsize=7.6, color=INK, va='center')
    ax.text(0.82, y - 0.018, obs + ('  (1 finding)' if obs == 'match' else '  (0 findings)'), fontsize=7.6, color=INK, va='center', fontweight='bold')
ax.text(0.0, 0.012, 'Expected = observed in 12 of 12. Synthetic files written by Claude; run by Claude, not yet by me. Source: data/test_material/k4_variants/.', fontsize=7, color=GREY)
fig.savefig('figure_10_k4_variants_2026-11-19.png', dpi=200, bbox_inches='tight', facecolor='white'); plt.close(fig)
