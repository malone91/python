import socket
from urllib import request, parse, error

url = 'http://wwww.baidu.com'
response = request.urlopen(url, timeout=1)
print(response.read().decode('utf-8'))

data = bytes(parse.urlencode({'word':'hello'}), encoding='utf-8')
print(data)

response = request.urlopen('http://httpbin.org/post', data=data)
print(response.read().decode('utf-8'))

response = request.urlopen('http://httpbin.org/get', timeout=1)
print(response.read)

try:
    response = request.urlopen('http://httpbin.org/get', timeout=0.1)
    print(response.read)
except error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
    else:
        print('other exception')
