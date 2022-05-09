using System;

using UnityEngine;

public class Main : MonoBehaviour
{
	const string ESCAPE = "escape";

	private void Start()
	{
	}

	private void Update()
	{
		if ( Input.GetKey( ESCAPE ) )
		{
			Application.Quit();
		}
	}
}
