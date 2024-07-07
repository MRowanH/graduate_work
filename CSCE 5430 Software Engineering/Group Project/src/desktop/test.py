# test.py
#
# contains all the unittests for the project
# as of now this will just be some functions that run... if we really want a unittest test framework that is
# fine as well.

import time
from common import *
from database import DBHandler

class UnitTests():
    class TestMealPlanToShoppingList():
        def empty_meal_plan():
            expected = 0
            actual = len(meal_plan_to_shopping_list({}))
            return actual == expected, expected, actual
        
        def case_1():
            expected = [
                Ingredient("egg",   2, "--"),
                Ingredient("flour", 2, "cups"),
                Ingredient("milk",  2, "cups"),
                Ingredient("sugar", 4, "tablespoons")
            ]
            meal_plan = {
                0: Recipe(0, "cake", [Ingredient("egg", 2, "--"),
                                      Ingredient("flour", 2, "cups"),
                                      Ingredient("milk", 2, "cups"),
                                      Ingredient("sugar", 4, "tablespoons")], 6, "how to make", "", "", [])
            }
            actual = meal_plan_to_shopping_list(meal_plan)
            return actual == expected, expected, actual
    
        def same_item_accross_recipes():
            expected = [Ingredient("egg", 4, "--")]
            meal_plan = {
                0: Recipe(0, "a", [Ingredient("egg", 2, "--")], 1, "how to", "", "", []),
                1: Recipe(0, "b", [Ingredient("egg", 2, "--")], 1, "how to", "", "", [])
            }
            actual = meal_plan_to_shopping_list(meal_plan)
            return actual == expected, expected, actual
        
        def inventory_has_item():
            inventory = [Ingredient("salt", 4, "lbs")]
            expected = [Ingredient("egg", 4, "--")]
            meal_plan = {
                0: Recipe(0, "a", [Ingredient("egg", 2, "--")], 1, "how to", "", "", []),
                1: Recipe(0, "b", [Ingredient("egg", 2, "--")], 1, "how to", "", "", []),
                2: Recipe(0, "c", [Ingredient("salt", 5, "tsp")], 1, "how to", "", "", [])
            }
            actual = meal_plan_to_shopping_list(meal_plan, inventory)
            return actual == expected, expected, actual
        
        def add_other_item():
            other_items = [Ingredient("cat food", 20, "lbs"), Ingredient("bleach", 1, "bottle")]
            inventory = [Ingredient("salt", 4, "lbs")]
            expected = sorted([Ingredient("egg", 4, "--"), Ingredient("cat food", 20, "lbs"), Ingredient("bleach", 1, "bottle")], key=lambda x: x.name)
            meal_plan = {
                0: Recipe(0, "a", [Ingredient("egg", 2, "--")], 1, "how to", "", "", []),
                1: Recipe(0, "b", [Ingredient("egg", 2, "--")], 1, "how to", "", "", []),
                2: Recipe(0, "c", [Ingredient("salt", 5, "tsp")], 1, "how to", "", "", [])
            }
            actual = meal_plan_to_shopping_list(meal_plan, inventory, other_items)
            return  actual == expected, expected, actual


    class TestDatabase():
        def test_add_recipe_1():
            db = DBHandler()
            recipe_to_add = Recipe(999996, "newtest", [Ingredient("paprika", 2.0, "lbs")], 2, "how to", 0, TEST_USER_ID, [], False)
            id = db.add_recipe(recipe_to_add)
            db.cursor.execute("SELECT id FROM Recipes WHERE id = %s", (id,))
            actual   = len(db.cursor.fetchall())
            expected = 1
            db.clean_test_entries()
            return expected == actual, expected, actual

        def test_add_recipe_2():
            # test id already exists
            db = DBHandler()
            recipe_to_add = Recipe(999998, "addmeagain", [Ingredient("pepper", 1.0, "lbs")], 2, "how to", 0, TEST_USER_ID, [], False)
            db.add_recipe(recipe_to_add)
            expected = -1
            actual = db.add_recipe(recipe_to_add)
            db.clean_test_entries()
            return expected == actual, expected, actual

        def test_rem_recipe():
            db = DBHandler()
            recipe_to_rem = Recipe(999995, "removeme", [Ingredient("pepper", 1.0, "lbs")], 2, "how to", 0, TEST_USER_ID, [], False)
            id = db.add_recipe(recipe_to_rem)
            assert id != -1, "should add"
            recipe_to_rem.id = id
            db.rem_recipe(recipe_to_rem, TEST_USER_ID)
            db.cursor.execute("SELECT id FROM Recipes WHERE id = %s", (id,))
            actual   = len(db.cursor.fetchall())
            expected = 0
            db.clean_test_entries()
            return expected == actual, expected, actual

        def test_add_to_meal_plan_1():
            db = DBHandler()
            recipe_to_add = Recipe(-1, "addmetomealplan", [], 2, "how to", 0, TEST_USER_ID, [], False)
            actual_id = db.add_recipe(recipe_to_add)
            recipe_to_add.id = actual_id
            db.add_to_meal_plan(actual_id)
            db.cursor.execute("SELECT * from MealPlan WHERE userID = %s AND recipeID = %s", (CURR_USER.id, actual_id))
            actual   = db.cursor.fetchall()
            expected = [(CURR_USER.id, actual_id)]
            db.clean_test_entries()
            return expected == actual, expected, actual

        def test_add_to_meal_plan_2():
            db = DBHandler()
            actual_id = -1
            assert not db.add_to_meal_plan(actual_id), "meal plan should return false here"
            db.cursor.execute("SELECT * FROM MealPlan WHERE userID = %s AND recipeID = %s", (CURR_USER.id, actual_id))
            actual   = db.cursor.fetchall()
            expected = []
            db.clean_test_entries()
            return expected == actual, expected, actual

        def test_rem_from_meal_plan_1():
            db = DBHandler()
            recipe_to_add = Recipe(-1, "addmetomealplan", [], 2, "how to", 0, TEST_USER_ID, [], False)
            actual_id = db.add_recipe(recipe_to_add)
            recipe_to_add.id = actual_id
            assert db.add_to_meal_plan(actual_id), "added meal plan"
            assert db.rem_from_meal_plan(actual_id), "removed meal plan"
            db.cursor.execute("SELECT * FROM MealPlan WHERE userID = %s AND recipeID = %s", (CURR_USER.id, actual_id))
            actual   = db.cursor.fetchall()
            expected = []
            db.clean_test_entries()
            return expected == actual, expected, actual

        def test_rem_from_meal_plan_2():
            db = DBHandler()
            recipe_to_add = Recipe(-1, "addmetomealplan", [], 2, "how to", 0, TEST_USER_ID, [], False)
            actual_id = db.add_recipe(recipe_to_add)
            recipe_to_add.id = actual_id
            assert db.add_to_meal_plan(actual_id), "added meal plan"
            
            set_user_to_fake_user()
            assert db.rem_from_meal_plan(actual_id), "remove should fail"
            set_user_to_test()
            db.cursor.execute("SELECT * FROM MealPlan WHERE userID = %s AND recipeID = %s", (CURR_USER.id, actual_id))
            actual   = db.cursor.fetchall()
            expected = [(CURR_USER.id, actual_id)]
            db.clean_test_entries()
            return expected == actual, expected, actual

        def test_add_to_extra_items_1():
            db = DBHandler()
            ingredient_to_add = Ingredient("fake one", 1, 'lbs')
            assert db.add_to_extra_items(ingredient_to_add.name, ingredient_to_add.quantity, ingredient_to_add.unit), "should add"
            db.cursor.execute("SELECT item FROM ExtraItems WHERE item = %s", ("fake one", ))
            expected = [("fake one", )]
            actual = db.cursor.fetchall()
            db.clean_test_entries()
            return expected == actual, expected, actual

        def test_add_to_extra_items_2():
            db = DBHandler()
            name = "another fake one"
            ingredient_to_add = Ingredient(name, 1, 'lbs')
            set_user_to_fake_user()
            assert not db.add_to_extra_items(ingredient_to_add.name, ingredient_to_add.quantity, ingredient_to_add.unit), "add extra should fail"
            set_user_to_test()
            db.cursor.execute("SELECT item FROM ExtraItems WHERE item = %s", (name, ))
            expected = []
            actual = db.cursor.fetchall()
            db.clean_test_entries()
            return expected == actual, expected, actual

        def test_rem_from_extra_items_1():
            db = DBHandler()
            name = "remove this item"
            ingredient_to_add = Ingredient(name, 1, 'lbs')
            assert db.add_to_extra_items(ingredient_to_add.name, ingredient_to_add.quantity, ingredient_to_add.unit), "should add"
            assert db.rem_from_extra_items(ingredient_to_add.name, ingredient_to_add.quantity, ingredient_to_add.unit), "should remove"
            db.cursor.execute("SELECT item FROM ExtraItems WHERE item = %s", (name, ))
            expected = []
            actual = db.cursor.fetchall()
            db.clean_test_entries()
            return expected == actual, expected, actual


    class TestConversions():
        def change_recipe_by_factor_1():
            input_recipe = Recipe(1, "a", [Ingredient("salt", 1, "tsp")], 1, "", 1, "", [])
            input_factor = 2
            expected = Recipe(1, "a", [Ingredient("salt", 2, "tsp")], 2, "", 1, "", [])
            change_recipe_serving_by_factor(input_recipe, input_factor)
            return input_recipe == expected, expected, input_recipe
        
        def change_recipe_by_factor_2():
            input_recipe = Recipe(1, "a", [Ingredient("salt", 1, "tsp"), Ingredient("pepper", 5, "scoops")], 1, "", 1, "", [])
            input_factor = 3
            expected = Recipe(1, "a", [Ingredient("salt", 3, "tsp"), Ingredient("pepper", 15, "scoops")], 3, "", 1, "", [])
            change_recipe_serving_by_factor(input_recipe, input_factor)
            return input_recipe == expected, expected, input_recipe

        def change_recipe_by_factor_3():
            input_recipe = Recipe(1, "a", [Ingredient("butter", 5, "tsp")], 2, "", 1, "", [])
            input_factor = 0.5
            expected = Recipe(1, "a", [Ingredient("butter", 2.5, "tsp")], 1, "", 1, "", [])
            change_recipe_serving_by_factor(input_recipe, input_factor)
            return input_recipe == expected, expected, input_recipe

        def compare_quantities_1():
            a = 2
            b = 1
            expected = 0  # a is larger
            actual = compare_quant_and_unit(a, "", b, "")
            return actual == expected, expected, actual

        def compare_quantities_2():
            a = 1
            b = 2
            expected = 1  # b is larger
            actual = compare_quant_and_unit(a, "", b, "")
            return actual == expected, expected, actual

        def compare_quantities_3():
            a = 1
            b = 1
            expected = 0  # they are the same
            actual = compare_quant_and_unit(a, "", b, "")
            return actual == expected, expected, actual

        def compare_quantities_4():
            a = 1
            b = 1
            a_unit = "a_unit"
            b_unit = "b_unit"
            expected = -1  # different units and units not known
            actual = compare_quant_and_unit(a, a_unit, b, b_unit)
            return actual == expected, expected, actual

        def compare_quantities_5():
            a = 2
            b = 1
            a_unit = "tsp"
            b_unit = "tbsp"
            expected = 1  # 1 tablespoon is bigger than 2 teaspoons
            actual = compare_quant_and_unit(a, a_unit, b, b_unit)
            return actual == expected, expected, actual

        def compare_quantities_6():
            a = 3
            b = 1
            a_unit = "tsp"
            b_unit = "tbsp"
            expected = 0  # 1 tbsp == 3 tsp
            actual = compare_quant_and_unit(a, a_unit, b, b_unit)
            return actual == expected, expected, actual
        
        def unit_convert_1():
            a_quant = 2
            a_unit = "cup"
            b_unit = "fl oz"
            expected = 16
            actual = unit_convert(a_quant, a_unit, b_unit)
            return actual == expected, expected, actual

        def unit_convert_2():
            a_quant = 4
            a_unit = "gallon"
            b_unit = "pint"
            expected = 32
            actual = unit_convert(a_quant, a_unit, b_unit)
            return actual == expected, expected, actual

        def unit_convert_3():
            a_quant = 1
            a_unit = "tsp"
            b_unit = "tsp"
            expected = 1
            actual = unit_convert(a_quant, a_unit, b_unit)
            return actual == expected, expected, actual

class UiTests:
    class TestLogin():
        def test_sign_in_1(self, main):
            assert not main.tab_widget.isTabEnabled(DASHBOARD), "shopping list should be disabled"
            assert not main.tab_widget.isTabEnabled(MEAL_PLAN), "dashboard should be disabled"
            assert not main.tab_widget.isTabEnabled(MY_RECIPES), "my_recipes should be disabled"
            assert not main.tab_widget.isTabEnabled(BOOKS), "books should be disabled"
            assert not main.tab_widget.isTabEnabled(CREATE_RECIPE), "create recipe should be disabled"
            assert not main.tab_widget.isTabEnabled(SHOPPING_LIST), "shopping list should be disabled"
            assert not main.tab_widget.isTabEnabled(INVENTORY), "inventory should be disabled"

            login = main.tab_widget.widget(USER_INFO)
            login.username_input.setText("Brice")
            login.password_input.setText("pass2")
            login.get_login_info()

            assert main.tab_widget.isTabEnabled(DASHBOARD), "shopping list should be enabled"
            assert main.tab_widget.isTabEnabled(MEAL_PLAN), "dashboard should be enabled"
            assert main.tab_widget.isTabEnabled(MY_RECIPES), "my_recipes should be enabled"
            assert main.tab_widget.isTabEnabled(BOOKS), "books should be enabled"
            assert main.tab_widget.isTabEnabled(CREATE_RECIPE), "create recipe should be enabled"
            assert main.tab_widget.isTabEnabled(SHOPPING_LIST), "shopping list should be enabled"
            assert main.tab_widget.isTabEnabled(INVENTORY), "inventory should be enabled"

            main.logout()

            return True, True, True

    class TestDashboard:
        def test_add_to_meal_plan_1(self, main):
            dash_widget = main.tab_widget.widget(DASHBOARD)
            recipe_tree = main.tab_widget.widget(DASHBOARD).recipe_tree
            meal_plan_tree = main.tab_widget.widget(DASHBOARD).meal_plan_tree

            expected = recipe_tree.topLevelItem(0).text(0)
            dash_widget.item_clicked(recipe_tree.topLevelItem(0), SELECT_INDEX)
            actual = meal_plan_tree.topLevelItem(0).text(0)
            dash_widget.item_clicked(meal_plan_tree.topLevelItem(0), SELECT_INDEX)  # undo the selection
            return expected == actual, expected, actual

        def test_rem_from_meal_plan_1(self, main):
            dash_widget = main.tab_widget.widget(DASHBOARD)
            recipe_tree = main.tab_widget.widget(DASHBOARD).recipe_tree
            meal_plan_tree = main.tab_widget.widget(DASHBOARD).meal_plan_tree

            dash_widget.item_clicked(recipe_tree.topLevelItem(0), SELECT_INDEX)
            assert meal_plan_tree.topLevelItem(0), "should add to meal plan"
            dash_widget.item_clicked(meal_plan_tree.topLevelItem(0), SELECT_INDEX)

            expected = None
            actual = meal_plan_tree.topLevelItem(0)
            return expected == actual, expected, actual

        def test_rem_from_meal_plan_2(self, main):
            dash_widget = main.tab_widget.widget(DASHBOARD)
            recipe_tree = main.tab_widget.widget(DASHBOARD).recipe_tree
            meal_plan_widget = main.tab_widget.widget(MEAL_PLAN)
            meal_plan_tree = main.tab_widget.widget(MEAL_PLAN).meal_plan_tree

            dash_widget.item_clicked(recipe_tree.topLevelItem(0), SELECT_INDEX)
            assert meal_plan_tree.topLevelItem(0), "should add to meal plan"
            meal_plan_widget.item_clicked(meal_plan_tree.topLevelItem(0), SELECT_INDEX-1)

            expected = recipe_tree.topLevelItem(0).text(0)
            actual = meal_plan_tree.takeTopLevelItem(0).text(0)
            dash_widget.item_clicked(recipe_tree.topLevelItem(0), SELECT_INDEX)  # undo the selection
            return expected == actual, expected, actual

    class TestDashboardMealPlan:
        def test_add_to_meal_plan(self, main):
            dash_widget = main.tab_widget.widget(DASHBOARD)
            recipe_tree = main.tab_widget.widget(DASHBOARD).recipe_tree
            meal_plan_tree = main.tab_widget.widget(MEAL_PLAN).meal_plan_tree

            expected = recipe_tree.topLevelItem(0).text(0)
            dash_widget.item_clicked(recipe_tree.topLevelItem(0), SELECT_INDEX)
            actual = meal_plan_tree.topLevelItem(0).text(0)
            dash_widget.item_clicked(meal_plan_tree.topLevelItem(0), SELECT_INDEX)  # undo the selection
            return expected == actual, expected, actual

        def test_rem_from_meal_plan(self, main):
            dash_widget = main.tab_widget.widget(DASHBOARD)
            recipe_tree = main.tab_widget.widget(DASHBOARD).recipe_tree
            meal_plan_widget = main.tab_widget.widget(MEAL_PLAN)
            meal_plan_tree = main.tab_widget.widget(DASHBOARD).meal_plan_tree

            dash_widget.item_clicked(recipe_tree.topLevelItem(0), SELECT_INDEX)
            assert meal_plan_tree.topLevelItem(0), "should add to meal plan"
            meal_plan_widget.item_clicked(meal_plan_tree.topLevelItem(0), SELECT_INDEX)

            expected = None
            actual = meal_plan_tree.topLevelItem(0)
            return expected == actual, expected, actual


def run_tests(ui = False, main = None):
    failures = []
    success  = []
    start_time = time.time()

    set_user_to_test()

    if ui:
        tests = UiTests.__dict__.items()
    else:
        tests = UnitTests.__dict__.items()

    for name, fn_or_class in tests:
        if type(fn_or_class) is type:
            for _name, fn in fn_or_class.__dict__.items():
                if callable(fn):
                    dot_name = f"%s.%s" % (name, _name)
                    print(dot_name, end="")

                    try:
                        if ui:
                            status, expected, actual = fn(None, main)
                        else:
                            status, expected, actual = fn()
                    except AssertionError as e:
                        status = False
                        expected = "Assert: " + str(e)
                        actual = "Failed"
                    
                    if status:
                        success.append(dot_name)
                        print(u' [\u2713]')
                    else:
                        failures.append(dot_name)
                        print(" [x]")
                        print("\t expected: ", expected)
                        print("\t actual  : ", actual)

        elif callable(fn_or_class):
            print(name, end="")
            
            try:
                status, expected, actual = fn_or_class()
            except AssertionError as e:
                status = False
                expected = "Assert: " + str(e)
                actual = "Failed"

            if status:
                success.append(name)
                print(u' [\u2713]')
            else:
                failures.append(name)
                print(" [x]")
                print(" [x]")
                print("\t expected: ", expected)
                print("\t actual  : ", actual)

    end_time = time.time()
    print("\nfailed: %d\tsuccess: %d\ttime: %f" % (len(failures), len(success), (end_time - start_time)))


if __name__ == "__main__":
    run_tests()