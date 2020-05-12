class hinhchunhat(object):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def dien_tich(self):
        return self.a*self.b
    pass
a=int(input("nhap chieu dai:"))
b=int(input("nhap chieu rong:"))
c=hinhchunhat(a,b)
print('dien tich :', c.dien_tich())

      
