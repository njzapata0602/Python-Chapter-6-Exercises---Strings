#Nick Zapata
#Exercise 3:
def count(string, letter):
    x = 0
    for i in string:
        if i == letter:
            x += 1
    print "The letter "+letter+" appears " +str(x)+" times in the string: "+string
    
count("This is a test", "t")
