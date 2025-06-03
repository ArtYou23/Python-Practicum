import csv


L = float(input().strip())
fy = int(input())
result = []
with open('city.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        geo_lon = float(row['geo_lon'])
        foundation_year = int(row['foundation_year'])
        if geo_lon >= L and foundation_year <= fy:
            city = row['city']
            population = row['population']
            result.append((city, population))
result.sort(reverse=True)
for city, population in result:
    print(f"{city} {population}")