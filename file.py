def read_file():
    try:
        text1 = open('lorem.txt', mode='r', encoding='utf-8')

#        print(text1.readline())
#        print(text1.readlines())
        print(text1.read())
    
    except IOError as ioe:
        print(ioe)
    
    finally:
        text1.close()

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