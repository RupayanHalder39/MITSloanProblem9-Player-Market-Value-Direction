#!/usr/bin/env python3
"""Verify the frozen aggregate evidence and public-release structure."""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def rows(name: str) -> list[dict[str, str]]:
    with (ROOT / "results" / name).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def close(actual: str, expected: float, tolerance: float = 5e-7) -> None:
    assert abs(float(actual) - expected) <= tolerance, (actual, expected)


def main() -> int:
    primary = {row["metric"]: row for row in rows("championship_m1_vs_m5.csv")}
    close(primary["residual_mae"]["M1_value"], 0.3065964562236665)
    close(primary["residual_mae"]["M5_value"], 0.2956541488506693)
    close(primary["direction_accuracy"]["M1_value"], 0.35638297872340424)
    close(primary["direction_accuracy"]["M5_value"], 0.46675531914893614)
    close(primary["residual_spearman"]["M1_value"], 0.27837776827220767)
    close(primary["residual_spearman"]["M5_value"], 0.29595104062310823)

    direction = {row["model"]: row for row in rows("championship_direction_metrics.csv")}
    close(direction["Naive_majority_class"]["accuracy"], 0.4228723404255319)

    external = rows("external_competition_summary.csv")[0]
    assert int(external["n_competitions"]) == 27
    assert int(external["n_M5_beats_M1_on_direction"]) == 27
    assert int(external["n_M5_beats_M1_on_MAE"]) == 8

    bootstrap = {row["metric"]: row for row in rows("player_clustered_bootstrap.csv")}
    assert all(int(row["n_resamples"]) == 2000 for row in bootstrap.values())
    assert bootstrap["mae_diff"]["interval_excludes_zero"] == "True"
    assert bootstrap["direction_acc_diff"]["interval_excludes_zero"] == "True"
    assert bootstrap["spearman_diff"]["interval_excludes_zero"] == "False"

    required = [
        "README.md", "LICENSE", "CITATION.cff", "paper/Problem9_Beyond_Todays_Price.pdf",
        "figures/cross_league_direction.png", "figures/riser_faller_shortlist.png",
        "assets/RupayanHalder.jpeg", "assets/SoccerSolverLogo.png",
    ]
    missing = [path for path in required if not (ROOT / path).is_file()]
    assert not missing, f"Missing files: {missing}"

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for link in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", readme):
        if "://" not in link and not link.startswith("mailto:"):
            assert (ROOT / link).exists(), f"Broken README link: {link}"

    forbidden = "/Users/" + "rupayan/SoccerSolverProjects/" + "real-time-player-market-valuation"
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".md", ".py", ".csv", ".cff", ".txt"}:
            assert forbidden not in path.read_text(encoding="utf-8", errors="ignore"), path

    print("PASS: frozen Problem 9 aggregate metrics and release structure verified")
    return 0


if __name__ == "__main__":
    sys.exit(main())
