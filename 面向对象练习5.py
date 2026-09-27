class 学员管理系统:
    def __init__(self, *item):
        self.姓名 = item[0]
        self.地址 = item[1]
        self.手机号 = item[2]
        self.__饭卡余额 = item[3]  # 饭卡余额不能随意修改，所以用私有变量

    def 查询(self):
        print(self.姓名, self.地址, self.手机号, self.__饭卡余额)

    def 购买功能(self):
        print("商品1 3RMB,商品2 77RMB,商品3 78RMB")
        money = float(input("请输入商品金额"))  # 因为需要计算，所以要把input输入的结果转成浮点数
        if self.__饭卡余额 > money:  # 如果余额大于所购买的金额的话
            self.__饭卡余额 = self.__饭卡余额 - money  # 就正常扣款
            print("还剩", self.__饭卡余额)  # 并打印
        else:  # 否则
            print("请充值")  # 就提示充值


张三 = 学员管理系统("张三", "地址1", "187xxxx7777", 40000)  # 余额为了方便计算。需用数字类型
张三.查询()
张三.购买功能()
