def steps(number):
    if number <= 0:
        raise ValueError('Only positive integers are allowed')

    step_count = 0
    while number > 1:
        number = number * 3 + 1 if is_odd(number) else number / 2
        step_count += 1

    return step_count


def is_odd(number):
    return number % 2 == 1
