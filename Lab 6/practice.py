def running_total(nums):
    total = 0
    lst = []
    for num in nums:
        total += num
        lst.append(total)
    return lst

print(running_total([2, 4, 1, 3]))

def removedups(nums):
    running = []
    for num in nums:
        if num in running:
            nums.remove(num)
            continue
        else:
            running.append(num)
    return nums

print(removedups([1, 2, 1, 3, 2]))

try:
    x = int("hello")
    print(x)
except:
    print("Nope")

def safeDivide(x, y):
    try:
        z = x / y
        print(z)
    except:
        print("Invalid")

safeDivide(3, 0)

file = open("numbers.txt", "r")
lines = file.readlines()
total = 0
for line in lines:
    total += int(line)

print(total)
file.close()

file = open("score.txt", "w")
scores = [90, 85, 100]
for score in scores:
    file.write(str(score) + "\n")
file.close()

def counter(word):
    if word == '':
        return 0
    else:
        return 1 + counter(word[1:])

print(counter("hello"))

def countletword(word, letter):
    if word == '':
        return 0
    else:
        if word[0] == letter:
            return 1 + countletword(word[1:], letter)
        else:
            return countletword(word[1:], letter)

print(countletword("hello", 'l'))

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def __str__(self):
        return f"Rectangle: width={self.width}, height={self.height}"


class Square(Rectangle):
    def __init__(self, width, height):
        super().__init__(width, height)

square = Square(3, 5)
print(square.area())

class Animal:
    def __init__(self, sound, name):
        self.sound = sound
        self.name = name
    def speak(self):
        return self.sound

class Dog(Animal):
    def __init__(self, sound, name, age):
        super().__init__(sound, name)
        self.age = age
    def speak(self):
        return "woof"


dog = Dog("ruff", "dave", 4)
print(dog.speak())
print(dog.age)

nums = [1, 2, 3, 4]
print([x*2 for x in nums])
print(list(filter(lambda x: x % 2 == 0, nums)))
print(['even' for x in nums if x % 2 == 0])
print(['even' if x % 2 == 0 else "odd" for x in nums])

x = 4
def f():
    y = x + 1
    print(y)

f()
