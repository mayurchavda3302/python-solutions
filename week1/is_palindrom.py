

def is_palindrom(mystr)->bool:
     
    new_str=""
    for i in mystr:
        # print("i",i)
        new_str+= i
    print("new_str",new_str)
    if new_str == mystr:
        return True
    False

def is_palindrom_bulit_function(mystr)-> bool: 

    new_str=''.join(reversed(mystr))
    print("new_str",new_str)
    if new_str == mystr:
        return True
    False

newstr="nayan"

print(is_palindrom(newstr))
print(is_palindrom_bulit_function(newstr))