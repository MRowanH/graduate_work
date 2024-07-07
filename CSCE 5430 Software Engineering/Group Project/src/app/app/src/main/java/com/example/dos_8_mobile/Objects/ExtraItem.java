package com.example.dos_8_mobile.Objects;

public class ExtraItem
{
	private int userID;
	public int getUserID()
	{
		return this.userID;
	}
	public void setUserID(int value)
	{
		this.userID = value;
	}

	private String item;
	public String getItem()
	{
		return this.item;
	}
	public void setItem(String value)
	{
		this.item= value;
	}

	private double quantity;
	public double getQuantity()
	{
		return this.quantity;
	}
	public void setQuantity(double value)
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


	public ExtraItem(int userid, String item, double quantity, String unit)
	{
		this.userID = userid;
		this.item = item;
		this.quantity = quantity;
		this.unit = unit;
	}
}