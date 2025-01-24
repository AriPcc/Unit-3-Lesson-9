TAX_RATE = 0.0875

def main():
    print("Welcome to the tax calculator program!\n")
    # Prompt for cost
    cost = float(input("Enter cost of item: "))
    # Calculate tax
    tax = (cost) * TAX_RATE
    # Print cost, tax, and total cost
    print("Cost: $ ", format(cost, ".2f"))
    print("Tax: $ ", format(tax, ".2f"))
    print("Total: $ ", format((cost + tax), ".2f"))
    # Say goodbye
    print("\nGoodbye!")
main()