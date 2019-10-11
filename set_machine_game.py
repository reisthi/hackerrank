# Sets is a matching game, played with a special deck of cards. Each
# card in the deck has a pictogram on it.
#
# Each pictogram has four properties; each property has three choices:
#
#   - Shape   (pill/diamond/squiggle)
#   - Number  (1/2/3)
#   - Color   (red/green/purple)
#   - Fill    (solid/open/hatch)
#
# The deck is made up of one card with each possible combination of
# properties. No two cards are exactly the same.
#
# The objective of the game is to find sets of three cards which
# form a "set". A set is formed when ALL of the following are true
# about a group of three cards:
#
# - They all have the same number or have three different numbers.
# - They all have the same shape or have three different shapes.
# - They all have the same fill or have three different fills.
# - They all have the same color or have three different colors.
#
# Here's an example
# https://d2r55xnwy6nx47.cloudfront.net/uploads/2016/05/SETPoint_2000.png
# https://mrrgteacher.files.wordpress.com/2011/12/sets_examples1-1024x586.png

# different properties a card can have
PROPERTIES = {
    'shape': ['Pill', 'Diamond', 'Squiggle'],
    'number': [1, 2, 3],
    'color': ['Red', 'Green', 'Purple'],
    'fill': ['Solid', 'Open', 'Hatch'],
}

# example of a card instance
my_card = {
    'shape': 'Pill',
    'number': 2,
    'color': 'Purple',
    'fill': 'Solid',
}


# 1, 2, 3
# "purple", "purple", "blue"
def is_valid(properties):
    unique_values = len(set(properties))
    return unique_values == 1 or unique_values == 3


def is_set(cards):
    for prop in PROPERTIES:
        if not is_valid([cards[0][prop], cards[1][prop], cards[2][prop]]):
            return False

    return True

    # number_valid = is_valid([cards[0]["number"], cards[1]["number"], cards[2]["number"]])
    # return number_valid

    # [{'shape': 'Pill', 'number': 3, 'color': 'Red', 'fill': 'Solid'}, {'shape': 'Diamond', 'number': 2, 'color': 'Green', 'fill': 'Hatch'}, {'shape': 'Squiggle', 'number': 1, 'color': 'Purple', 'fill': 'Open'}]
    # set_one = cards[0]
    # set_two = cards[1]
    # set_three = cards[2]

    # if set_one == set_two:
    #     if set_two == set_three:
    #         if set_one == set_three:
    #             passed = True

    # if len((set(set_one.values()) - set(set_two.values()))) == 3:
    #     if len((set(set_one.values()) - set(set_three.values()))) == 3:
    #         if len((set(set_two.values()) - set(set_three.values()))) == 3:
    #             passed = True

    # list_two = set_two.values()
    # list_three = set_three.values()

    # print(number)
    # if not number == set_two['number'] and not number == set_three['number']:
    #     passed = False
    # if not shape == set_two['shape'] and not shape == set_three['shape']:
    #     passed = False
    # if not shape == set_two['shape'] and not shape == set_three['shape']:
    #     passed = False
    # print(passed)
    # return passed


if __name__ == '__main__':
    # valid
    # ['Pill', 3, 'Red', 'Solid']
    # ['Diamond', 2, 'Green', 'Hatch']
    # ['Squiggle', 1, 'Purple', 'Open']
    card1 = {
        'shape': 'Pill',
        'number': 3,
        'color': 'Red',
        'fill': 'Solid',
    }
    card2 = {
        'shape': 'Diamond',
        'number': 2,
        'color': 'Green',
        'fill': 'Hatch',
    }
    card3 = {
        'shape': 'Squiggle',
        'number': 1,
        'color': 'Purple',
        'fill': 'Open',
    }

    # valid
    # ['Pill', 2, 'Green', 'Open']
    # ['Diamond', 2, 'Green', 'Hatch']
    # ['Squiggle', 2, 'Green', 'Solid']
    card4 = {
        'shape': 'Pill',
        'number': 2,
        'color': 'Green',
        'fill': 'Open',
    }
    card5 = {
        'shape': 'Diamond',
        'number': 2,
        'color': 'Green',
        'fill': 'Hatch',
    }
    card6 = {
        'shape': 'Squiggle',
        'number': 2,
        'color': 'Green',
        'fill': 'Solid',
    }

    # not valid
    # ['Pill', 2, 'Green', 'Solid']
    # ['Diamond', 2, 'Green', 'Hatch']
    # ['Squiggle', 2, 'Green', 'Solid']
    card7 = {
        'shape': 'Pill',
        'number': 2,
        'color': 'Green',
        'fill': 'Solid',
    }
    card8 = {
        'shape': 'Diamond',
        'number': 2,
        'color': 'Green',
        'fill': 'Hatch',
    }
    card9 = {
        'shape': 'Squiggle',
        'number': 2,
        'color': 'Green',
        'fill': 'Solid',
    }

    print(is_set([card1, card2, card3]), True)
    print(is_set([card4, card5, card6]), True)
    print(is_set([card7, card8, card9]), False)
