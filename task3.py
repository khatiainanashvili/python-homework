# 1. შექმენი ფუნქცია, რომელიც მომხმარებლისგან მიღებულ ინფორმაციას გაასამმაგებს
# და დაბეჭდავს შემდეგნაირად:
# input: “word”
# Output: „Tripled: wordwordword“

def tripled(word):
    output = f"Tripled: {word * 3}"
    print(output)
    return output

tripled(input("ente the word... "))


# 2. შექმენი ფუნქცია, რომელიც მიიღებს მომხმარებლის წონას და დააბრუნებს მის წონას
# მთვარეზე. (მთვარის გრავიტაცია 6_ჯერ ნაკლებია დედამიწისაზე)

def weight(your_weight):
    moon_weight = round(your_weight / 6 , 2)
    print(f"your weight on the moon will be... {moon_weight}")
    return moon_weight

weight(int(input("enter your weight")))

# 3. შექმენი კალკულატორის ფუნქცია, რომელიც მიიღებს გამოსახულებას
# მომხმარებლისგან input() ფუნქციის დახმარებით (სამ მონაცემს _ პირველ რიცხვს,
# მოქმედებას (+ - * / ^), მეორე რიცხვს)
# მაგ. „2 * 6“ დათვლის და დააბრუნებს შედეგს. გაითვალისწინე რომ რიცხვის შეყვანის
# მაგიერ სიმბოლოების შეყვანის შემთხვევაში უნდა დააბრუნოს ფუნქციამ შესაბამისი 
# მესიჯი. ასევე ნულზე გაყოფა არ შეიძ₾ება, ამ შემთხვევაშიც უნდა დააბრუნოს
# შესაბამისი მესიჯი. (დააბრუნოს და არა დაპრინტოს)

num1 = int(input("enter first number... "))
num2 = int(input("enter 2nd number... "))
operation = input("enter operation..")

 
def calculator(number1, number2):
        if type(num1) == int or type(num1) == int:
            if operation == "+":
                print(number1 + number2)
                return number1 + number2
            elif operation == "-":
                print(number1 - number2)
                return number1 - number2
            elif operation == "*":
                print(number1 * number2)
                return number1 * number2
            elif operation == "/":
                if num2 == 0:
                    return "you can not divide by 0"
                else:
                    print(number1 / number2)
                    return number1 / number2
            elif operation == "^":
                print(number1 ** number2)
                return number1 ** number2
        else:
            print("For the operation to be done, you must enter the Number...") 
            return ("For the operation to be done, you must enter the Number...")
calculator(num1, num2)
