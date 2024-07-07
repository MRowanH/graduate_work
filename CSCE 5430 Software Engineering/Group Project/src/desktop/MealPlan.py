# MealPlanWidget.py
#
# Widget for the meal plan view
# NOTE: this entire widget might just be useless... all of its functionality is contained in the dash board and its presence *sort of* 
# pollutes the codebase


from PySide6.QtWidgets import QWidget, QTreeWidgetItem
from ui.ui_MealPlan import Ui_MealPlanWidget
from common import *

class MealPlan(QWidget, Ui_MealPlanWidget):
    def __init__(self, parent: QWidget = None) -> None:
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.parent = parent

        self.recipe_tree.hideColumn(ID_INDEX)
        self.meal_plan_tree.hideColumn(ID_INDEX)

        init_recipe_tree(self.parent.recipe_table, self.recipe_tree)
        init_recipe_tree(self.parent.meal_plan_table, self.meal_plan_tree)

        self.recipe_tree.itemClicked.connect(self.item_clicked)
        self.meal_plan_tree.itemClicked.connect(self.item_clicked)


    #
    # when user clicked on the checkbox column, update the meal plan and recipe table accordingly
    def item_clicked(self, item: QTreeWidgetItem, col: int) -> None:
        if col == SELECT_INDEX:
            self.parent.recipe_item_selection_changed(int(item.text(ID_INDEX)))

    
    # 
    # just update the structures as appropriate for this widget - access the parent widget for necessary information
    # update is a function for qwidget that we don't want to override so we call this my_update()
    # @param recipe_id - the id of the recipe that is causing update (either selected or deselected
    # NOTE: in the future, should there be other things to update that do not pertian to selecting or deselecting a recipe, we can make 
    #       the recipe ID an optional parameter and have this update do different tasks based on the parameters
    def my_update(self, recipe_id: int):
        update_tree_widgets(self, recipe_id)
