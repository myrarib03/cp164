"""
-------------------------------------------------------
[Functions]
-------------------------------------------------------
Author:  Myra Ribeiro
ID:      169030590
Email:   ribe0590@mylaurier.ca
__updated__ = "2024-07-17"
-------------------------------------------------------
"""
# Imports
from enum import Enum
from Stack_array import Stack
# Constants


def stack_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks.
    When finished source stack is empty. Values are
    pushed alternately onto the returned target stacks.
    Use: target1, target2 = stack_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - the stack to split into two parts (Stack)
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    TEST:
    s = Stack()
    s.push(5)
    s.push(7)
    s.push(8)
    s.push(9)
    s.push(12)
    s.push(14)
    s.push(8)

    for i in s:
        print("s:", i)

    print()

    target1, target2 = stack_split_alt(s)

    for i in target1:
        print("target1:", i)
    print()
    for i in target2:
        print("target2:", i)
    """
    turn = True
    target1 = Stack()
    target2 = Stack()
    # target1 takes first value. target 2 takes the second value.
    # splits until it is empty. once it is empty we ignore.
    # should it be one value target 1 takes it and target 2 is done
    # should it be two values target 2 takes the last and then we are done.

    while not source.is_empty():
        if turn:
            target1.push(source.pop())
        else:
            target2.push(source.pop())
        turn = not turn

    return target1, target2


def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    new_list = []
    while not source.is_empty():
        new_list.append(source.pop())
    new_list = new_list[::-1]
    while len(new_list) != 0:
        source.push(new_list.pop())
    return


# Constants
OPERATORS = "+-*/"


def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    for i in string:
        if i.isdigit():
            store_numbers.push(int(i))
        else:
            if i in ["+", "-", "*", "/"]:
                num2 = store_numbers.pop()
                num1 = store_numbers.pop()
                if i == "+":
                    store_numbers.push((num1 + num2))
                if i == "-":
                    store_numbers.push((num1 - num2))
                if i == "*":
                    store_numbers.push((num1*num2))
                if i == "/":
                    store_numbers.push((num1/num2)
    """
    # Algorithm:
    # if element is number, push onto the stack
    # if element is operator, pop the numbers for the operator from the stack
    # evaluate the operator with the top number on the right of the operator, and the
    # next number on the left of the operator
    # then push the result back onto the stack
    # once done, the number on top will be the final answer and should be the last one in the stack.
    store_numbers = Stack()
    count = 0
    digits = 1
    string = string.split(" ")

    while count < len(string):  # while our indexes are less than the length of our strings
        if string[count].isdigit():  # if our string elements are digits
            # our number equals the first string element
            number = string[count]
            store_numbers.push(int(number))
        else:
            if string[count] in ["+", "-", "*", "/"]:
                num2 = store_numbers.pop()
                num1 = store_numbers.pop()
                if string[count] == "+":
                    store_numbers.push((num1 + num2))
                if string[count] == "-":
                    store_numbers.push((num1 - num2))
                if string[count] == "*":
                    store_numbers.push((num1*num2))
                if string[count] == "/":
                    store_numbers.push((num1/num2))
        count += 1

    value = store_numbers.peek()
    return float(value)


def reroute(opstring, values_in):
    """
    -------------------------------------------------------
    Reroutes values in a list according to a operating string and
    returns a new list of values. values_in is unchanged.
    In opstring, 'S' means push onto stack,
    'X' means pop from stack into values_out.
    Use: values_out = reroute(opstring, values_in)
    -------------------------------------------------------
    Parameters:
        opstring - String containing only 'S' and 'X's (str)
        values_in - A valid list (list of ?)
    Returns:
        values_out - if opstring is valid then values_out contains a
            reordered version of values_in, otherwise returns
            None (list of ?)
    -------------------------------------------------------
            for i in opstring:
            if i == "S":
                s.push(values_in.pop(0))
            else:
                values_out.append(s.pop())
    """
    # first check if opstring is valid.
    # if valid, follow sequence and rewrite values
    # given - values_in, values_in length, etc and the sequence that is to be expected.
    # SXXSSXXS not valid -  because there is more x's proceeding the s's.

    valid = True
    count = 0
    x_count = 0
    s_count = 0

    while valid is True and count < len(opstring):
        if opstring[count] in ['S', 'X']:
            if opstring[count] == 'S':
                s_count += 1
            else:
                x_count += 1
        else:
            valid = False

        if x_count > s_count:
            valid = False

        count += 1

    if s_count != x_count:
        valid = False

    if len(opstring) == 0:
        valid = False

    if len(values_in) == 0:
        valid = False

    if not valid:
        values_out = None
    else:
        s = Stack()
        values_out = []
        count = 0
        while count < len(opstring):
            if opstring[count] == "S":
                s.push(values_in.pop(0))
            else:
                values_out.append(s.pop())
            count += 1
    return values_out


# Imports

# Enumerated constant
MIRRORED = Enum('MIRRORED',
                {'IS_MIRRORED': "is a mirror", 'TOO_MANY_LEFT': "too many characters in L",
                 'TOO_MANY_RIGHT': "too many characters in R", 'MISMATCHED': "L and R don't match",
                 'INVALID_CHAR': "invalid character", 'NOT_MIRRORED': "no mirror character"})


def is_mirror_stack(string, valid_chars, m):
    """
    -------------------------------------------------------
    Determines if string is a mirror of characters in valid_chars around the pivot m.
    A mirror is of the form LmR, where L is the reverse of R, and L and R
    contain only characters in valid_chars.
    Use: mirror = is_mirror_stack(string, valid_chars, m)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
        valid_chars - a string of valid characters (str)
        m - the mirror pivot string (str - one character not in valid_chars)
    Returns:
        mirror - the state of the string (Enum MIRRORED)
    -------------------------------------------------------
    """
    assert m not in valid_chars, \
        f"cannot use '{m}' as the mirror character"
    mirrored = True
    stack = Stack()
    length = len(string)
    index = 0
    mirror = MIRRORED.IS_MIRRORED
    if m in valid_chars or len(m) == 0 or len(string) == 0 or m not in string:
        mirror = MIRRORED.NOT_MIRRORED
        mirrored = False
    while mirrored is True and index < length and string[index] != m:
        if string[index] not in valid_chars:
            mirrored = False
            mirror = MIRRORED.INVALID_CHAR
        stack.push(string[index])
        index += 1
    if string[index] == m and len(string) == 1:
        mirrored = False
        mirror = MIRRORED.INVALID_CHAR
    index += 1
    while mirrored and index < length and not stack.is_empty():
        value = stack.pop()
        if string[index] not in valid_chars:
            mirrored = False
            mirror = MIRRORED.INVALID_CHAR
        if value != string[index]:
            mirrored = False
            mirror = MIRRORED.MISMATCHED
        else:
            index += 1
    if mirrored is True:
        if stack.is_empty() is False:
            mirror = MIRRORED.TOO_MANY_LEFT
            mirrored = False
        elif index != length:
            mirror = MIRRORED.TOO_MANY_RIGHT
            mirrored = False
    return mirror
