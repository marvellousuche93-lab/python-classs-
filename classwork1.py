# name_class = "Hello promise"

# print(name_class)
# name ='promise'
# age ='29'
# print(f"my name is {name} and am {age} years old")

# name = 'bright', 'innocent', 'success', 'dozie'
# a, b, c, d = name

# print(a)
# print(b)
# print(c)

# name = "promise"
# age = 29
# print(f"my name is promise\nI'm 29 years old!\nAm a software developer")

# x ='promise '
# y = 'is a good girl '
# z = 'always'

# print(x + y+ z)

x ='promise'


def people():
    print("my name is " + x)

people()

def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x)

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello, World!"
print(len(a))


a = "Hello, World!"
print(a[1])

# for x in "apple":
#     print(x)

# for x in "banana":
#   print(x)

# txt = "The best things in life are free!"
# print("free" in txt)

# txt = "The best things in life are free!"
# print("fortune" in txt)

# txt = "The best things in life are free!"
# if "free" in txt:
#     print("Yes, 'free' is present. " )

# txt = "The best in life are free"
# if "expensive" not in txt:
#    print("expensive not in txt")

# b = "Hello, World!"
# print(b[3:8])

# name = "  Hello World"
# print(name[6:])
# print(name.strip())
# print(name.replace("H", "J"))

# name = 'Marvellous'
# career =  'Web developer '
# nationality = 'Nigeria'
# Bio = name + career + nationality
# print(Bio)

# price = 30
# print(f"I need {price: .4f} dollar")

# price = f"I need {40 * 4} dollar"
# print(price)

# txt = "We are the so-called \"Vikings\" from the north."
# print(txt)




txt = "hello World "
result = txt.capitalize()
print(result)



txt = "Hello World"
result = txt.casefold()
print(result)


txt = "Hello World"
result = txt.center(109)
print(result)

a = "Python"
b = "PYTHON"
print(a.casefold() ==b.casefold())

txt = "Python"
print(txt.center(10))

txt = "Python is fun, and Python is"
print(txt.count("Python"))

txt = "Python"
encoded_txt = txt.encode()
print(encoded_txt)

txt = "I love 🦆 Python"
encoded = txt.encode("utf-8")
print(encoded)

txt = "hello world"
print(txt.endswith("world"))

txt = "Python\tis\tfun"
print(txt.expandtabs())


txt = "Python is fun"
print(txt.find("fun"))

txt = "My name is {} and I am {} years old "
print(txt.format("Marvellous", 20))

txt = "I love {0} and {1}. {0} is awsome"
print(txt.format("Python", "Javascript"))

person = {"name": "Marvellous",  "age":20 }
txt = "My name is {name} and I am {age} "
print(txt.format_map(person))

txt = "Python is fun"
print(txt.index("fun"))

txt= "Hello world"
print(txt.isalnum())

txt = "Python3"
print(txt.isalnum())

txt = "Hello world"
print(txt.isalpha())

txt = "Python3"
print(txt.isalpha())

