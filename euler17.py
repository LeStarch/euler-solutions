#!/usr/bin/env python
from __future__ import print_function
import itertools
#Constants setups
singles = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
thousand = len("one thousand")


nums = singles + teens + [item[0] + " " + item[1] for item in itertools.product(tens, singles)]
hundreds = [item + " hundred" for item in singles if item != ""]
nums = nums + [item[0] + (" and " if len(item[1]) > 0 else "") + item[1] for item in  itertools.product(hundreds, nums)]
nums = nums + ["one thousand"]

def main():
    ''' Count letters '''
    print("Numbers:\n"+"\n\t".join(nums))
    print("Numbers (small):\n |", "|\n\t|".join([item.replace(" ", "") for item in nums])+"|")
    print("Count: ", sum([len(item.replace(" ", "")) for item in nums]))
if __name__ == "__main__":
    main()
