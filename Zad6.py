def digits_to_english(number):

    digits =  ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']

    if number < 10:

        return digits[number]

    else:

        return digits_to_english(number//10) + ' ' + digits[number % 10]

number = abs(int(input("Enter number: ")))
print("The digits of number in English are: ", digits_to_english(number))