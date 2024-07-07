# This Python file uses the following encoding: utf-8

# imports
import sys

# qt imports
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

# ui imports
from ui.ui_mainwindow import Ui_MainWindow
from MealPlan import MealPlan
from Dashboard import Dashboard
from ShoppingList import ShoppingList
from PublicRecipes import PublicRecipes
from PrivateRecipes import PrivateRecipes
from CreateARecipe import CreateARecipe
from RecipeBookBrowser import RecipeBookBrowser
from Inventory import Inventory
from Login import Login
from SignUp import SignUp
from common import *
from database import DBHandler
# just making sure that this change gets captured

from test import run_tests

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, testing = False):
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        # Database handler
        self.db = DBHandler()
        
        # Global data
        self.user = CURR_USER.id
        self.recipe_table    : Dict[int, Recipe] = self.db.load_recipe_list()
        self.meal_plan_table : Dict[int, Recipe] = self.db.load_meal_plan(self.recipe_table)
        self.inventory       : List[Ingredient]  = self.db.load_inventory() 
        self.shopping_list   : List[Ingredient]  = meal_plan_to_shopping_list(self.meal_plan_table, [], [])
        self.extra_items     : List[Ingredient]  = self.db.load_extra_items()
        self.recipe_books    : Dict[int, Book]   = self.db.load_recipe_books(self.recipe_table)

        # add tabs and assign the tab indices
        DASHBOARD     = self.tab_widget.addTab(Dashboard(self),      "Dashboard")
        MEAL_PLAN     = self.tab_widget.addTab(MealPlan(self),       "MealPlan")
        PUBLIC_RECIPES= self.tab_widget.addTab(PublicRecipes(self),  "Public Recipes")
        MY_RECIPES    = self.tab_widget.addTab(PrivateRecipes(self), "My Recipes")
        BOOKS         = self.tab_widget.addTab(RecipeBookBrowser(self), "My Recipe Books") 
        CREATE_RECIPE = self.tab_widget.addTab(CreateARecipe(self),  "Create A Recipe")
        SHOPPING_LIST = self.tab_widget.addTab(ShoppingList(self),   "Shopping List")
        INVENTORY     = self.tab_widget.addTab(Inventory(self),      "Inventory")
        USER_INFO     = self.tab_widget.addTab(Login(self),          "Profile")
        SIGNUP_INFO   = self.tab_widget.addTab(SignUp(self),           "Sign Up")

        set_shopping_list(self.shopping_list, self.extra_items, self.tab_widget.widget(SHOPPING_LIST).shopping_list)
        set_shopping_list(self.shopping_list, self.extra_items, self.tab_widget.widget(DASHBOARD).shopping_list_tree)

        #print(f'SignUp - Current User Logged In?: {CURR_USER.logged_in}')
        #print(type(self.tab_widget.widget(DASHBOARD)))
        if not CURR_USER.logged_in:
            self.disable_tabs()
            self.tab_widget.setTabEnabled(USER_INFO, True)
            self.tab_widget.setTabEnabled(SIGNUP_INFO, True)
            
        # for k in self.recipe_table:
        #     print(self.recipe_table[k].id)
        #     print(self.recipe_table[k].name)
        #     print(self.recipe_table[k].serves)
        #     print(self.recipe_table[k].status)
        #     print(self.recipe_table[k].owner)
        #     print(self.recipe_table[k].selected)
        #     print(self.recipe_table[k].instructions)
        #     print()

        if testing:
            set_user_to_test()
            run_tests(True, self)
            sys.exit(0)

    #
    def login(self, username, password):
        user = self.db.verify_user(User(-1, username, password, False))

        if user == None:  # user did not exist, or username/password was wrong
            #self.username_input.clear()
            #self.password_input.clear()
            #self.tab_widget.widget(USER_INFO)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Question)
            msg.setText(f'You have entered an incorrect username or password, please try again')
            msg.setWindowTitle('Invalid User')
            msg.exec()
            print(f'THIS USER {username} DOES NOT EXIST: please enter an existing user')
            return  # should tell user invalid username/password
        else:  # user exists update current user to this verified user
            # print(f'Login existing user: {username}')
            if self.db.verify_password(user):
                user.logged_in = True
                CURR_USER = user
                # print(f'SignUp - Current User Logged In?: {CURR_USER.logged_in}')
                self.enable_tabs() # when you are logged in,
                self.tab_widget.setTabEnabled(SIGNUP_INFO, False)
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Question)
                msg.setText(f'You have entered an incorrect username or password, please try again')
                msg.setWindowTitle('Invalid User')
                print(f'You have entered an incorrect password: {password}')
                msg.exec()
            # #user cannot sign up as well
            # should change login screen to profile screen
            # should update info for all other pages

    def logout(self):
        # print(f'User Logging out')
        self.disable_tabs()
        self.tab_widget.setTabEnabled(USER_INFO, True)
        self.tab_widget.setTabEnabled(SIGNUP_INFO, True)

    def sign_up(self, username, password):
        user = self.db.verify_user(User(-1, username, password, False))

        if user is None:
            print(f'New user signed up')
            user = self.db.add_user(username, password)
            user.logged_in = True
            CURR_USER = user
            # print(f'SignUp - Current User Logged In?: {CURR_USER.logged_in}')
            self.enable_tabs() #can't login when signed up
            self.tab_widget.setTabEnabled(USER_INFO, False)
        else:
            print(f'Duplicate User signing up')
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Question)
            msg.setText(f'This user {username}, ALREADY EXISTS please enter a new username')
            msg.setWindowTitle('Invalid User')
            print(f'You have entered an incorrect username: {username}')
            msg.exec()
            return

    def disable_tabs(self):
        for i in range(DASHBOARD, SIGNUP_INFO + 1):
            self.tab_widget.setTabEnabled(i, False)

    def enable_tabs(self, dont_enable_tabs=[]):
        for i in range(DASHBOARD, SIGNUP_INFO + 1):
            self.tab_widget.setTabEnabled(i, True)

    # update all appropriate structures for such an event
    def recipe_item_selection_changed(self, recipe_id: int):
        # call the update functions of tabs that depend on mainwindow structures before they have been updated
        self.tab_widget.widget(DASHBOARD).my_update(recipe_id)
        self.tab_widget.widget(MEAL_PLAN).my_update(recipe_id)

        # after updating all the views we update the structures 
        if recipe_id in self.meal_plan_table:
            self.meal_plan_table.pop(recipe_id)
            self.db.rem_from_meal_plan(recipe_id)
        else:
            self.meal_plan_table[recipe_id] = self.recipe_table[recipe_id]
            self.db.add_to_meal_plan(recipe_id)
        
        # call update functions of those that depend on the shopping list generated from new meal table 
        self.shopping_list = meal_plan_to_shopping_list(self.meal_plan_table)
        self.shopping_list += self.db.load_extra_items()
        set_shopping_list(self.shopping_list, self.extra_items, self.tab_widget.widget(SHOPPING_LIST).shopping_list)
        set_shopping_list(self.shopping_list, self.extra_items, self.tab_widget.widget(DASHBOARD).shopping_list_tree)


    def item_checked_off_shopping_list(self) -> None:
        ...


if __name__ == "__main__":
    app = QApplication([])

    if sys.argv[-1] == 'test':
        window = MainWindow(True)
    else:
        window = MainWindow(False)

    window.show()
    sys.exit(app.exec())
