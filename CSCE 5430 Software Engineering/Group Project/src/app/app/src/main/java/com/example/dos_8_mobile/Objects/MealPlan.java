package com.example.dos_8_mobile.Objects;

public class MealPlan
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

	private int recipeID;
	public int getRecipeID()
	{
		return this.recipeID;
	}
	public void setRecipeID(int value)
	{
		this.recipeID = value;
	}


	public MealPlan(int userid,int recipeid)
	{
		this.userID = userid;
		this.recipeID = recipeid;
	}
}

