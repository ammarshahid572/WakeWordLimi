# Introduction 
This file shows my process as I am following it. 
First, I wanted to build entire project from scratch myself but given the short deadline time I will follow fast option.

# Environment Setup.
 I dont have a raspberry pi on hand to test the system as a whole but my personal PC uses Debian Linux similar to that of Raspberry Pi. So I will run the codes on this instead.
 I have to make a Virtual Environment since debian linux no longer allows system wide python package installation (added those to gitignore)
    Tools used:
        VSCode, Git, PlatformIO, ChatGPT, Mosquitto Mqtt, MQTTX (GUI for MQTT, for debugging)
    
    Created Git Remote




# Got base codes from ChatGPT, these I will use as templates and fix as I build.
    Got wakeWordDetection.py
    Got firmware/Esp32-wake-word/src/main.cpp  <- I am using platform IO as it is faster and has intellisense



# Libraries Setup:
    For python:
        paho-mqtt 
        portaudio
    
    For Esp32:
        PubSubClient.h 



# Dev Time line:
## First Iteration: 
    Setup Mosquito Mqtt to allow connections outside of localhost. 
     
    -- Check wakeWordDetection.py, to see if its sending messages. without wake word.
    -- Check firmware src main.cpp, to see if its receiving the messages  

## Second Iteration:
    Integration of Wake word detection using snowboy.
        -- Needed to install dependencies, challenge in pyaudio as it requires portaudio which in newer linux system has to be installed manually.
        -- issues with installation, as the repo isnt maintained for quite a while

    Integration of Porcupine, 
        -- I copied a demo code (porcupineDemo.py) for testing of wake word detection 
        -- added .env file to hide Access key from git 

    In firmware I changed the code to also publish a message on a different topic indicating the processing has been done. 



## Third Iteration
    First Create a backend service (backend.py) that listens to MQTT messages and calls an MCP service and test it.
    Next Create a simple Mcp dockerized container, this one uses stdin to be called, and test it.
    ~~Now use Docker MCP gateway to present an endpoint our backend can call via HTTP.~~
    Make backend call the service. 



 