# AUTHOR: Colin Brinton
# FILENAME: P3.py
# DATE: 04/22/2016
# REVISION HISTORY: 1.0

from re import compile, X
from sys import argv

FILE = 1
DOLLARS = 0
CENTS = 1
SALE = '.99'
OUTPUT1 = 'bucks.txt'
OUTPUT2 = 'sale.txt'
OUTPUT3 = 'misc.txt'
PREFIX = '$'
DELIM = '\n'

f = open(argv[FILE], 'r')
string = f.read()
f.close()

price = compile(r"""
                     \$              # Start of a valid price signified by dollar sign
                                     # First capturing group:
                     ([1-9]\d*)      #   Price must start with a non-zero digit, followed optionally by other digits
                                     # Second capturing group:
                     (\.\d\d)?       #   The cent portion of the price is optional, one dot and two any digits match
                                     # Negative Lookahead:
                     (?![\d.])       #   Reject the price if the cent portion has an extra digit or dot """, X)

valid_prices = price.findall(string)

bucks = [price for price in valid_prices if not price[CENTS]]
b = open(OUTPUT1, 'w')
for price in bucks:
    b.write(PREFIX)
    b.write(price[DOLLARS])
    b.write(DELIM)
b.close()

sale = [price for price in valid_prices if price[CENTS] == SALE]
s = open(OUTPUT2, 'w')
for price in sale:
    s.write(PREFIX)
    s.write(price[DOLLARS])
    s.write(price[CENTS])
    s.write(DELIM)
s.close()

misc = [price for price in valid_prices if price not in bucks and price not in sale]
m = open(OUTPUT3, 'w')
for price in misc:
    m.write(PREFIX)
    m.write(price[DOLLARS])
    m.write(price[CENTS])
    m.write(DELIM)
m.close() 

