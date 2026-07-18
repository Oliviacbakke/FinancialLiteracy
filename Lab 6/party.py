def vowels(word):
    if len(word) == 0:
        return 0

    if word[0] in "aeiou":
        return 1 + vowels(word[1:])
    else:
        return vowels(word[1:])


print(vowels('hello'))

def myRange(low, hi, lst):
    if low == hi:
        return lst
    else:
        lst.append(low)
        low = low + 1
        return myRange(low, hi, lst)

print(myRange(2, 7, []))

def myMax(lst, max):
    if len(lst) == 0:
        return max
    else:
        if max < lst[0]:
            max = lst[0]
        return myMax(lst[1:], max)

print(myMax([1, 34, 6, 23], 0))

def mySum(lst):
        if len(lst) == 0:
            return max
        else:
            return (lst)


{key: value for key, value in variable}ef mySum(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + mySum(lst[1:])
