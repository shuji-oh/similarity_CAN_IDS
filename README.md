similarity_CAN_IDS: Normal and Malicious Sliding Windows Similarity Analysis Method for Fast and Accurate IDS against DoS Attacks on In-Vehicle Networks
====

[![Build Status](https://travis-ci.com/shuji-oh/similarity_CAN_IDS.svg?token=Pqsitpmqbb4Dofx7SdpB&branch=master)](https://travis-ci.com/shuji-oh/similarity_CAN_IDS)

## Overview

The similarity_CAN_IDS is a state-of-the-art DoS attacks detection method on CAN bus.

[Shuji Ohira, Araya Kibrom Desta, Ismail Arai, Hiroyuki Inoue, Kazutoshi Fujikawa, "Normal and Malicious Sliding Windows Similarity Analysis Method for Fast and Accurate IDS against DoS Attacks on In-Vehicle Networks.", IEEE Access, Vol.8, pp.42422-42435, 2020.](https://ieeexplore.ieee.org/document/9007444) 

```
@article{ohira2020similarity_based_IDS,
  title={Normal and Malicious Sliding Windows Similarity Analysis Method for Fast and Accurate IDS against DoS Attacks on In-Vehicle Networks},
  author={Ohira, Shuji and Araya, Kibrom Desta and Arai, Ismail and Inoue, Hiroyuki and Fujikawa, Kazutoshi},
  journal={IEEE Access},
  volume={8},
  pages={42422--42435},
  year={2020},
  publisher={IEEE}
}
```

## Description

We demonstrated that an entropy_CAN_IDS (conventional method) cannot detect an entropy-manipulated attack in which an adversary adjusts the entropy of a DoS attack to a normal value. Thus, we proposed the similarity_CAN_IDS that is a state-of-the-art detection method on the CAN bus. The proposed method use not entropy but similarity to detect intrusion detection.

## Directory Structure

similarity_CAN_IDS  
┣━ off-line_learning_phase  
┃	┣━ README.md  
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
┗━ README.md  

## Requirement

python3, gcc

## Usage

```shell
$ git clone https://github.com/shuji-oh/similarity_CAN_IDS  
$ cd similarity_CAN_IDS/off-line_learning_phase  
$ python3 output_params.py ../test_data/test_data.log  
$ cd ../on-line_detection_phase/  
$ make  
$ ./similarity_CAN_IDS can0  
```

## Contribution

## Author

[shuji-oh](https://github.com/shuji-oh)
