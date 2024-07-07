:: turn off echo
@echo off

:: compile the ui files
pyside6-uic ui/mainwindow.ui > ui/ui_mainwindow.py
pyside6-uic ui/MealPlanWidget.ui > ui/ui_MealPlan.py
pyside6-uic ui/InventoryWidget.ui > ui/ui_Inventory.py
pyside6-uic ui/PublicRecipesWidget.ui > ui/ui_PublicRecipes.py
pyside6-uic ui/ShoppingListWidget.ui > ui/ui_ShoppingList.py
pyside6-uic ui/DashboardWidget.ui > ui/ui_Dashboard.py
pyside6-uic ui/CreateARecipeWidget.ui > ui/ui_CreateARecipe.py
pyside6-uic ui/PrivateRecipesWidget.ui > ui/ui_PrivateRecipes.py
pyside6-uic ui/LoginWidget.ui > ui/ui_Login.py
pyside6-uic ui/AddNewForm.ui > ui/ui_AddNewForm.py
pyside6-uic ui/RecipeBookBrowserWidget.ui > ui/ui_RecipeBookBrowser.py
pyside6-uic ui/RecipeBookGenericWidget.ui > ui/ui_RecipeBookGeneric.py
pyside6-uic ui/CreateABookWidget.ui > ui/ui_CreateABook.py

:: run
python -u mainwindow.py