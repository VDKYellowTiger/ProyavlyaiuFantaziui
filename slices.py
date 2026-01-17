#Срезы:

#lst = [k**2 for k in range(1, 11)]

#print(lst, lst[2:7:2])

string = 'А роза упала на лапу Азора'

def is_palindrome(string: str) -> bool:
    spaceless = [k.upper() for k in string if k != ' ']

    return spaceless == spaceless[::-1]

ret = is_palindrome(string)

print(ret)
