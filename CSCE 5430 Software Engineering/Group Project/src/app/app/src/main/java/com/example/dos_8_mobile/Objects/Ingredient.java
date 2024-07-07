package com.example.dos_8_mobile.Objects;

public class Ingredient
{
	private int id;
	public int getId()
	{
		return this.id;
	}
	public void setId(int value)
	{
		this.id = value;
	}

	private int recipeID;
	public int getRecipeID()
	{
		return this.recipeID;
	}
	public void setRecipeID(int value)
	{
		this.recipeID = value;
	}

	private String ingredient;
	public String getIngredient()
	{
		return this.ingredient;
	}
	public void setIngredient(String value)
	{
		this.ingredient = value;
	}

	private double quantity;
	public double getQuantity()
	{
		return this.quantity;
	}
	public void setQuantity(int value)
	{
		this.quantity = value;
	}

	private String unit;
	public String getUnit()
	{
		return this.unit;
	}
	public void setUnit(String value)
	{
		this.unit = value;
	}


	public Ingredient(int id, int recipeid, String ingredient, double quantity, String unit)
	{
		this.id = id;
		this.recipeID = recipeid;
		this.ingredient = ingredient;
		this.quantity = quantity;
		this.unit = unit;
	}
}
