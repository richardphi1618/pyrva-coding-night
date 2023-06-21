from enum import IntEnum

ONE_BEER = "hansa"
ONE_CIDER = "grans"
A_PROPER_CIDER = "strongbow"
GT = "gt"
BACARDI_SPECIAL = "bacardi_special"

class Ingredients(IntEnum):
    rum = 65
    grenadine = 10
    juice = 10
    green_stuff = 10
    tonic_water = 20
    gin = 85


def compute_cost(drink: str, is_student: bool, amount: int):
    if amount > 2 and (drink == GT or drink == BACARDI_SPECIAL):
        raise ValueError('Too many drinks, max 2.')

    ingredient = Ingredients

    drink_prices = {
        ONE_BEER: 74,
        ONE_CIDER: 103,
        A_PROPER_CIDER: 110,
        GT: ingredient.gin + ingredient.tonic_water + ingredient.green_stuff,
        BACARDI_SPECIAL: ingredient.gin / 2 + ingredient.rum + ingredient.grenadine + ingredient.juice
    }

    price = drink_prices.get(drink, None)
    if price is None:
        raise ValueError('No such drink exists')

    if is_student and (drink == ONE_CIDER or drink == ONE_BEER or drink == A_PROPER_CIDER):
        price = price - price / 10
    return price * amount
