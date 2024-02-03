# Python program to check if two lists have at-least one element common using set and property.

def check_element(a,b):
    set_a=set(a)
    set_b=set(b)
    if (set_a and set_b):
        return True
    else:
        return False

a=[1,2,3,4,5,6]
b=[5,6,7,8,9,0]
print(check_element(a,b))


#using built-in method

x={"a","d","e","t"}
y={1,2,3,4,5,6,7,8,"t","q"}
x.intersection_update(y)
print(x)


