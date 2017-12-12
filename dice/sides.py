from random import randint


def dice(num=1, side=0):
    if not side:
        raise ValueError('No sides to your dice!')

    return [randint(1, side) for x in range(0, num)]


def d4(num=1):
    return dice(num, 4)


def d6(num=1):
    return dice(num, 6)


def d8(num=1):
    return dice(num, 8)


def d10(num=1):
    return dice(num, 10)


def d12(num=1):
    return dice(num, 12)


def d20(num=1):
    return dice(num, 20)


def d100(num=1):
    return dice(num, 100)

def best_of(picks, rolls, die=d6):
    assert picks > 0
    assert rolls > 0
    result = die(rolls)
    assert result.rolls('rolls')
    sorted_rolls = result.sort(reverse=True)
    return sorted_rolls[:picks]
