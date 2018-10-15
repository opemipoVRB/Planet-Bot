     function firstResponse(){

       function addZero(i){
            if(i < 10){
                i = "0" + i
            }
            return i;
        }

        var d = new Date();
        var h = addZero(d.getHours());
        var m = addZero(d.getMinutes());

            $('#message-feed').append(
                '<div class="message message-from"><div class="message-name"><h1>Govbot</h1></div><div class="message-body"><p>Hi, my name is Govbot. please enter your phone number to proceed </p></div><div class="message-timestamp"><p>Today ' + h + ' : ' + m + '</p></div>'
            );
        }

$(document).ready(function () {

    if(!("WebSocket" in window)){
        $('#chatLog, input, button, #examples').fadeOut("fast");
        $('<p>Oh no, you need a browser that supports WebSockets. How about <a href="http://www.google.com/chrome">Google Chrome</a>?</p>').appendTo('#container');
        }
    else{
    connect();
    function connect(){
    var socket;

    var host = "ws://127.0.0.1:3000";
//    var host = "ws://154.113.17.206:3000";
//  var host = "ws://ec2-18-191-196-135.us-east-2.compute.amazonaws.com:3000/";
    // var host = "ws://127.0.0.1:3000";
//    var host = "ws://ec2-18-191-196-135.us-east-2.compute.amazonaws.com:3000/";
    var mediaExpand = document.getElementById("media-expand-arrow");
    var mediaBar = document.getElementById("media-bar");
    var mediaCross = document.getElementById("media-bar-cross");
    var messageFeed = document.getElementById("message-feed");
    try{
        var socket = new WebSocket(host);

        console.log('Socket Status Initialization : '+socket.readyState);

        socket.onopen = function(){
            console.log('Socket Status : '+socket.readyState+' (open)');
             firstResponse();

        }


        socket.onclose = function(){
         
            console.log('Socket Status: '+socket.readyState+' (Closed)');
        }			

    } catch(exception){
        console.log('Error occurered '+exception);
    }


    
    console.log(mediaExpand + mediaBar);
    
    function mediaOpen(){
        mediaBar.className += " media-bar-open"
    };
    
    mediaExpand.addEventListener("click", mediaOpen, false);
    
    function mediaClose(){
        mediaBar.className = "media-bar"
    };
    
    mediaCross.addEventListener("click", mediaClose, false);
    
    function wScroll(){
        console.log(messageFeed.scrollTop);
        
        let messageHeight = messageFeed.offsetHeight;
    
        var heightToScroll = (130);
        var header = document.getElementById('header');
    
        if(messageFeed.scrollTop > heightToScroll){
            header.className = "header header-scrolled"
            messageFeed.className = "message-feed message-feed-scrolled"
        }
        else if(messageFeed.scrollTop < 1){
            header.className = "header header-unscrolled"
            messageFeed.className = "message-feed"
        }
     };
    
    messageFeed.addEventListener("scroll", wScroll, false);
    
    wScroll();
        
        
    function logMessage(event){
        
        
        //get time
        function addZero(i){
            if(i < 10){
                i = "0" + i    
            }
            return i;
        }
    
        var d = new Date();    
        var h = addZero(d.getHours());
        var m = addZero(d.getMinutes()); 
        
        //build message


        
        function appendMessage() {
            try{
                socket.send(messageVal)
                console.log(messageVal)

                $('#message-feed').append(
                    '<div class="message message-to"><div class="message-name"><h1>You</h1></div><div class="message-body"><p>' + messageVal + '</p></div><div class="message-timestamp"><p>Today ' + h + ' : ' + m + '</p></div>'   
                );

            }
            catch(exception){
                message('<p class="warning">');
            }
        }
        
        //set event trigger

        
        var messageInput = document.getElementById("message-input");
        
        var messageVal = messageInput.value;
        
        //Govbot responses


        function timedResponse(msg){
            setTimeout(
            function appendResponse() {
            $('#message-feed').append(
                '<div class="message message-from"><div class="message-name"><h1>Govbot</h1></div><div class="message-body"><p>'+msg+'</p></div><div class="message-timestamp"><p>Today ' + h + ' : ' + m + '</p></div>'   
            );
                messageFeed.scrollTop = messageFeed.scrollHeight;
            }, 500);
        };
        
        
        //fire on enter
        
        
        if (event.keyCode == 13) {
            event.preventDefault();
            messageInput.value= "";
//            alert(messageVal);
            if (messageVal.trim()!=""){
            appendMessage()
            }

            //;
            messageFeed.scrollTop = messageFeed.scrollHeight;
            socket.onmessage = function(msg){
            
                console.log("I am the message ",msg.data)
              timedResponse(msg.data);
            }
        }        
        
    };
        
    document.addEventListener("keypress", logMessage, false);
    }
    }    
});

