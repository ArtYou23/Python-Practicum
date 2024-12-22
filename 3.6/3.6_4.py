from itertools import product


def generate_words(n, letters):
    combinations = product(*letters)

    unique_words = set(''.join(combination) for combination in combinations)

    sorted_words = sorted(unique_words)

    return sorted_words


N = int(input())
letters = [input().strip().split('-') for _ in range(N)]

results = generate_words(N, letters)
for word in results:
    print(word)
