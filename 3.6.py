def reverse(s):
    str=""
    for i in s:
        str=i+str
    return str
s=input('enter a string')
print(reverse(s))
