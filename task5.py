import random

# 1. ციკლის მეშვეობით 3 მომხმარებელს შეაყვანინე
# ინფორმაცია საკუთარი სახელის, გვარის და ასაკის
# შესახებ. თითოეული მომხმარებლის ინფორმაცია
# შეინახე ინდივიდუალურ სიაში. შემდეგ კი სამივე სია
# დაამატე საერთო ცალრიელ სიას სახელად consumer_info.
# Input_ის მეშვეობით მომხმარებლის ინდექსის შეყვანის
# შემთხვევაში პროგრამამ უნდა დაბრუნოს არჩეულ
# მომხმარებელზე ინფორმაცია შემდეგნაირად:
# Name: Elene
# Lastname: Khardava
# Age: 21

i = 0
user_name = []
user_lastname = []
user_age = []
while i < 3:
    name = input("Enter Name... ")
    lastname = input("Enter Lastname... ")
    age = input("Enter age... ")
    i += 1
    user_name.append(name)
    user_lastname.append(lastname)
    user_age.append(age)

user1 = [user_name[0], user_lastname[0], user_age[0]]
user2 = [user_name[1], user_lastname[1], user_age[1]]
user3 = [user_name[2], user_lastname[2], user_age[2]]

consumer_info = [user1, user2, user3]
user_index = int(input("enter user index... "))

print(f"user N {user_index} is: \nName: {consumer_info[user_index][0]}\n"
      f"Lastname: {consumer_info[user_index][1]}\nAge: {consumer_info[user_index][2]}")

# 2. შექმენი ჩაშენებული სია, რომელშიც იქნება შენახული
# ცნობილი მსახიობების შესახებ ინფორმაცია.
# მომხმარებელს შემოჰყავს მსახიობის სახელი ან გვარი.
# თუ სიაში მოიძებნა მსახიობი, დაბეჭდე მის შესახებ
# არსებული ინფორმაცია რეზუმის სახით.


actors = [
    ["Tom Hanks","Thomas Jeffrey Hanks is an American actor and filmmaker. Known for both his comedic and dramatic roles, he is one of the most popular and recognizable film stars worldwide, and is regarded as an American cultural icon."],
    ["Harrison Ford", "Harrison Ford is an American actor. He has been a leading man in films of several genres, and is regarded as an American cultural icon."],
    ["Will Smith", "Willard Carroll Smith II is an American actor, rapper and film producer. He has received multiple accolades, including an Academy Award, a Golden Globe Award, a BAFTA Award, and four Grammy Awards."],
    ["Natalie Portman", "Natalie Portman is the first person born in the 1980s to have won the Academy Award for Best Actress (for Black Swan (2010)"]
]
search_item = input("search the actor... ").lower()


def actor_info(search):

    for i in actors:
        name = i[0].split(" ")
        if search in name[0].lower():
            return i[1]
        elif search in name[1].lower():
            return i[1]
        # else:
        #     return "actor not found..." #ამას თუ კომენტარს მოვუხსნი, მატრო else-ს ასრულებს და if-სა და elif-ში არ შედის. ამის გარეშე სრულდება
        # ჩემშია პრობლემა თუ python ში :დდ


print(actor_info(search_item))

# 3. შექმენი ფუნქცია რომელიც მიიღებს სიას და
# დააბრუნებს ასევე სიას, თუმცა უნიკალური
# ელემენტებით (გამოიყენე set მონაცემთა ტიპი).
#
# def unique_list():
# ...
# return ...

my_list = [1, 2, 7, 7, "G", "%", True, "%"]


def unique_list(list1):
    unique = set(list1)
    return list(unique)


print(unique_list(my_list))

# 4. შექმენი ფუნქცია რომელიც მიიღებს ორ set ტიპის
# მონაცემს, გააერთიანებს მათ, შემდეგ კი გადააქცევს
# tuple ტიპის მონაცემად და დააბრუნებს შედეგს.
# def set_to_tuple():
# ...
# return ...

def set_to_tuple():
    fruits1 = {"apple", "banana", "cherry", "kiwi"}
    fruits2 = {"pineapple", "banana", "orange", "strawberry"}
    fruits = tuple(fruits1.union(fruits2))
    return fruits


print(set_to_tuple())

# 5. შექმენი ფუნქცია, რომელიც შეამოწმებს გადაცემული
# ლექსიკონი არის თუ არა ცარიელი.

dict1 = {"key": 0}
dict2 = {}


def is_dictionary_empty(dictionary):

    if len(dictionary) == 0:
        return " dictionary Is empty"
    else:
        return " dictionary Isn't empty "


print(is_dictionary_empty(dict1))
print(is_dictionary_empty(dict2))
# 6. დაწერე პროგრამა რომელიც სტრიქონისგან ქმნის
# ლექსიკონს.
# დათვალე სტრიქონში კონკრეტული სიმბოლოს
# ოდენობა. მაგალითად პროგრამას გადავეცით
# სტრიქონი უნდა დააბრუნოს ლექსიკონი:


string = "w3schools"
dictionary = {}


def dict_by_str():
    for char in string:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1


    return dictionary


print(dict_by_str())
# 7. შექმენი while ციკლი, რომელიც მომხმარებელს ხუთჯერ
# შემოატანინებს ინფორმაციას და ჩაამატებს ცარიელ
# სიაში. შედეგი დაბეჭდე. (append მეთოდი)

my_arr = []
i = 0
while i < 5:
    info = input("enter something IDK... ")
    i += 1
    my_arr.append(info)
print("My List: ", my_arr)

# 8. მიღებული სიის პირველ და ბოლო ელემენტებს ადგილი
# შეუცვალე და დაბეჭდე შედეგი.

my_arr[0], my_arr[-1] = my_arr[-1], my_arr[0]

print("My List after swapping last and first elements: ", my_arr)

# წაშალე სიაში მომხმარებლის მიერ მოთხოვნილი
# ელემენტი. (remove მეთოდი)

remove_element = input("Enter Element of List that You want to Delete...")
my_arr.remove(remove_element)

print("My List after Remove Element...", my_arr)

# 9. იპოვე სიის სიგრძე მინიმუმ ორი მეთოდით.
arr_length = len(my_arr)
count = 0
for i in my_arr:
    count += 1
print(f"My List's length is {arr_length}")
print(f"My List's length is {count}")



# 10. ამობეჭდე სიის ყოველი ელემენტი მის ინდექსთან
# ერთად მინიმუმ ორი მეთოდით.
arr_index = 0
for i in my_arr:
    arr_index += 1
    print(f"{i} : {arr_index}")
for index, value in enumerate(my_arr):
    print(f"{value} : {index}")

# 11. შეკრიბე ორი სია და დაბეჭდე შედეგი.

list_one = [1, 2, 3, 4, 5]
list_two = [6, 7, 8, 9, 10]
merged_list = list_one + list_two
print(merged_list)

# 12. შეასრულე იგივე ოპერაცია extend მეთოდის
# დახმარებით.

list_one.extend(list_two)

# 13. გაამრავლე სია რიცხვზე და დაბეჭდე შედეგი.

list_three = ["apple", "banana", "pineapple"]
tripled = list_three * 3
print(tripled)

# 14. Slicing _ ის გამოყენებით შეაბრუნე სია და დაბეჭდე
# შედეგი.

reversed_list = list_three[::-1]

print(reversed_list)

# 15. გააკეთე იგივე reverse მეთოდის გამოყენებით.

listt = [1, 2, 3, 4, 5, 6, 8, 20, 32, 77]
listt.reverse()
print(listt)

# 16. მომხმარებელს შემოაყვანინე წინადადება და
# გადააქციე სიტყვების სიად.

sentence = input("Enter Sentence... ")
words_list = sentence.split(" ")
print(words_list)

# 17. დაწერე პროგრამა, რომელიც ცარიელ სიაში
# ჩაამატებს 10 შემთხვევითად შერჩეულ რიცხვს,
# რიცხვების დიაპაზონი შემოჰყავს მომხმარებელს.

num1 = int(input("Enter First Number... "))
num2 = int(input("Enter Second Number... "))
random_numbers = []
i = 0
while i < 10:
    random_numbers.append(random.randrange(num1, num2,))
    i += 1
print(random_numbers)


# 18. მოცემულია სია:
#
# [“apple”, “orange”, “banana”, “strawberry”]
# მომხმარებელს შეაყვანინე სიტყვა, და თუ ეს სიტყვა
# მოიძებნა მოცემულ სიაში, ამობეჭდე მისი ინდექსი.

list_items = ['apple', 'orange', 'banana', 'strawberry']
search_fruit = input("Search... ").lower()

for index, char in enumerate(list_items):
    if char == search_fruit:
        print(index)
    else:
        print("fruit not found... ")

# 19. შემთხვევითი რიცხვებით შექმენი სია, იპოვე
# მინიმალური და მაქსიმალური ელემენტი და დაბეჭდე. (min
# max ფუნქციები)

random_numbers2 = []
i = 0
while i < 10:
    random_numbers2.append(random.randrange(20, 60))
    i += 1

maximum = max(random_numbers2)
minimum = min(random_numbers2)
print(f"min = {minimum}, max = {maximum}")

# 20. წაშალე სიის ბოლო ელემენტი, ამავე დროს ამოპრინტე
# წაშლილი ელემენტი და მიღებული სია. (pop მეთოდის
# გამოყენებით)

new_list = ["bear", "camel", "dog", "fox", "giraffe"]
popd = new_list.pop()
print(f"removed element: '{popd}', rest of the list: {new_list}")
