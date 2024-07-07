package com.example.dos_8_mobile.Objects;

public class Recipe
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

	private String recipename;
	public String getRecipename()
	{
		return this.recipename;
	}
	public void setRecipename(String value)
	{
		this.recipename = value;
	}

	private String recipe;
	public String getRecipe()
	{
		return this.recipe;
	}
	public void setRecipe(String value)
	{
		this.recipe = value;
	}

	private int serves;
	public int getServes() {return this.serves; }
	public void setServes(int value) { this.serves = value; }

	private boolean isPublic;
	public boolean getIsPublic() {return  this.isPublic; }
	public void setIsPublic(boolean value) { this.isPublic = value; }


	public Recipe(int id, int userid, String recipename, String recipe, int serves, boolean isPublic)
	{
		this.id = id;
		this.userID = userid;
		this.recipename = recipename;
		this.recipe = recipe;
		this.serves = serves;
		this.isPublic = isPublic;
	}
}
