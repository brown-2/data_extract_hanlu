import os

def write_test():
    s1 = '123\n456\n'
    s2 = '123\r456\r'
    s3 = '123\r\n456\r\n'
    with open('test.txt', 'w') as f:
        f.write(s1)
        f.write(s2)
        f.write(s3)

def read_test():
    with open('test.txt', newline = None) as f:
        data = f.read()
    print(repr(data))

def main():
    '''
    os.chdir(os.listdir()[-1])
    filename = os.listdir()[0]
    with open(filename, newline = '') as f:
        data = f.read()
    print(repr(data[:100]))
    '''
    write_test()
    read_test()

if __name__ == '__main__':
    main()
