const socketUrl = process.env.NODE_ENV === 'production' ? "wss://localhost:54000/" : "ws://localhost:54000/";
const socketConfig = {
    socketConnection: new WebSocket(socketUrl)
};

export default function initializeSocket(func: Function = sayHelloToServer) {
    socketConfig.socketConnection = new WebSocket(socketUrl);

    socketConfig.socketConnection.onopen = () => {
        if (socketConfig.socketConnection.readyState){
            socketConfig.socketConnection.send("Fucker mother, here i cummer");

            console.log("[+] Websocket connect success")

            func()
        }
    }

    socketConfig.socketConnection.onmessage = (event: any) => {
        const raw = JSON.parse(event.data)

        console.log(raw)
        console.log("[+] Get websocket message")
    }
    
    socketConfig.socketConnection.onclose = function(event: any) {
            if (event.wasClean) {
                alert('Perfectly ending (like in One Piece (get it?))');
            } else {
                alert('Connection is lost :<'); 
            }
            alert('Error code (not js code, bruh): ' + event.code + ' the reason: ' + event.reason + '\nJust kidding, it is all js problem, totally not my');
    };
        
}



export function sayHelloToServer(){
    socketConfig.socketConnection.send('image/webp');
}