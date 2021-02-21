from fizz_buzz import get_reply
max = 100
count = 5
while count < max:
        number = int(input("please give me a number: "))
        result = get_reply(number)
        print("number is: " + result + ".")
        if number > max:
            print ("it's too much")
            break