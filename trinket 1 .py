#Nick Zapata
#Exercise 1:
#Using 'while' loop
fruit=raw_input('Enter a string: ')
index = len(fruit)
while index > 0:
    letter = fruit[index-1]
    print letter
    index = index - 1