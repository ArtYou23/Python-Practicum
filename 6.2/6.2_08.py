import pandas as pd


def update(journal: pd.DataFrame):
    j = journal.copy()
    j["average"] = ((j["maths"] + j["physics"] + j["computer science"]) / 3).astype(float)
    return j.sort_values(by=["average", "name"], ascending=(False, True))