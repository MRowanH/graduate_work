from PySide6.QtWidgets import QWidget, QListWidgetItem, QListWidget, QTextBrowser
from ui.ui_RecipeBookGeneric import Ui_RecipeBookGenericWidget
from common import *

class RecipeBookGeneric(QWidget, Ui_RecipeBookGenericWidget):
    def __init__(self, parent: QWidget = None, book_id=None) -> None:
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.parent = parent
        self.book_id = book_id
        
        # Get recipes in the book
        self.curr_idx = None
        self.recipes = {}
        self.items = {}
        if self.book_id is not None:
            self.init_recipe_list()
        
        # Connect actions
        self.recipes_list.itemClicked.connect(self.recipe_clicked)
        self.add_to_meal_plan.clicked.connect(self.add_to_meal_plan_clicked)
        self.remove_recipe.clicked.connect(self.remove_recipe_from_book)
        self.delete_book.clicked.connect(self.delete_book_call)
    
    # Initializes recipe list
    def init_recipe_list(self):
        self.name = self.parent.parent.recipe_books[self.book_id].name
        for r in self.parent.parent.recipe_books[self.book_id].recipe_list:
            self.recipes.update({r: self.parent.parent.recipe_table[r]})
            list_item = QListWidgetItem(self.recipes[r].name, self.recipes_list)
            
    def update_recipe_list(self):
        self.recipes_list.clear()
        self.init_recipe_list()
    
    # Displays text of recipe selected
    def recipe_clicked(self, item):
        # print(item.text(), "\t")
        self.curr_idx = get_id_of_recipe(self.parent.parent.recipe_table, item.text())
        
        recipe = self.parent.parent.recipe_table[self.curr_idx]
        text = recipe.name + "\n\nServes: " + str(recipe.serves) + "\n\nIngredients: \n\n"
        for i in recipe.ingredient_list:
            text += i.name + "   " + str(i.quantity) + "   " + i.unit + "\n"
        text += "\nInstructions:\n\n" + recipe.instructions
        
        self.recipe_view.setPlainText(text)

        if recipe.id in self.parent.parent.meal_plan_table:
            self.add_to_meal_plan.setChecked(True)
        else:
            self.add_to_meal_plan.setChecked(False)
            
    # Remove current recipe from recipe book
    def remove_recipe_from_book(self):
        
        # Update master recipe list
        if self.curr_idx is not None:
            self.parent.parent.recipe_books[self.book_id].recipe_list.remove(self.curr_idx)
            
            # Update database
            self.parent.parent.db.remove_recipe_from_book(self.book_id, self.curr_idx)
            
            # Update GUI and index
            del self.recipes[self.curr_idx]
            self.recipes_list.takeItem(self.recipes_list.row(self.recipes_list.currentItem()))
            try:
                self.recipe_clicked(self.recipes_list.currentItem())
                if self.parent.parent.recipe_table[self.curr_idx].id in self.parent.parent.meal_plan_table:
                    self.add_to_meal_plan.setChecked(True)
                else:
                    self.add_to_meal_plan.setChecked(False)
            except:
                self.curr_idx = None
                self.recipe_view.setPlainText("")
                self.add_to_meal_plan.setChecked(False)

    # Updates master meal plan
    def add_to_meal_plan_clicked(self):
        curr_item = self.recipes_list.currentItem().text()
        idx = get_id_of_recipe(self.parent.parent.recipe_table, curr_item)
        recipe = self.parent.parent.recipe_table[idx]
        self.parent.parent.recipe_item_selection_changed(recipe.id)

    def delete_book_call(self):
        self.parent.delete_book_by_id(self.book_id)