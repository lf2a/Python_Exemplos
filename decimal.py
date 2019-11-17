from decimal import Decimal
from math import pi

d = Decimal(pi)

print('before: %s' % pi)

pi = '{:.3}'.format(d)
print('after: %s' % pi)