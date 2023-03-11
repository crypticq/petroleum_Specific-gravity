#!/usr/bin/env python3


def specific_gravity(API):

    Specific_Gravity = (141.5 / API) - 131.5
    if API >= 35:
        return round(Specific_Gravity, 2)
    if API >= 45:
        return round(Specific_Gravity, 2)
    if API <= 35:
        return round(Specific_Gravity, 2)
    if API <= 25:
        return round(Specific_Gravity, 2)
    if API < 15:
        return round(Specific_Gravity, 2)


def run():
    API = float(input("Enter API: "))
    if API >= 35:
        print(
            "The specific gravity is {} ans it's Light crude Oil".format(
                abs(int(specific_gravity(API)))
            )
        )
    elif API >= 45:
        print(
            "The specific gravity is {} ans it's Medium crude Oil".format(
                abs(int(specific_gravity(API)))
            )
        )
    elif API <= 35:
        print(
            "The specific gravity is {} ans it's Heavy crude Oil".format(
                abs(int(specific_gravity(API)))
            )
        )
    elif API <= 25:
        print(
            "The specific gravity is {} ans it's Very Heavy crude Oil".format(
                abs(int(specific_gravity(API)))
            )
        )
    elif API < 15:
        print(
            "The specific gravity is {} ans it's Extremely Heavy crude Oil".format(
                abs(int(specific_gravity(API)))
            )
        )
    else:
        print("The specific gravity is {}".format(abs(int(specific_gravity(API)))))


if __name__ == "__main__":
    run()
