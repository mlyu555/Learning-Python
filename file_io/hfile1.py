
gbk_file = 'gbk.txt'
utf8_file = 'utf8.txt'

def test():
    f = open(gbk_file, 'r', encoding='utf-8')
    # print("gbk文件by'utf8':\t", f.read())s

    f = open(gbk_file, 'rb')
    print("gbk文件:\t", f.read())
    f = open(utf8_file, 'rb')
    print("utf8文件:\t", f.read())

    f = open(utf8_file, 'r', encoding='gb2312')
    print("utf8文件by'gb2312':\t", f.read())
    f.close()


def test_access_mode():

    def _test(mode):
        f = open(utf8_file, mode, encoding='utf-8')
        print(mode, '\t', f.tell())
        f.close()

    _test('r')
    _test('r+')
    _test('w')
    _test('w+')
    _test('a')
    _test('a+')


def test_read_content():
    f = open(utf8_file, 'r', encoding='utf-8')
    print('read:        \t', f.read())
    f.seek(0)
    print('tell:        \t', f.tell())
    print('read(5):     \t', f.read(5))
    f.seek(0)
    print('readline:    \t', f.readline())
    f.seek(0)
    print('readline(5): \t', f.readline(5))
    f.seek(0)
    print('readlines:   \t', f.readlines())
    f.close()



if __name__ == '__main__':
    # test()
    # test_access_mode()
    test_read_content()
