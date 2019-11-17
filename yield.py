def par():
    for i in range(100):
        if i % 2 == 0:
            yield {'value': i}

print(list(par()))