def meal_cost_calc(cost, tip, tax):
    """ Compute the total cost of a meal
        given the cost$, tip%, tax%"""
    tip = cost * (tip / 100)
    tax = cost * (tax / 100)
    return round(cost + tip + tax)


if __name__ == "__main__":
    cost = float(input())
    tip = int(input())
    tax = int(input())

    total = meal_cost_calc(cost, tip, tax)
    print("The total meal cost is {} dollars.".format(total))
