#!/bin/bash

IMGLINK="https://thoseawesomeguys.com/prompts/Xelu_Free_Controller&Key_Prompts.zip"

mkdir -p img/
wget $IMGLINK -O prompts.zip
unzip prompts.zip -d img/
