class Commander:
    def __init__(self,n,r,w,h,a):
        self.name = n
        self.rank = r
        self.weight = w
        self.height = h
        self.age = a
        self.danger_level = self.calculate_danger()
        print(f"Danger level of {self.name} : {self.danger_level}")

    def calculate_danger(self):
        return round((self.weight+self.height)/self.age)
        
c = Commander(n ='Barzak',r=4,w=40,h=12,a=33)