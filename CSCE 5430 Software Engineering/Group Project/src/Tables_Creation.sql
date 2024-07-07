DROP TABLE ExtraItems;
DROP TABLE Inventory;
DROP TABLE MealPlan;
DROP TABLE Ingredients;
DROP TABLE Recipes;
DROP TABLE BookRecipe;
DROP TABLE UserBooks;
DROP TABLE Users;

CREATE TABLE Users (
	id int AUTO_INCREMENT PRIMARY KEY,
	username varchar(32) NOT NULL,
	password varchar(32) NOT NULL
);

CREATE TABLE Recipes (
	id int AUTO_INCREMENT PRIMARY KEY,
	userID int NOT NULL,
	publicly_available boolean DEFAULT 0,
    	serves int NOT NULL, 
	recipe_name varchar(32) NOT NULL,
	recipe text NOT NULL,
    FOREIGN KEY (userID)
    	REFERENCES Users(id)
);

CREATE TABLE Ingredients(
	id int AUTO_INCREMENT PRIMARY KEY,
	recipeID int NOT NULL,
	ingredient varchar(128) NOT NULL,
	quantity float NOT NULL,
	unit varchar(32) DEFAULT '---',
    FOREIGN KEY (recipeID)
    	REFERENCES Recipes(id)
);

CREATE TABLE Inventory (
   	id int AUTO_INCREMENT PRIMARY KEY,
	userID int NOT NULL,
	ingredient varchar(128) NOT NULL,
	quantity float NOT NULL,
	unit varchar(32) DEFAULT '---',
    FOREIGN KEY (userID)
    	REFERENCES Users(id)
);

CREATE TABLE MealPlan (
	userID int NOT NULL,
	recipeID int NOT NULL,
	FOREIGN KEY (userID)
    	REFERENCES Users(id),
    FOREIGN KEY (recipeID)
    	REFERENCES Recipes(id)
);

CREATE TABLE ExtraItems (
	userID int,
	item varchar(128),
	quantity float,
	unit varchar(32),
	PRIMARY KEY (userID, item),
    FOREIGN KEY (userID)
    	REFERENCES Users(id)
);

CREATE TABLE UserBooks (
	bookID int AUTO_INCREMENT,
    userID int NOT NULL, 
    name varchar(255) NOT NULL,
    PRIMARY KEY (bookID), 
    FOREIGN KEY (userID)
		REFERENCES Users(id)
);

CREATE TABLE BookRecipe (
	bookID int NOT NULL,
    recipeID int NOT NULL,
    PRIMARY KEY (bookID, recipeID), 
    FOREIGN KEY (bookID)
		REFERENCES UserBooks(bookID),
	FOREIGN KEY (recipeID)
		REFERENCES Recipes(id)
);