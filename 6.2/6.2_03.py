import pandas as pd


def cheque(price_list, **kwargs):
    prod = sorted(kwargs)
    dict = {
        "product": prod,
        "price": [price_list[i] for i in prod],
        "number": [kwargs[i] for i in prod],
    }
    dict["cost"] = [price_list[i] * dict["number"][index] for index, i in enumerate(prod)]
    return pd.DataFrame(dict)