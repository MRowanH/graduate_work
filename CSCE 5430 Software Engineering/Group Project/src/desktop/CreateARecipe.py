from PySide6.QtWidgets import QWidget, QTableWidget, QTableWidgetItem
from ui.ui_CreateARecipe import Ui_CreateARecipeWidget
from common import *

class CreateARecipe(QWidget, Ui_CreateARecipeWidget):
    
    def __init__(self, parent: QWidget = None) -> None:
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.parent = parent
        
        # Public/private combo box
        self.public_private_combo.addItems(["Public", "Private"])
        
        # Ingredients input
        self.ingredients_input.setColumnCount(3)
        self.ingredients_input.setRowCount(1)
        self.num_rows = 1
        self.ingredients_input.setHorizontalHeaderLabels(["Name", "Quantity", "Type"])
        self.ingredients_input.cellChanged.connect(self.ingredients_changed)
        
        # Connect actions
        self.commit_button.clicked.connect(self.commit_recipe)

    def ingredients_changed(self):
        # Add row to ingredients table if there is an ingredient name in the first column
        row = self.ingredients_input.currentRow()
        col = self.ingredients_input.currentColumn()
        if row == self.num_rows - 1 and col == 0:
            self.ingredients_input.insertRow(self.num_rows)
            self.num_rows += 1

    def commit_recipe(self):
        # Commit values on page to ingredients list and database
        
        # Get title
        title = self.title_input.text()
        self.title_input.clear()
        
        # Get public/private
        pub_pri = self.public_private_combo.currentText()
        if pub_pri == "Public":
            pub_pri = 1 # 1 for public
        else:
            pub_pri = 0 # 0 for private
            
        # Get number of servings
        serves = self.serves_input.text()
        self.serves_input.clear()
        try:
            serves = int(serves)
        except:
            serves = -1
        
        # Get ingredients
        ingredients = []
        for i in range(self.num_rows - 1):
            name = self.ingredients_input.item(i, 0).text()
            quan = self.ingredients_input.item(i, 1).text()
            unit = self.ingredients_input.item(i, 2).text()
            ingredients.append(Ingredient(name, quan, unit))
        self.ingredients_input.clearContents()
        self.ingredients_input.setRowCount(1)
        self.num_rows = 1
        
        # Get instructions
        instructions = self.instructions_input.toPlainText()
        self.instructions_input.clear()
        
        r_new = Recipe(len(self.parent.recipe_table) + 1, 
                       title,
                       ingredients,
                       serves, 
                       instructions, 
                       pub_pri, 
                       CURR_USER.id, 
                       []
                       )
        r_id = self.parent.db.add_recipe(r_new)
        r_new.id = r_id
        self.parent.recipe_table.update({r_id: r_new})