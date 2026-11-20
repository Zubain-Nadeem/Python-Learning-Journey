# fahrenheit to celsius formula
# c = 5 * (f - 32) / 9

# celsius to fahrenheit formula
# f = (c * 1.8) + 32 


def f_to_c(f):
    return 5 * (f - 32) / 9

f = int(input("Enter a number : "))
c_round = round(f_to_c(f) , 2)

print(f'{c_round} °C')



# def c_to_f(c):
#     return (c * 1.8) + 32

# c = int(input("Enter a number : "))
# f_round = round(c_to_f(c))

# print(f'{f_round} °F')

