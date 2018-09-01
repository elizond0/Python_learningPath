class Store(object):
    # 店铺信息
    def __init__(self, name, begin):
        self.store_name = name
        self.store_begin = begin

        # 简单工厂模式
        self.simpleFactory = SimpleFactory()

    # 生成订单
    def order(self, meat_type):
        return self.simpleFactory.meat_type(meat_type)


# 简单工厂模式
class SimpleFactory(object):
    def meat_type(self, meat_type):
        if meat_type == "猪肉":
            return Pork()
        elif meat_type == "牛肉":
            return Beef()


class Products(Store):
    def __init__(self, date):
        self.production_date = date


class Pork(Products):
    production_name = "猪肉"

    def __init__(self):
        pass


class Beef(Products):
    production_name = "牛肉"

    def __init__(self):
        pass


# 开店-肉店
meat_store = Store("猪肉荣肉铺", "始于1912年")
# print(meat_store.store_name,meat_store.store_begin) # 猪肉荣肉铺 始于1912年

# 买猪肉
buy_prok = meat_store.order("猪肉")
# print(buy_prok.production_name) # 猪肉
