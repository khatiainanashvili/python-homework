# 1. დაწერე პროგრამა რომელიც გეკითხება ჯერ სახელს, შემდეგ გვარს და ინფორმაციის მიღების
# შემდეგ ტერმინალში ბეჭდავს ერთმანეთის გვერდით.

firstname = input("Enter your Firstname: ")
surname = input("Enter your Surname: ")

fullname = firstname + " " + surname
print(fullname)
# or
print(firstname, surname, sep = " ")

# 2. დაწერე პროგრამა რომელიც ითხოვს ორ რიცხვს, პირველი რიცხვი აჰყავს მეორის ხარისხში
# და შედეგი იბეჭდება ტერმინალში.

num1 = int(input("Enter the number: "))
num2 = int(input("Enter the exponentiation number: "))
exponentiation = (num1 ** num2)

print(exponentiation)

# 3. დაწერე პროგრამა რომელიც გეკითხება სახელს, გვარს, ასაკს და ქალაქს და ბეჭდავს
# ინფორმაციას შემდეგი სახით:
# Name: Lia
# Surname: Kebadze
# Age: 20
# City: Tbilisi

name2 = input("Enter your name...")
surname2 = input("Enter your surname...")
age = input("Enter your age...")
city = input("Eenter your City...")

user ="""
Name: {}
Surname: {}
Age: {}
City: {}
    """.format(name2, surname2, age, city)

print(user)


# დაწერე პროგრამა, რომელიც გთხოვს შეიყვანო ნებისმიერი სამი სხვადასხვა ხილის
# დასახელება ცალცალკე. რეზულტატი კი იბეჭდება შემდეგი სახით:
# Apple//Peach%%Orange

fruit1 = input("Enter your favorite fruit...")
fruit2 = input("Enter your second favorite fruit...")
fruit3 = input("Enter your third favorite fruit...")

print(fruit1 + "//" + fruit2 + "%%" + fruit3)

# 5. დაწერე პროგრამა, რომელიც გთხოვს შეიყვანო ტექსტი, დათვლის მასში არსებული
# სიმბოლოების რაოდენობას და გამოიტანს შედეგს შემდეგნაირად:
# Number of symbols: 50

message = input("Enter the message...")

print("Number of symbols: ", len(message))

