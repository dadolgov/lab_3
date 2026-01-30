"""
List of items
Author: Dmitrii Dolgov
Purpose: prints out the list of things in different orders
1/30/2026
"""

my_items=["tent","tent poles", "hammer", "swiss knife", "compass","map", 
          "spare boots", "fishing rod", "tackle box", "book"]
print(f"I have {len(my_items)} items in my list.")
my_items.sort()
print("here they are in alphabetical order:")
print(*my_items,sep=", ")
print()