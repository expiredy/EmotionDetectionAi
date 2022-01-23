using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MainCharecterMovement : MonoBehaviour
{
    public static const float MOUSE_INPUT_SENSETIVITY = 2.0f;

    const float SLOWERING_SPEED = 0.7f;
    
    private float _currentMovementSpeed = 10f;
    private float _xMovementAxis, _zMovementAxis;
    
    
    void Update()
    {
        ListenUserInput();
        MakePersonMove();
    }

    void ListenUserInput()
    {
        this._xMovementAxis = Input.GetAxis("Horizontal");
        this._zMovementAxis = Input.GetAxis("Vertical");
    }

    void MakePersonMove()
    {
        if ((Mathf.Abs(this._xMovementAxis) <= SLOWERING_SPEED) && (Mathf.Abs(this._zMovementAxis) <= SLOWERING_SPEED))
        {
            //Start doing animations of walk starting
        }
        else
        {
            this.transform.position = new Vector3(this.transform.position.x + this._xMovementAxis * this._currentMovementSpeed * Time.deltaTime,
                                                  this.transform.position.y,
                                                  this.transform.position.z + this._zMovementAxis * this._currentMovementSpeed * Time.deltaTime);
        }
    }

}
