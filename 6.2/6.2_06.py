import pandas as pd


def best(journal: pd.DataFrame):
    j = journal.copy()
    return j[(j["maths"] > 3) & (j["physics"] > 3) & (j["computer science"] > 3)]