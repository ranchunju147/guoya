class book():
    def __init__(self,yuwen,shuxue,yingyu):
        self.yuwen=yuwen
        self.shuxue=shuxue
        self.yingyu=yingyu
    def fenshu(self):
        print(self.yingyu+'xiaomingde')
    def  job(self):
        print(self.shuxue+'woaini')

if __name__ == '__main__':
   b=book('44','77','969',)
   b.fenshu()
   b.job()

