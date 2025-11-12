print(''' 
My Name is  David
I love Football
And I also love swimming''')

text = ("PYTHON")
print(text[3:6])

language = ("PYTHON")
for language in language:
   print(language)

store = ["Maggi," "Sugar," "Milk", "Chocolate"]
for store in store:
    print(store)

    fruit = "Banana"
    print(len(fruit))

    word = ("Learning Python is cool")
    print("Learning" in word)

    word = ("Learning Python and Java is cool")
if ("Java" in word):
      print("Yes")
else:
      print("No! Java is Unavailable")

message = "Coding is Fun and we love knocking it down"

count = 0

for n in message:
   if n == "n":
      count += 1

print(count)


poem = """
Roses are red,
Violets are blue,
Python is rare and 
I think it's cool"""
print(poem.upper())