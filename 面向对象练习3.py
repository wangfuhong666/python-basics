class 汽车想法:
    def __init__(self, *item):
        self.动力核心 = item[0]
        self.驱动形式 = item[1]
        self.车身架构 = item[2]
        self.是否能进行人机交互 = item[3]
        self.安全系统 = item[4]
        self.颜色 = item[5]

    def a(self):
        print(self.动力核心, self.驱动形式, self.车身架构, self.是否能进行人机交互, self.安全系统, self.颜色,
              "设计成功")


第一辆车 = 汽车想法("内燃机", "前驱", "承载式车身", "否", "被动安全", "深绿")
第一辆车.a()
第二辆车 = 汽车想法("混合动力", "四驱", "非承载式车身", "是", "主动安全", "深蓝")
第二辆车.a()
