class Car:
    def __init__(self, brand, speed=0):
        """初始化汽车属性"""
        self.brand = brand  # 品牌
        self.speed = speed  # 速度，默认为0

    def accelerate(self, m):
        """加速方法，m次每次增加10"""
        for _ in range(m):
            self.speed += 10
        return self.speed

    def brake(self, n):
        """刹车方法，n次每次减少10，不低于0"""
        for _ in range(n):
            self.speed = max(0, self.speed - 10)  # 确保速度不低于0
        return self.speed

    def __str__(self):
        """打印对象信息"""
        return f"{self.brand}汽车，当前速度: {self.speed}"

# 创建Car实例
my_car = Car("Toyota", 30)

# 测试加速和刹车
print(my_car)  # 初始状态
my_car.accelerate(3)  # 加速3次
print("加速后:", my_car)  # 速度应为60
my_car.brake(2)  # 刹车2次
print("刹车后:", my_car)  # 速度应为40
my_car.brake(5)  # 刹车5次（会降到0）
print("再次刹车后:", my_car)  # 速度应为0


class ElectricCar(Car):
    def __init__(self, brand, speed=0, battery=50):
        """初始化电动汽车属性"""
        super().__init__(brand, speed)  # 调用父类初始化
        self.battery = battery  # 电量，默认50

    def charge(self, times=1):
        """充电方法，每次增加20，不超过100"""
        for _ in range(times):
            self.battery = min(100, self.battery + 20)  # 确保电量不超过100
        return self.battery

    def __str__(self):
        """重写打印方法，增加电量信息"""
        return f"{super().__str__()}，当前电量: {self.battery}%"

# 创建ElectricCar实例
my_ev = ElectricCar("Tesla", 20, 60)

# 测试继承的方法和新增方法
print("\n电动汽车测试:")
print(my_ev)  # 初始状态
my_ev.accelerate(2)  # 加速2次
my_ev.charge(3)  # 充电3次
print("加速和充电后:", my_ev)  # 速度40，电量100
my_ev.brake(1)  # 刹车1次
print("刹车后:", my_ev)  # 速度30，电量100