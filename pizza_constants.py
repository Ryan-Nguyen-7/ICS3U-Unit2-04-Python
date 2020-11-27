#!/usr/bin/env python3

# Created by Ryan Nguyen
# Created on November 2020
# This program calculates the cost of a pizza
#    using constants and user input

import constants


def main():
    # this function calculates za total

    # input
    diameter = int(input("Enter diameter of pizza (inch):"))

    # process
    total = (diameter*constants.COST_PER_INCH+constants.RENT +
             constants.LABOUR)*(constants.HST+1)

    # output
    print("")
    print("The total cost for {0} \
        inch pizza is %{1:,.2f}".format(diameter, total))


if __name__ == "__main__":
    main()
