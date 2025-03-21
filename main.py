import sale 
import decision as d

#游戏主程序
if __name__ == "__main__":
    print("Welcome to Street Market!")

#系统准备资源
    #实例化商品
    apple = sale.Product("Apple",5,10,0.3)
    broccoli = sale.Product("Broccoli", 4, 8, 0.2)
    shrimp = sale.Product("Shrimp", 12, 20, 0.25)
    beef = sale.Product("Beef",10, 25, 0.3)
    salt = sale.Product("Salt",1,4,0.1)

    #实例化上架商品
    inventory = sale.Inventory()
    stall = sale.Market()
    stall.update(inventory) 

#游戏开始
    #提问玩家选择哪个商品
    choice_input = d.ask_choice()  #公共变量1
    #验证输入是否有效
    valid_products = stall.display(inventory) #获取有效商品
    valid_invetory = [product.lower() for product in stall.display(inventory)] #把有效商品list里的内容全部改成小写

    while choice_input.lower() not in valid_invetory: #如果不在有效商品里，就重新输入
        print("Invalid choice. Please enter a valid product.")
        print(valid_products)
        choice_input = d.ask_choice()
        if choice_input.lower() in valid_products: #如果在有效商品里，就停止询问选择
            break    
    #Format用户输入
    f_choice = choice_input.capitalize()  

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


#玩家循环
    #控制循环的变量
    times = 5
    IsContinue = True
    price = inventory.get_price(f_choice) #获得公共变量3
    lowest_price = inventory.get_lowest_price(f_choice) #获得公共变量4

    #循环开始
    while (times>0 or IsContinue):
        #玩家出价
        player_bid = d.ask_bid() #公共变量2

        #实例化二叉树的节点
        root = d.Node("Is bid larger than or equal to price?")
        Node1= d.Node("Too high! Bid Again")
        Node2 = d.Node("Is bid equal to lowest price?")
        Node3 = d.Node("Congratularions!")
        Node4 = d.Node("Is bid larger than lowest price?")
        Node5 = d.Node("Your price is higher!")
        Node6 = d.Node("Your price is lower!")

        #实例构建二叉树
        root.left = Node1
        root.right = Node2
        root.right.left = Node3
        root.right.right = Node4
        root.right.right.left = Node5
        root.right.right.right = Node6

        #如果是第一次出价 不提供建议出价，但会给出反馈
        if times == 5:
            #实例化商人决策
            merchant_decision = d.Decision_tree().decision(root,player_bid,price,lowest_price)

        #如果不是第一次出价，提供建议出价，根据出价提供反馈
        else:
            d.binary_suggest(player_bid,lowest_price)
            merchant_decision = d.Decision_tree().decision(root,player_bid,price,lowest_price)

        times-=1

        #检查是否继续讨价还价，如果出价等于最低价格，结束讨价还价
        if player_bid == lowest_price:
            IsContinue = False
            print("Your Transaction is successful!")

        #检查是否继续进行游戏
        if (times == 0 or not IsContinue):
            print("Game is over!")
            break