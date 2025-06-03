import requests
from collections import defaultdict


string_counts = defaultdict(int)
seen_responses = set()
base_url = "http://127.0.0.1:5000/"
while True:
    response = requests.get(base_url)
    if response.status_code != 200:
        break
    current_response = tuple(response.json())
    if current_response in seen_responses:
        break
    seen_responses.add(current_response)
    for string in response.json():
        string_counts[string] += 1
unique_strings = [string for string, count in string_counts.items() if count == 1]
unique_strings_sorted = sorted(unique_strings, key=lambda s: s.lower(), reverse=True)
for s in unique_strings_sorted:
    print(s)