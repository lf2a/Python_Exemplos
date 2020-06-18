import urllib.request

"""
    O módulo urllib.request define funções e classes que ajudam a abrir URLs (principalmente HTTP) 
    em um mundo complexo - autenticação básica e digest, redirecionamentos, cookies e muito mais.
"""

URL = 'http://localhost:5000?nome=luiz%20filipy&pais=brasil'

# post
byte_response = urllib.request.urlopen(url=URL, data=b'{"name": "luiz"}')

print(f'GET_URL: {byte_response.geturl()}')

print(f'INFO:\n{byte_response.info()}')

print(f'STATUS: {byte_response.getcode()}')

