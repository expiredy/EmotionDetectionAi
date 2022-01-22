using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MainCharecterMovement : MonoBehaviour
{
    const float startingStoppingSpeed = 0.7f; 
    
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
        if ((Mathf.Abs(this._xMovementAxis) <= startingStoppingSpeed) && (Mathf.Abs(this._zMovementAxis) <= startingStoppingSpeed))
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
