import xml.etree.ElementTree as ET
import urllib.request

url = input("Enter Location: ")
data = urllib.request.urlopen(url).read()

tree = ET.fromstring(data)
total = 0

print(f"Retriveing {url}")
print(f"Retrievd {len(data)} characters")

counts = tree.findall('.//count')
for count in counts:
    total += int(count.text)

print(f"Count: {len(counts)}")
print(f"Sum: {total}")

