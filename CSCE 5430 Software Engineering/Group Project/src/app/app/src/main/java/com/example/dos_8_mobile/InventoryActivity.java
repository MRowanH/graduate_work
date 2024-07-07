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
import com.example.dos_8_mobile.Objects.User;
import com.example.dos_8_mobile.DbConnection;

import java.util.ArrayList;

public class inventoryActivity extends AppCompatActivity {
    public inventoryActivity() {
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.inventory);

        startLoadData();

    }

    public void startLoadData() {
        TableLayout stack = findViewById(R.id.mainTable);
        TableRow trow0 = new TableRow(this);
//        User user7 = User();
//        Ingredient ingredient1 = new ingredient(1, 3, "lemon", "cornmeal" true);
////        DbConnection.getIngredients(ingredient1);
//        System.out.println(DbConnection.getIngredients(ingredient3));
//        Integer count = DbConnection.getIngredientsCount(ingredient3);
             stack.addView(trow0);
        for (int i = 0; i < 25; i++) {
            String[] testIngredients = {"Eggs", "Chicken", "Flour", "Pancake Mix", "Salt", "Pepper", "Soda"};
//item, quantity, unit
               // data columns
                final TextView tv = new TextView(this);
                tv.setLayoutParams(new
                        TableRow.LayoutParams(TableRow.LayoutParams.WRAP_CONTENT,
                        TableRow.LayoutParams.WRAP_CONTENT));
                tv.setGravity(Gravity.LEFT);
                tv.setPadding(5, 15, 0, 15);
                if (i == -1) {
                    tv.setBackgroundColor(Color.parseColor("#f0f0f0"));
                    tv.setTextSize(TypedValue.COMPLEX_UNIT_PX, smallTextSize);
                } else {
                    tv.setBackgroundColor(Color.parseColor("#f8f8f8"));
                    tv.setText(String.valueOf(ingredient));
                    tv.setTextSize(TypedValue.COMPLEX_UNIT_PX, textSize);
                }
                final TextView tv2 = new TextView(this);
                if (i == -1) {
                    tv2.setLayoutParams(new
                            TableRow.LayoutParams(TableRow.LayoutParams.MATCH_PARENT,
                            TableRow.LayoutParams.WRAP_CONTENT));
                    tv2.setTextSize(TypedValue.COMPLEX_UNIT_PX, smallTextSize);
                } else {
                    tv2.setLayoutParams(new
                            TableRow.LayoutParams(TableRow.LayoutParams.WRAP_CONTENT,
                            TableRow.LayoutParams.MATCH_PARENT));
                    tv2.setTextSize(TypedValue.COMPLEX_UNIT_PX, textSize);
                }
                tv2.setGravity(Gravity.LEFT);
                tv2.setPadding(5, 15, 0, 15);
                if (i == -1) {
                    tv2.setBackgroundColor(Color.parseColor("#f7f7f7"));
                } else {
                    tv2.setBackgroundColor(Color.parseColor("#ffffff"));
                    tv2.setTextColor(Color.parseColor("#000000"));
                }
                final LinearLayout layUsers = new LinearLayout(this);
                layUsers.setOrientation(LinearLayout.VERTICAL);
                layUsers.setPadding(0, 10, 0, 10);
                layUsers.setBackgroundColor(Color.parseColor("#f8f8f8"));
                final TextView tv3 = new TextView(this);
                tv3.setLayoutParams(new
                        TableRow.LayoutParams(TableRow.LayoutParams.MATCH_PARENT,
                        TableRow.LayoutParams.MATCH_PARENT));
                if (i == -1) {
                    tv3.setPadding(5, 5, 0, 5);
                    tv3.setTextSize(TypedValue.COMPLEX_UNIT_PX, smallTextSize);
                } else {
                    tv3.setPadding(5, 0, 0, 5);
                    tv3.setTextSize(TypedValue.COMPLEX_UNIT_PX, textSize);
                }
                tv3.setGravity(Gravity.TOP);
                if (i == -1) {
                    tv3.setText("Inv.#");
                    tv3.setBackgroundColor(Color.parseColor("#f0f0f0"));
                } else {
                    tv3.setBackgroundColor(Color.parseColor("#f8f8f8"));
                    tv3.setTextColor(Color.parseColor("#000000"));
                    tv3.setTextSize(TypedValue.COMPLEX_UNIT_PX, smallTextSize);
                    tv3.setText((Integer) userID);
                }
                layUsers.addView(tv3);
                if (i > -1) {
                    final TextView tv3b = new TextView(this);
                    tv3b.setLayoutParams(new
                            TableRow.LayoutParams(TableRow.LayoutParams.WRAP_CONTENT,
                            TableRow.LayoutParams.WRAP_CONTENT));
                    tv3b.setGravity(Gravity.RIGHT);
                    tv3b.setTextSize(TypedValue.COMPLEX_UNIT_PX, textSize);
                    tv3b.setPadding(5, 1, 0, 5);
                    tv3b.setTextColor(Color.parseColor("#aaaaaa"));
                    tv3b.setBackgroundColor(Color.parseColor("#f8f8f8"));
                    tv3b.setText((char) ingredient);
                    layUsers.addView(tv3b);
                }
                class LoadDataTask extends AsyncTask<Integer, Integer, String> {
                    @Override
                    protected String doInBackground(Integer... params) {
                        try {
                            Thread.sleep(2000);
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                        return "Task Completed.";
                    }

                    @Override
                    protected void onPostExecute(String result) {
                        mProgressBar.hide();
                        loadData();
                    }

                    private void loadData() {
                    }

                    @Override
                    protected void onPreExecute() {
                    }

                    @Override
                    protected void onProgressUpdate(Integer... values) {
                    }
                }

            }
        }

    }     
