from PySide6.QtWidgets import QWidget, QTableWidget, QTableWidgetItem
from ui.ui_CreateABook import Ui_CreateABookWidget
from common import *
from RecipeBookGeneric import RecipeBookGeneric

class CreateABook(QWidget, Ui_CreateABookWidget):
    
    def __init__(self, parent: QWidget = None) -> None:
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.parent = parent
        
        # Connect actions
        self.commit_button.clicked.connect(self.commit_book)

    def commit_book(self):
        # Commit values on page to ingredients list and database
        
        # Get title
        title = self.title_input.text().title()
        if title.strip() == "":
            return 1
        self.title_input.clear()
        
        # Update master recipe books list and database
        b_id = self.parent.parent.db.add_recipe_book(title)
        self.parent.parent.recipe_books.update({b_id: Book(b_id, title, [])})
        
        # Update GUI
        self.parent.drop_books()
        self.parent.init_books_list()
        
        # Update public and private recipe book check boxes
        self.parent.parent.tab_widget.widget(PUBLIC_RECIPES).update_recipe_books_check_boxes()
        self.parent.parent.tab_widget.widget(MY_RECIPES).update_recipe_books_check_boxes()