from PySide6.QtWidgets import QWidget, QTableWidgetItem
from ui.ui_Inventory import Ui_Inventory
from ShoppingList import *
from database import DBHandler
from common import *
import re
uid=5
class Inventory(QWidget, Ui_Inventory):
    def __init__(self, parent: QWidget):
        QWidget.__init__(self)
        self.parent = parent
        self.setupUi(self)
        self.finallist=[]
        # self.mydb=connect_to_database()  # TODO (tam): there is a database class in database.py that provides db functionality - you should use that rather than opening up two different connections to the database.
        #my code did before database.py was created, so I intergrate now
        self.dbhandle= DBHandler()
        # self.cursor = self.db.cursor()#DBHandler
        # when Add button is clicked, the function insert_button is called
        self.Add_button.clicked.connect(lambda : self.insert_button())
        # when Delete button is clicked, the function remove_button is called
        self.Delete_button.clicked.connect(lambda: self.remove_button())
        # self.Typing_button.clicked.connect(lambda: self.add_typing_item_button())
        s=self.get_all_ingredients()
        # put each item from the set s to listWidget
        for si in s:
            self.listWidget.addItem(si)
        # sort the items  in  listWidget
        self.listWidget.sortItems()
        #get all items in Inventory table on database
        l1=self.get_inventory_from_database()
        for j in l1:
            #count the current row of tableWidget
            row = self.tableWidget.rowCount()
            # insert an empty row to the table
            self.tableWidget.insertRow(row)
            # get the selected item from the listWidget
            text = str(j)
            # set a new QTableWidgetItem object
            # and pass the selected item from the listWidget to a new QTableWidgetItem object
            newItem = QTableWidgetItem(text)
            # put the new QTableWidgetItem object to the empty cell
            self.tableWidget.setItem(row, 0, newItem)


     # the fucntion inserts an item to the tableWidget
    # insert item to the Inventory table on database
    def insert_button(self):
        # l_current = self.get_inventory_from_database()
        l_current=self.get_current_item()
        text1 = str(self.listWidget.currentItem().text())
        # prevent user add one item many times
        if text1 not in l_current:

            #get the the number of rows of the currently table
            row = self.tableWidget.rowCount()
            # column = self.tableWidget.columnCount()
            # insert an empty row to the table
            self.tableWidget.insertRow(row)
            # get the selected item from the listWidget
            text1 = str(self.listWidget.currentItem().text())
            l_current = self.get_inventory_from_database()



            # set a new QTableWidgetItem object
            # and pass the selected item from the listWidget to a new QTableWidgetItem object
            newItem = QTableWidgetItem(str(text1))
            # put the new QTableWidgetItem object to the empty cell
            self.tableWidget.setItem(row, 0,newItem)

            ###################################

            ####################################
            #start to communicate with database
            # mycursor = self.mydb.cursor()# my code did before database.py was created
            mycursor=self.dbhandle.cursor
            # insert item to the Inventory table on database
            sql = "INSERT INTO Inventory (userID,ingredient,quantity,unit) VALUES (%s, %s,%s, %s)"
            val = (1,text1,'','')
            mycursor.execute(sql, val)
            self.dbhandle.db.commit()
            #check the database update or not
            self.get_inventory_from_database()




    # the fucntion remove  an item from the table
    def remove_button(self):
        #get QItemSelectionModel of the selected item which is highligted in the table
        item = self.tableWidget.selectionModel()
        # get the integer value of the row which contains the selected item
        for i in item.selectedIndexes():
            row_i = i.row()
        # start to communicate with database
        # mycursor = self.mydb.cursor()# mycode did before database.py was created
        mycursor = self.dbhandle.cursor
        #get the text from selected cell
        text1=self.tableWidget.item(row_i,0).text()


        # delete a row which contains the selected text in tableWidget
        sql = "DELETE FROM Inventory WHERE ingredient = %s"
        t= (text1,)
        mycursor.execute(sql, t)
        self.dbhandle.db.commit()
        # remove the row  which contains the selected item
        self.tableWidget.removeRow(row_i)
        # check the database update or not
        self.get_inventory_from_database()



    # function gets current items in tableWidget
    def get_current_item(self):
        row = self.tableWidget.rowCount()
        self.finallist = []
        for i in range(0,row):
            item=self.tableWidget.item(i,0).text()
            self.finallist.append(item)
            print(f"the list item in table: {self.finallist}")
        return self.finallist

    #function get the ingredients from Inventory on database
    def get_inventory_from_database(self):
        l1 = []
        # mycursor = self.mydb.cursor()# my code did before database.py was created
        mycursor = self.dbhandle.cursor
        mycursor.execute("SELECT ingredient FROM Inventory")
        my_inventory = mycursor.fetchall()
        for x in my_inventory:
            for j in x:
                l1.append(j)
        # print(f"there are {len(l1)} ingredients from Inventory on database now which include : {l1}")
        return l1

# This fuction gets all ingredients in the table Ingredients on database
    def get_all_ingredients(self):
        # mycursor = self.mydb.cursor()# my code did before database.py was created
        mycursor = self.dbhandle.cursor
        # mycursor.execute("SELECT * FROM Ingredients")
        mycursor.execute("SELECT ingredient FROM Ingredients")
        my_ingredients = mycursor.fetchall()
        l = []
        for ingredient in my_ingredients:
            for i in ingredient:
                l.append(re.sub('[^a-zA-Z0-9 ]', '', i))
        all_ingre = set(l)
        return all_ingre

# This function will get ingredients from shopping list that are bought
    def get_shopping_list_ingredients(self):

        return 1

