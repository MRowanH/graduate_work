# Dashboard.py
#
# widget class for the dashboard
from PySide6.QtWidgets import QWidget, QTreeWidgetItem,QTableWidgetItem
import PySide6.QtCore as QtCore
from ui.ui_Dashboard import Ui_Dashboard
from common import *
from Inventory import *
class Dashboard(QWidget, Ui_Dashboard):
    def __init__(self, parent: QWidget = None) -> None:
        QWidget.__init__(self)
        self.setupUi(self)

        self.parent = parent

        self.recipe_tree.hideColumn(ID_INDEX)
        self.meal_plan_tree.hideColumn(ID_INDEX)

        init_recipe_tree(self.parent.recipe_table, self.recipe_tree)
        init_recipe_tree(self.parent.meal_plan_table, self.meal_plan_tree)

        self.recipe_tree.itemClicked.connect(self.item_clicked)
        self.meal_plan_tree.itemClicked.connect(self.item_clicked)
    def update_inventory_dashboard(self):
        # l=get_current_item()
        l=get_inventory_from_database()
        print(f" inventory dashboar:{l}")
        for i in l:
            row = self.tableWidget.rowCount()
            self.inventory_table.insertRow(row)
            text1 = str(i)
            newItem = QTableWidgetItem(text1)
            # put the new QTableWidgetItem object to the empty cell
            self.inventory_table.setItem(row, 0, newItem)



    #
    # when user selected the checkbox column of either the meal plan or the recipe tree, update structures
    def item_clicked(self, item, col):
        if col == SELECT_INDEX:
            self.parent.recipe_item_selection_changed(int(item.text(ID_INDEX)))

    
    #
    # update this widgets structures
    # NOTE: if we want more functionality in the future regarding 
    def my_update(self, recipe_id: int):
        update_tree_widgets(self, recipe_id)