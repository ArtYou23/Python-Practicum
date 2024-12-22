n, m = [input(), input()]
print('\n'.join(list(f"{i.replace(',', '')} - {j.replace(',', '')}" for i, j in list(zip(n.split(), m.split())))))