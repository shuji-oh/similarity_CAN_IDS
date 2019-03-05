test_data.log
====

### log format

[labels] 	[CAN_messages]  
0 			080#0017dc09161116bb  
0 			081#408487000000006b  
0 			165#0008800000000880  
. 			.  
.			.  
.			.  

[labels]		0:Normal message, 1:DoS Attack message  
[CAN_messages] 	[CAN ID]#[Data Fields]  

### candump_format2similarity_CAN_IDS_format command  

$ cat candump-2019-xx-xx_xxxxxx.log | awk '{print 0,$3}' > test_data.log  
