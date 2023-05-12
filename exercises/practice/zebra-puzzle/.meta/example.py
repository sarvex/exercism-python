"""This solution for the Zebra Puzzle is adapted from a solution
by Peter Norvig for the course "Design of Computer Programs" on Udacity.
https://www.udacity.com/course/cs212
"""

from itertools import permutations


def just_right_of(width, height):
    return width - height == 1


def next_to(width, height):
    return abs(width - height) == 1


def solution():
    houses = first, _, middle, _, _ = range(5)
    orderings = list(permutations(houses))

    return next(
        [
            {
                english_man: 'Englishman',
                spaniard: 'Spaniard',
                ukrainian: 'Ukrainian',
                japanese: 'Japanese',
                norwegian: 'Norwegian',
            }[idx]
            for idx in (water, zebra)
        ]
        for (red, green, ivory, yellow, blue) in orderings
        if just_right_of(green, ivory)
        for (
            english_man,
            spaniard,
            ukrainian,
            japanese,
            norwegian,
        ) in orderings
        if english_man is red
        if norwegian is first
        if next_to(norwegian, blue)
        for (coffee, tea, milk, orange_juice, water) in orderings
        if coffee is green
        if ukrainian is tea
        if milk is middle
        for (
            old_gold,
            kools,
            chesterfields,
            lucky_strike,
            parliaments,
        ) in orderings
        if kools is yellow
        if lucky_strike is orange_juice
        if japanese is parliaments
        for (dog, snails, fox, horse, zebra) in orderings
        if spaniard is dog
        if old_gold is snails
        if next_to(chesterfields, fox)
        if next_to(kools, horse)
    )


def drinks_water():
    answer, _ = solution()
    return answer


def owns_zebra():
    _, answer = solution()
    return answer
