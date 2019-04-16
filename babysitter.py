
def chargeA(time):
    if 15 <= time < 23:
        return 15
    elif 23 <= time < 28:
        return 20
    else:
        return 0


def chargeB(time):
    if 17 <= time < 22:
        return 12
    elif 22 <= time < 24:
        return 8
    elif 24 <= time < 28:
        return 16
    else:
        return 0


def chargeC(time):
    if 17 <= time < 21:
        return 21
    elif 21 <= time < 28:
        return 15
    else:
        return 0


class Family:

    def __init__(self, family):
        if family == "Family B":
            self.charge = chargeB

        elif family == "Family C":
            self.charge = chargeC

        elif family == "Family A":
            self.charge = chargeA

        else:
            raise Exception("INVALID FAMILY")


def calculate(start, stop, family):
    if 4 <= start < 17:
        raise Exception()

    if 4 < stop <= 17:
        raise Exception()

    if stop < 17:
        stop += 24

    if start < 17:
        start += 24

    fee = 0

    f = Family(family)

    for i in range(start, stop):
        fee += f.charge(i)

    return fee
