a = {'aa': '1', 'bb': '2'}
b={'dd':'name','gg':'123456'}

def dict_aa():
    print(a['aa'])
    a.pop('aa')
    print(a)
    a['cc']='25'
    print(a)
    a['aa']='66'
    print(a)
    c=dict(a,**b)
    print(c)




if __name__ == '__main__':
    dict_aa()
