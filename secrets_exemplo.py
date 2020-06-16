import secrets

# permite gerar codigos aletorios

# gera codigos aleatorios em formato de bytes
tb = secrets.token_bytes(20)
print(tb)

th = secrets.token_hex(20)
print(th)

# gera codigos aleatorios para serem usados em urls
tus = secrets.token_urlsafe(5)
print(tus)
