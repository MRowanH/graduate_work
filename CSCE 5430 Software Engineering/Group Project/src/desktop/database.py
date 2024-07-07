# Class containing all database handlers including:
#     connecting
#     queries and their responses
#     database updates
# 
# The information for the database is:
#     Host: sql5.freesqldatabase.com
#     Database name and user: sql5445221
#     Database password: 27vqdQxKTN
# 
# The table schema for the database is:
#     ExtraItems
#          ('userID', 'int(11)', 'NO', 'PRI', '0', '')
#          ('item', 'varchar(128)', 'NO', 'PRI', '', '')
#          ('quantity', 'tinyint(4)', 'YES', '', None, '')
#          ('unit', 'varchar(32)', 'YES', '', None, '')
#     Ingredients
#          ('id', 'int(11)', 'NO', 'PRI', None, 'auto_increment')
#          ('recipeID', 'int(11)', 'NO', 'MUL', None, '')
#          ('ingredient', 'varchar(128)', 'NO', '', None, '')
#          ('quantity', 'tinyint(4)', 'NO', '', None, '')
#          ('unit', 'varchar(32)', 'YES', '', '---', '')
#     Inventory
#          ('id', 'int(11)', 'NO', 'PRI', None, 'auto_increment')
#          ('ingredient', 'varchar(128)', 'NO', '', None, '')
#          ('quantity', 'tinyint(4)', 'NO', '', None, '')
#          ('unit', 'varchar(32)', 'YES', '', '---', '')
#     MealPlan
#          ('userID', 'int(11)', 'NO', 'MUL', None, '')
#          ('recipeID', 'int(11)', 'NO', 'MUL', None, '')
#     Recipes
#          ('id', 'int(11)', 'NO', 'PRI', None, 'auto_increment')
#          ('userID', 'int(11)', 'NO', 'MUL', None, '')
#          ('publicly_available', 'tinyint(1)', 'YES', '', '0', '')
#          ('recipe_name', 'varchar(32)', 'NO', '', None, '')
#          ('recipe', 'mediumtext', 'NO', '', None, '')
#     Users
#          ('id', 'int(11)', 'NO', 'PRI', None, 'auto_increment')
#          ('username', 'varchar(32)', 'NO', '', None, '')
#          ('password', 'varchar(32)', 'NO', '', None, '')

# Imports ---------------------------------------------------------------------
import sys
import mysql.connector
from common import *

# Class -----------------------------------------------------------------------
class DBHandler():
    def __init__(self):
        # Initialize database connection
        
        # Connect to databse
        self.db = mysql.connector.connect(host="sql5.freesqldatabase.com", 
                                          database="sql5445221", 
                                          user="sql5445221", 
                                          password="27vqdQxKTN"
                                          )
        self.cursor = self.db.cursor()
        
        # TEST
        # self.test()
        self.load_recipe_list()

    # Code for adding user data to database -----------------------------------

    def get_all_users(self):
        query = "SELECT * from Users"
        vals = self.cursor.execute(query)
        result = self.cursor.fetchall()
        for user in result:
            print(f'user info: {user}')

    def add_user(self, username, password):
        query = "INSERT INTO Users (username, password) VALUES (%s, %s)"
        '''
        for field in dir(self.cursor):
            if 'id' in field:
                print(f'id field: {field}')
        '''
        #print(f'Last row id: {self.cursor.lastrowid + 1}')
        # user = User(id, username, password)
        vals = (username, password)
        self.cursor.execute(query, vals)
        self.db.commit()

        vals = self.cursor.execute("SELECT id FROM Users WHERE username = %s", (username, ))
        r_id = self.cursor.fetchall()
        id = r_id[0][0]
        print(f'function add_user: user_id = {id}')
        return User(id, username, password, False)

        #print(f'User id: {user.id}')


    # Push Data to Database ---------------------------------------------------
    
    #
    # addes a recipe to the selected recipes for the current user
    # on success, returns id of recipe it added
    # on failure, returns a -1
    def add_recipe(self, recipe):
        # check duplicate recipe
        check_query = "SELECT * FROM Recipes WHERE recipe_name = %s AND userID = %s"
        vals = (str(recipe.name), str(recipe.owner))
        self.cursor.execute(check_query, vals)
        result = self.cursor.fetchall()
        if len(result) > 0:
            return -1
        
        # Insert new recipe
        query = "INSERT INTO Recipes (userID, publicly_available, recipe_name, recipe) VALUES (%s, %s, %s, %s)"
        vals = (str(recipe.owner), str(recipe.status), recipe.name, recipe.instructions)
        self.cursor.execute(query, vals)
        self.db.commit()
        
        # Get recipe id
        vals = self.cursor.execute("SELECT id FROM Recipes WHERE recipe_name = %s", (recipe.name, ))
        r_id = self.cursor.fetchall()
        r_id = r_id[0][0]
            
        # Insert new ingredients
        query = "INSERT INTO Ingredients (recipeID, ingredient, quantity, unit) VALUES (%s, %s, %s, %s)"
        for i in recipe.ingredient_list:
            vals = (str(r_id), i.name, str(i.quantity), i.unit)
            self.cursor.execute(query, vals)
            self.db.commit()
        
        return r_id

    def add_to_meal_plan(self, recipe_id):
        try:
            query = "INSERT INTO MealPlan (userID, recipeID) VALUES (%s, %s)"
            vals  = (str(CURR_USER.id), str(recipe_id))
            self.cursor.execute(query, vals)
            self.db.commit()
            return True
        except mysql.connector.errors.IntegrityError:
            return False

    def rem_from_meal_plan(self, recipe_id):
        try:
            query = "DELETE FROM MealPlan WHERE userID = %s AND recipeID = %s"
            vals  = (str(CURR_USER.id), str(recipe_id))
            self.cursor.execute(query, vals)
            self.db.commit()
            return True
        except mysql.connector.errors.IntegrityError:
            return False  # NOTE: this should probably catch different errors and return different codes depending on those

    def add_to_extra_items(self, item: str, quantity: str, units: str):
        try:
            query = "INSERT INTO ExtraItems (userID, item, quantity, unit) VALUES (%s, %s, %s, %s)"
            vals = (str(CURR_USER.id), item, quantity, units)
            self.cursor.execute(query, vals)
            self.db.commit()
            return True
        except mysql.connector.errors.IntegrityError:
            return False

    def rem_from_extra_items(self, item, quantity, units):
        try:
            query = "DELETE FROM ExtraItems WHERE userID = %s AND item = %s AND quantity = %s AND unit = %s"
            vals = (str(CURR_USER.id), item, quantity, units)
            self.cursor.execute(query, vals)
            self.db.commit()
            return True
        except mysql.connector.errors.IntegrityError:
            return False
        
    def add_recipe_book(self, name):
        query = "INSERT INTO UserBooks (userID, name) VALUES (%s, %s)"
        vals = (str(CURR_USER.id), name)
        self.cursor.execute(query, vals)
        self.db.commit()
        
        self.cursor.execute("SELECT bookID FROM UserBooks WHERE userID = %s AND name = %s", (str(CURR_USER.id), name))
        b_id = self.cursor.fetchall()
        b_id = b_id[0][0]
        return b_id
    
    def remove_recipe_from_book(self, book_id, recipe_id):
        query = "DELETE FROM BookRecipe WHERE bookID = %s AND recipeID = %s"
        vals = (str(book_id), str(recipe_id))
        self.cursor.execute(query, vals)
        self.db.commit()
    
    def add_to_inventory(self, ingredient):
        query = "INSERT INTO Inventory (userID,ingredient,quantity,unit) VALUES (%s, %s,%s, %s)"
        vals = (CURR_USER.id, ingredient.name, ingredient.quantity, ingredient.unit)
        self.cursor.execute(query, vals)
        self.db.commit()

    def remove_from_inventory(self, ingredient):
        query = "DELETE FROM Inventory WHERE ingredient = %s" #should be done with id instead of name
        vals = ingredient.name
        self.cursor.execute(query, vals)
        self.db.commit()
        
    def add_to_recipe_book(self, book_id, recipe_id):
        query = "INSERT INTO BookRecipe (bookID, recipeID) VALUES (%s, %s)"
        vals = (str(book_id), str(recipe_id))
        self.cursor.execute(query, vals)
        self.db.commit()
        
    def remove_from_recipe_book(self, book_id, recipe_id):
        query = "DELETE FROM BookRecipe WHERE bookID = %s AND recipeID = %s"
        vals = (str(book_id), str(recipe_id))
        self.cursor.execute(query, vals)
        self.db.commit()
        
    def delete_recipe_book(self, book_id, user_id, name):
        query = "DELETE FROM UserBooks WHERE bookID = %s AND userID = %s AND name = %s"
        vals = (str(book_id), str(user_id), name)
        print(query)
        print(vals)
        self.cursor.execute(query, vals)
        self.db.commit()
        
    def rem_recipe(self, recipe, user_id):
        sel_query = "SELECT id FROM Recipes WHERE recipe_name = %s AND userID = %s"
        sel_vals = (recipe.name, str(user_id))
        self.cursor.execute(sel_query, sel_vals)
        recipe_ids_to_delete = [id for id, in self.cursor.fetchall()]  # NOTE: in theory this is length 1 - generalize to handle dups

        for recipe_id in recipe_ids_to_delete:
            query = "DELETE FROM MealPlan WHERE recipeID = %s"
            vals = (recipe_id, )
            self.cursor.execute(query, vals)
            self.db.commit()

            query = "DELETE FROM Ingredients WHERE recipeID = %s"
            vals = (recipe_id, )
            self.cursor.execute(query, vals)
            self.db.commit()

            query = "DELETE FROM Recipes WHERE userID = %s AND id = %s"
            vals = (user_id, recipe_id)
            self.cursor.execute(query, vals)
            self.db.commit()

    def clean_test_entries(self):
        select_query = "SELECT id FROM Recipes WHERE userID = %s"
        self.cursor.execute(select_query, (TEST_USER_ID, ))
        result = self.cursor.fetchall()
        for id, in result:
            ing_query = "DELETE FROM Ingredients WHERE recipeID = %s"
            vals = (str(id), )
            self.cursor.execute(ing_query, vals)
            self.db.commit()

            query = "DELETE FROM MealPlan WHERE recipeID = %s"
            vals = (id, )
            self.cursor.execute(query, vals)
            self.db.commit()

        query = "DELETE FROM Recipes WHERE userID = %s"
        self.cursor.execute(query, (TEST_USER_ID, ))
        self.db.commit()

        query = "DELETE FROM ExtraItems WHERE userID = %s"
        vals = (str(TEST_USER_ID), )
        self.cursor.execute(query, vals)
        self.db.commit()

    # Load Data From Database on Startup --------------------------------------
        
    def load_meal_plan(self, recipe_table: Dict[int, Recipe]) -> Dict[int, Recipe]:
        meal_plan_ids = []
        meal_plan_table : Dict[int, Recipe] = {}

        self.cursor.execute("SELECT * FROM MealPlan WHERE userID = %d" % CURR_USER.id)
        meal_plan_results = self.cursor.fetchall()
        for _, recipe_id in meal_plan_results:
            meal_plan_ids.append(recipe_id)

        for id in meal_plan_ids:
            meal_plan_table[id] = recipe_table[id]
            meal_plan_table[id].selected = True

        return meal_plan_table
    
    def load_inventory(self) -> List[Ingredient]:
        # Load the inventory from the db
        inventory = []
        self.cursor.execute("SELECT * FROM Inventory WHERE userID = %d" % CURR_USER.id)
        results = self.cursor.fetchall()
        # id, userID, ingredient, quan, unit
        for row in results:
            inventory.append(Ingredient(row[2], row[3], row[4]))
        return inventory
    
    def load_recipe_list(self) -> Dict[int, Recipe]:
        # Build recipes list from the db
        recipes = {}
        
        # Get recipes from databse
        self.cursor.execute("SELECT * FROM Recipes")
        results_r = self.cursor.fetchall()
        for rr in results_r:
            
            # Get values from results
            id_r = rr[0]
            owner = rr[1]
            pub_pri = rr[2]
            serves = rr[3]
            title = rr[4]
            instructions = rr[5]
            
            # Convert pub_pri
            # if pub_pri == 0:
            #     pub_pri = "private"
            # else:
            #     pub_pri = "public"
                
            # Get ingredients of recipe
            self.cursor.execute("SELECT * FROM Ingredients WHERE recipeID = %d"%id_r)
            results_i = self.cursor.fetchall()
            ingredient_list = []
            for ri in results_i:
                idx = ri[0]
                ingredient = ri[2]
                quantity = ri[3]
                unit = ri[4]
                ingredient_list.append(Ingredient(ingredient, quantity, unit))
            
            # Update recipe list
            recipes.update({id_r: Recipe(id_r, title, ingredient_list, serves, instructions, pub_pri, owner, [])})
        return recipes

    
    def load_extra_items(self) -> List[Ingredient]:
        self.cursor.execute("SELECT item, quantity, unit FROM ExtraItems WHERE userID=%s" % str(CURR_USER.id))
        query_result = self.cursor.fetchall()
        output = []
        for name, quantity, unit in query_result:
            output.append(Ingredient(name, quantity, unit))
        
        return output
    
    def load_recipe_books(self, recipe_table):
        
        # Get all of user's books from db
        books = {}
        self.cursor.execute("SELECT * FROM UserBooks WHERE userID = %d"%CURR_USER.id)
        results = self.cursor.fetchall()
        for row in results:                     # bookID, userID, name
            books.update({row[0]: row[2]})
            
        # Get all recipes for each book
        for idx in books:
            recipes = []
            name = books[idx]
            self.cursor.execute("SELECT * from BookRecipe WHERE bookID = %d"%idx)
            results = self.cursor.fetchall()
            for row in results:             # bookID, recipeID
                recipes.append(row[1])
                
            # Build dictionary
            books[idx] = Book(idx, name, recipes)
                
        return books

    def verify_user(self, user):
        #self.get_all_users()
        self.cursor.execute("SELECT * FROM Users WHERE username = %s", (user.name,))
        result = self.cursor.fetchone()
        #print(f'Result type: {type(result)}, result value: {result}')

        if result is None:
            return None
        elif self.cursor.rowcount != 1:
            return None
        else:
            user.id = result[0]
            return user      #User: id, username, password

    def verify_password(self, user):
        self.cursor.execute("SELECT * FROM Users WHERE username = %s", (user.name,))
        result = self.cursor.fetchone()
        password= result[2]
        # print(f'verify password function - database password: {password}, user entered password: {user.password}')
        if user.password != password:
            return False
        else:
            return True
        #return id

    # TEST --------------------------------------------------------------------
    
    def each_table(self, table):
        print("%s:"%table)
        
        print("Columns:")
        self.cursor.execute("SHOW COLUMNS FROM %s"%table)
        r = self.cursor.fetchall()
        for x in r:
            print("\t", x)
        
        print("Values")
        self.cursor.execute("SELECT * FROM %s"%table)
        r = self.cursor.fetchall()
        print("Len: ", len(r))
        for x in r:
            print("\t", x)
        print()
    
    def test(self):
        
        # Get table names
        self.cursor.execute("Show tables;")
        r = self.cursor.fetchall()
        print("Tables:")
        for x in r:
            print(x)
        print()
        
        # Get column names and table values
        tables = ["ExtraItems", "Ingredients", "Inventory", "MealPlan", "Recipes", "Users"]
        for t in tables:
            self.each_table(t)