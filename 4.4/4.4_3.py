def count_pairs(*numbers, div=10):
    c = 0
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if (numbers[i] + numbers[j]) % div == 0:
                c += 1
    return c