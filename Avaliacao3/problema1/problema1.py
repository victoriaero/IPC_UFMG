# problema 1

def fizz_buzz(numero):
    if (numero % 3 == 0) and (numero % 5 == 0):
        return "FizzBuzz"
    elif numero % 3 == 0:
        return "Fizz"
    elif numero % 5 == 0:
        return "Buzz"
    else:
        return numero