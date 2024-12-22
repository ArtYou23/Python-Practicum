s = ''
for i in range(int(input())):
    s += input() + ' '
s = s.replace(',', '').replace('\n', ' ')
print('\n'.join(list(f"{int(i)}. {j}" for i, j in enumerate(sorted(s.split()), 1))))