from PySide6.QtWidgets import QApplication, QMainWindow

from PySide6.QtWidgets import QWidget, QListWidgetItem, QListWidget, QTextBrowser, QStackedWidget
from ui.ui_RecipeBookBrowser import Ui_RecipeBookBrowserWidget
from common import *
from RecipeBookGeneric import RecipeBookGeneric
from CreateABook import CreateABook

class RecipeBookBrowser(QWidget, Ui_RecipeBookBrowserWidget):
    def __init__(self, parent: QWidget = None) -> None:
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.parent = parent
        
        # Remove auto-generated tabs
        self.browser.removeTab(0)
        self.browser.removeTab(0)
            
        # Add create a book page
        self.idxs = {}
        self.book_pages = {}
        CREATE = self.browser.addTab(CreateABook(self), "Create A Recipe Book")
        self.idxs.update({CREATE: "Create A Recipe Book"})
        
        # Build books list
        self.init_books_list()
        
    def drop_books(self):
        while self.browser.count() > 1:
            self.browser.removeTab(self.browser.count()-1)
            
    def delete_book_by_id(self, book_id):
        for b in self.parent.recipe_books:
            book = self.parent.recipe_books[b]
            if book.id == book_id:
                for idx in self.idxs:
                    if self.idxs[idx] == book.name:
                        self.browser.removeTab(idx)
                        del self.parent.recipe_books[b]
                        self.parent.tab_widget.widget(PUBLIC_RECIPES).update_recipe_books_check_boxes()
                        self.parent.tab_widget.widget(MY_RECIPES).update_recipe_books_check_boxes()
                        self.parent.db.delete_recipe_book(b, CURR_USER.id, book.name)
                        return 0
        
    def init_books_list(self):
        
        # Get user-created books
        for b in self.parent.recipe_books:
            book = self.parent.recipe_books[b]
            self.book_pages.update({book.name: RecipeBookGeneric(self, book_id=b)})
            IDX = self.browser.addTab(self.book_pages[book.name], book.name)
            self.idxs.update({IDX: book.name})