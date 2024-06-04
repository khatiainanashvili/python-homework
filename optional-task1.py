# 1. ონლაინ მაღაზია
# პროგრამა გთავაზობს პროდუქტის სამ კატეგორიას.
# მაგ.
# 1. ლეპტოპები
# 2. პერსონალური კომპიუტერები
# 3. მობილურები
# მომხმარებელი ირჩევს ერთ-ერთს.
# პროგრამა ითხოვს მაქსიმალურ ბიუჯეტს და ბიუჯეტის მიხედვით სთავაზობს
# მომხმარებელს კონკრეტულ მოდელს არჩეულ კატეგორიაში.
# (თითო კატეგორიაში მინიმუმ 3 პროდუქტი მაინც უნდა იყოს)
# თუ ბიუჯეტი ძალიან მცირეა, პროგრამა ბეჭდავს, რომ ამ თანხაში არ გააჩნია
# შემოთავაზება.

choseCategory= input("Choose Category:\nLaptops\nPCs\nMobile Phones ").lower()
if choseCategory: 
    budget = int(input("Enter your max budget..."))
    if choseCategory == "laptops":
        laptops = input("Choose product:\nHP\nAcer\nLenovo ").lower()

        if laptops =="hp":
            if budget >= 6000:
                print("HP Spectre\nprice: 5999.00")
                print("HP Notebook Pavilion 15\nprice: 2299.99")
                print("HP Notebook (250G10/8D450ES)\nprice: 1349.99 ")
                print("HP Notebook 15s\nprice: 899.99  ")
            elif budget >= 2300 and budget <= 6000:
                print("HP Notebook Pavilion 15\nprice: 2299.99")
                print("HP Notebook (250G10/8D450ES)\nprice: 1349.99 ")
            elif budget >= 1350 and budget <= 2300:
                print("HP Notebook (250G10/8D450ES)\nprice: 1349.99 ")
                print("HP Notebook 15s\nprice: 899.99  ")
            elif budget >= 900 and budget < 1350:
                print("HP Notebook 15s\nprice: 899.99  ")
            else:
                print("No Item Found")     
        if laptops == "acer":
            if budget >= 6700:
                print("Acer Nitro 5 R9-7940HS\nprice:6699.99")
                print("Acer Swift 5 Touch - SF514\nprice: 2499.99 ")
                print("Acer Aspire 5 Laptop\nprice: 1499.00")
            elif budget >= 2499 and budget <= 6700:
                print("Acer Swift 5 Touch - SF514\nprice: 2499.99 ")
                print("Acer Aspire 5 Laptop\nprice: 1499.00")
            elif budget >= 1499 and budget <= 2499:
                print("Acer Aspire 5 Laptop\nprice: 1499.00")
            else:
                print("No Item Found")  
        if laptops == "lenovo":
            if budget >= 6700:
                print("Lenovo \nprice:6699.99")
                print("Lenovo\nprice: 2499.99 ")
                print("Lenovo\nprice: 1499.00")
            elif budget >= 2499 and budget < 6700:
                print("Lenovo\nprice: 2499.99 ")
                print("Lenovo\nprice: 1499.00")
            elif budget >= 1499 and budget < 2499:
                print("Lenovo\nprice: 1499.00")
            else:
                print("No Item Found") 
             
    if choseCategory == "pcs":
        pcs = input("Choose product:\nDELL\nHP\nLenovo ").lower()
        if pcs == "hp":
             if budget >= 6000:
                 print("HP\nprice: 5999.00")
                 print("HP\nprice: 2299.99")
                 print("HP\nprice: 1349.99 ")
             elif budget > 2300 and budget < 6000:
                 print("HP\nprice: 2299.99")
                 print("HP\nprice: 1349.99 ")
             elif budget > 1350 and budget < 2300:
                 print("HP\nprice: 1349.99 ")
                 print("HP\nprice: 899.99  ")
             elif budget > 900 and budget < 1350:
                 print("HP\nprice: 899.99  ")
             else:
                 print("No Item Found")     
        if pcs == "dell":
             if budget >= 6700:
                 print("DELL\nprice:6699.99")
                 print("DELL\nprice: 2499.99 ")
                 print("DELL\nprice: 1499.00")
             elif budget > 2499 and budget <= 6700:
                 print("DELL\nprice: 2499.99 ")
                 print("DELL\nprice: 1499.00")
             elif budget >= 1499 and budget <= 2499:
                 print("DELL\nprice: 1499.00")
             else:
                 print("No Item Found")   
        if pcs == "lenovo":
             if budget >= 6700:
                 print("Lenovo \nprice:6699.99")
                 print("Lenovo\nprice: 2499.99 ")
                 print("Lenovo\nprice: 1499.00")
             elif budget >= 2499 and budget <= 6700:
                 print("Lenovo\nprice: 2499.99 ")
                 print("Lenovo\nprice: 1499.00")
             elif budget >= 1499 and budget <= 2499:
                 print("Lenovo\nprice: 1499.00")
             else:
                 print("No Item Found") 
     
    if choseCategory == "mobile phones":
        mobile = input("Choose product:\nApple\nSamsung\nXiaomi ").lower()
        if mobile == "apple":
             if budget >= 6000:
                 print("iPhone\nprice: 5999.00")
                 print("iPhone\nprice: 2299.99")
                 print("iPhone\nprice: 1349.99 ")
             elif budget >= 2300 and budget <= 6000:
                 print("iPone\nprice: 2299.99")
                 print("iPhone\nprice: 1349.99 ")
             elif budget >= 1350 and budget <= 2300:
                 print("iPhone\nprice: 1349.99 ")
             else:
                 print("No Item Found")     
        if mobile == "samsung":
             if budget >= 6700:
                 print("Samsung\nprice:6699.99")
                 print("Samsung\nprice: 2499.99 ")
                 print("Samsung\nprice: 1499.00")
             elif budget >= 2499 and budget <= 6700:
                 print("Samsung\nprice: 2499.99 ")
                 print("Samsung\nprice: 1499.00")
             elif budget >= 1499 and budget <= 2499:
                print("Samsung\nprice: 1499.00")
             else:
                 print("No Item Found")   
        if mobile == "xiaomi":
             if budget >= 6700:
                 print("Xiaomi \nprice:6699.99")
                 print("Xiaomi\nprice: 2499.99 ")
                 print("Xiaomi\nprice: 1499.00")
             elif budget >= 2499 and budget <= 6700:
                 print("Xiaomi\nprice: 2499.99 ")
                 print("Xiaomi\nprice: 1499.00")
             elif budget >= 1499 and budget <= 2499:
                 print("Xiaomi\nprice: 1499.00")
             else:
                 print("No Item Found") 
     
# 2. ქუესთის შედგენა (Text Based Adventure Game)
# დაწერე ერთმანეთში ჩასმული if-else კონსტრუქციების

# გამოყენებით მარტივი ტექსტზე დაფუძნებული სათავგადასავლო თამაში.
# მაგ. თავიდან პროგრამა ბეჭდავს მომხმარებლის ადგილსამყოფელს და სთავაზობს
# მქომედების რამდენიმე ვარიანტს. სხვადასხვა არჩევანის შემთხვევაში თამაშ
# სხვადასხვანაირად ვითარდება.


character = input("Choose Character (Thieve) or (Magician)").lower()

if character == "thieve":
    start = input("You are in the middle of the forest. You have to go (straight), or (right)... ").lower()
    if start == "straight":
        step1 = input("You see the dragon's Cave. You have to go (inside) or (keep going)").lower()
        if step1 == "inside":
            step2 = int(input("The dragon is not here. You have to take as much gold as you can.\nEnter the amount of gold you want to take... "))
            if step2 >=20:
                step3 = input("The dragon is back, you have to (fight) or try(escape) ").lower()
                if step3 == "escape":
                    print("The dragon let out a burst of fire... You die.")
                else:
                    print("You are brave! You win!")
            if step2 < 20:
                step3 = input("There is not enough gold... Go (home) and come again, or (stay) and take more gold.").lower()
                if step3 == "home":
                    print("Come back tomorow")
                else: 
                    step4 = input("The dragon is back, you have to (fight) or try(escape) ").lower()
                    if step3 == "escape":
                       print("The dragon let out a burst of fire...\nYou die...")
                    else:
                        print("You are brave!\nYou win!")
        else:
            print("Where are you going,\nloser?!")
    else:
        step1 = input("You see the troll's Lair. You have go (inside) or (keep going)").lower()
        if step1 == "inside":
            step2 = input("The troll is  here. you have to (fight) or try(escape)").lower()
            if step2 == "escape":
                step3 = input("You havn't enough gold... Go (home) and come again, or (fight) and take more gold.").lower()
                if step3 == "home":
                    print("Come back Again...")
                else: print("You are brave!\nYou win!")
            if step2 == "fight":
                print("You are brave!\nYou win!")
        else:
            print("Where are you going,\nloser?!")

if character == "magician":
    print("You are in your treehouse, alone, and sometimes you pretend to be killing Disney's princesses.")

# 3. კარიერის შემრჩევი (არასავალდებულო დავალება)
# პროგრამა უსვამს მომხმარებელს რამდენიმე კითხვას
# (თქვენი იმპროვიზაციით) და ურჩევს მისთვის შესაფერის
# პროფესიას.

question1 = input("Which one is your favorite subject in school? (Math/Art)").lower()

if question1 == "art":  
    question3 = input("DO you like make the art? (Yes/NO)").lower()  

    if question3 == "yes":
        question5 = input("Do you like to make digital art? (Yes/NO)").lower()
        if question5 == "yes":
            print("You Will be a great digital artist")
        else:
            question4 = input("Do you like traditional media art? (Yse/NO)").lower()
            if question4 == "yes":
                question6 = input("Do you like to drow clothes? (Yes/NO)").lower()
                if question6 == "yes":
                    print("you will be a great fashion designer")
                else:
                    print("you will be a great painter") 
            else:
                  print("you will be a graet painter")
    else:
        question2 = input("Do you like the theory of art? (Yes/NO)").lower()
        if question2 == "yes":
            print("You Will be a great art historian")
        else:
            print("You Will be a great art critic")

if question1 == "math":
    question2 = input("Do you like to solve problems? (Yes/NO)").lower()
    if question2 == "yes":
        question3 = input("Are you interested in computer science? (Yes/NO)").lower()
        if question3 == "yes":
            print("You will be a great Rocket Scientist")
        else:
            question5= input("Are you interested in machine learning? (Yes/NO)").lower()
            if question5 == "yes":
                print("You will a be great Data Scientist")
            else: 
                print("Try web development.")
    else:
        question4= input("Are you interested in social science? (Yes/NO)").lower()
        if question4 == "yes":
             print("You will be a great Economist")
        else:
            print("You can become a math teacher.")