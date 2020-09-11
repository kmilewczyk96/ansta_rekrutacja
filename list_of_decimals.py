from decimal import Decimal


def list_of_decimals(first, last, step):
    result = []
    first = Decimal(first)
    last = Decimal(last)
    step = Decimal(step)

    while first <= last:
        result.append(first)
        first += step

    return result


if __name__ == '__main__':
    print(list_of_decimals(2, 5.5, 0.5))
