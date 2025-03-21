#实例化
import sale
inventory = sale.Inventory()

class Node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.player_bid = 0

class Decision_tree(Node):
    def __init__(self,value=0):
        super().__init__(value)

    def decision(self,root,player_bid,price,lowest_price):
        if player_bid >= price: #root
            print (f"Merchant:{root.left.value}") #Node1
        elif player_bid < price: 
            if player_bid == lowest_price: #Node2
                print(f"Merchant:{root.right.left.value}") #Node3
            elif player_bid > lowest_price: #Node4
                print(f"Merchant:{root.right.right.left.value}") #Node5
            else:
                print(f"Merchant:{root.right.right.right.value}") #Node6


def ask_choice():
    p_input = input("Which product you want to bargain with?\nEnter the name here:")
    return p_input

def ask_bid():
    bid = input("Enter my bid:")
    if bid.isdigit():  # 检查输入是否为数字
        return int(bid)
    else:
        print("Invalid input. Please enter a valid number.")
    

def binary_suggest(player_bid,lowest_price): #建议出价
    if player_bid > lowest_price:
        suggest_price = (player_bid+lowest_price)//2
        print(f"Suggested Bid: {suggest_price}")


