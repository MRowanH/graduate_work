package com.example.dos_8_mobile;

import java.sql.*;
import java.util.ArrayList;

import com.example.dos_8_mobile.Objects.*;

public final class DbConnection {
    private static Connection conn = null;

    private static boolean openConnection() {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver").newInstance();
            conn = DriverManager.getConnection("jdbc:mysql://sql5.freesqldatabase.com/sql5445221", "sql5445221", "27vqdQxKTN");
            return true;
        }
        catch (Exception e) {
            System.out.println(e);
            return false;
        }
    }

    public static boolean authUser(User user) {
        String username = user.getUsername();
        String password = user.getPassword();

        boolean authenticated = false;

        openConnection();

        try{
            String query = "SELECT count(*) FROM Users WHERE username = '?' AND password = '?'";
            PreparedStatement ps = conn.prepareStatement(query);
            ps.setString(1, username);
            ps.setString(2, password);

            ResultSet rs = ps.executeQuery(query);

            authenticated = rs.getInt("count(*)") == 1;

        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }

        closeConnection();

        return authenticated;
    }

    public static ArrayList<Recipe> getRecipes(User user) {
        openConnection();

        ArrayList<Recipe> recipes = new ArrayList<>();

        try{
            String query = "SELECT * FROM Recipes WHERE userID = ?";
            PreparedStatement ps = conn.prepareStatement(query);
            ps.setInt(1, user.getId());

            ResultSet rs = ps.executeQuery(query);

            while(rs.next()) {
                Recipe recipe = new Recipe(rs.getInt("id"), rs.getInt("userID"), rs.getString("recipe_name"), rs.getString("recipe"), rs.getInt("serves"), rs.getBoolean("publicly_available"));
                recipes.add(recipe);
            }

        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }

        closeConnection();

        return recipes;
    }

    public static ArrayList<Recipe> getAllPublicRecipes() {
        openConnection();

        ArrayList<Recipe> recipes = new ArrayList<>();

        try{
            String query = "SELECT * FROM Recipes WHERE publicly_available = ?";
            PreparedStatement ps = conn.prepareStatement(query);
            ps.setBoolean(1, true);

            ResultSet rs = ps.executeQuery(query);

            while(rs.next()) {
                Recipe recipe = new Recipe(rs.getInt("id"), rs.getInt("userID"), rs.getString("recipe_name"), rs.getString("recipe"), rs.getInt("serves"), true);
                recipes.add(recipe);
            }

        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }

        closeConnection();

        return recipes;
    }

    public static ArrayList<Ingredient> getIngredients(Recipe recipe) {
        openConnection();

        ArrayList<Ingredient> ingredients = new ArrayList<>();

        try{
            String query = "SELECT * FROM Ingredients WHERE recipeID = ?";
            PreparedStatement ps = conn.prepareStatement(query);
            ps.setInt(1, recipe.getId());

            ResultSet rs = ps.executeQuery(query);

            while(rs.next()) {
                Ingredient ingredient = new Ingredient(rs.getInt("id"), rs.getInt("recipeID"), rs.getString("ingredient"), rs.getFloat("quantity"), rs.getString("unit"));
                ingredients.add(ingredient);
            }

        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }

        closeConnection();

        return ingredients;
    }

    public static ArrayList<Inventory> getInventory(User user) {
        openConnection();

        ArrayList<Inventory> inventoryItems = new ArrayList<>();

        try{
            String query = "SELECT * FROM Inventory WHERE userID = ?";

            PreparedStatement ps = conn.prepareStatement(query);
            ps.setInt(1, user.getId());

            ResultSet rs = ps.executeQuery(query);

            while(rs.next()) {
                Inventory item = new Inventory(rs.getInt("id"), rs.getInt("userID"), rs.getString("ingredient"), rs.getFloat("quantity"), rs.getString("unit"));
                inventoryItems.add(item);
            }

        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }

        closeConnection();

        return  inventoryItems;
    }

    public static ArrayList<Recipe> getMealPlan(User user) {
        openConnection();

        ArrayList<Recipe> mealPlan = new ArrayList<>();

        try{
            String query = "SELECT * FROM MealPlan JOIN Recipes ON MealPlan.recipeID = Recipes.id WHERE MealPlan.userID = ?";

            PreparedStatement ps = conn.prepareStatement(query);
            ps.setInt(1, user.getId());

            ResultSet rs = ps.executeQuery(query);

            while(rs.next()) {
                Recipe recipe = new Recipe(rs.getInt("recipeID"), rs.getInt("userID"), rs.getString("recipe_name"), rs.getString("recipe"), rs.getInt("serves"), rs.getBoolean("publicly_available"));
                mealPlan.add(recipe);
            }
        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }

        closeConnection();

        return mealPlan;
    }

    public static ArrayList<ExtraItem> getExtraItems(User user) {
        openConnection();

        ArrayList<ExtraItem> extraItems = new ArrayList<>();

        try{
            String query = "SELECT * FROM ExtraItems WHERE userID = ?";

            PreparedStatement ps = conn.prepareStatement(query);
            ps.setInt(1, user.getId());

            ResultSet rs = ps.executeQuery(query);

            while(rs.next()) {
                ExtraItem item = new ExtraItem(rs.getInt("userID"), rs.getString("item"), rs.getFloat("quantity"), rs.getString("unit"));
                extraItems.add(item);
            }
        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }

        closeConnection();

        return extraItems;
    }

    public static void insertUser(String username, String password) {
        openConnection();

        try{
            String query = "INSERT INTO Users (username, password) VALUES (?, ?)";
            PreparedStatement ps = conn.prepareStatement(query);
            ps.setString(1, username);
            ps.setString(2, password);

            ps.executeUpdate();
        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }

        closeConnection();
    }

    public static void insertRecipe(User user, Recipe recipe) {
        openConnection();

        try{
            String query = "INSERT INTO Recipe (userId, serves, recipe_name, recipe) VALUES (?, ?, ?, ?)";
            PreparedStatement ps = conn.prepareStatement(query);
            ps.setInt(1, user.getId());
            ps.setInt(2, recipe.getServes());
            ps.setString(3, recipe.getRecipename());
            ps.setString(4, recipe.getRecipe());

            ps.executeUpdate();
        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }

        closeConnection();
    }

    public static void insertIngredient(Ingredient ingredient) {
        openConnection();

        try{
            String query = "INSERT INTO Ingredients (recipeID, ingredient, quantity, unit) VALUES (?, ?, ?, ?)";
            PreparedStatement ps = conn.prepareStatement(query);
            ps.setInt(1, ingredient.getRecipeID());
            ps.setString(2, ingredient.getIngredient());
            ps.setDouble(3, ingredient.getQuantity());
            ps.setString(4, ingredient.getUnit());

            ps.executeUpdate();
        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }

        closeConnection();
    }

    //TODO: might have to modify to insert multiple items
    public static void insertItemsIntoInventory(Inventory inventory) {
        openConnection();

        try{
            String query = "INSERT INTO Inventory (userID, ingredient, quantity, unit) VALUES (?, ?, ?, ?)";
            PreparedStatement ps = conn.prepareStatement(query);
            ps.setInt(1, inventory.getUserID());
            ps.setString(2, inventory.getIngredient());
            ps.setDouble(3, inventory.getQuantity());
            ps.setString(4, inventory.getUnit());

            ps.executeUpdate();
        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }

        closeConnection();
    }

    public static void insertMealPlan(MealPlan mealPlan) {
        openConnection();

        try{
            String query = "INSERT INTO MealPlan (userID, recipeID) VALUES (?, ?)";
            PreparedStatement ps = conn.prepareStatement(query);
            ps.setInt(1, mealPlan.getUserID());
            ps.setInt(2, mealPlan.getRecipeID());

            ps.executeUpdate();
        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }

        closeConnection();
    }

    public static void insertExtraItems(ExtraItem item) {
        openConnection();

        try{
            String query = "INSERT INTO ExtraItems (userId, item, quantity, unit) VALUES (?, ?, ?, ?)";
            PreparedStatement ps = conn.prepareStatement(query);
            ps.setInt(1, item.getUserID());
            ps.setString(2, item.getItem());
            ps.setDouble(3, item.getQuantity());
            ps.setString(4, item.getUnit());

            ps.executeUpdate();
        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }

        closeConnection();
    }

    private static void closeConnection() {
        try {
            conn.close();
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
