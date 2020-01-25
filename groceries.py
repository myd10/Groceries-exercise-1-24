# groceries.py

#from pprint import pprint

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
   {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
   {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#print(products)
# pprint(products)

# TODO: write some Python code here to produce the desired output
#Header, There are 20 products example

products_count = len(products)

print("--------------")
print("THERE ARE " + str(products_count) + " PRODUCTS:")
print("--------------")
 
#important to sort before you look through them and print
 
def sort_by_name(my_product):
    return my_product["name"]
sorted_products = sorted(products, key=sort_by_name)

 #printing the list of products and price
for my_product in sorted_products:
    #print(my_product["name"]), just printing name
    #price_usd = my_product["price"], prints price w/o formating
    price_usd = " (${0:.2f})".format(my_product["price"])
    print(" + " + my_product["name"] + str(price_usd))


#
#second stage of exercise, departments
#

departments = []
for my_product in products:
    #print(my_product["department"]), print department name
    if my_product["department"] not in departments:
        departments.append(my_product["department"])



department_count = len(departments)

print("-----------")
print("THERE ARE " + str(department_count) + " DEPARTMENTS")
print("-----------")


departments.sort()


for the_department in departments:
    products_per_department =[my_product for my_product in products if my_product["department"] == the_department]
    products_per_department_count = len(products_per_department)
    if products_per_department_count > 1: #if products_per_department count is less than 1 it won't show up so I am not worried about the phrase 0 product
        label = "products"
    else:
        label = "product" 
    print(" + " + the_department.title() + " (" + str(products_per_department_count) + " " + label + ")")



#--------------
#THERE ARE 20 DEPARTMENTS:
#--------------
# + All-Seasons Salt ($4.99)
# + Chocolate Fudge Layer Cake ($18.50)
# + Chocolate Sandwich Cookies ($3.50)
# + Cut Russet Potatoes Steam N' Mash ($4.25)
# + Dry Nose Oil ($21.99)
# + Fresh Scent Dishwasher Cleaner ($4.99)
# + Gluten Free Quinoa Three Cheese & Mushroom Blend ($3.99)
# + Green Chile Anytime Sauce ($7.99)
# + Light Strawberry Blueberry Yogurt ($6.50)
# + Mint Chocolate Flavored Syrup ($4.50)
# + Overnight Diapers Size 6 ($25.50)
# + Peach Mango Juice ($1.99)
# + Pizza For One Suprema Frozen Pizza ($12.50)
# + Pomegranate Cranberry & Aloe Vera Enrich Drink ($4.25)
# + Pure Coconut Water With Orange ($3.50)
# + Rendered Duck Fat ($9.99)
# + Robust Golden Unsweetened Oolong Tea ($2.49)
# + Saline Nasal Mist ($16.00)
# + Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce ($6.99)
# + Sparkling Orange Juice & Prickly Pear Beverage ($2.99) 
# -------------
# THERE ARE 10 DEPARTMENTS:
# -------------
# + Babies (1 product)
# + Beverages (5 products)
# + Dairy Eggs (1 product)
# + Dry Goods Pasta (1 product)
# + Frozen (4 products)
# + Household (1 product)
# + Meat Seafood (1 product)
# + Pantry (2 products)
# + Personal Care (2 products)
# + Snacks (2 products)