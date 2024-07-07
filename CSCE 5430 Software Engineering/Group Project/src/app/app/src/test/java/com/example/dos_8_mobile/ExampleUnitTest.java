package com.example.dos_8_mobile;

import org.junit.Test;

import static org.junit.Assert.*;

import java.util.ArrayList;

/**
 * Example local unit test, which will execute on the development machine (host).
 *
 * @see <a href="http://d.android.com/tools/testing">Testing documentation</a>
 */
public class ExampleUnitTest {
    @Test
    public void addition_isCorrect() {
        assertEquals(4, 2 + 2);
    }

    @Test
    public void userAuth_isCorrect() {
        User user = new User(1, "Mica", "pass1");

        boolean exits = DbConnection.authUser(user);

        assertTrue(exits);
    }

    @Test
    public void getRecipes_isCorrect() {
        User user = new User(1, "Mica", "pass1");

        ArrayList<Recipe> recipes = DbConnection.getRecipes(user);

        assertTrue(recipes.size() > 0);
    }

    @Test
    public void getAllPublicRecipes_isCorrect() {
        ArrayList<Recipe> recipes = DbConnection.getAllPublicRecipes();

        assertTrue(recipes.size() > 0);
    }

    @Test
    public void getIngredients_isCorrect() {
        Recipe recipe = new Recipe(1, 1, "", "", 0, true);

        ArrayList<Ingredient> ingredients = DbConnection.getIngredients(recipe);

        assertTrue(ingredients.size() > 0);
    }

    @Test
    public void getInventory_isCorrect() {
        User user = new User(1, "Mica", "pass1");

        ArrayList<Inventory> inventory = DbConnection.getInventory(user);

        assertTrue(inventory.size() > 0);
    }

    @Test
    public void getMealPlan_isCorrect() {
        User user = new User(1, "Mica", "pass1");

        ArrayList<MealPLan> mealPlan = DbConnection.getMealPlan(user);

        assertTrue(mealPlan.size() > 0);
    }

    @Test
    public void getExtraItems_isCorrect() {
        User user = new User(1, "Mica", "pass1");

        ArrayList<ExtraItem> items = DbConnection.getExtraItems(user);

        assertTrue(items.size() > 0);
    }
}