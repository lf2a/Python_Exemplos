import urllib.request

URL = 'http://localhost:5000?nome=luiz%20filipy&pais=brasil'

request_obj = urllib.request.Request(url=URL, data=b'{"nome": "luiz filipy"}', headers={"test-key": 1234}, method='PUT')
response = urllib.request.urlopen(request_obj)

print('%s - %s %s' % (response.geturl(), response.getcode(), response.msg))
print(response.getheaders())
print(str(response.read(), encoding='utf-8'))
