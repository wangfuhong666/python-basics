class 水果:
    def __init__(self,x,y,z):
        self.名字 = x
        self.颜色 =y
        self.味道 =z

    def a(self):
        print(self.名字, self.颜色, self.味道)


水果1 = 水果("苹果","清甜爽口","红")
水果1.a()
