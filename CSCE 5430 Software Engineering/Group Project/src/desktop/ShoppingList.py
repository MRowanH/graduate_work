# ShoppingList.py
#
# contains class definitions for the 

from PySide6.QtWidgets import QWidget, QTreeWidgetItem
from ui.ui_ShoppingList import Ui_ShoppingListWidget
from ui.ui_AddNewForm import Ui_AddNewForm
import PySide6.QtCore as QtCore
from common import *

lst = []

class AddNewForm(QWidget, Ui_AddNewForm):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self)
        self.setupUi(self)
        self.parent = parent


class ShoppingList(QWidget, Ui_ShoppingListWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.parent = parent
        self.form = None  # NOTE: if we ever add another 'form' to this page, we should change this name
        self.db_item_buffer = []  # keep these to push to the database when we are done adding things to the menu
        self.column_edit = 0

        self.add_button.clicked.connect(self.on_add_clicked)
        self.remove_button.clicked.connect(self.on_remove_clicked)
        self.shopping_list.itemClicked.connect(self.on_shopping_list_item_clicked)
        #self.update_inventory_button.clicked.connect(self.on_update_clicked)

    def on_shopping_list_item_clicked(self, item, col):
        if col == 3:  # 3 indicates purchased
            item_purchased(item)

    def on_add_clicked(self):
        self.form = AddNewForm(self)
        self.form.add_another_button.clicked.connect(self.add_and_continue)
        self.form.finish_button.clicked.connect(self.finish)
        self.form.show()

    
    def on_remove_clicked(self):
        curr_item = self.shopping_list.currentItem()
        if curr_item.flags() & QtCore.Qt.ItemIsEditable == QtCore.Qt.ItemIsEditable:  # only custom items are editable
            name = curr_item.text(0)
            quantity = curr_item.text(1)
            unit = curr_item.text(2)

            self.shopping_list.takeTopLevelItem(self.shopping_list.indexOfTopLevelItem(curr_item))
            self.parent.db.rem_from_extra_items(name, quantity, unit)


    def add_and_continue(self):
        name = self.form.name.text()
        quantity = self.form.quantity.text()
        unit = self.form.unit.text()

        # check input
        if name == "" or quantity == "" or unit == "":
            self.form.status_label.setText("Bad entry!")
            return
        
        # add to db buffer
        self.db_item_buffer.append((name, quantity, unit))
        self.form.status_label.setText("Sucess!")

        # add to the list widget
        new_item = QTreeWidgetItem(self.shopping_list, [name, quantity, unit])
        new_item.setFlags(new_item.flags() | QtCore.Qt.ItemIsEditable)
        self.shopping_list.addTopLevelItem(new_item)
        self.shopping_list.editItem(new_item)

        # reset
        self.form.name.setText("")
        self.form.quantity.setText("")
        self.form.unit.setText("")

    
    def finish(self):
        # push to add to the database
        name = self.form.name.text()
        quantity = self.form.quantity.text()
        unit = self.form.unit.text()

        if self.db_item_buffer == [] or self.db_item_buffer[-1] == (name, quantity, unit):
            self.form.close()
        elif name != "" and quantity != "" and unit != "":
            self.db_item_buffer.append((name, quantity, unit))

        for name, quantity, unit in self.db_item_buffer:
            self.parent.db.add_to_extra_items(name, quantity, unit)

        self.form.close()
