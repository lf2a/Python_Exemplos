from multiprocessing import Pool, cpu_count


def mult(v):
    return v * v


if __name__ == '__main__':
    """Executa paralelamente a funcão mult com varias vezes dado a quantidade de input em uma lista
    """
    with Pool(cpu_count()) as p:
        print(p.map(mult, [2, 4, 6]))
