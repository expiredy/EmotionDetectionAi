using UnityEngine;

//��� ������� ���������� ��� ��� ������ �� ��������� ���� �� ������ ����� ������������� ������ ����������
[RequireComponent(typeof(Rigidbody))]
[RequireComponent(typeof(CapsuleCollider))]
public class  Playercontroller: MonoBehaviour
{
    public float speed = 0.3f;
    public float jumpForce = 1f;


    public LayerMask groundLayer = 1; 

    private Rigidbody _rb;
    private CapsuleCollider _collider; 

    private bool _isGrounded
    {
        get
        {
            var bottomCenterPoint = new Vector3(_collider.bounds.center.x, _collider.bounds.min.y, _collider.bounds.center.z);

            //������� ��������� ���������� ������� � ��������� �� ���������� �� ��� ������ ������� ��������� � ����

            //_collider.bounds.size.x / 2 * 0.9f -- ��� �������� ����������� ����� ������ �������.
            // ��� �� ����������� ������ -- ������ �� ������ ��������, � ��� ����� ��-�������������

            return Physics.CheckCapsule(_collider.bounds.center, bottomCenterPoint, _collider.bounds.size.x / 2 * 0.9f, groundLayer);
            // ���� ����� ����� ������� � �������, �� ����� ����� �������� ���������� 0.9 �� �������.
        }
    }

    private Vector3 _movementVector
    {
        get
        {
            var horizontal = Input.GetAxis("Horizontal");
            var vertical = Input.GetAxis("Vertical");

            return new Vector3(horizontal, 0.0f, vertical);
        }
    }

    void Start()
    {
        _rb = GetComponent<Rigidbody>();
        _collider = GetComponent<CapsuleCollider>();

        //�.�. ��� �� ����� ��� �� �������� ��� ������ ��� ��-���� ��� ������ �� �� ��������.
        //�� ����� ��������� ������� �� ���� X � Z
        _rb.constraints = RigidbodyConstraints.FreezeRotationX | RigidbodyConstraints.FreezeRotationZ;

        //  ������ �� ������
        if (groundLayer == gameObject.layer)
            Debug.LogError("Player SortingLayer must be different from Ground SourtingLayer!");
    }

    void FixedUpdate()
    {
        JumpLogic();
        MoveLogic();
    }

    private void MoveLogic()
    {
        // �.�. �� ������ ������ ������������ ���������� �������� �����,
        // �� ������ � ��������� Time.fixedDeltaTime
        _rb.AddForce(_movementVector * speed, ForceMode.Impulse);
    }

    private void JumpLogic()
    {
        if (_isGrounded && (Input.GetAxis("Jump") > 0))
        {
            _rb.AddForce(Vector3.up * jumpForce, ForceMode.Impulse);
        }
    }
}