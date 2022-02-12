export const initializeCameraInputSession = () => {
    
}
function createCameraStream(){
    
}


function AllowUsingCamera(){
    navigator.getUserMedia = ( navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msgGetUserMedia );

    if(navigator.getUserMedia)
    {
        navigator.getUserMedia({
            video: {
                width: { min: 1024, ideal: 1280, max: 1920 },
                height: { min: 576, ideal: 720, max: 1080 }
            }, 
            audio: false
        }, createCameraStream);
    }
}