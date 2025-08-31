def cel_far(C):
    F = (9/5 * C) + 32
    return F 

def far_cel(F):
    C = (F - 32) * 5/9
    return C

wtd = ()
print('!!Welcome to Temperature Converter!!')
while wtd != 3:
    print("Enter 1 for converting Celcius° to Fahrenheit°")
    print("Enter 2 for converting Fahrenheit° to Celcius°")
    print("Enter 3 for Quit Program")
    wtd = int(input("Enter 1, 2 or 3 here: "))
    if wtd == 1:
        C = float(input("Enter the Celcius° to convert here: "))
        print(f"{C}°C = {cel_far(C)}°F")
    elif wtd == 2:
        F = float(input("Enter the Fahrenheit° to convert here: "))
        print(f"{F}°F = {far_cel(F)}°C")
    else:
        print("Thank You for Using")
        print("Made by #trooperdroid01@penguin")
        break