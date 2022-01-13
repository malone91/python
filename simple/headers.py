from urllib import parse, request

headers = {
    "Accept-Encoding": "identity",
    "Content-Length": "10",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "httpbin.org",
    "User-Agent": "Python-urllib/3.7",
    "X-Amzn-Trace-Id": "Root=1-61dfdce5-07a663cd2ba3a90a7fb06166"
}
dict = {
    'name': 'value'
}
url = 'http://httpbin.org/post'

data = bytes(parse.urlencode(dict), encoding='utf-8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))