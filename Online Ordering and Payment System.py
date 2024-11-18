print("Welcome to online Ordering")
print()

items = {"pizza": 40000,"chips": 20000,"chicken": 10000,"soda": 2000,"water": 1500}

order = input("Would you like to make an order? (yes or no)")
print()
if order == "yes":
    print("Here are some choices to consider:")
    for key,value in items.items():
      print(f"{key.capitalize()}:{value}")
      
if order=="yes":
      print()
      print("Now You Can Make Your Choices")
 
choice2=[]
total_cost=0
while True:
  item_choice=input(f"Enter item{len(choice2)+1} (or type 'done' to stop):    ")
  if  item_choice=="done":
    break
  elif item_choice in items and  item_choice not in choice2:
    choice2.append( item_choice)
    total_cost +=items[item_choice]
    print(f"{ item_choice.capitalize()} added to ur order.")

  elif  item_choice in choice2:
    print("You have already chosen this item.Please select another one")
  else:
    print("invalid choice.Please select an item from the menu")
  
if choice2:
  print("\nYou have Chosen the following items: ")
  for item in choice2:
    print(f"{item.capitalize()} for {items[item]}")
  
  print(f"\nTotal cost: {total_cost}shs")
  
else:
  print("No items selected.")

  
if order=="no":
  print("Okay, Maybe next time!")

  
  # paying
payment = input("\nWould You LIke To Pay Now?(yes/no):   ")
if payment =="yes":
  
  while True:
   pin= input("Enter your payment PIN to Corfirm: ")
   if  pin.isdigit() and len(pin) in [4, 5]:
     break
   else:
     print("Invalid PIN. Please enter a 4 or 5-digit PIN.")
     
  while True:
   phone_Number=input("Please enter Your Phone Number:  ")
   if  phone_Number.isdigit() and len(phone_Number) == 10:
    break
  else:
    print("Invalid phone number. Please enter a 10-digit phone number.")
    
  Location= input("Please enter Your Location:  ")
  
  print("\npayment received. Your order will be delivered to:")
  print(f"Phone Number:      { phone_Number}")
  print(f"Delivery Location: { Location}")
  print("Thank you for your order! It will be delivered soon.")
  
  
  # receipt
  print("\n--- RECEIPT ---")
  print("Online.com Receipt")
  print(f"Phone Number:      {phone_Number}")
  print(f"Delivery Location: {Location}")
  print("\nItems Ordered:")

  for item in choice2:
     print(f"{item.capitalize()}: {items[item]} shs")
            
  print(f"\nTotal: {total_cost} shs")
  print("\nThank you for shopping with us!")
  print("Your order is being processed and will arrive shortly.")
        
else:
  print("Payment not received. Please comeback when you are ready!!!!!")
  