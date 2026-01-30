"""
List of items
Author: Dmitrii Dolgov
Purpose: removes binoculars from the list and prints out the final list and its length
1/30/2026
"""

from lab3_ddolgov1_replace import my_items

print("Actually, I don't want binoculars...")
my_items.remove("binoculars")
print("So here's my final list:")
print(*my_items, sep=", ")
print(f"In total, I'm taking {len(my_items)} items to my camping trip.")