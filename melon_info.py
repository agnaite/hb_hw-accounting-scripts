"""
Prints out all the melons in our inventory
"""

from melons import melons

for melon, items in melons.items():
    print melon.upper()
    for key, value in items.items():
        print "   {}: {}".format(key, value)
