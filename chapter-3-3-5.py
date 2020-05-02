# 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
#
# • Start with your program from Exercise 3-4. Add a print statement at the end of your program stating the name of the guest who can’t make it.
#
# • Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#
# • Print a second set of invitation messages, one for each person who is still in your list.

# Exercise 3-4
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