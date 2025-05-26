
fruits = ["apple", "banana", "orange"]
vegetables = ["carrot", "broccoli", "spinach"]
meats = ["chicken", "beef", "pork"]

# Create a 2D collection (list of lists)

grocery_list = [fruits, vegetables, meats]
# Accessing elements in the 2D collection

groceries = [["apple", "banana", "orange"],["carrot", "broccoli", "spinach"],["chicken", "beef", "pork"]]

print(grocery_list)

#can display prints as 2D grid, eg: grocieries[1][3] = "spinach"

for collection in grocery_list:
    for item in collection:
        print(item)
    print()
#can also use a for loop to iterate through the 2D collection
#also can use a nested for loop to iterate through each sublist
#can also use tuples instead of lists for 2D collections


