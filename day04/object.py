class sdudent(object):
    def __init__(self,name,age,sex,xuehao):
        self.name=name
        self.age=age
        self.xuhao=xuehao
    def play(self):
        print(self.name+'玩游戏')
    def  see(self):
        print(self.name+'看电视')
    def info(self):
        print('她叫%s，今年%s，性别%s，学号%s'%(self.name,self.age,self.sex,self.xuhao))
        self.play()
class ddddd(sdudent):
    def __init__(self,name,age,sex,xuehao,job):
        self.name=name
        self.age=age
        self.sex=sex
        self.xuhao=xuehao
        self.job=job
    def play(self):
        print(self.name+'玩刺激战场')
    def work(self):
        print(self.name+'认真工作')





if __name__ == '__main__':
    # boy =  sdudent('yanyan',20,'女',666)
    # boy.play()
    # boy.info()
    # boy.see()
    dd=ddddd('xiaomin',22,'nan',999,'jiaoshi')
    dd.play()
    dd.work()
    dd.info()




