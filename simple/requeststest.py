import re

import requests

url = 'http://httpbin.org'
data = {
    'key': 'value',
    'abc': 'xyz'
}
# get
response = requests.get(url, data)
print(response.text)

url = 'http://httpbin.org/post'
response = requests.post(url, data)
print(response.json())

# 正则
content = requests.get('http://www.cnu.cc/discoveryPage/hot-人像').text
print(content)

pattern = re.compile(r'<a href="(.*?)".*?title"(.*?)</div>',re.S)
results = re.findall(pattern, content)
print(results)

for result in results:
    url, name = result
    print(url, re.sub('\s', '', name))