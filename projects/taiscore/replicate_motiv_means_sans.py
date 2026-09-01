#!/usr/bin/env python3
"""Reproduce the motivating-analysis bar chart in Matplotlib.

The original assets are left untouched. This script writes replicated PDF and
PNG files next to the originals in ``figure/``.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


OUTPUT_DIR = Path(__file__).resolve().parent / "figure"

# The website PNG is a 300-dpi rendering (1083 x 803 px). Its dimensions
# differ from the source PDF page by less than 0.04 pt because of raster
# rounding, so use the raster dimensions to reproduce the published asset.
FIGSIZE_IN = (1083 / 300, 803 / 300)
DPI = 300

GREY = "#9aa3ad"
BLUE = "#1f4e9c"
GREY_TEXT = "#5f6873"
BLUE_TEXT = "#13315f"
GRID = "#e9ecef"
SPINE = "#444444"


def build_figure() -> tuple[plt.Figure, plt.Axes]:
    """Build the chart using the values reported in the paper."""
    plt.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["DejaVu Sans"],
            "mathtext.fontset": "dejavusans",
            "pdf.fonttype": 42,
            "axes.unicode_minus": True,
        }
    )

    fig, ax = plt.subplots(figsize=FIGSIZE_IN, dpi=DPI)

    # Match the original 1083 x 803 px plot rectangle.
    fig.subplots_adjust(
        left=154 / 1083,
        right=1053 / 1083,
        bottom=122 / 803,
        top=774 / 803,
    )

    x = np.arange(3)
    width = 0.34
    critic_delta = np.array([0.21, -0.07, 0.09])
    refiner_delta = np.array([np.nan, 1.29, 0.39])

    ax.bar(
        x - width / 2,
        critic_delta,
        width,
        color=GREY,
        label="Larger critic (same y₀ and refiner)",
        zorder=3,
    )
    ax.bar(
        x + width / 2,
        refiner_delta,
        width,
        color=BLUE,
        label="Larger refiner (same y₀ and critique)",
        zorder=3,
    )

    ax.set_xlim(-0.55, 2.55)
    ax.set_ylim(-0.34, 1.98)
    ax.set_xticks(x)
    ax.set_xticklabels(
        ["Critique\nquality", "Critique\nadherence", "Downstream\ngain"],
        fontsize=8.5,
    )
    ax.set_yticks([0.0, 0.5, 1.0, 1.5])
    ax.tick_params(axis="x", length=0, pad=4)
    ax.tick_params(axis="y", length=0, pad=4, labelsize=8.5)
    ax.set_ylabel("Δ (larger − smaller)", fontsize=9, labelpad=4)

    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color=GRID, linewidth=0.8)
    ax.xaxis.grid(False)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(SPINE)
        ax.spines[side].set_linewidth(0.8)
    ax.axhline(0, color=SPINE, linewidth=0.8, zorder=4)

    ax.legend(
        loc="upper left",
        frameon=False,
        fontsize=7,
        handlelength=1.1,
        handleheight=0.9,
        handletextpad=0.55,
        labelspacing=0.35,
        borderaxespad=0.25,
    )

    annotation_size = 7
    for xpos, value in zip(x - width / 2, critic_delta):
        if value >= 0:
            ax.text(
                xpos,
                value + 0.035,
                f"+{value:.2f}",
                ha="center",
                va="bottom",
                fontsize=annotation_size,
                color=GREY_TEXT,
            )
        else:
            ax.text(
                xpos,
                value - 0.035,
                f"{value:.2f}",
                ha="center",
                va="top",
                fontsize=annotation_size,
                color=GREY_TEXT,
            )

    for xpos, value in zip(x + width / 2, refiner_delta):
        if np.isfinite(value):
            ax.text(
                xpos,
                value + 0.035,
                f"+{value:.2f}",
                ha="center",
                va="bottom",
                fontsize=annotation_size,
                color=BLUE_TEXT,
            )

    ax.text(
        x[0] + width / 2,
        0.06,
        "fixed",
        ha="center",
        va="bottom",
        fontsize=annotation_size,
        color=BLUE_TEXT,
        fontstyle="italic",
    )

    return fig, ax


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    fig, _ = build_figure()
    fig.savefig(OUTPUT_DIR / "motiv_means_sans_replicated.pdf")
    fig.savefig(OUTPUT_DIR / "motiv_means_sans_replicated.png", dpi=DPI)
    plt.close(fig)


if __name__ == "__main__":
    main()
