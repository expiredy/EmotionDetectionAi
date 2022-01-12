using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MainCharecterMovement : MonoBehaviour
{

    private static float _currentMovementSpeed = 10f;
    private float _xHorizontalAxis, _yVerticalAxis;
    
    void Update()
    {
        ListenUserInput();
        MakePersonMove();
    }

    void ListenUserInput()
    {
        this._yVerticalAxis = Input.GetAxis("Vertical");
        this._xHorizontalAxis = Input.GetAxis("Horizontal");
    }

    void MakePersonMove()
    {
        
    }
}
