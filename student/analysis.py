"""
Author: Olivia Bakke
Starting Date: Jan 15

Initial creation by Dietrich Geisler on 10/12/2025
Edits by Anastasia Kurdia on 1/14/2026

A script to analyze and report on "getting to know you" survey results
"""

# By convention, imports go at the top of our file
# We import utilities for use in our menu
import utils

# These are _constants_, which can be used to index your data
# For example, line[INDEX_YEAR] will give you the graduation year of that line of data
# In Python, any variable can be changed
# But by convention, variables named in ALL_CAPS are intended to not be modified
INDEX_FIRST = 0
INDEX_LAST = 1
INDEX_PRONOUNS = 2
INDEX_DESCRIPTION = 3
INDEX_YEAR = 4
INDEX_MAJOR = 5
INDEX_IDEAL_MAJOR = 6
INDEX_BEVERAGE = 7
INDEX_EMOJI_FAV = 8
INDEX_LIVE_WHERE = 9
INDEX_LIVE_WITH = 10
INDEX_BIRTHDAY = 11
INDEX_FOOD = 12
INDEX_FUN_THING = 13
INDEX_LAT_NORTH = 14
INDEX_LAT_SOUTH = 15
INDEX_COOL_THING = 16
INDEX_THING_TO_MAKE = 17
INDEX_STUDY_TIME = 18
INDEX_STUDY_GOOD_AT = 19
INDEX_STUDY_HELP_WITH = 20

# We also use a constant to decide which data file to open
DATA_FILE = 'cs150data-w26.csv'
# --------------------------------------------------------------------------

# Here are some already-implemented functions that might help
#   give you a sense of the pattern our code will tend to follow

def first_name(data):
    """Returns a list of the first names of all students in data

    Args:
        data (list[list[str]]): Dataset of students

    Returns:
        list[str]: the list of first names
    """
    result = []
    for student in data:
        first = student[INDEX_FIRST]
        result.append(first)
    return result

def introduction(data):
    """Returns a list of the first name and description about each student:

    Specifically, this returns a list of strings in the following format:
    "Hi, this is {first_name}!"
    "\t{description}"

    (Note that '\t' is the tab character)

    Additionally, the description has extra whitespace on either end removed (using strip)
    If a student did not provide a description, the student is skipped

    Args:
        data (list[list[str]]): Dataset of students

    Returns:
        list[str]: the list of formatted strings
    """
    result = []
    for student in data:
        line = []
        first = student[INDEX_FIRST]
        # note the use of .strip() to remove extra whitespace
        description = student[INDEX_DESCRIPTION].strip()

        # Notice the newline between first and description
        line.append(f'Hi, this is {first}!\n\t{description}')

        # only include this student if a description was given
        if description != '':
            result.append(line)

    return result

def cs_count(data):
    """Returns the integer number of students who list a cs major

    Includes any capitalization of CS, comp sci, and computer science

    Args:
        data (list[list[str]]): Dataset of students

    Returns:
        int: the (positive) number of students who list a cs major
    """
    count = 0
    for student in data:
        major = student[INDEX_MAJOR]
        # allows us to ignore capitalization
        major = major.lower()

        if ('cs' in major) or ('comp sci' in major) or ('computer science' in major):
            count += 1
    return count

# --------------------------------------------------------------------------

# TODO: Your primary task is to implement all of the following functions
# Remember to implement extra test cases first!

# Part 1

def number_of_students(data):
    """Returns the number of students in our data set

    Args:
        data (list[list[str]]): Dataset of students

    Returns:
        int: The number of students in data
    """
    # Hint: don't overthink this function

    # TODO: Implement me!
    count = 0
    for student in data:
        count = count + 1
    return count

def number_of_anonymous(data):
    """Returns the number of "anonymous" names in our data set

    Args:
        data (list[list[str]]): Dataset of students

    Returns:
        int: The number of students in data who requested to be anonymous
    """

    # Note: you can use either first or last name when calculating this
    #   both of which must be "anonymous" if a student chose to be anonymous

    # TODO: Implement me
    count = 0
    for student in data:
        name = student[INDEX_FIRST]
        if name == 'anonymous':
            count = count + 1
    return count

def number_of_ramen_recommends(data):
    """Returns the number of students who recommended a ramen restaurant in "INDEX_FOOD"

    NOTE: any mention of "ramen" in the recommendation is sufficient, even as part of another word
    NOTE: this must include any capitalization of the word ramen (such as Ramen)

    Args:
        data (list[list[str]]): Dataset of students

    Returns:
        int: The number of ramen recommendations, including lowercase recommendations
    """
    # Hint: consider using .lower() to make upper/lowercase easier to manage
    # Hint: recall that the expression 'abc' in 'def abc ghi' returns True,
    #   since abc is "in" the second string

    # TODO: Implement me!
    count = 0
    for student in data:
        sentence = student[INDEX_FOOD].lower()
        if 'ramen' in sentence:
            count = count + 1
    return count

# ------------------------------------------
# Part 2

def first_last(data):
    """Returns the first and last name of each student as a list

    Each string in this list has the format '{first_name} {last_name}'

    Args:
        data (list[list[str]]): Dataset of students

    Returns:
        list[str]: a list of the first and last names of each student
    """
    # Hint: consider trying out f-strings!

    # TODO: Implement me!
    names = []
    for student in data:
        first = student[INDEX_FIRST]
        last = student[INDEX_LAST]
        names.append(f"{first} {last}")
    return names

def tea_enjoyers(data):
    """Returns the names of all students who prefer tea

    Concretely, returns a list of strings of the form:
      "{first_name} {last_name}"
    For all students include "tea" or "chai" in their preferred beverages

    NOTE: this must include any capitalization of tea and chai

    Args:
        data (list[list[str]]): Dataset of students

    Returns:
        list[string]: a list of names of tea-enjoying students
    """
    # Hint: as with the ramen function, consider using .lower and the in expression

    # TODO: Implement me!
    list = []
    for student in data:
        drink = student[INDEX_BEVERAGE].lower()
        if 'tea' in drink or 'chai' in drink:
            first = student[INDEX_FIRST]
            last = student[INDEX_LAST]
            list.append(f"{first} {last}")
    return list

def coffee_enjoyers(data):
    """Returns the names of all students who prefer coffee

    Concretely, returns a list of strings of the form:
      "{first_name} {last_name}"
    For all students include any of the following in their preferred beverages:
      "coffee" or "espresso" or "brew" or "mocha" or "americano"

    NOTE: this must include any capitalization of these coffee variations

    Args:
        data (list[list[str]]): Dataset of students

    Returns:
        list[string]: a list of names of coffee-enjoying students
    """

    # TODO: Implement me!
    list = []
    for student in data:
        drink = student[INDEX_BEVERAGE].lower()
        if 'coffee' in drink or 'espresso' in drink or 'brew' in drink or 'mocha' in drink or 'americano' in drink:
            first = student[INDEX_FIRST]
            last = student[INDEX_LAST]
            list.append(f"{first} {last}")
    return list

def travelled_south(data):
    """Returns a list of all students who have travelled south of Key West

    Concretely, returns a list of strings of the form:
      f"{first_name} {last_name} ({student_lat}°)"
    For all students who have travelled SOUTH of the Key West  (24.555059 degrees N)
    (Based on their response to the question on southern latitude)

    Note the use of the special character ° in the output string

    Any student with an empty value for their southernmost latitude is not included

    Args:
        data (list[list[str]]): Dataset of students

    Returns:
        list[string]: a list of names of students who travelled south of Key West
    """
    # Hint: recall that you can convert (valid) strings to floats using float(string)
    # Hint: you can't convert an empty string to a float, so beware of errors!
    KEYWEST_LAT = 24.555059

    # TODO: Implement me!
    list = []
    for student in data:
        if student[INDEX_LAT_SOUTH] != "":
            if float(student[INDEX_LAT_SOUTH]) < KEYWEST_LAT:
                first = student[INDEX_FIRST]
                last = student[INDEX_LAST]
                lat = student[INDEX_LAT_SOUTH]
                list.append(f"{first} {last} ({lat}°)")
    return list

# ------------------------------------------
# Part 3

def list_majors(data):
    """Returns the full name, major, and ideal major for each student as a list

    Each string should have the format:
       "{first_name} {last_name} ({real_major}): {ideal_major}"

    Args:
        data (list[list[str]]): Dataset of students

    Returns:
        list[str]: a list of the major information of each student
    """
    # Hint: consider using f-strings to match the given formatting

    # TODO: Implement me!
    list = []
    for student in data:
        first = student[INDEX_FIRST]
        last = student[INDEX_LAST]
        major = student[INDEX_MAJOR]
        ideal_major = student[INDEX_IDEAL_MAJOR]
        list.append(f"{first} {last} ({major}): {ideal_major}")
    return list

def cool_things(data):
    """Returns some "cool information" about each student as a list

    Specifically, for each student in data, this returns a list
      where each element is a list containing three string values:
        1. the first/last name of the student
        2. the cool thing a student has seen made with code
        3. a thing the student would like to make

    These strings have the following format, respectively:
    "{first_name} {last_name}"
    "\t{cool_thing}"
    "\t{thing_to_make}"

    (Note that '\t' is the tab character)

    NOTE: This only includes "cool thing" in the list the if the student has an answer to "cool thing"
      Similarly, this only includes "thing to make" in the list the if the student has an answer to "thing to make"
    NOTE: the second two strings (i.e. "cool thing" and "thing to make") must have
      whitespace removed on either end

    Args:
        data (list[list[str]]): Dataset of students

    Returns:
        list[list[str]]: cool information about each student
    """
    # Hint: Use strip() to remove whitespace from either end of a string

    # TODO: Implement me!
    list = []
    for student in data:
        list1 = [f"{student[INDEX_FIRST]} {student[INDEX_LAST]}"]
        if student[INDEX_COOL_THING] != "":
            list1.append(f"\t{student[INDEX_COOL_THING].strip()}")
        if student[INDEX_THING_TO_MAKE] != "":
            list1.append(f"\t{student[INDEX_THING_TO_MAKE].strip()}")
        list.append(list1)
    return list

def emojis(data):
    """Returns a list of the emojis preferred for each student

    Any emoji is permitted, including plain-text emoji such as :-)

    Args:
        data (list[list[str]]): Dataset of students

    Returns:
        list[str]: A list of student's favorite emojis
    """

    # TODO: Implement me!
    list = []
    for student in data:
        if student[INDEX_EMOJI_FAV] != "":
            list.append(student[INDEX_EMOJI_FAV])
    return list

def study_partners(data):
    """Returns name and study-group information for interested students in data

    Specifically, for each student in data, this returns a list
      where each element is a list containing three string values:
        1. "{first_name} {last_name} {study_time}"
        2. "\t{good_at}"
        3. "\t{help_with}"

    Where good_at refers to the column where the student described their strengths
      and help_with refers to the column where the student described
      what they most need help with

    NOTE: If a student doesn't include study_time, good_at, *and* help_with,
      The student is not considered to be "interested" and is not added to the list
    NOTE: You _may_ remove whitespace on either end (with strip) of each string
      but are not required to do so

    Args:
        data (list[list[str]]): Dataset of students

    Returns:
        list[list[str]]: study group information for each student
    """

    # TODO: Implement me!
    list = []
    for student in data:
        if student[INDEX_STUDY_TIME] != "" and student[INDEX_STUDY_GOOD_AT] != "" and student[INDEX_STUDY_HELP_WITH] != "":
            list1 = [f"{student[INDEX_FIRST]} {student[INDEX_LAST]} {student[INDEX_STUDY_TIME]}"]
            list1.append(f"\t{student[INDEX_STUDY_GOOD_AT]}")
            list1.append(f"\t{student[INDEX_STUDY_HELP_WITH]}")
            list.append(list1)
    return list

# ------------------------------------------
# Part 4

def graduation_years(data):
    """Returns a dictionary mapping graduation years to the number of students graduating in that year

    Graduation years and number of students are both given as integers

    Args:
        data (list[list[str]]): Dataset of students

    Returns:
        dict[int, int]: Dictionary mapping graduation years to number of students
    """
    # Hint: you can use int(s) to convert a string to an integer
    #   Note that, as with floats, empty strings cannot be converted to an integer
    # Note: it's bad style (and unnecessary) to hard-code specific
    #   years for this problem (e.g. explicitly including 2026 and 2027)
    # Instead, how can you build your dictionary with each year as you encounter it?
    grad_years = {}
    for student in data:
        if student[INDEX_YEAR] != "":
            year = int(student[INDEX_YEAR])
            if year in grad_years:
                grad_years[year] = grad_years[year] + 1
            else:
                grad_years[year] = 1
    return grad_years

def birthday_buddies(data):
    """Returns a dictionary mapping birthdays to all birthday buddies on that date

    Birthday buddies are a list of students that all share a birthday
    Birthday buddies are included only if there is more than one student in the list
    Students are represented as strings in the format f'{first_name} {last_name}'

    Args:
        data (list[list[str]]): Dataset of students

    Returns:
        dict[str, list[str]]: Dictionary mapping birthdays to lists of students
    """
    # Hint: Create the dictionary up-front and add to it
    # After finding all birthday buddies, make a _second_ dictionary
    #  and only add keys/values from the first dictionary
    #  if the value list has more than one element
    # Hint: remember, you can loop over the keys of a dictionary using a for loop!
    birthdays = {}
    for student in data:
        birthday = student[INDEX_BIRTHDAY]
        if birthday != "":
            birthdays[birthday] = birthdays.get(birthday, 0) + 1
    results = {}
    for student in data:
        birthday = student[INDEX_BIRTHDAY]
        if birthday != "" and birthdays[birthday] > 1:
            if birthday not in results:
                results[birthday] = []
            results[birthday].append(f"{student[INDEX_FIRST]} {student[INDEX_LAST]}")
    return results

# ----------------------------------------------------------------------------

# Implementation of the main menu
# NOTE: You don't need to modify anything past this line

def main_menu(data):
    """Prints the main menu and requests input to select and call an option

    Args:
        data (list[list[str]]): Dataset of students

    Returns:
        None
    """
    print('Select an analysis function to apply by giving a single number:')
    print('1: first names')
    print('2: introduction')
    print('3: cs major count')
    print('4: number of students')
    print('5: number of anonymous students')
    print('6: number of ramen recommendations')
    print('7: first and last names')
    print('8: tea enjoyers')
    print('9: coffee enjoyers')
    print('0: more options')
    choice = input()
    print() # spacing

    # Make sure we got a number
    if not choice.isdigit():
        print('ERROR: Please give a number')
        return

    # Convert to a number and call an appropriate function
    choice = int(choice)
    # Note that we use '\n'.join to print out our data "nicely"
    if choice == 1:
        utils.print_lines(first_name(data))
    elif choice == 2:
        utils.print_nested_lines(introduction(data))
    elif choice == 3:
        print(f'Number of CS majors: {cs_count(data)}')
    elif choice == 4:
        print(f'Number of students: {number_of_students(data)}')
    elif choice == 5:
        print(f'Number of anonymous responses: {number_of_anonymous(data)}')
    elif choice == 6:
        print(f'Number of ramen recommendations: {number_of_ramen_recommends(data)}')
    elif choice == 7:
        utils.print_lines(first_last(data))
    elif choice == 8:
        utils.print_lines(tea_enjoyers(data))
    elif choice == 9:
        utils.print_lines(coffee_enjoyers(data))
    elif choice == 0:
        extra_options(data) # print extra options for the user
    else:
        print('ERROR: please give a number between 1 and 9')

def extra_options(data):
    """Provides additional options and requests input to select and call an option

    Args:
        data (list[list[str]]): Dataset of students

    Returns:
        None
    """
    print('More analysis options, select a single number:')
    print('1: southern travelers')
    print('2: majors')
    print('3: cool things to make')
    print('4: emojis we like')
    print('5: study groups')
    print('6: graduation years')
    print('7: birthday buddies')
    choice = input()
    print() # spacing

    # Make sure we got a number
    if not choice.isdigit():
        print('ERROR: Please give a number')
        return

    # Convert to a number and call the appropriate function
    choice = int(choice)
    if choice == 1:
        utils.print_lines(travelled_south(data))
    elif choice == 2:
        utils.print_lines(list_majors(data))
    elif choice == 3:
        utils.print_nested_lines(cool_things(data))
    elif choice == 4:
        utils.print_lines(emojis(data))
    elif choice == 5:
        utils.print_nested_lines(study_partners(data))
    elif choice == 6:
        utils.print_dictionary_pretty(graduation_years(data))
    elif choice == 7:
        utils.print_dictionary_pretty(birthday_buddies(data))
    else:
        print('ERROR: please give a number between 1 and 9')

def main():
    """Main function for this program

    Loads the data from DATA_FILE and opens a main menu for the user

    Returns:
        None
    """
    data = utils.read_data(DATA_FILE)
    main_menu(data)

if __name__ == "__main__":
    main()
