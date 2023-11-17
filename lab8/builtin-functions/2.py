#Write a Python program with builtin function that accepts a string and calculate the number of 
# upper case letters and lower case letters

def string_test(s):
    d={"upper_case":0, "lower_case":0}
    for c in s:
        if c.isupper():
           d["upper_case"]+=1
        elif c.islower():
           d["lower_case"]+=1
        else:
           pass
    print ("Original String: ", s)
    print ("number of upper case letters : ", d["upper_case"])
    print ("number of lower case letters : ", d["lower_case"])

string_test('Salem Alem')