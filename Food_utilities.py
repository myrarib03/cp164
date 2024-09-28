"""
-------------------------------------------------------
Food class utility functions.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2024-01-19"
-------------------------------------------------------
"""
from Food import Food


def get_food():
    """
    -------------------------------------------------------
    Creates a Food object by requesting data from a user.
    Use: source = get_food()
    -------------------------------------------------------
    Returns:
        food - a completed food object (Food).
    -------------------------------------------------------
    """

    # Your code here
    name = input("Name:")
    origin = int(input(f"{Food.origins()}:"))
    vegetarian = input("Vegetarian (Y/N):")
    if vegetarian == 'Y':
        is_vegetarian = True
    else:
        is_vegetarian = False
    calories = int(input("Calories:"))
    food = Food(name, origin, is_vegetarian, calories)
    return food


def read_food(line):
    """
    -------------------------------------------------------
    Creates and returns a Food object from a line of string data.
    Use: source = read_food(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of food data in the format
          name|origin|is_vegetarian|calories (str)
    Returns:
        food - contains the data from line (Food)
    -------------------------------------------------------
    """
    variables = line.strip().split('|')
    name = variables[0]
    origin = int(variables[1])
    if variables[2] == "True":
        is_vegetarian = True
    elif variables[2] == "False":
        is_vegetarian = False
    calories = int(variables[3])
    # Your code here
    food = Food(name, origin, is_vegetarian, calories)
    return food


def read_foods(file_variable):
    """
    -------------------------------------------------------
    Reads a file of food strings into a list of Food objects.
    Use: foods = read_foods(file_variable)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
    Returns:
        foods - a list of food objects (list of Food)
    -------------------------------------------------------
    """
    foods = []

    # Your code here
    for line in file_variable:
        variables = line.split('|')
        name = variables[0]
        origin = int(variables[1])
        if variables[2] == "True":
            is_vegetarian = True
        elif variables[2] == "False":
            is_vegetarian = False
        calories = int(variables[3])
        food = Food(name, origin, is_vegetarian, calories)
        foods.append(food)
    return foods


def write_foods(file_variable, foods):
    """
    -------------------------------------------------------
    Writes a list of Food objects to a file.
    file_variable contains the objects in foods as strings in the format
          name|origin|is_vegetarian|calories
    foods is unchanged.
    Use: write_foods(file_variable, foods)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file variable)
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """
    for food in foods:
        file_variable.write(
            f"{food.name}|{food.origin}|{food.is_vegetarian}|{food.calories}\n")
    return None


def get_vegetarian(foods):
    """
    -------------------------------------------------------
    Creates a list of vegetarian Food objects.
    foods is unchanged.
    Use: v_foods = get_vegetarian(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        veggies - Food objects from foods that are vegetarian (list of Food)
    -------------------------------------------------------
    """
    veggies = []

    # Your code here
    for food in foods:
        if food.is_vegetarian == True:
            veggies.append(food)
    return veggies


def by_origin(foods, origin):
    """
    -------------------------------------------------------
    Creates a list of Food objects by origin.
    foods is unchanged.
    Use: o_foods = by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - a food origin (int)
    Returns:
        origins - Food objects from foods that are of a particular origin (list of Food)
    -------------------------------------------------------
    """
    # takes origin and creates a sorted list of food objects that only have that origin
    assert origin in range(len(Food.ORIGIN))
    origins = []
    for food in foods:
        if food.origin == origin:
            origins.append(food)
    return origins


def average_calories(foods):
    """
    -------------------------------------------------------
    Determines the average calories in a list of Foods objects.
    foods is unchanged.
    Use: avg = average_calories(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        avg - average calories in all Food objects of foods (int)
    -------------------------------------------------------
    """
    calories = 0
    count = 0
    for element in foods:
        calories += element.calories
        count += 1
    avg = calories / count
    # Your code here

    return avg


def calories_by_origin(foods, origin):
    """
    -------------------------------------------------------
    Determines the average calories in a list of Foods objects.
    foods is unchanged.
    Use: by_origin = calories_by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the Food objects to find (int)
    Returns:
        avg - average calories for all Foods of the requested origin (int)
    -------------------------------------------------------
    """
    # average calories in a list of foods with a specified origin
    assert origin in range(len(Food.ORIGIN))
    origins = []
    for food in foods:
        if food.origin == origin:
            origins.append(food)
    calories = 0
    count = 0
    for element in origins:
        calories += element.calories
        count += 1
    avg = calories / count
    return avg


def food_table(foods):
    """
    -------------------------------------------------------
    Prints a formatted table of Food objects, sorted by name.
    foods is unchanged.
    Use: food_table(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """
    print("""Food                                Origin       Vegetarian Calories
----------------------------------- ------------ ---------- --------""")
    for i in foods:
        if i.is_vegetarian == 0:
            vegetarian = "False"
        else:
            vegetarian = "True"
        print(
            f"{i.name:<36}{Food.ORIGIN[i.origin]:<18}{vegetarian:<11}{i.calories:<8}")
    return None


def food_search(foods, origin, max_cals, is_veg):
    """
    -------------------------------------------------------
    Searches for Food objects that fit certain conditions.
    foods is unchanged.
    Use: results = food_search(foods, origin, max_cals, is_veg)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the food; if -1, accept any origin (int)
        max_cals - the maximum calories for the food; if 0, accept any calories value (int)
        is_veg - whether the food is vegetarian or not; if False accept any food (boolean)
    Returns:
        result - a list of foods that fit the conditions (list of Food)
            foods parameter must be unchanged
    -------------------------------------------------------
    """
    assert origin in range(-1, len(Food.ORIGIN))
    result = []
    for food in foods:
        if food.origin == origin:
            if food.is_vegetarian == is_veg:
                if food.calories <= max_cals:
                    result.append(food)
    return result
