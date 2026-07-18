def count_lowercase(s):
    """Calculates the number of lowercase letters in a string

    Args:
        s (str): the string to search

    Returns:
        int: the number of lowercase letters
    """
    # Implement me!
    count = 0
    for letter in s:
        if letter.lower() == letter:
            count = count + 1
    return count


def test_count_lowercase():
    # Implement me!
    assert 1 == count_lowercase("i")
    assert 0 == count_lowercase("I")
    assert 0 == count_lowercase("")
    assert 5 == count_lowercase("hello")
    assert 4 == count_lowercase("Hello")


def are_all_evens(lst):
    """Returns whether all integers in a list are even

    Args:
        lst (list[int]): the list to search

    Returns:
        bool: True if all integers in the list are even and False otherwise
    """
    # Implement me!
    even = True
    for num in lst:
        if num % 2 != 0:
            even = False
            break
    return even


def test_are_all_evens():
    # Implement me!
    assert True == are_all_evens([2, 4, 6])
    assert False == are_all_evens([1, 4, 6])
    assert True == are_all_evens([])
    assert False == are_all_evens([1, 3, 5])


def is_perfect_square(x):
    """Returns whether x is a perfect square

    For example, 4 is a perfect square, and 5 is not

    Args:
        x (int): the number we check is a perfect square

    Returns:
        bool: True if x is a perfect square and False otherwise
    """
    if x > 0:
        x = x ** .5
        if x == int(x):
            return True
        else:
            return False
    else:
        return False


def test_is_perfect_square():
    # implement me!
    assert True == is_perfect_square(4)
    assert False == is_perfect_square(5)
    assert False == is_perfect_square(-4)


def sum_negatives(lst):
    """Calculates the sum of all negative numbers in a list

    Positive numbers are ignored entirely in this calculation

    Args:
        lst (list[int]): the list to search

    Returns:
        int: the sum of all negative numbers in the list
    """
    total = 0
    for num in lst:
        if num < 0:
            total = total + num
    return total


def test_sum_negatives():
    # implement me!
    assert -10 == sum_negatives([-1, -2, -3, -4])
    assert 0 == sum_negatives([])
    assert 0 == sum_negatives([1, 2, 3, 4])
    assert -7 == sum_negatives([1, 2, -3, -4])


def is_prime(num):
    """Returns whether or not num is prime

    A prime number is any number that is only divided by 1 and itself

    For this function, negative numbers and 0 are not prime
    Additionally, 1 is considered a prime number

    Args:
        x (int): the number we check to be prime

    Returns:
        bool: True if x is a prime and False otherwise
    """
    start = 2
    answer = True

    if num <= 0:
        return False
    if num == 1:
        return True
    while start < num:
        if num % start == 0:
            return False
        start = start + 1
    return True



def test_is_prime():
    # implement me!
    assert False == is_prime(21)
    assert False == is_prime(0)
    assert False == is_prime(-5)
    assert True == is_prime(1)
    assert True == is_prime(17)


def count_vowels(lst):
    """Calculates the number of vowels in all strings in a list

    Assumes that all strings in lst must consist only of lowercase letters

    A vowel is any letter a, e, i, o, or u
    Additionally, y is considered a vowel so long as it's not the first letter of a string

    Args:
        lst (list[str]): the list to search

    Returns:
        int: the number of vowels in all strings of lst
    """
    count = 0
    if len(lst) > 0:
        for word in lst:
            for letter in word:
                letter1 = letter.lower()
                if letter1 == "a" or letter1 == "e" or letter1 == "i" or letter1 == "o" or letter1 == "u" or letter1 == "y":
                    count = count + 1
            if word[0].lower() == 'y':
                count = count - 1
    return count


def test_count_vowels():
    # implement me!
    assert 2 == count_vowels(['abc', 'efg', 'dd'])
    assert 0 == count_vowels(['fth', 'gdf', 'dpl'])
    assert 1 == count_vowels(['a'])
    assert 0 == count_vowels([])
    assert 2 == count_vowels(['Arr', 'Ell', 'Lll'])
    assert 3 == count_vowels(['Sky', 'Ool'])
    assert 0 == count_vowels(['Ykk'])


# we'll explain what this __name__ == "__main__" means in lecture
# the short of it is that it says to only run this code when we run this file directly
if __name__ == "__main__":
    # run all of our tests (one at a time)
    test_count_lowercase()
    test_are_all_evens()
    test_is_perfect_square()
    test_sum_negatives()
    test_is_prime()
    test_count_vowels()
    print('All tests passed!')
