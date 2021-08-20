

class Data:
    A = '喻'
    B = u'喻'


if __name__ == '__main__':
    print(Data().A.encode())
    print(Data().B.encode())
    # print(unicode(Data().B, "utf-8"))