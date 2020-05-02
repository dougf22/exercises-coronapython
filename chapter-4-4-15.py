# 4-15. Code Review: Choose three of the programs you’ve written in this chapter and modify each one to comply with PEP 8:
#
# • Use four spaces for each indentation level. Set your text editor to insert four spaces every time you press TAB, if you haven’t already done so (see Appendix B for instructions on how to do this).
#
# • Use less than 80 characters on each line, and set your editor to show a vertical guideline at the 80th character position.
#
# • Don’t use blank lines excessively in your program files.

# Exercise 4-7
numbers = range(3,31,3)
for i in numbers:
    print(str(i))

# Exercise 4-9
complist = [i**3 for i in range(1,11)]
print(complist)

# Exercise 4-12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite pizzas are: ")
for i in my_foods:
    print(i)

print("My friend’s favorite foods are: ")
for i in friend_foods:
    print(i)