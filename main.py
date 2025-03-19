#游戏设计师 FANG xifan
'''
【游戏目标】
玩家扮演顾客在集市中与商人讨价还价 在5次之内与商人达成交易即可获胜

【游戏流程】
1.开始游戏 商人随机选择3样物品上架
*画面:价格，成本，出价输入框
2.玩家输入价格进行报价
3.商人进行决策 根据报价进行反馈
*画面:商人提示价格高低
4.玩家第二次输入价格进行报价
*画面:价格，成本，建议出价，出价输入框
5.如此往复4次
6.如果在5次内成交,游戏胜利;如果5次仍未达成游戏,游戏结束。
'''

import sale
if __name__ == "__main__":
    print("Welcome to Street Market!")
    
    #实例化
    apple = sale.Product("Apple",5,10,0.3)
    broccoli = sale.Product("Broccoli", 4, 8, 0.2)
    shrimp = sale.Product("Shrimp", 12, 20, 0.25)
    beef = sale.Product("Beef",10, 25, 0.3)
    salt = sale.Product("Salt",1,4,0.1)

    #往库存里添加商品
    inventory = sale.Inventory()
    inventory.add_products(apple)
    inventory.add_products(broccoli)
    inventory.add_products(shrimp)
    inventory.add_products(beef)
    inventory.add_products(salt)

    #实例化上架商品
    stall = sale.Market()
    stall.update(inventory)  

    #提问玩家选择哪个商品
    choice_input = input("Which product you want to bargain with?\nEnter the name here:")
    #验证输入是否有效

    #展示商品信息
    if choice_input.lower() == "apple":
        apple.display_item()
    elif choice_input.lower() == "broccoli":
        broccoli.display_item()
    elif choice_input.lower() == "shrimp":
        shrimp.display_item()
    elif choice_input.lower() == "beef":
        beef.display_item()
    else:
        salt.display_item()
    #询问玩家出价
    try:
        bid = int(input("Enter my bid:"))
    except ValueError:
        print("The input is not an integer!")


#前端设计师 Sze-To TSZ KIN




#后端设计师 ZHANG jiayuan





#美术设计师 LAW kahei




#测试者 CHI xuanyi