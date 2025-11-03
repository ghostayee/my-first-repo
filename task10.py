# Write a program that calculates the total stock in a company
# from the array/list below if we know that the stock is the last
#  digit in every array/list.
# prods = [[‘omo’,’30kes’,’300’],
#  [‘milk’,’50kes’,’200’],[‘bread’,’45kes’,’359’],
#  [‘coffee’,’5kes’,’79’]]

# NB: ONCE YOU COPY AND PASTE THE LIST ABOVE,REWRITE THE SINGLE
# QUOTES AS THE ABOVE LIST WILL GIVE YOU AN ERROR.

prods = [
    ['omo','30kes','300'],
    ['milk','50kes','200'],
    ['bread','45kes','359'],
    ['coffee','5kes','79']
    ]
stock = 0
for product in prods:
    stock_index = int(product[-1])
    stock += stock_index

print("Total stock in the company is", stock)