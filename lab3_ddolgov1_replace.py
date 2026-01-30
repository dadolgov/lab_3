"""
List of items
Author: Dmitrii Dolgov
Purpose: prints out the list of things in different orders
1/30/2026
"""
import random
from lab3_ddolgov1_add import my_items

print("Replacing random thing with binoculars:")
#it wasn't specified how exactly to choose wich line to change, so I used random()
my_items[random.randint(1,len(my_items)-2)]="binoculars"
print(*my_items[0:my_items.index("binoculars")], sep=", ")
print(my_items[my_items.index("binoculars")])
print(*my_items[my_items.index("binoculars")+1:], sep=", ")