import urllib.request
from bs4 import BeautifulSoup

url = input('Enter Url: ').strip()
count = int(input('Enter Count: ').strip())
position = int(input('Enter Position: ').strip())

for i in range(count):
    print('Retrieving: ', url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    tag = tags[position - 1]
    url = tag.get('href')

print('Retrieving: ', url)
name = url.split('_')[-1].split('.')[0]
print(f'The answer to the assignment for this execution is "{name}"')