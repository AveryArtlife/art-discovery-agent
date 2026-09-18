"""Charts for the Reserve Clinic margin-and-growth proposal.
Palette and axis treatment follow the validated categorical palette used elsewhere in this project.
"""
import json, os
import matplotlib
matplotlib.use("Agg")
# never let a dollar sign in a label be parsed as TeX math
matplotlib.rcParams["text.parse_math"] = False
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np

CAT = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300"]
SEQ = ["#cde2fb", "#9ec5f4", "#6da7ec", "#3987e5", "#256abf", "#184f95", "#0d366b"]
GRID = "#e1e0d9"; AXIS = "#c3c2b7"; INK_MUTED = "#898781"; BG = "#fcfcfb"
SCN = ["Conservative", "Baseline", "Aggressive"]
SCOL = {"Conservative": CAT[3], "Baseline": CAT[0], "Aggressive": CAT[2]}


def _style(ax, title=None, ygrid=True):
    ax.set_facecolor(BG)
    for sp in ("top", "right"): ax.spines[sp].set_visible(False)
    for sp in ("left", "bottom"): ax.spines[sp].set_color(AXIS)
    ax.tick_params(colors=INK_MUTED, labelsize=8)
    if ygrid:
        ax.yaxis.grid(True, color=GRID, linewidth=0.6); ax.set_axisbelow(True)
    if title: ax.set_title(title, loc="left", fontsize=10, color="#0b0b0b", pad=10)


def _save(fig, path):
    fig.patch.set_facecolor(BG); fig.tight_layout(); fig.savefig(path, dpi=200); plt.close(fig)


def _m(v):
    a = abs(v)
    if a >= 1e6: s = f"${a/1e6:.1f}M"
    elif a >= 1e3: s = f"${a/1e3:.0f}k"
    else: s = f"${a:.0f}"
    return ("-" if v < 0 else "") + s


def c_trajectory(mv, path):
    """Monthly net revenue (log) and cumulative cash by scenario."""
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.3))
    ax = axes[0]; _style(ax, "Monthly net revenue by scenario (log scale)")
    for s in SCN:
        y = [max(1, v) for v in mv["monthly"][s]["net_rev"]]
        ax.plot(range(1, 37), y, color=SCOL[s], linewidth=2.1)
        ax.annotate(s, (36, y[-1]), xytext=(4, 0), textcoords="offset points", fontsize=7.5,
                    color=SCOL[s], va="center", fontweight="bold")
    ax.set_yscale("log"); ax.set_xlim(1, 44); ax.set_ylim(1e3, 4e7)
    ax.set_xticks([1, 6, 12, 18, 24, 30, 36])
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: _m(v)))
    ax.set_xlabel("Model month", fontsize=8, color=INK_MUTED)
    ax.yaxis.grid(True, which="major", color=GRID, linewidth=0.6)

    ax = axes[1]
    _style(ax, "Cumulative cash flow — the trough is the capital need")
    troughs = {}
    for s in SCN:
        y = [v / 1e6 for v in mv["monthly"][s]["cum_cash"]]
        troughs[s] = (min(y), y.index(min(y)) + 1, y[-1])
        ax.plot(range(1, 37), y, color=SCOL[s], linewidth=2.1, clip_on=True)
        lo, mo, _ = troughs[s]
        ax.plot([mo], [lo], marker="o", markersize=4.5, color=SCOL[s], zorder=5)
        ax.annotate(f"-${abs(lo):.2f}M", (mo, lo),
                    xytext=((-42, -11) if mo > 29 else (3, -11)), textcoords="offset points",
                    fontsize=7, color=SCOL[s], fontweight="bold")
    ax.axhline(0, color="#6b6b66", linewidth=0.9)
    ax.set_ylim(-2.4, 3.2); ax.set_xlim(1, 36)
    ax.set_xticks([1, 6, 12, 18, 24, 30, 36])
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"${v:,.0f}M"))
    ax.set_xlabel("Model month", fontsize=8, color=INK_MUTED)
    ax.annotate(f"Aggressive leaves the frame at month {[i for i, v in enumerate(mv['monthly']['Aggressive']['cum_cash'], 1) if v/1e6 > 3.2][0]}\n"
                f"and reaches ${mv['monthly']['Aggressive']['cum_cash'][-1]/1e6:,.1f}M by month 36",
                xy=(0.30, 0.90), xycoords="axes fraction", fontsize=7, color=CAT[2], fontweight="bold")
    _save(fig, path)


def c_waterfall(mv, path):
    """Where each $100 of net revenue goes, by line, baseline drivers."""
    a = mv["assum"]; b = lambda k: a[k]["Baseline"]
    # non-Rx, per order
    aov = b("nonrx_aov"); rf = b("refund_pct"); pf = b("pay_fee")
    net = aov * (1 - rf)
    nx = [("Product COGS", aov * b("nonrx_cogs_pct")), ("Pick, pack, ship", b("nonrx_fulfil")),
          ("Card processing", net * pf)]
    nx_cm = net - sum(v for _, v in nx)
    # Rx, per member-month
    pp = b("rx_price"); rnet = pp * (1 - rf)
    rx = [("Medication (pharmacy)", b("pharm_cost")), ("Clinician monitoring", b("refill_cost")),
          ("Cold-chain shipping", b("coldchain_ship")), ("Support", b("rx_support")),
          ("Card processing", rnet * pf)]
    rx_cm = rnet - sum(v for _, v in rx)

    fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.2))
    for ax, (ttl, base, items, cm, unit) in zip(axes, [
            ("Non-prescription order", net, nx, nx_cm, f"per ${aov:.0f} order, net of refunds"),
            ("Prescription member-month", rnet, rx, rx_cm, f"per ${pp:.0f} member-month, net of refunds")]):
        _style(ax, ttl, ygrid=False)
        ax.set_title(ttl, loc="left", fontsize=10, color="#0b0b0b", pad=16)
        ax.annotate(unit, xy=(0, 1.035), xycoords="axes fraction", fontsize=7.5, color=INK_MUTED)
        left = 0.0
        cols = [CAT[1], CAT[3], CAT[4], CAT[5], "#9a9a94", "#c9c9c2"]
        for i, (lab, v) in enumerate(items):
            pct = v / base * 100
            ax.barh([0], [pct], left=left, color=cols[i % len(cols)], height=0.46,
                    edgecolor="white", linewidth=0.8)
            if pct > 6.5:
                ax.annotate(f"{pct:.0f}%", (left + pct / 2, 0), ha="center", va="center",
                            fontsize=7.5, color="white", fontweight="bold")
            left += pct
        ax.barh([0], [cm / base * 100], left=left, color=CAT[2], height=0.46,
                edgecolor="white", linewidth=0.8)
        ax.annotate(f"{cm/base*100:.0f}%", (left + (cm / base * 100) / 2, 0), ha="center", va="center",
                    fontsize=8.5, color="white", fontweight="bold")
        # legend rows below
        ys = -0.52
        for i, (lab, v) in enumerate(items + [("CONTRIBUTION", cm)]):
            c = CAT[2] if lab == "CONTRIBUTION" else cols[i % len(cols)]
            ax.add_patch(plt.Rectangle((1, ys - 0.035), 3.2, 0.07, color=c, clip_on=False))
            ax.annotate(f"{lab}   ${v:,.2f}", (6, ys), fontsize=7.2, va="center", color="#3b3b37",
                        fontweight=("bold" if lab == "CONTRIBUTION" else "normal"), annotation_clip=False)
            ys -= 0.155
        ax.set_xlim(0, 100); ax.set_ylim(ys - 0.1, 0.4); ax.set_yticks([])
        ax.set_xticks([0, 25, 50, 75, 100]); ax.set_xticklabels(["0%", "25%", "50%", "75%", "100%"])
        for sp in ("left",): ax.spines[sp].set_visible(False)
    _save(fig, path)


def c_mix(mv, path):
    """Revenue mix over time, baseline."""
    m = mv["monthly"]["Baseline"]
    x = range(1, 37)
    nx = [v / 1e3 for v in m["nonrx_rev_net"]]; rx = [v / 1e3 for v in m["rx_rev_net"]]
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.0))
    ax = axes[0]; _style(ax, "Baseline net revenue by line ($k per month)")
    ax.stackplot(x, nx, rx, colors=[CAT[0], CAT[1]], labels=["Non-prescription supplements", "Prescription programmes"], edgecolor="white", linewidth=0.4)
    ax.legend(frameon=False, fontsize=7.5, loc="upper left")
    ax.set_xlim(1, 36); ax.set_xlabel("Model month", fontsize=8, color=INK_MUTED)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"${v:,.0f}k"))

    ax = axes[1]; _style(ax, "Gross margin by line (baseline)")
    for i, (lab, gp, rev) in enumerate([("Non-prescription", m["nonrx_gp"], m["nonrx_rev_net"]),
                                        ("Prescription", m["rx_gp"], m["rx_rev_net"])]):
        y = [(g / r * 100 if r > 500 else None) for g, r in zip(gp, rev)]
        ax.plot(x, y, color=CAT[i], linewidth=2.1, label=lab)
    y = [(g / r * 100 if r > 500 else None) for g, r in zip(m["gross_profit"], m["net_rev"])]
    ax.plot(x, y, color="#4a4a45", linewidth=1.6, linestyle="--", label="Blended")
    ax.legend(frameon=False, fontsize=7.5, loc="lower right")
    ax.set_xlim(1, 36); ax.set_ylim(0, 80); ax.set_xlabel("Model month", fontsize=8, color=INK_MUTED)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:.0f}%"))
    _save(fig, path)


def c_years(mv, path):
    """Year-by-year revenue and EBITDA, three scenarios."""
    s = mv["summary"]
    rev = {k: [s[f"Net revenue, year {y}"][k] / 1e6 for y in (1, 2, 3)] for k in SCN}
    eb = {k: [s[f"EBITDA, year {y}"][k] / 1e6 for y in (1, 2, 3)] for k in SCN}
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.1))
    w = 0.26
    for ax, data, ttl in ((axes[0], rev, "Net revenue by year ($M)"), (axes[1], eb, "EBITDA by year ($M)")):
        _style(ax, ttl)
        for i, k in enumerate(SCN):
            xs = np.arange(3) + (i - 1) * w
            ax.bar(xs, data[k], width=w, color=SCOL[k], label=k)
            for xx, vv in zip(xs, data[k]):
                ax.annotate(_m(vv * 1e6), (xx, vv), xytext=(0, 3 if vv >= 0 else -11),
                            textcoords="offset points", ha="center", fontsize=6.8, color="#52514e")
        ax.set_xticks(range(3)); ax.set_xticklabels(["Year 1", "Year 2", "Year 3"])
        ax.axhline(0, color="#6b6b66", linewidth=0.9)
        ax.set_yscale("symlog", linthresh=1)
        ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"${v:,.0f}M"))
    axes[0].legend(frameon=False, fontsize=7.5, loc="upper left")
    _save(fig, path)


def c_ltvcac(mv, path):
    g = mv["sens"]["ltvcac"]
    arr = np.array(g["grid"], dtype=float)
    fig, ax = plt.subplots(figsize=(9.2, 2.9))
    ax.set_facecolor(BG)
    im = ax.imshow(arr, cmap="RdYlGn", vmin=0.8, vmax=7.0, aspect="auto")
    ax.set_xticks(range(len(g["cacs"]))); ax.set_xticklabels([f"${c:,.0f}" for c in g["cacs"]], fontsize=8)
    ax.set_yticks(range(len(g["churns"]))); ax.set_yticklabels([f"{c:.1%}" for c in g["churns"]], fontsize=8)
    ax.set_xlabel("Blended cost to acquire one prescription member", fontsize=8, color=INK_MUTED)
    ax.set_ylabel("Monthly churn", fontsize=8, color=INK_MUTED)
    ax.set_title(f"Prescription LTV:CAC — contribution ${mv['sens']['contrib_mm']:.0f} per member-month (baseline drivers)",
                 loc="left", fontsize=10, color="#0b0b0b", pad=10)
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            v = arr[i, j]
            ax.annotate(f"{v:.1f}x", (j, i), ha="center", va="center", fontsize=7.6,
                        color=("white" if v < 1.6 else "#14171C"),
                        fontweight=("bold" if v >= 3.0 else "normal"))
    ax.tick_params(colors=INK_MUTED, length=0)
    for sp in ax.spines.values(): sp.set_visible(False)
    ax.annotate("bold = at or above the 3.0x floor", xy=(0, 1.02), xycoords="axes fraction",
                fontsize=7, color=INK_MUTED)
    _save(fig, path)


def c_audience(mv, path):
    """Followers to customers, baseline, month 12."""
    m = mv["monthly"]["Baseline"]; a = mv["assum"]; b = lambda k: a[k]["Baseline"]
    i = 11
    steps = [("Followers", b("followers")),
             ("Reached by\nbrand posts", b("followers") * b("reach_pct") * b("posts_per_month")),
             ("Sessions from\nthe partner", m["partner_sessions"][i]),
             ("All sessions\n(+ organic, paid)", m["sessions"][i]),
             ("New customers\nserved", m["nonrx_new_cust"][i]),
             ("New Rx\nmembers", m["rx_new"][i])]
    fig, ax = plt.subplots(figsize=(9.2, 3.0))
    _style(ax, "Baseline audience engine, month 12: each step is a separate, stated, testable rate")
    vals = [max(1, v) for _, v in steps]
    cols = [SEQ[5], SEQ[4], CAT[0], CAT[0], CAT[2], CAT[1]]
    ax.bar([s for s, _ in steps], vals, color=cols, width=0.6)
    ax.set_yscale("log"); ax.set_ylim(1, 1e8)
    ax.yaxis.grid(True, which="both", color=GRID, linewidth=0.5)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:,.0f}" if v < 1e6 else f"{v/1e6:,.0f}M"))
    for k, (lab, _) in enumerate(steps):
        ax.annotate(f"{vals[k]:,.0f}", (k, vals[k]), xytext=(0, 4), textcoords="offset points",
                    ha="center", fontsize=8, color="#3b3b37", fontweight="bold")
    for k in range(len(steps) - 1):
        r = vals[k + 1] / vals[k]
        ax.annotate(f"x{r:.4f}".rstrip("0") if r < 0.1 else f"x{r:.2f}", (k + 0.5, 2.2),
                    ha="center", fontsize=7, color=INK_MUTED)
    ax.tick_params(axis="x", labelsize=7.2)
    _save(fig, path)


def c_capital(mv, path):
    s = mv["summary"]
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 2.7))
    ax = axes[0]; _style(ax, "Capital required (cash trough plus 30% buffer)", ygrid=False)
    v = [s["Capital required (deficit plus 30% buffer)"][k] / 1e6 for k in SCN]
    ax.barh(SCN[::-1], v[::-1], color=[SCOL[k] for k in SCN[::-1]], height=0.55)
    ax.xaxis.grid(True, color=GRID, linewidth=0.6)
    for i, vv in enumerate(v[::-1]):
        ax.annotate(f"${vv:.2f}M", (vv, i), xytext=(5, 0), textcoords="offset points", va="center",
                    fontsize=8, color="#3b3b37", fontweight="bold")
    ax.set_xlim(0, max(v) * 1.35); ax.tick_params(axis="y", labelsize=8)
    ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f"${x:,.1f}M"))

    ax = axes[1]; _style(ax, "Months to the first EBITDA-positive month", ygrid=False)
    lab, val, col = [], [], []
    for k in SCN:
        b = s["First EBITDA-positive month"][k]
        lab.append(k); col.append(SCOL[k])
        val.append(0 if isinstance(b, str) else b)
    ax.barh(lab[::-1], val[::-1], color=col[::-1], height=0.55)
    ax.xaxis.grid(True, color=GRID, linewidth=0.6)
    for i, k in enumerate(SCN[::-1]):
        b = s["First EBITDA-positive month"][k]
        txt = "not within 36 months" if isinstance(b, str) else f"month {b:.0f}"
        xx = 0.4 if isinstance(b, str) else b
        ax.annotate(txt, (xx, i), xytext=(5, 0), textcoords="offset points", va="center",
                    fontsize=8, color="#3b3b37", fontweight="bold")
    ax.set_xlim(0, 38); ax.tick_params(axis="y", labelsize=8)
    ax.set_xlabel("Model month", fontsize=8, color=INK_MUTED)
    _save(fig, path)


def c_market(path):
    """Category growth context. Every figure labelled with what it is and is not."""
    rows = [("Peptide therapeutics, global", 58.0, 83.6, "context only"),
            ("Dietary supplements, global", 228.2, 300.0, "context only"),
            ("US cash-pay DTC telehealth", 5.0, 8.5, "adjacent"),
            ("US cash-pay hormone and peptide optimisation", 4.0, 6.5, "core"),
            ("US wellness-peptide niche (order of magnitude)", 2.0, 3.4, "directly addressable")]
    cmap = {"context only": "#bdbcb4", "adjacent": CAT[3], "core": CAT[0], "directly addressable": CAT[2]}
    fig, ax = plt.subplots(figsize=(9.2, 2.9))
    _style(ax, None, ygrid=False)
    names = [r[0] for r in rows][::-1]
    for i, (n, a, b, tag) in enumerate(rows[::-1]):
        ax.plot([a, b], [i, i], color=cmap[tag], linewidth=7.5, solid_capstyle="round")
        ax.annotate(f"${a:,.0f}B to ${b:,.0f}B", (b, i), xytext=(8, 0), textcoords="offset points",
                    va="center", fontsize=7.4, color="#3b3b37", fontweight="bold")
    ax.set_yticks(range(len(rows))); ax.set_yticklabels(names, fontsize=7.6)
    ax.set_xscale("log"); ax.set_xlim(1, 1700); ax.set_ylim(-0.7, len(rows) - 0.3)
    ax.set_xticks([1, 10, 100, 1000])
    ax.xaxis.grid(True, color=GRID, linewidth=0.6)
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: f"${v:,.0f}B"))
    handles = [plt.Line2D([0], [0], color=c, linewidth=6, solid_capstyle="round", label=t)
               for t, c in cmap.items()]
    ax.legend(handles=handles, frameon=False, fontsize=7.2, ncol=4, loc="upper center",
              bbox_to_anchor=(0.5, 1.13), handlelength=1.2, columnspacing=1.6)
    ax.set_xlabel("Vendor market reports; firms disagree widely. Log scale. The two grey rows are not addressable by a cash-pay consumer brand.",
                  fontsize=7.2, color=INK_MUTED)
    _save(fig, path)


def c_reachgrid(mv, path):
    g = mv["sens"]["reach"]
    arr = np.array(g["grid"], dtype=float) / 1000.0
    fig, ax = plt.subplots(figsize=(9.2, 2.6))
    ax.set_facecolor(BG)
    im = ax.imshow(np.log10(np.maximum(arr, 0.1)), cmap="Blues", aspect="auto")
    ax.set_xticks(range(len(g["ctrs"]))); ax.set_xticklabels([f"{c:.2%}" for c in g["ctrs"]], fontsize=8)
    ax.set_yticks(range(len(g["reaches"]))); ax.set_yticklabels([f"{c:.0%}" for c in g["reaches"]], fontsize=8)
    ax.set_xlabel("Click-through per reached impression", fontsize=8, color=INK_MUTED)
    ax.set_ylabel("Reach per post\n(share of followers)", fontsize=8, color=INK_MUTED)
    ax.set_title("Month-12 partner-driven sessions per month, in thousands — the two least-evidenced drivers, multiplied",
                 loc="left", fontsize=9.6, color="#0b0b0b", pad=10)
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            v = arr[i, j]
            ax.annotate(f"{v:,.0f}k", (j, i), ha="center", va="center", fontsize=7.6,
                        color=("white" if np.log10(max(v, 0.1)) > 1.7 else "#14171C"))
    ax.tick_params(colors=INK_MUTED, length=0)
    for sp in ax.spines.values(): sp.set_visible(False)
    _save(fig, path)


def build_all(mv, outdir):
    os.makedirs(outdir, exist_ok=True)
    p = lambda n: os.path.join(outdir, n)
    c_trajectory(mv, p("m_traj.png")); c_waterfall(mv, p("m_water.png"))
    c_mix(mv, p("m_mix.png")); c_years(mv, p("m_years.png"))
    c_ltvcac(mv, p("m_ltvcac.png")); c_audience(mv, p("m_aud.png"))
    c_capital(mv, p("m_cap.png")); c_market(p("m_market.png"))
    c_reachgrid(mv, p("m_reach.png"))
    return outdir


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    mv = json.load(open(os.path.join(here, "margin_values.json")))
    print(build_all(mv, os.path.join(here, "charts")))
