a = {'aa': '1', 'bb': '2'}
b={'dd':'name','gg':'123456'}

def dict_aa():
    a = {'aa': '1', 'bb': '2'}
    b = {'dd': 'name', 'gg': '123456'}

    print(a['aa'])
    a.pop('aa')
    print(a)
    a['cc']='25'
    print(a)
    a['aa']='66'
    print(a)
    c=dict(a,**b)
    print(c)
def aaaaaa():
    list=[1,2,3,4,5]
    print(list[2])
    print(list[1:4])
    list.pop(3)
    list.append('6')
    list[0]='5'
    print(len(list))
    print(list)
def paixu():
    aa=[22,33,54,2,4,2,5,8,5,8,7,9,]
    aa.sort()
    print(aa)
    aa.sort(reverse=True)
    print(aa)
    print(set(aa))
    dd=list(set(aa))
    print(dd)










if __name__ == '__main__':
    paixu()
