<template>
    <div class="web-camera-container">       
        <div class="camera-box">
            <video ref="camera" :width="450" :height="337.5" autoplay></video>            
        </div>
        
    </div>
</template>

<script>

const currentWindow = window;
const mainStreamThread = {currentThread: null};

function createCameraElement() {
    currentWindow.isFrameLoading = true;
    const constraints = (currentWindow.constraints = {
        audio: false,
        video: true
    });
    
    currentWindow.navigator.mediaDevices
        .getUserMedia(constraints)
        .then(stream => {
            mainStreamThread.currentThread = stream;

            var recorderOptions = {mimeType: 'video/webm; codecs=vp8'};
            var mediaRecorder = new MediaRecorder(s, recorderOptions );
            mediaRecorder.ondataavailable = function(event) {
                if (event.data && event.data.size > 0) {
                    //TODO: send with web sockets from event.data
                }
            }

            mediaRecorder.start(100); // делит поток на кусочки по 100 мс каждый
        }).catch(error => {
                    alert("May the browser didn't support or there is some errors." + error.message);})
}

function stopCameraStream(){
    let tracks = this.$refs.camera.srcObject.getTracks();
    tracks.forEach(track => {
        console.log(track);
        track.stop();
    });
}
function toggleCamera() {
    if (currentWindow.isCameraActive) {
    	currentWindow.isCameraActive = false;
        stopCameraStream();
    } else {
    	currentWindow.isCameraActive = true;
        createCameraElement();
    }
}




let isCameraActive = true;
currentWindow.addEventListener('load', toggleCamera(window));

export default {
    name: 'DebugViewer',
    data () {
        return {
            link: '#'
        }
    },
    methods: {
        toggleCamera,
        stopCameraStream,
        createCameraElement
    }
}
</script>


<style>
.web-camera-container {
    margin-top: 2rem;
    margin-bottom: 2rem;
    padding: 2rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    border: 1px solid #ccc;
    border-radius: 4px;
    width: 500px;

    .camera-box .camera-shutter {
        opacity: 0;
        width: 450px;
        height: 337.5px;
        background-color: #fff;
        position: absolute;
    }
    .camera-box .flash {
        opacity: 1;
    }
       
    .camera-shoot {
        margin: 1rem 0;
        
    }
  
    .camera-loading {
        overflow: hidden;
        height: 100%;
        position: absolute;
        width: 100%;
        min-height: 150px;
        margin: 3rem 0 0 -1.2rem;
    
        ul {
            height: 100%;
            position: absolute;
            width: 100%;
            z-index: 999999;
            margin: 0;
        }
    }

    @keyframes preload {
        0% {
            opacity: 1
        }
        50% {
            opacity: .4
        }
        100% {
            opacity: 1
        }
    }
}
</style>