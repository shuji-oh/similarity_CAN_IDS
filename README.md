similarity_CAN_IDS
====

### Overview

similarity_CAN_IDS is State-of-the-art intrusion detection method agaist DoS attack on CAN.

"Fast Detection Method Based on Similarity of Sliding Windows against DoS Attack on In-vehicle Network"

## Description

## Directory Structure

similarity_CAN_IDS  
┣━ off-line_learning_phase  
┃	┣━ similarity_of_slindingwindow_detect.py  
┃	┣━ eval_similarity_of_slindingwindow_detect.py  
┃	┗━ similarity_calc.py  
┣━ on-line_detection_phase  
┃	┣━ fastDoSdetect.c  
┃	┣━ Makefile  
┃	┣━ lib.c  
┃   ┣━ lib.h  
┃	┗━ terminal.h  
┣━ paper.pdf  
┗━ README.md  

## Requirement

python3, gcc

## Usage

$ git clone https://github.com/ohirangosta/similarity_CAN_IDS  
$ cd similarity_CAN_IDS  
$ ./build.sh release  

## Contribution

## Author

[rangosta](https://github.com/ohirangosta)
