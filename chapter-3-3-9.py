# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (page 46), use len() to print a message indicating the number of people you are inviting to dinner.

# Exercise 3-6
presidents = ["Obama", "Lula", "Merkel"]

presidents.remove(presidents[2])
presidents.insert(2,"Macron")

presidents.insert(0,"Lincoln")
presidents.insert(1,"Fernando")
presidents.append("Boris")

print("Number of people on dinner: " + str(len(presidents)))