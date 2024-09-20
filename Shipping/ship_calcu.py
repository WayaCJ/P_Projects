weight = input("Package weight: ")
cost = 0
dronecost = 0
premium = 125.00
try:
    weight = int(weight)
# Ground Shipping
    if weight <= 2:
        cost = (1.50 * weight) + 20
    elif weight <= 6:
        cost = (3.00 * weight) + 20
    elif weight <= 10:
        cost = (4.00 * weight) + 20
    else:
        cost = (4.75 * weight) + 20
    print("Ground Shipping: $", cost)
    print("Ground Shipping Premium: $", premium)

# Drone Shipping
    if weight <= 2:
        dronecost = (4.50 * weight)
    elif weight <= 6:
        dronecost = (9.00 * weight)
    elif weight <= 10:
        dronecost = (12.00 * weight)
    else:
        dronecost = (14.25 * weight)
    print("Drone Shipping: $", dronecost)

    if cost < dronecost and cost < premium:
        print("The cheapest way is by Ground Shipping")
    elif dronecost < cost and dronecost < premium:
        print("The cheapest way is by Drone Shipping")
    else:
        print("We recommend using Premium Ground Shipping")
except ValueError:
    print("Try again. Try using just numbers")