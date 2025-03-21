import random

class Product:
    def __init__(self,name,cost,price,profit_rate):
        self.name = name
        self.cost = cost
        self.price = price
        self._profit_rate = profit_rate
        self._lowest_price = self.cost*(1+profit_rate)

    def display_item(self): #展示商品详情
        print(f"Product:{self.name}\nPrice:{self.price}\nCost:{self.cost}")

class Inventory:
    def __init__(self):
        self.products = {
            "Apple" : [5,10,6],
            "Broccoli" : [4, 8,4.8],
            "Shrimp" : [12, 20,15],
            "Beef" : [10, 25,13],
            "Salt": [1,4,1]
        }
    def update(self): #上架商品
        pass
    def get_price(self,product_name): #获得价格
        return int(self.products.get(product_name)[1])
    def get_lowest_price(self,product_name): #获得最低价格
        return int(self.products.get(product_name)[2])
    
class Market(Inventory):
    def update(self,inventory): #上架商品
        #返回dic里所有的键值对，并随机抽取3个项
        result_list = random.sample(list(inventory.products.keys()),3) #返回一个list
        #处理list变成单个string
        result = ",".join(result_list)
        #上架信息
        print("Today's Products:",result)
        
    def display(self,inventory): #展示商品
        result_list = random.sample(list(inventory.products.keys()),3) #返回一个list
        return result_list