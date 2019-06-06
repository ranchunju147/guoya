def paixu():
    alist=[2,4,9,7,23,14,52,33,12,32,13]
    for i in range(len(alist)-1):
        for j in range(len(alist)-i-1):
         if alist[j]>alist[j+1]:
             temp=alist[j]
             alist[j]=alist[j+1]
             alist[j+1]=temp
    print(alist)

def jiujiu():
        for i in range(1, 10):
            for j in range(1, i + 1):
                print('%s *%s = %s' % (i, j, i * j), end=' ')
            print("")
if __name__ == '__main__':
    paixu()
    jiujiu()
