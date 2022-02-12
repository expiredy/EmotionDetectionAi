var canvas = document.getElementById("preview");
var context = canvas.getContext('2d');
canvas.width = 900;
canvas.height = 700;
context.width = canvas.width;
context.height = canvas.height;
var video = document.getElementById("video");
var socket = io('ws://localhost:8001');
function logger(msg){
    $('#log').text(msg);
}
function loadCamera(stream){
  try {
      video.srcObject = stream;
  } 
  
  catch (error) {
   video.src = URL.createObjectURL(stream);
  }
   logger("Camera connected");
}
function loadFail(){
    logger("Camera not connected");
}
function Draw(video,context){
    context.drawImage(video,0,0,context.width,context.height);
    socket.emit('stream',canvas.toDataURL('image/webp'));
}
$(function(){
    navigator.getUserMedia = ( navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msgGetUserMedia );

    if(navigator.getUserMedia)
    {
        navigator.getUserMedia({
            video: true, 
            audio: false
        },loadCamera,loadFail);
    }
    setInterval(function(){
        Draw(video,context);
    },0.1);
});
