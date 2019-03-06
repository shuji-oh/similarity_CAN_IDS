similarity_CAN_IDS
====

## Overview

similarity_CAN_IDS is State-of-the-art DoS attacks detection method on CAN bus.

Shuji Ohira et al. "DoS Attacks Fast Detection Method Based on Similarity of Sliding Windows on In-vehicle Network"

## Description

The entropy_CAN_IDS (Conventional method) cannot detect an entropy-manipulated attack in which an adversary adjusts the entropy of a DoS attack to a normal value. Thus, we proposed the similarity_CAN_IDS that is State-of-the-art DoS attacks detection method on CAN bus. The proposed method use not entropy but similarity to detect intrusion detection.

## Directory Structure

similarity_CAN_IDS  
┣━ off-line_learning_phase  
┃	┣━ output_similarity.py  
┃	┣━ eval_similarity_CAN_IDS.py  
┃	┗━ output_params.py  
┣━ on-line_detection_phase  
┃	┣━ similarity_CAN_IDS.c  
┃	┣━ Makefile  
┃	┣━ lib.c  
┃   ┣━ lib.h  
┃	┗━ terminal.h  
┣━ CIDs.txt  
┣━ optimazed_params.txt  
┣━ paper.pdf  
┗━ README.md  

## Requirement

python3, gcc

## Usage

$ git clone https://github.com/ohirangosta/similarity_CAN_IDS  
$ cd similarity_CAN_IDS/off-line_learning_phase  
$ python3 output_params.py ../test_data/test_data.log  
$ cd ../on-line_detection_phase/  
$ make  
$ ./similarity_CAN_IDS can0  

## Contribution

## Author

[rangosta](https://github.com/ohirangosta)
