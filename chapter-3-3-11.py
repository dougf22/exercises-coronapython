# 3-11. Intentional Error: If you haven’t received an index error in one of your programs yet, try to make one happen. Change an index in one of your programs to produce an index error. Make sure you correct the error before closing the program.

# Exercise 3-10
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
print("Hey, " + presidents[6] + " i am making dinner, please come!")

print("Number of people on dinner: " + str(len(presidents)))