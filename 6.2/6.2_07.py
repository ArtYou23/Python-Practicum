import pandas as pd


def need_to_work_better(journal: pd.DataFrame):
    j = journal.copy()
    return j[(j["maths"] == 2) | (j["physics"] == 2) | (j["computer science"] == 2)]