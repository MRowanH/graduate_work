-- Insert Users
INSERT INTO Users(username, password)
VALUES ("default", "pass0");

INSERT INTO Users (username, password)
VALUES ("Mica", "pass1");

INSERT INTO Users (username, password)
VALUES ("Brice", "pass2");

INSERT INTO Users (username, password)
VALUES ("Nestor", "pass3");

INSERT INTO Users (username, password)
VALUES ("Mustafa", "pass4");

INSERT INTO Users (username, password)
VALUES ("Tam", "pass5");

INSERT INTO Users (username, password)
VALUES ("Nikhil", "pass6");

INSERT INTO Users (username, password)
VALUES ("Vandana", "pass7");

INSERT INTO Users (username, password)
VALUES ("Naveen", "pass8");

-- Insert Recipes
INSERT INTO Recipes (userID, publicly_available, serves, recipe_name, recipe)
VALUES (1, 1, 4, "Carmelized Onion Chicken", "Sprinkle chicken with salt and pepper. Heat oil in a large nonstick skillet over medium-high heat. Add onion, and sauté 2 minutes. Add chicken to pan; sauté 8 minutes or until chicken is done. Remove onion and chicken from pan. Add jam and remaining ingredients to pan; cook 2 minutes, stirring constantly with a whisk. Return chicken mixture to pan; cook 4 minutes, stirring occasionally.");

INSERT INTO Recipes (userID, publicly_available, serves, recipe_name, recipe)
VALUES (1, 1, 4, "Chicken with Honey-Beer Sauce", "1. Heat a large skillet over medium-high heat. Add oil to pan; swirl to coat. Sprinkle chicken evenly with pepper and salt. Add chicken to pan; sauté 6 minutes on each side or until done. Remove chicken from pan; keep warm. Add shallots to pan; cook 1 minute or until translucent. Combine beer and next 3 ingredients (through honey) in a small bowl; stir with a whisk. Add beer mixture to pan; bring to a boil, scraping pan to loosen browned bits. Cook 3 minutes or until liquid is reduced to 1/2 cup. Return chicken to pan; turn to coat with sauce. Sprinkle evenly with parsley.");

INSERT INTO Recipes (userID, publicly_available, serves, recipe_name, recipe)
VALUES (1, 0, 4, "Chicken and Mushrooms in Garlic White Wine Sauce", "Cook noodles according to package directions, omitting salt and fat. Drain and keep warm. Cut chicken into 1-inch pieces. Place chicken breast halves in a shallow dish. Combine 1 tablespoon flour, 1/4 teaspoon salt, and 1/8 teaspoon pepper, stirring well with a whisk. Sprinkle flour mixture over chicken; toss to coat. Heat 1 tablespoon oil in a large nonstick skillet over medium-high heat. Add chicken to pan; sauté 4 minutes or until browned. Remove chicken from pan. Add remaining 1 tablespoon oil to pan. Add garlic, tarragon, and mushrooms to pan; sauté for 3 minutes or until liquid evaporates and mushrooms darken. Add white wine to pan; cook 1 minute. Stir in remaining 1 tablespoon flour; cook 1 minute, stirring constantly. Stir in broth, remaining 1/4 teaspoon salt, and remaining 1/8 teaspoon pepper; cook 1 minute or until slightly thick, stirring frequently. Return chicken to the pan. Cover and simmer 2 minutes. Uncover; cook 1 minute or until chicken is done. Stir in noodles; cook 1 minute or until thoroughly heated. Place about 1 1/2 cups chicken mixture on each of 4 plates; top each serving with 1 tablespoon cheese.");

INSERT INTO Recipes (userID, publicly_available, serves, recipe_name, recipe)
VALUES (2, 1, 4, "Crisp-Crusted Catfish", "Preheat oven to 425°. Combine the dressing and egg whites in a small bowl, and stir well with a whisk. Combine the cornmeal, cheese, flour, pepper, and salt in a shallow dish. Dip fish in egg white mixture; dredge in cornmeal mixture. Place fish on a baking sheet coated with cooking spray; bake at 425° for 12 minutes on each side or until lightly browned and fish flakes easily when tested with a fork. Serve with lemon wedges.");

-- Insert Ingredients
INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (1, "chicken breast", 1, "lb");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (1, "salt", 0.5, "tsp");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (1, "black pepper", 0.25, "tsp");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (1, "olive oil", 1, "tsp");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (1, "onion, sliced", 0.5, "cup");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (1, "raspberry jam, seedless", 0.5, "cup");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (1, "vinegar, red wine", 1, "tbsp");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (1, "soy sauce", 1, "tbsp");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (1, "ginger, minced", 1, "tsp");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (1, "rosemary, dried", 0.5, "tsp");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (2, "oil, canola", 2, "tsp");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (2, "chicken breast", 24, "oz");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (2, "black pepper", 0.25, "tsp");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (2, "salt", 0125, "tsp");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (2, "shallots, sliced", 3, "tbsp");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (2, "beer", 0.5, "cup");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (2, "soy sauce", 2, "tbsp");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (2, "dijon mustard", 1, "tbsp");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (2, "honey", 1, "tbsp");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (2, "parsely, fresh", 12, "tbsp");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (3, "egg noodles, uncooked", 4, "oz");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (3, "chicken breast", 1, "lb");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (3, "flour, all-purpose", 2, "tbsp");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (3, "salt", 0.5, "tsp");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (3, "black pepper", 0.25, "tsp");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (3, "olive oil", 2, "tbsp");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (3, "garlic, minced", 1, "tbsp");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (3, "mushrooms", 8, "oz");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (3, "wine, dry white", 0.5, "cup");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (3, "broth, chicken", 0.5, "cup");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (3, "tarragon, fresh", 1, "tsp");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (3, "cheese, parmesean", 0.25, "cup");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (4, "ranch dressing", 2, "tbsp");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (4, "egg whites", 2, "egg whites");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (4, "cornmeal, yellow", 6, "tbsp");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (4, "cheese, parmesean", 0.25, "cup");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (4, "flour, all-purpose", 2, "tbsp");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (4, "red pepper", 0.25, "tsp");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (4, "salt", 0.125, "tsp");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (4, "catfish", 24, "oz");

INSERT INTO Ingredients (recipeID, ingredient, quantity, unit)
VALUES (4, "lemon, wedges", 4, "wedges");

-- Insert Extra Items
INSERT INTO ExtraItems (userID, item, quantity, unit)
VALUES (1, "windex", 1, "bottle");

INSERT INTO ExtraItems (userID, item, quantity, unit)
VALUES (1, "eggs", 12, "eggs");

INSERT INTO ExtraItems (userID, item, quantity, unit)
VALUES (2, "ice cream", 1, "carton");

-- Insert Innventory
/*INSERT INTO Inventory (userID, ingredientID)
VALUES (1, 1);

INSERT INTO Inventory (userID, ingredientID)
VALUES (1, 3);

INSERT INTO Inventory (userID, ingredientID)
VALUES (1, 5);

INSERT INTO Inventory (userID, ingredientID)
VALUES (1, 10);

INSERT INTO Inventory (userID, ingredientID)
VALUES (1, 11);

INSERT INTO Inventory (userID, ingredientID)
VALUES (1, 12);

INSERT INTO Inventory (userID, ingredientID)
VALUES (1, 3);

INSERT INTO Inventory (userID, ingredientID)
VALUES (2, 5);*/

-- Insert Meal Plans
INSERT INTO MealPlan (userID, recipeID)
VALUES (1, 1);

INSERT INTO MealPlan (userID, recipeID)
VALUES (1, 2);

INSERT INTO MealPlan (userID, recipeID)
VALUES (1, 3);

INSERT INTO MealPlan (userID, recipeID)
VALUES (2, 1);

INSERT INTO MealPlan (userID, recipeID)
VALUES (2, 3);

INSERT INTO UserBooks (userID, name)
VALUES (1, "Test");

INSERT INTO BookRecipe (bookID, recipeID)
VALUES (1, 1);

INSERT INTO BookRecipe (bookID, recipeID)
VALUES(1, 2);

SELECT * FROM Inventory;