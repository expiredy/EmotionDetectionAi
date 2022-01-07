#include <iostream>
#include <WS2tcpip.h>
#pragma comment(lib, "ws2_32.lib")
#include <string>


static bool isListeningLoopIsAvailable = true;


int main()
{
    // Initialze winsock
    WSADATA winSocketData;
    WORD ver = MAKEWORD(2, 2);

    int wsOk = WSAStartup(ver, &winSocketData);
    if (wsOk != 0)
    {
        std::cerr << "Can't Initialize winsock! Quitting" << std::endl;
        return 1;
    }

    // Create a socket
    SOCKET listeningSocket = socket(AF_INET, SOCK_STREAM, 0);
    if (listeningSocket == INVALID_SOCKET)
    {
        std::cerr << "Can't create a socket! Quitting" << std::endl;
        return 1;
    }

    sockaddr_in hint;
    hint.sin_family = AF_INET;
    hint.sin_port = htons(54000);
    hint.sin_addr.S_un.S_addr = INADDR_ANY;

    bind(listeningSocket, (sockaddr*)&hint, sizeof(hint));
    listen(listeningSocket, SOMAXCONN);

    // Wait for a connection
    sockaddr_in client;
    int clientSize = sizeof(client);

    SOCKET clientSocket = accept(listeningSocket, (sockaddr*)&client, &clientSize);

    char host[NI_MAXHOST];
    char service[NI_MAXSERV];

    ZeroMemory(host, NI_MAXHOST);
    ZeroMemory(service, NI_MAXSERV);

    if (getnameinfo((sockaddr*)&client,
                    sizeof(client),
                    host,
                    NI_MAXHOST,
                    service,
                    NI_MAXSERV,
                    0) == 0)
    {
        std::cout << host << " connected on port " << service << std::endl;
    }
    else
    {
        inet_ntop(AF_INET, &client.sin_addr, host, NI_MAXHOST);
        std::cout << host << " connected on port " <<
             ntohs(client.sin_port) << std::endl;
    }

    closesocket(listeningSocket);
    char buf[4096];

    while (isListeningLoopIsAvailable)
    {
        ZeroMemory(buf, 4096);

        int bytesReceived = recv(clientSocket, buf, 4096, 0);
        if (bytesReceived == SOCKET_ERROR)
        {
            std::cerr << "Error in recv(). Quitting" << std::endl;
            isListeningLoopIsAvailable = false;
        }

        if (bytesReceived == 0)
        {
            std::cout << "Client disconnected " << std::endl;
            isListeningLoopIsAvailable = false;
        }
        std::cout << std::string(buf, 0, bytesReceived) << std::endl;
        send(clientSocket, buf, bytesReceived + 1, 0);

    }

    closesocket(clientSocket);
    WSACleanup();

    system("pause");
    return 0;
}