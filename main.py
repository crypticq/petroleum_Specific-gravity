#!/usr/bin/env python3


def api_denisty(Specific_Gravity):

    API = (141.5 / Specific_Gravity) - 131.5
    if API >= 35:
        return "Oil Has {} API and it's Light crude Oil".format(round(API))
    if API >= 45:
        return "Oil Has {} API and it's Extra light oil".format(round(API))
    if API <= 35:
        return "Oil has {} API and it's medium crude Oil".format(round(API))
    if API <= 25:
        return "Oil Has {} API and it's heavy crude Oil ".format(round(API))
    if API < 15:
        return "Oil has {} API and it's very heavy oil".format(round(API))


if __name__ == "__main__":
    api = float(input(" Enter Specific Gravity:  "))
    density = api_denisty(api)
    print(density)
