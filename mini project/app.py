#RESTRO MANAGEMENT SYSTEM

menu={
    'pizza':100,
    'pasta':80,
    'burger':120,
    'salad':90,
    'soft drink':120,
    'coffee':80,
}

print("WELCOME TO J14 RESTAURANT")
print("pizza:100\npasta:80\nburder:120\nsalad:90\nsoft drint:120\ncoffee:80")

order_total=0

item_1=input("Enter the name of item you want to oreder:")
if item_1 in menu:
    order_total+= menu[item_1]
    print(f"your item{item_1} has been added to your order")
else:
    print(f"ordered item{item_1} is not available yet")

another_order=input("Do you want to add another item? (yes/no)")
if another_order=="yes":
    item_2=input("Enter the name of new item:")
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f"Item{item_2} has been added to order")
    else:
        print(f"ordered item{item_2} is not available.!!")
print(f"The total amount of items is {order_total}")