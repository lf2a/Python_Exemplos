def even():
    for i in range(100):
        if i % 2 == 0:
            yield '%d' % i
        else:
            yield 'odd'


list_ = even()

for index, value in enumerate(list_):
    print('list_[%s] = %s' % (index, value))
