similarity_CAN_IDS
====

### Overview

similarity_CAN_IDS is State-of-the-art intrusion detection method agaist DoS attack on CAN.

"Fast Detection Method Based on Similarity of Sliding Windows against DoS Attack on In-vehicle Network"

## Description



## Directory Structure

similarity_CAN_IDS  
┣━ off-line_learning_phase  
┃	┣━ output_similarity.py  
┃	┣━ eval_similarity_CAN_IDS.py  
┃	┗━ output_CIDs.py  
┣━ on-line_detection_phase  
┃	┣━ similarity_CAN_IDS.c  
┃	┣━ Makefile  
┃	┣━ lib.c  
┃   ┣━ lib.h  
┃	┗━ terminal.h  
┣━ CIDs.txt  
┣━ paper.pdf  
┗━ README.md  

## Requirement

python3, gcc

## Usage

$ git clone https://github.com/ohirangosta/similarity_CAN_IDS  
$ cd similarity_CAN_IDS/  
$ python3 off-line_learning_phase/output_CIDs.py test_data/test_data.log  
$ cd on-line_detection_phase/  
$ make  
$ ./similarity_CAN_IDS can0  

## Contribution

## Author

[rangosta](https://github.com/ohirangosta)
