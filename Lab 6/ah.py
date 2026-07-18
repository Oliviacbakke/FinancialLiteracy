def update(lst):
    lst[0] = 77
    print(lst)

values = [5, 10, 15, 20]
update(values)
print(values)

def apply_tax(price):
    total = price * (1 + .08)
    print(total)

result = apply_tax(100)
print(result)
