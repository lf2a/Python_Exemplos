from csv import reader, writer

def read():
    with open('data.csv', 'rt') as csv_file:
        r = reader(csv_file)
        for row in r:
            print(row)

def write():
    with open('data_write.csv', 'wt') as csv_file:
        w = writer(csv_file)
        w.writerow(('id', 'valor (id * 2)'))
        
        for i in range(2):
            row = (
                    i,
                    i * 2
            )
            w.writerow(row)
    
    print(open('data_write.csv', 'rt').read())

if __name__ == '__main__':
#    read()
    write()