import hashlib

h1 = hashlib.sha384()
h1.update(b'luiz filipy')
h1.digest()

print(f'block size: {h1.block_size}')
print(f'digest: {h1.digest()}')
print(f'hexdigest: {h1.hexdigest()}')
print(f'digest size: {h1.digest_size}')

h2 = hashlib.sha256(b'luiz filipy')
print(f'h2: {h2.hexdigest()}')

h2.update(b'brasil')
print(f'h2 update: {h2.hexdigest()}')
