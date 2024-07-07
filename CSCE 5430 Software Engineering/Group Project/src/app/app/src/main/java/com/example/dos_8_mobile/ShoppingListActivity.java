package com.example.dos_8_mobile;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;
import android.view.Gravity;
import java.util.Random;
import android.view.View;
import android.widget.Button;
import android.widget.TableLayout;
import android.widget.TableRow;
import android.widget.TextView;

import com.example.dos_8_mobile.Objects.Ingredient;
import com.example.dos_8_mobile.Objects.Recipe;
import com.example.dos_8_mobile.Objects.User;
import com.example.dos_8_mobile.DbConnection;

import java.util.ArrayList;

public class ShoppingListActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.shopping_list);

        init();

    }


    public void init() {
        TableLayout stk = (TableLayout) findViewById(R.id.mainTable);
        TableRow tbrow0 = new TableRow(this);

        Recipe recipe1 = new Recipe(1, 2, "Carmelized Onion Chicken", "Sprinkle chicken with salt and pepper. Heat oil in a large nonstick skillet over medium-high heat. Add onion, and sauté 2 minutes. Add chicken to pan; sauté 8 minutes or until chicken is done. Remove onion and chicken from pan. Add jam and remaining ingredients to pan; cook 2 minutes, stirring constantly with a whisk. Return chicken mixture to pan; cook 4 minutes, stirring occasionally.", 4, true);


        class Foo implements Runnable {
            private volatile ArrayList<Ingredient> ingredients;

            @Override
            public void run() {
                ingredients = DbConnection.getIngredients(recipe1);
            }

            public ArrayList<Ingredient> getValue() {
                return ingredients;
            };
        }

        Foo foo = new Foo();

        Thread t = new Thread(foo);
        t.start();
        try {
            t.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        foo.getValue();

        stk.addView(tbrow0);
        Random rand = new Random();
        String[] testIngredients = {"Eggs", "Chicken", "Flour", "Pancake Mix", "Salt", "Pepper", "Soda"};
//item, quantity, unit
        for (int i = 0; i < 7; i++) {
            TableRow tbrow = new TableRow(this);
            TextView t1v = new TextView(this);
            t1v.setText("" + i + "  ");
            t1v.setTextColor(Color.BLACK);
            t1v.setTextSize(20);
            //t1v.setGravity(Gravity.CENTER);
            tbrow.addView(t1v);
            TextView t2v = new TextView(this);
            t2v.setText(testIngredients[i]);
            t2v.setTextColor(Color.BLACK);
            t2v.setTextSize(20);
            //t2v.setGravity(Gravity.CENTER);
            tbrow.addView(t2v);
            int int_random = rand.nextInt(10);
            String randomNo = String.valueOf(int_random);
            TextView t3v = new TextView(this);
            t3v.setText("       "+ randomNo);
            t3v.setTextColor(Color.BLACK);
            t3v.setGravity(Gravity.CENTER);
            t3v.setTextSize(20);
            tbrow.addView(t3v);
//            TextView t4v = new TextView(this);
//            t4v.setText("" + i * 15 / 32 * 10);
//            t4v.setTextColor(Color.WHITE);
//            t4v.setGravity(Gravity.CENTER);
            //tbrow.addView(t4v);
            stk.addView(tbrow);
        }

    }
}