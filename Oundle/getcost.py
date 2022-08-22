def getCost(weight, volume):
    x = weight * 2
    y = volume * 20
    if weight > 4 and volume > 0.3 and x > y:
        print("cost is", x)
    elif weight > 4 and volume > 0.3 and x < y:
        print("cost is", y)