# Asks the user for a food product and the price of that product
# Has an exit clause if the user wishes to stop the program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy or press q to quit: ")
    if food.lower() == 'q':
        break
    else:
        try:
            price = float(input(f"Enter the price of the {food}: R"))
        except ValueError:
            print("Please enter a valid number for the price.")
            continue
        foods.append(food) 
        prices.append(price)

print("\n-------YOUR CART--------")
for i in range(len(foods)):
    print(f"{foods[i]}: R{prices[i]:.2f}")

total = sum(prices) 

print("\nYour total is: R{:.2f}".format(total))
