##1-No Return & No Parameters##
def greetings():
    print("Hello, World!")

greetings()

##2-No Return & Has Parameters##
def greetings_1(name):
    print("Hello,",name+"!")

greetings_1("Devansh")

##3-Has Return & Has Parameters##
def greetings_3(name):
    return f"Hello, {name}!"

print(greetings_3("DeVaNsH"))
