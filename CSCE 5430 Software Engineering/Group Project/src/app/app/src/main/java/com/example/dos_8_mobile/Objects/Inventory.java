package com.example.dos_8_mobile.Objects;

public class Inventory
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

	private int userID;
	public int getUserID()
	{
		return this.userID;
	}
	public void setUserID(int value)
	{
		this.userID = value;
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

	public Inventory(int id, int userID, String ingredient, double quantity, String unit) {
		this.id = id;
		this.userID = userID;
		this.ingredient = ingredient;
		this.quantity = quantity;
		this.unit = unit;
	}


}

