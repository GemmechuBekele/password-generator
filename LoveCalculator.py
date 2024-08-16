print("Welcome to Love Calculator!")
name1 = input("What is your full name? \n")
name2 = input("What is your lover full name? \n")

# change the name into lower case
lower_name1 = name1.lower()
lower_name2 = name2.lower()

# concatenation
name = lower_name1 + lower_name2
# count the letter
t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")
true = t + r + u + e
print(true)
# again count for love
l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")
love = l + o + v + e
print(love)
if love == 10:
    love = 1
elif true == 10:
    true = 9
true_love = str(true) + str(love)
love_score = int(true_love)
if love_score < 100 or love_score > 90:
    print(f"your score is {love_score}, you go together like Coke and Mentos")
elif 40 < love_score < 50:
    print(f"your score is {love_score}, you are alright together")
else:
    print(f"your score is {love_score}")
