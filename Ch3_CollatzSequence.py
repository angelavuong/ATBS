def collatz(number):
    if (number%2==0): #even
        new_number = number // 2
        print (new_number)
        return new_number
    else:
        new_number = 3 * number + 1
        print (new_number)
        return new_number

value = 0
while (value != 1):
    print ("Enter number: ")
    user_input = int(input())
    value = collatz(user_input)
