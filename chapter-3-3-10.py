# 3-10. Every Function: Think of something you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.

# Exercise 3-9
presidents = ["Obama", "Lula", "Merkel"]

presidents.remove(presidents[2])
presidents.insert(2,"Macron")

presidents.insert(0,"Lincoln")
presidents.insert(1,"Fernando")
presidents.append("Boris")

print(presidents)
print(sorted(presidents,reverse=True))
presidents.reverse()
print(presidents)
presidents.sort(reverse=True)
print(presidents)

print("Hey, " + presidents[0] + " i am making dinner, please come!")
print("Hey, " + presidents[1] + " i am making dinner, please come!")
print("Hey, " + presidents[2] + " i am making dinner, please come!")
print("Hey, " + presidents[3] + " i am making dinner, please come!")
print("Hey, " + presidents[4] + " i am making dinner, please come!")
print("Hey, " + presidents[5] + " i am making dinner, please come!")

print("Number of people on dinner: " + str(len(presidents)))