guests=['Stephen Hawking', 'Nikola Tesla', 'Albert Einstein', 'Abraham Lincoln']
print("Hello, " + guests[0] + " I'm organizing a small dinner. It would be an honor to have you here with us" )
print("Hello, " + guests[1] + " I'm organizing a small dinner. It would be an honor to have you here with us" )
print("Hello, " + guests[2] + " I'm organizing a small dinner. It would be an honor to have you here with us" )
print("Hello, " + guests[3] + " I'm organizing a small dinner. It would be an honor to have you here with us" )

print("Sadly " + guests[1] + " couldn't join us for the dinner tonight")

guests[1]= 'Steve Jobs'
print("Hello, " + guests[0] + " I'm organizing a small dinner. It would be an honor to have you here with us" )
print("Hello, " + guests[1] + " I'm organizing a small dinner. It would be an honor to have you here with us" )
print("Hello, " + guests[2] + " I'm organizing a small dinner. It would be an honor to have you here with us" )
print("Hello, " + guests[3] + " I'm organizing a small dinner. It would be an honor to have you here with us" )

guests.insert(0, "Charles Dickens")
guests.insert(2, "Charles Darwin")
guests.append("Marie Curie")
print("Hello, " + guests[0] + " I'm organizing a small dinner. It would be an honor to have you here with us" )
print("Hello, " + guests[1] + " I'm organizing a small dinner. It would be an honor to have you here with us" )
print("Hello, " + guests[2] + " I'm organizing a small dinner. It would be an honor to have you here with us" )
print("Hello, " + guests[3] + " I'm organizing a small dinner. It would be an honor to have you here with us" )
print("Hello, " + guests[4] + " I'm organizing a small dinner. It would be an honor to have you here with us" )
print("Hello, " + guests[5] + " I'm organizing a small dinner. It would be an honor to have you here with us" )
print("Hello, " + guests[6] + " I'm organizing a small dinner. It would be an honor to have you here with us" )

print("It is with great embarrasment that I have to tell you that I can only invite two peope for dinner since my new dinner table didn't arrive.")

removed= guests.pop()
print ("I'm really sorry I couldn't invite you for my dinner tongiht, " + removed + ".")

removed= guests.pop()
print ("I'm really sorry I couldn't invite you for my dinner tongiht, " + removed + ".")

removed= guests.pop()
print ("I'm really sorry I couldn't invite you for my dinner tongiht, " + removed + ".")

removed= guests.pop()
print ("I'm really sorry I couldn't invite you for my dinner tongiht, " + removed + ".")

removed= guests.pop()
print ("I'm really sorry I couldn't invite you for my dinner tongiht, " + removed + ".")

print ("Hey, " + guests[0] + " it is with great pleasure that I tell you that you are still invited to the dinner!")
print ("Hey, " + guests[1] + " it is with great pleasure that I tell you that you are still invited to the dinner!")

del guests[1]
del guests[0]

print (guests)

