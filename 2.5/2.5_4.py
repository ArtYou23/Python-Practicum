mn = [int(input()) for i in range(int(input()))]
mmm = max([mn[i + 1] for i in range(len(mn) - 1) if mn[i + 1] < mn[i]])
print(mmm)