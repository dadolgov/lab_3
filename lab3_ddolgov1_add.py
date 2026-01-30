"""
List of items
Author: Dmitrii Dolgov
Purpose: prints out the list of things in different orders
1/30/2026
"""

from lab3_ddolgov1_list import my_items
#using .extend() is more optimal than using .append() 5 times
my_items.extend(["food","water","matches","shovel","sleeping bag"])
my_items.sort(reverse=True)
print("Here is the extended list of my things in reverse order:")

print(*my_items, sep=", ")
print(" ")
