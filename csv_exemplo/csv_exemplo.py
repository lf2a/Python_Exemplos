import csv


def read():
    with open('data_read.csv', 'rt') as csv_file:
        r = csv.reader(csv_file)
        print('----------------------- READ ------------------------')
        for row in r:
            for col in row:
                print(f'\t{col}\t', end='')
            print('\n-----------------------------------------------------')


def write():
    with open('data_write.csv', 'wt') as csv_file:
        w = csv.writer(csv_file)
        w.writerow(('id', 'valor'))

        for i in range(2):
            row = (i, i * 2)
            w.writerow(row)
    print(open('data_write.csv', 'rt').read())


if __name__ == '__main__':
    read()
    write()
