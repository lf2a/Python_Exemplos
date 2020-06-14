import decimal
import math

d = decimal.Decimal(math.pi)

print('before: %s' % math.pi)

pi = '{:.3}'.format(d)
print('after: %s' % pi)
