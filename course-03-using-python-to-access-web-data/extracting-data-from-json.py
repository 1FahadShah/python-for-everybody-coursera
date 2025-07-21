import urllib.request
import json

url = input('Enter Location: ').strip()
data = urllib.request.urlopen(url).read()

info = json.loads(data)
print(f'Retrieving {url}')
print(f'Retrieved {len(data)} characters')

total = 0
count = 0

for item in info['comments']:
    total += int(item['count'])
    count += 1

print(f'Count: {count}')
print(f'Sum: {total}')
