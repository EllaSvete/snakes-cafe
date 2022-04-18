print('$ python snakes_cafe.py')
print('***************')
print('** Welcome to the Snakes Cafe **')
print('** Please see our menu below **')
print('To quit at any time, type quit')

appetizers = ['Wings','Cookies','Spring Rolls']
entrees = ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden']
desserts = ['Ice Cream', 'Cake', 'Pie']
drinks = ['Coffee', 'Tea', 'Unicorn']

print("""
Appetizers
----------""")

for appetizer in appetizers:
  print(appetizer)

print("""
Entrees
----------""")

for entree in entrees:
  print(entree)

print(entree)

print("""
Desserts
----------""")
for dessert in desserts:
  print(dessert)

print("""
Drinks
----------""")
for drink in drinks:
  print(drink)

print('***********************************')
print('** What would you like to order? **')
print('***********************************')

items = {}

while True:
  order = input('> ')
  if order == 'quit':
    break
  elif order not in items:
    items[order] = 0

  items[order] += 1
  print(f"** {items[order]} order of {order} has been added to your meal **")

