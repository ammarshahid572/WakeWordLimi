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
    
    For Esp32:
        PubSubClient.h 



# Dev Time line:
## First Iteration: 
    -- Check wakeWordDetection.py, 