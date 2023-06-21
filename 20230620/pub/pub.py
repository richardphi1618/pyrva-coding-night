from enum import IntEnum

ONE_BEER = "hansa"
ONE_CIDER = "grans"
A_PROPER_CIDER = "strongbow"
GT = "gt"
BACARDI_SPECIAL = "bacardi_special"


class ingredients_cost(IntEnum):
    rum = 65
    grenadine = 10
    juice = 10
    green_stuff = 10
    tonic_water = 20
    gin = 85


def drink_cost(drink: str, amount: int):
    # import ingredients
    i = ingredients_cost

    # check for error conditions
    if amount > 2 and (drink == GT or drink == BACARDI_SPECIAL):
        raise ValueError('Too many drinks, max 2.')

    # compute price
    drink_prices = {
        ONE_BEER: 74,
        ONE_CIDER: 103,
        A_PROPER_CIDER: 110,
        GT: i.gin + i.tonic_water + i.green_stuff,
        BACARDI_SPECIAL: i.gin / 2 + i.rum + i.grenadine + i.juice
    }
    price = drink_prices.get(drink, None)
    if price is None:
        raise ValueError('No such drink exists')

    return price * amount


def compute_cost(drink: str, is_student: bool, amount: int):
    # calculate cost of drinks
    drinks_cost = drink_cost(drink, amount)

    # calculate drinks discounts
    if is_student and (drink == ONE_CIDER or drink == ONE_BEER or drink == A_PROPER_CIDER):
        drinks_cost = drinks_cost - drinks_cost / 10

    # calculate cost of food
    food_cost = 0

    # calculate food discounts
    # TBD

    # return total cost
    return drinks_cost + food_cost
