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


def discount(chq):
    ch = chq.copy()
    ch["cost"] = ch["cost"].astype(float)
    ch.loc[ch["number"] > 2, "cost"] *= 0.5
    return ch


products = ['bread', 'milk', 'soda', 'cream']
prices = [37, 58, 99, 72]
price_list = pd.Series(prices, products)
result = cheque(price_list, soda=3, milk=2, cream=1)
with_discount = discount(result)
print(result)
print(with_discount)