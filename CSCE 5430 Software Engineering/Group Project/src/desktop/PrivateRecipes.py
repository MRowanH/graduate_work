from PySide6.QtWidgets import QWidget, QListWidgetItem, QListWidget, QTextBrowser, QVBoxLayout, QCheckBox
from ui.ui_PrivateRecipes import Ui_PrivateRecipesWidget
from common import *

class PrivateRecipes(QWidget, Ui_PrivateRecipesWidget):
    def __init__(self, parent: QWidget = None) -> None:
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.parent = parent
        
        # Recipe list
        self.curr_idx = None
        self.init_private_recipes_list()
        
        # Recipe books
        self.init_recipe_books_check_boxes()
        
        # Connect actions
        self.recipes_list.itemClicked.connect(self.recipe_clicked)
        self.add_to_meal_plan.clicked.connect(self.add_to_meal_plan_clicked)
        for rbook in self.rbooks_cboxes:
            self.rbooks_cboxes[rbook].clicked.connect(self.update_recipe_book)
        
    # Initilizes private recipes
    def init_private_recipes_list(self):
        for _, recipe in self.parent.recipe_table.items():   
            if recipe.owner == CURR_USER.id:
                list_item = QListWidgetItem(recipe.name, self.recipes_list)
                
    def init_recipe_books_check_boxes(self):
        self.vbox = QVBoxLayout(self)
        self.recipe_books_cboxes.setLayout(self.vbox)
        self.rbooks_cboxes = {}
        for b in self.parent.recipe_books:
            name = self.parent.recipe_books[b].name
            self.rbooks_cboxes.update({name: QCheckBox(name, self)})
            self.vbox.addWidget(self.rbooks_cboxes[name])
        # self.recipe_books_cboxes.setLayout(self.vbox)
        
    def update_recipe_books_check_boxes(self):
        
        # Add any unknown books
        for b in self.parent.recipe_books:
            name = self.parent.recipe_books[b].name
            if name not in self.rbooks_cboxes:
                self.rbooks_cboxes.update({name: QCheckBox(name, self)})
                self.vbox.addWidget(self.rbooks_cboxes[name])
                
        # Remove any extra books
        drops = []
        for book in self.rbooks_cboxes:
            flag = False
            for b in self.parent.recipe_books:
                if self.parent.recipe_books[b].name == book:
                    flag = True
            if flag is False:
                drops.append(book)
        for b in drops:
            self.vbox.removeWidget(self.rbooks_cboxes[b])
            self.rbooks_cboxes[b].deleteLater()
            del self.rbooks_cboxes[b]
    
    # Shows text of recipe selected.
    def recipe_clicked(self, item):
        
        # Get recipe's id
        self.curr_idx = get_id_of_recipe(self.parent.recipe_table, item.text())
        
        # Get recipe's text
        recipe = self.parent.recipe_table[self.curr_idx]
        text = recipe.name + "\n\nServes: " + str(recipe.serves) + "\n\nIngredients: \n\n"
        for i in recipe.ingredient_list:
            text += i.name + "   " + str(i.quantity) + "   " + i.unit + "\n"
        text += "\nInstructions:\n\n" + recipe.instructions
        
        # Display
        self.recipe_view.setPlainText(text)
        
        # Set meal plan check box
        if recipe.id in self.parent.meal_plan_table:
            self.add_to_meal_plan.setChecked(True)
        else:
            self.add_to_meal_plan.setChecked(False)
            
        # Set recipe books check boxes
        for b in self.parent.recipe_books:
            if self.curr_idx in self.parent.recipe_books[b].recipe_list:
                self.rbooks_cboxes[self.parent.recipe_books[b].name].setChecked(True)
            else:
                self.rbooks_cboxes[self.parent.recipe_books[b].name].setChecked(False)
            
    # Add recipe to a book
    def update_recipe_book(self):
        id_book = {}
        for rbook in self.parent.recipe_books:
            id_book.update({self.parent.recipe_books[rbook].name: rbook})
        for rbook in self.rbooks_cboxes:
            
            # Add recipe to book
            if self.rbooks_cboxes[rbook].isChecked() is True:
                if self.curr_idx not in self.parent.recipe_books[id_book[rbook]].recipe_list:
                    self.parent.recipe_books[id_book[rbook]].recipe_list.append(self.curr_idx)
                    self.parent.tab_widget.widget(BOOKS).book_pages[rbook].update_recipe_list()
                    self.parent.db.add_to_recipe_book(id_book[rbook], self.curr_idx)
                
            # Remove recipe from book
            else:
                if self.curr_idx in self.parent.recipe_books[id_book[rbook]].recipe_list:
                    self.parent.recipe_books[id_book[rbook]].recipe_list.remove(self.curr_idx)
                    self.parent.tab_widget.widget(BOOKS).book_pages[rbook].update_recipe_list()
                    self.parent.db.remove_from_recipe_book(id_book[rbook], self.curr_idx)
        
    # Updates the master meal plan
    def add_to_meal_plan_clicked(self):
        curr_item = self.recipes_list.currentItem().text()
        idx = get_id_of_recipe(self.parent.recipe_table, curr_item)
        recipe = self.parent.recipe_table[idx]
        self.parent.recipe_item_selection_changed(recipe.id)
