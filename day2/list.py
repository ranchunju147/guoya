#删除某个
alist=['hhh',33,'你好',5,6,7,8]

def listt():

    a=alist.pop(2)
    print(alist)
    print((a))

#添加
def blist():
    blist = [1, '2', 3, 4, 'sfds', 5, 6]
    blist.append('999')
    print(blist)
    blist.append(999)
    print(blist)
    clist=[9,8,7,]
    blist.extend(clist)
    print(blist)
    blist.append(clist)
    print(blist)
    #update
def list_update():
    wlist=[9,8,7,6,5,4]
    wlist[2]=200
    print((wlist))
    wlist[5]='中国'
    print(wlist)
    wlist[4]=666
    print(wlist)
    #order by
def list_order_by():
    klist=[1,9,3,55,4,44,66]
    klist.sort()
    print(klist)
    klist.sort(reverse=True)
    print(klist)
def list_distinct():
    dlist=[1,1,12,3,16,4,5,6,6,7]
    dlist=list(set(dlist))
    print(dlist)
    print(len(dlist))
def list_a():
    listtt=[1,2,5,3,4,]
    print(listtt[2])
    print(listtt[1:4])
    a=listtt.pop(3)
    print(a)
    listtt.append(7)
    listtt.append(9)
    print(listtt)
    listtt[0]='5'
    print(listtt)
    print(len(listtt))








if __name__ == '__main__':
     list_a()
