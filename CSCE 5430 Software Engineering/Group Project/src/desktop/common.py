# common.py
#
# contains classes (that are not UI elements) and functions that are common to 
# all parts of the program.
# does this show up?
# just making sure that this change gets captured

from PySide6.QtWidgets import QWidget, QTreeWidget, QTableWidget, QTreeWidgetItem, QListWidget, QListWidgetItem
import PySide6.QtCore as QtCore
from dataclasses import dataclass
from typing import List, Dict, Tuple
import mysql.connector

# column index constants for recipe tree widgets in dashboard and meal plan
NAME_INDEX     = 0
SERVES_INDEX   = 1
QUANTITY_INDEX = 2
UNIT_INDEX     = 3
SELECT_INDEX   = 4
ID_INDEX       = 5  # store data in the item but this is a hidden column

# Tab indices - these get reset by the mainwindow's init function
DASHBOARD      = 0
MEAL_PLAN      = 1
PUBLIC_RECIPES = 2
MY_RECIPES     = 3
BOOKS          = 4
CREATE_RECIPE  = 5
SHOPPING_LIST  = 6
INVENTORY      = 7
USER_INFO      = 8
SIGNUP_INFO    = 9

# conversion
TSP        = 0
TBSP       = 1
CUP        = 2
ML         = 3
FL_OZ      = 4
PINT       = 5
QUART      = 6
GALLON     = 7

POUNDS     = 8
OUNCES     = 9
GRAMS      = 10
MILLIGRAMS = 11

conv_indices = {
    'tsp': TSP,
    'tbsp': TBSP,
    'cup': CUP,
    'ml': ML,
    'fl oz': FL_OZ,
    'pint': PINT,
    'quart': QUART,
    'gallon': GALLON,
    'lb': POUNDS,
    'lbs': POUNDS,
    'oz': OUNCES,
    'g': GRAMS,
    'mg': MILLIGRAMS
}
conversion_matrix = [[1,        0.333333,  0.020833,   5,        0.166667, 0.0104,     0.0052,   0.0013,    None, None, None, None],  # TSP 
                     [3,        1,         0.0625,     14.7868,  0.5,      0.03125,    0.015625, 0.0039,    None, None, None, None],  # TBSP
                     [48.692,   16,        1,          236.588,  8,        0.5,        0.25,     0.0625,    None, None, None, None],  # CUP
                     [0.202884, 0.067628,  0.00422675, 1,        0.033814, 0.00211338, 0.0011,   0.00026,   None, None, None, None],  # ML
                     [6,        2,         0.125,      29.5735,  1,        0.0625,     0.03125,  0.0078125, None, None, None, None],  # Fl Oz
                     [96,       32,        2,          473.176,  16,       1,          0.5,      0.125,     None, None, None, None],  # pint
                     [192,      64,        4,          946.353,  32,       2,          1,        0.5,       None, None, None, None],  # quart
                     [768,      256,       15.775,     3785.41,  128,      8,          4,        1,         None, None, None, None],  # gallon
                     [None, None, None, None, None, None, None, None, 1, 16, 453.592, 453592],          # pound
                     [None, None, None, None, None, None, None, None, 0.0625, 1, 28.3495, 28349.5],     # ounce
                     [None, None, None, None, None, None, None, None, 0.00220462, 0.035274, 1, 1000],   # grams
                     [None, None, None, None, None, None, None, None, 2.2046E-6, 3.5274E-5, 0.001, 1]]  # milligrams

@dataclass
class Ingredient:
    name: str
    quantity: float
    unit: str

@dataclass
class Recipe:
    id: int
    name: str
    ingredient_list: List[Ingredient]
    serves: float
    instructions: str  # currently stored as a free-text field
    status: int
    owner: str
    tags: List[str]
    selected: bool = False
        
@dataclass
class Book:
    id: int
    name: str 
    recipe_list: List[int] # List of recipe ids
    
@dataclass
class User:
    id: int
    name: str
    password: str
    logged_in: bool

# Current user
CURR_USER = User(1, "default", "pass0", False)

def show_recipe(recipe: Recipe) -> None:
    print("===", recipe.name, ":: serves", recipe.serves, "===")
    for i in recipe.ingredient_list:
        print("   ", i.name, ",", i.quantity, ",", i.unit)
    print("\n   ", recipe.instructions[:25])


def change_recipe_serving_by_factor(recipe: Recipe, factor: float) -> None:
    # modify the recipe accordingly
    # update the widget and other related widgets
    recipe.serves *= factor
    for i in recipe.ingredient_list:
        i.quantity *= factor

#
# compares the quantity, unit tuples a and b with the unit taken into consideration
# returns 0 if `a` is larger or equal in quantity
# returns 1 if `b` is larget
# returns -1 if no conversion found
def compare_quant_and_unit(a_quant: float, a_unit: str, b_quant: float, b_unit: str) -> int:
    if a_unit == b_unit:
        if b_quant > a_quant:
            return 1
        else:
            return 0
    elif a_unit in conv_indices and b_unit in conv_indices:
        b_index = conv_indices[b_unit]
        a_index = conv_indices[a_unit]
        b_in_a_units = b_quant * conversion_matrix[b_index][a_index]
        if b_in_a_units > a_quant:
            return 1
        else:
            return 0
    else:
        return -1


#
# convert quantity of a in its given units to the units give by b_unit
# NOTE: this doesn't check if the conversion is valid... but it probably should
def unit_convert(a_quant: float, a_unit: str, b_unit: str) -> float:
    a_index = conv_indices[a_unit]
    b_index = conv_indices[b_unit]
    return a_quant * conversion_matrix[a_index][b_index]

#
# this is the function that does the main thing - convert our list of recipes into 
# a regular shopping list
def meal_plan_to_shopping_list(meal_plan: Dict[int, Recipe], inventory: List[Ingredient]=[], other_items: List[Ingredient] = []) -> List[Ingredient]:
    result = []
    dd_ingredients : Dict[str, Dict[str, int]]= { }
    set_inv = {x.name: (x.quantity, x.unit) for x in inventory}  # avoid the O(n^2) check on the inventory list
    
    for _, recipe in meal_plan.items():
        for ingredient in recipe.ingredient_list:
            name = ingredient.name
            unit = ingredient.unit
            quantity = ingredient.quantity

            if ingredient.name in set_inv:
                continue

            if name in dd_ingredients:
                if unit in dd_ingredients[name]:
                    dd_ingredients[name][unit] += quantity
                else:
                    for stored_unit in dd_ingredients[name]:
                        comparison = compare_quant_and_unit(1, unit, 1, stored_unit)
                        if comparison == 0:  # unit is larger unit
                            dd_ingredients[name][unit] = quantity + unit_convert(dd_ingredients[name][stored_unit], stored_unit, unit)
                            dd_ingredients[name].pop(stored_unit)
                            break
                        elif comparison == 1:  # stored_unit is larger unit
                            dd_ingredients[name][stored_unit] += unit_convert(quantity, unit, stored_unit)
                            break
                        else:  # no comparison known
                            dd_ingredients[name][unit] = quantity
                            break
            else:  # new name
                dd_ingredients[name] = {}
                dd_ingredients[name][unit] = quantity

    for ingredient in other_items:
        name = ingredient.name
        unit = ingredient.unit
        quantity = ingredient.quantity

        if ingredient.name in set_inv:
            continue

        if name in dd_ingredients:
            if unit in dd_ingredients[name]:
                dd_ingredients[name][unit] += quantity
            else:
                for stored_unit in dd_ingredients[name]:
                    comparison = compare_quant_and_unit(1, unit, 1, stored_unit)
                    if comparison == 0:  # unit is larger unit
                        dd_ingredients[name][unit] = quantity + unit_convert(dd_ingredients[name][stored_unit], stored_unit, unit)
                        dd_ingredients[name].pop(stored_unit)
                        break
                    elif comparison == 1:  # stored_unit is larger unit
                        dd_ingredients[name][stored_unit] += unit_convert(quantity, unit, stored_unit)
                        break
                    else:  # no comparison known
                        dd_ingredients[name][unit] = quantity
                        break
        else:  # new name
            dd_ingredients[name] = {}
            dd_ingredients[name][unit] = quantity

    for name, d_unit_quant in dd_ingredients.items():
        for unit, quant in d_unit_quant.items():
            result.append(Ingredient(name, quant, unit))

    return sorted(result, key=lambda x: x.name)

#
# updates a tree widget that holds recipes with 
def init_recipe_tree(recipe_dict: Dict[int, Recipe], tree_widget: QTreeWidget) -> None:
    for _, recipe in recipe_dict.items():    
        top_level_item = QTreeWidgetItem(tree_widget)
        top_level_item.setText(NAME_INDEX, recipe.name)
        top_level_item.setText(SERVES_INDEX, str(recipe.serves))
        top_level_item.setExpanded(True)
        top_level_item.setCheckState(SELECT_INDEX, QtCore.Qt.Checked if recipe.selected else QtCore.Qt.Unchecked)
        top_level_item.setText(5, str(recipe.id))
        tree_widget.addTopLevelItem(top_level_item)

        for ingredient in recipe.ingredient_list:
            child_item = QTreeWidgetItem(top_level_item)
            child_item.setText(NAME_INDEX, ingredient.name)
            child_item.setText(QUANTITY_INDEX, str(ingredient.quantity))
            child_item.setText(UNIT_INDEX, ingredient.unit)
            top_level_item.addChild(child_item)

#
# given a tree and a list of items, fill that tree with those items
# TODO: pass the inventory from main window and consider that when adding (or not adding) items to the inventory
# NOTE: inventory is a list - it would be great is you hashed all the items and just checked the hashes for O(1) lookup
def set_shopping_list(ingredients: List[Ingredient], extra_items: List[Ingredient], tree: QTreeWidget) -> None:
    tree.clear()
    for ingredient in ingredients:
        top_level_item = QTreeWidgetItem(tree)
        top_level_item.setText(0, ingredient.name)
        top_level_item.setText(1, str(ingredient.quantity))
        top_level_item.setText(2, ingredient.unit)
        top_level_item.setCheckState(3, QtCore.Qt.Unchecked)
        tree.addTopLevelItem(top_level_item)
    
    for ingredient in extra_items:
        top_level_item = QTreeWidgetItem(tree)
        top_level_item.setFlags(top_level_item.flags() | QtCore.Qt.ItemIsEditable)
        top_level_item.setText(0, ingredient.name)
        top_level_item.setText(1, str(ingredient.quantity))
        top_level_item.setText(2, ingredient.unit)
        top_level_item.setCheckState(3, QtCore.Qt.Unchecked)
        tree.addTopLevelItem(top_level_item)

#
# given a widget and an item id, update that item based on it being removed from / added to the meal plan
# @param widget - the widget that has two tree widget children named meal_plan_tree and recipe_tree (NOTE: it would be nice if that was not required - like passing the trees as parameters)
# @param recipe_id - id of the recipe that is causing the update (selecting or deselecting)
def update_tree_widgets(widget: QWidget, recipe_id: int):
    parent = widget.parent

    if recipe_id in parent.meal_plan_table:  # removing from meal plan
        root = widget.meal_plan_tree.invisibleRootItem()
        child_count = root.childCount()
        for i in range(child_count):  # find in the tree widget and remove it
            item = root.child(i)
            if int(item.text(ID_INDEX)) == recipe_id:
                widget.meal_plan_tree.takeTopLevelItem(i)
                break
        
        root = widget.recipe_tree.invisibleRootItem()
        for i in range(root.childCount()):
            item = root.child(i)
            if int(item.text(ID_INDEX)) == recipe_id:
                item.setCheckState(SELECT_INDEX, QtCore.Qt.Unchecked)
    else:  # adding to the meal plan
        recipe = parent.recipe_table[recipe_id]
        top_level_item = QTreeWidgetItem(widget.meal_plan_tree)
        top_level_item.setText(NAME_INDEX, recipe.name)
        top_level_item.setText(SERVES_INDEX, str(recipe.serves))
        top_level_item.setExpanded(True)
        top_level_item.setCheckState(SELECT_INDEX, QtCore.Qt.Checked)
        top_level_item.setText(ID_INDEX, str(recipe.id))
        top_level_item.setFlags(top_level_item.flags() | QtCore.Qt.ItemIsEditable)

        widget.meal_plan_tree.addTopLevelItem(top_level_item)

        for ingredient in recipe.ingredient_list:   
            child_item = QTreeWidgetItem(top_level_item)
            child_item.setText(NAME_INDEX, ingredient.name)
            child_item.setText(QUANTITY_INDEX, str(ingredient.quantity))
            child_item.setText(UNIT_INDEX, ingredient.unit)
            child_item.setFlags(child_item.flags() | QtCore.Qt.ItemIsEditable)
            top_level_item.addChild(child_item)
        
        root = widget.recipe_tree.invisibleRootItem()
        for i in range(root.childCount()):
            item = root.child(i)
            if int(item.text(ID_INDEX)) == recipe_id:
                item.setCheckState(SELECT_INDEX, QtCore.Qt.Checked)
#
# update the inventory based on if item is purchased (or unpurchased)
# @param check indicates the new check state of the item - that is, if they are "checking" or "unchecking" this item
def item_purchased(item: QTreeWidgetItem, check: bool):
    # TODO (tam, vandana, mustafa): do the inventory update stuff
    #   adjust the check state accordingly because clicking the column doesn't have to click the box
    #   add to inventory
    ...


# Gets ID of recipe based on name
def get_id_of_recipe(dict: Dict, recipe_name):
    for id, recipe in dict.items(): 
        if recipe.name == recipe_name:
            return id
    return None


#connect to database
def connect_to_database():
    mydb = mysql.connector.connect(user = 'sql5445221',
                                   password = '27vqdQxKTN',
                                   host = 'sql5.freesqldatabase.com',
                                   database = 'sql5445221')
    return mydb

# == For testing only ==

TEST_USER_ID = 99
TEST_USER = User(TEST_USER_ID, "test", "testpassword", False)

def set_user_to_test():
    TEST_USER.logged_in = True
    CURR_USER.id = TEST_USER.id
    CURR_USER.name = TEST_USER.name
    CURR_USER.password = TEST_USER.password
    CURR_USER.logged_in = TEST_USER.logged_in


def set_user_to_fake_user():
    TEST_USER.logged_in = False
    CURR_USER.id = -1
    CURR_USER.name = "fake"
    CURR_USER.password = "nopass"
    CURR_USER.logged_in = True

