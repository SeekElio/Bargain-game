import random

class Product:
    def __init__(self,name,cost,price,profit_rate):
        self.name = name
        self.cost = cost
        self.price = price
        self._profit_rate = profit_rate
    def display_item(self): #展示商品详情
        print(f"Product:{self.name}\nPrice:{self.price}\nCost:{self.cost}")

class Inventory:
    def __init__(self):
        self.products = {}
    def add_products(self,product): #添加商品
        self.products[product.name] = [product.cost,product.price]
    def update(self): #上架商品
        pass

class Market(Inventory):
    def update(self,inventory): #上架商品
        #返回dic里所有的键值对，并随机抽取3个项
        result_list = random.sample(list(inventory.products.keys()),3) #返回一个list
        #处理list变成单个string
        result = ",".join(result_list)
        #上架信息
        print("Today's Products:",result)
