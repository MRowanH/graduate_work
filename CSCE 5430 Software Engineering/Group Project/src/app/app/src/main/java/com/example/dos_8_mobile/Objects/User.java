package com.example.dos_8_mobile.Objects;

public class User
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

	private String username;
	public String getUsername()
	{
		return this.username;
	}
	public void setUsername(String value)
	{
		this.username = value;
	}

	private String password;
	public String getPassword()
	{
		return this.password;
	}
	public void setPassword(String value)
	{
		this.password = value;
	}


	public User(int id, String username, String password)
	{
		this.id = id;
		this.username = username;
		this.password = password;
	}
}