
# ==========================================
# STOCK PORTFOLIO TRACKER
# ==========================================

# Empty dictionary for stock prices
stock_prices = {}

# Empty dictionary for portfolio
portfolio = {}

# Variable to store total investment
total_investment = 0

# Number of different stocks
n = int(input("Enter number of stocks: "))

# Taking stock names, prices and quantities from user
for i in range(n):

    stock_name = input("\nEnter stock name: ").upper()

    stock_price = float(input("Enter stock price: "))

    quantity = int(input("Enter quantity: "))

    # Store stock price
    stock_prices[stock_name] = stock_price

# Store quantity
portfolio[stock_name] = quantity

# Display portfolio details
print("\n===== PORTFOLIO DETAILS =====")

for stock in portfolio:

    price = stock_prices[stock]
    quantity = portfolio[stock]

    investment = price * quantity

    total_investment += investment

    print(f"{stock} -> Price: ${price}, Quantity: {quantity}, Value: ${investment}")

# Display total investment
print("\nTotal Investment Value = $", total_investment)

# Save data into text file
file = open("portfolio.txt", "w")

file.write("===== PORTFOLIO DETAILS =====\n")

for stock in portfolio:

    price = stock_prices[stock]
    quantity = portfolio[stock]

    investment = price * quantity

    file.write(f"{stock} -> Price: ${price}, Quantity: {quantity}, Value: ${investment}\n")

file.write(f"\nTotal Investment Value = ${total_investment}")

file.close()

print("\nPortfolio saved successfully in portfolio.txt")
print()
print("\n DETAILS STORED IN TEXT FILE IS BEING SHOWN")


# Open and read the portfolio.txt file

file = open("portfolio.txt", "r")

content = file.read()

print(content)

file.close()
