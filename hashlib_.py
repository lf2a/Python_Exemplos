import hashlib


m1 = hashlib.sha256()
m1.update(b'luiz filipy')
m1.digest()
print('block size: ', m1.block_size)
print('digest: ', m1.digest())
print('hexdigest: ', m1.hexdigest())
print('digest size: ', m1.digest_size)


m2  = hashlib.sha256(b'luiz filipy').hexdigest()
print(m2)
