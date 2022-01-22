#include <iostream>
#include <WS2tcpip.h>
#include <thread>
#pragma comment(lib, "ws2_32.lib")
#include <string>
#include <vector>


const int MAX_CONNECTED_CLIENT_COUNT = 3;
static bool isServerIsActive = true;


class ClientStructrController{
public:
     ClientStructrController(SOCKET currentClientSocket){
        clientSocket = currentClientSocket;
        std::thread listeningThread(&ClientStructrController::ClientListenerLoop, clientSocket);
		std::thread respondingThread(&ClientStructrController::ClientDataTransmitterLoop, clientSocket);
    }

    void KillConnection(){
//		 listeningThread.join();
//		 respondingThread.join();
		 closesocket(clientSocket);
         WSACleanup();
         system("pause");
    }

private:
//    std::thread listeningThread, respondingThread;
    SOCKET clientSocket;
	void ClientListenerLoop(SOCKET clientSocket){
		char buffer[4096];

		while (isServerIsActive)
		{
			ZeroMemory(buffer, 4096);

			int bytesReceived = recv(clientSocket, buffer, 4096, 0);
			if (bytesReceived == SOCKET_ERROR)
			{
				std::cerr << "Error in recv(). Quitting" << std::endl;
				isServerIsActive = false;
			}

			if (bytesReceived == 0)
			{
				std::cout << "Client disconnected " << std::endl;
				isServerIsActive = false;
			}
			std::cout << std::string(buffer, 0, bytesReceived) << std::endl;
			send(clientSocket, buffer, bytesReceived + 1, 0);
		}
	}

	void ClientDataTransmitterLoop(SOCKET clientSocket){
		while (isServerIsActive){
			//TODO: make a respondiong loop
		}
	}

};


class SocketConnectionVideoReceiver{
    bool isConnectionLoopIsAvailable;
    char host[NI_MAXHOST];
    char service[NI_MAXSERV];

public:
    SocketConnectionVideoReceiver(bool listeningLoopFlag, bool connectionLoopFlag) {
        isServerIsActive = listeningLoopFlag;
        isConnectionLoopIsAvailable = connectionLoopFlag;
        listeningSocket = initializeListeningSocketServer();
        clientsControllersHolder = std::vector<ClientStructrController>();
        StartConnectingToServerSession();
    }

    void EndSession() {
        //TODO: make an ending for the current session with clearing main data vector
    }

private:
    SOCKET listeningSocket;
    sockaddr_in connectionHint;
    sockaddr_in client;
    WSADATA winSocketData;
    std::vector<ClientStructrController> clientsControllersHolder;

    SOCKET initializeListeningSocketServer(){

        WORD ver = MAKEWORD(2, 2);

        int wsOk = WSAStartup(ver, &winSocketData);
        if (wsOk != 0)
        {
            std::cerr << "Can't Initialize winsock! Quitting" << std::endl;
            return 1;
        }

        // Create a socket
        listeningSocket = socket(AF_INET, SOCK_STREAM, 0);
        if (listeningSocket == INVALID_SOCKET)
        {
            std::cerr << "Can't create a socket! Quitting" << std::endl;
            return 1;
        }

        StartListening();
        SetConnectionHintWay();

        // Wait for a connection
        return listeningSocket;
    }

    void StartListening(){
        bind(listeningSocket, (sockaddr*)&connectionHint, sizeof(connectionHint));
        listen(listeningSocket, SOMAXCONN);
    }

    void SetConnectionHintWay(){
        connectionHint.sin_family = AF_INET;
        connectionHint.sin_port = htons(54000);
        connectionHint.sin_addr.S_un.S_addr = INADDR_ANY;

    }

    void StartConnectingToServerSession(){
        while (isConnectionLoopIsAvailable){
            accept(listeningSocket, (sockaddr*)&client, NULL);
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
            if (clientsControllersHolder.size() < MAX_CONNECTED_CLIENT_COUNT){
                ClientStructrController newClient = ClientStructrController(listeningSocket);
                clientsControllersHolder.push_back(newClient);
            }
            else{
                isConnectionLoopIsAvailable = false;
            }
        }
    }

};

int main()
{
    SocketConnectionVideoReceiver currentServer = SocketConnectionVideoReceiver(true, true);
    currentServer.EndSession();

    return 0;
}