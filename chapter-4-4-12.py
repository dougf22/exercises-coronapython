# 4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing to save space. Choose a version of foods.py, and write two for loops to print each list of foods.

# First foods.py
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite pizzas are: ")
for i in my_foods:
    print(i)

print("My friend’s favorite foods are: ")
for i in friend_foods:
    print(i)