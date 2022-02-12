<template>
    <div class="web-camera-container">
        <div class="camera-button">
            <button type="button" class="button is-rounded" :class="{ 'is-primary' : !isCameraOpen, 'is-danger' : isCameraOpen}" @click="toggleCamera">
                <span>Press me</span>
            </button>
        </div>
          
        
        <div v-if="isCameraOpen" v-show="!isLoading" class="camera-box">
            <video ref="camera" :width="450" :height="337.5" autoplay></video>            
        </div>
        
    </div>
</template>

<script>

function createCameraElement() {
    this.isFrameLoading = true;
    const constraints = (window.constraints = {
        audio: false,
        video: true
    });
    
    navigator.mediaDevices
        .getUserMedia(constraints)
        .then(stream => {
                    this.isFrameLoading = false;
        this.$refs.camera.srcObject = stream;
        })
        .catch(error => {
        this.isFrameLoading = false;
        alert("May the browser didn't support or there is some errors.");
    });
}
function stopCameraStream(){
    let tracks = this.$refs.camera.srcObject.getTracks();
    tracks.forEach(track => {
        console.log(track);
        track.stop();
    });
}
function toggleCamera() {
    if (this.isCameraActive) {
    	this.isCameraActive = false;
        this.stopCameraStream();
    } else {
    	this.isCameraActive = true;
        this.createCameraElement();
    }
}

let isCameraActive = true;
let isFrameLoading = false;
window.addEventListener('load', toggleCamera());

export default {
    name: 'DebugViewer',
    data () {
        return {
            isCameraOpen: isCameraActive,
            isLoading: isFrameLoading,
            link: '#'
        }
    },
    methods: {
        toggleCamera,
        stopCameraStream,
        createCameraElement
        // takePhoto() {
        //   if(!this.isPhotoTaken) {
        //     this.isShotPhoto = true;

        //     const FLASH_TIMEOUT = 50;

        //     setTimeout(() => {
        //       this.isShotPhoto = false;
        //     }, FLASH_TIMEOUT);
        //   }

        //   this.isPhotoTaken = !this.isPhotoTaken;

        //   const context = this.$refs.canvas.getContext('2d');
        //   context.drawImage(this.$refs.camera, 0, 0, 450, 337.5);
        // },

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

  
    .camera-button {
        margin-bottom: 2rem;
    }
  
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