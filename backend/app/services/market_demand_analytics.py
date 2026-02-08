from dataclasses import dataclass
import importlib.util

from app.services.market_demand_data import DATASET


@dataclass(frozen=True)
class MarketDemandSummary:
    average_job_frequency: float
    average_growth_index: float
    average_salary_impact: float
    top_growth_skills: list[str]


def build_market_demand_summary() -> MarketDemandSummary:
    if _has_pandas_and_numpy():
        return _build_summary_with_pandas_numpy()
    return _build_summary_with_python()


def _has_pandas_and_numpy() -> bool:
    return importlib.util.find_spec("pandas") is not None and importlib.util.find_spec("numpy") is not None


def _build_summary_with_pandas_numpy() -> MarketDemandSummary:
    import numpy as np
    import pandas as pd

    frame = pd.DataFrame(
        [
            {
                "skill": item.skill,
                "job_frequency": item.job_frequency,
                "growth_index": item.growth_index,
                "salary_impact": item.salary_impact,
            }
            for item in DATASET
        ]
    )

    averages = frame[["job_frequency", "growth_index", "salary_impact"]].mean()
    top_growth = frame.sort_values("growth_index", ascending=False).head(3)["skill"].tolist()

    return MarketDemandSummary(
        average_job_frequency=float(np.round(averages["job_frequency"], 3)),
        average_growth_index=float(np.round(averages["growth_index"], 3)),
        average_salary_impact=float(np.round(averages["salary_impact"], 3)),
        top_growth_skills=top_growth,
    )


def _build_summary_with_python() -> MarketDemandSummary:
    count = len(DATASET)
    avg_job_frequency = round(sum(item.job_frequency for item in DATASET) / count, 3)
    avg_growth_index = round(sum(item.growth_index for item in DATASET) / count, 3)
    avg_salary_impact = round(sum(item.salary_impact for item in DATASET) / count, 3)
    top_growth = [item.skill for item in sorted(DATASET, key=lambda row: row.growth_index, reverse=True)[:3]]

    return MarketDemandSummary(
        average_job_frequency=avg_job_frequency,
        average_growth_index=avg_growth_index,
        average_salary_impact=avg_salary_impact,
        top_growth_skills=top_growth,
    )
