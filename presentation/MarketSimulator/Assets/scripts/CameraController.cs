
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraController : MonoBehaviour
{
    private Transform playerTrans;
    private Vector3 offset;
   
    private void Awake()
    {
        playerTrans = GameObject.FindWithTag("Player").transform;
        offset = transform.position - playerTrans.position;
        offset = new Vector3(0, offset.y, offset.z);
    }

    void Update()
    {
        transform.position = Vector3.Lerp(transform.position, playerTrans.position + offset, Time.deltaTime * 10);
    }
}