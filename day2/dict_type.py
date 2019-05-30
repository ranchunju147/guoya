import json

#字典，以{}包起来，;前面是key,后面是value


adict= {'username':'admin','password':'123456'}

def dict_sel():
    print(adict['username'])
def dict_updat():
    adict['username']='ld'
    print(adict)
def dict_del():
    adict.pop('username')
    adict.pop('password')
    print(adict)
def dict_add():
    adict['age']=25
    adict['great']=7
    print(adict)
    bdict={'list':[1,2,3,4,5,6],'tuple':(9,8,7)}
    adict.update(bdict)
    print(adict)
    cdict={'password':'999999','class':'1904'}
    ddict=dict(adict,**cdict)
    print(ddict)
def dict_zhuanhuan():
      print(type(adict))
      ab_str=json.dumps(adict)
      print(ab_str)
      print(type(ab_str))



if __name__ == '__main__':
   dict_zhuanhuan()
