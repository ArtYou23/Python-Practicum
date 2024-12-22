import math
import os


rsm = ["Б", "КБ", "МБ", "ГБ"]
c = 0
file_size = os.path.getsize(input())
while file_size > 1024:
    c += 1
    file_size /= 1024
print(math.ceil(file_size), rsm[c], sep='')