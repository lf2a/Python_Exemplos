def read_file():
    with open('lorem.txt', mode='r') as file:
        print(file.read())
        # print(file.readline()) # first line
        # print(file.readlines()) # line

def write_file():
    # a: appending
    # w: write
    # r: read
    with open('lorem_write.txt', mode='a', encoding='utf-8') as w:
        w.write('Lorem ipsum dolor sit amet\n')
        w.write('Lorem ipsum dolor sit amet')


if __name__ == '__main__':
    read_file()
#    write_file()
