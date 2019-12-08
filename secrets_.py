import secrets


tb = secrets.token_bytes(20)
print(tb)

th = secrets.token_hex(20)
print(th)

tus = secrets.token_urlsafe(10)
print(tus)

