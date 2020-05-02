# 3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
#
# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print statement to the end of your program informing people that you found a bigger dinner table.
#
# • Use insert() to add one new guest to the beginning of your list.
#
# • Use insert() to add one new guest to the middle of your list.
#
# • Use append() to add one new guest to the end of your list.
#
# • Print a new set of invitation messages, one for each person in your list. 

# Exercise 3-5
presidents = ["Obama", "Lula", "Merkel"]
print("Hey, " + presidents[0] + " i am making dinner, please come!")
print("Hey, " + presidents[1] + " i am making dinner, please come!")
print("Hey, " + presidents[2] + " i am making dinner, please come!")

print("Hey, " + presidents[2] + " can't make it.")

presidents.remove(presidents[2])
presidents.insert(2,"Macron")

print("Hey, " + presidents[0] + " i am making dinner, please come!")
print("Hey, " + presidents[1] + " i am making dinner, please come!")
print("Hey, " + presidents[2] + " i am making dinner, please come!")

print("I found a bigger table!")
presidents.insert(0,"Lincoln")
presidents.insert(1,"Fernando")
presidents.append("Boris")

print("Hey, " + presidents[0] + " i am making dinner, please come!")
print("Hey, " + presidents[1] + " i am making dinner, please come!")
print("Hey, " + presidents[2] + " i am making dinner, please come!")
print("Hey, " + presidents[3] + " i am making dinner, please come!")
print("Hey, " + presidents[4] + " i am making dinner, please come!")
print("Hey, " + presidents[5] + " i am making dinner, please come!")