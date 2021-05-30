import math
import sys
w_count = 0

ave = 0.8
k = 0.8
W =5
div = 0.358593

Ra = 0
Da = 0
Rn = 0
Dn = 0
Rt = 0

Ta_packet = 1000
Tn_packet = 1000

Ta = float(Ta_packet)/W
Tn = float(Tn_packet)/W

C1 = 1
C2 = 0.5
C3 = 1

id_i = 0

Max_SimpsonCoefficient = 0.0
Min_SimpsonCoefficient = 1000.0
Ave_SimpsonCoefficient = 0.0

SimpsonCoefficient = 0.0
num_intersection = 0
id_count_prev = []

Packet_count = 0
canid_list = list()

True_count = 0
False_count = 0

similarity_set = [0 for i in range(2048)]
'''
similarity_set[0x114]=1
similarity_set[0x116]=1
similarity_set[0x119]=1
similarity_set[0x120]=1
similarity_set[0x122]=1
similarity_set[0x124]=1
similarity_set[0x130]=1
similarity_set[0x131]=1
similarity_set[0x13f]=1
similarity_set[0x180]=1
similarity_set[0x18d]=1
similarity_set[0x18e]=1
similarity_set[0x18f]=1
similarity_set[0x1ac]=1
similarity_set[0x1af]=1
similarity_set[0x1b8]=1
similarity_set[0x1c0]=1
similarity_set[0x1c1]=1
similarity_set[0x1d0]=1
similarity_set[0x1d1]=1
similarity_set[0x1e2]=1
similarity_set[0x1ef]=1
similarity_set[0x3ce]=1
similarity_set[0x3f4]=1
'''
similarity_set[0x80]=1
similarity_set[0x81]=1
similarity_set[0x153]=1
similarity_set[0x164]=1
similarity_set[0x165]=1
similarity_set[0x18f]=1
similarity_set[0x220]=1
similarity_set[0x2a0]=1
similarity_set[0x2b0]=1
similarity_set[0x316]=1
similarity_set[0x329]=1
similarity_set[0x370]=1
similarity_set[0x382]=1
similarity_set[0x43f]=1
similarity_set[0x440]=1
similarity_set[0x4b0]=1
similarity_set[0x4b1]=1
similarity_set[0x545]=1
similarity_set[0x5a2]=1

def overlap_coefficient(num_intersection, WindowSize):
    return float(num_intersection)/WindowSize

def E ():
    global Ra
    global Rn
    global Rt
    return Ra*C1-Rn*C2-Rt*C3

argvs = sys.argv
argc = len(argvs)
if argc < 2:
    print('Usage: python3 %s filename' % argvs[0])
    print('[filename format]\n\t[label] [CAN ID]#[PAYLOAD]\nex)\t1 000#00000000')
    quit()

Data = argvs[1]

with open(Data) as f:
    for log in f:
        log_split = log.split(" ")
        canpacket = log_split[1].split("#")
        canid_list.append(canpacket[0])
        #print(canpacket[0])
        id_i += 1
        Packet_count += 1

        if log_split[0] == "1":
                True_count += 1
        else:
                False_count += 1

        if id_i == W:
            w_count += 1
            id_count = [0 for i in range(2048)]
            for canid in canid_list:
                #print(canid)
                id_count[int(canid, 16)] += 1
                if similarity_set[int(canid, 16)] == id_count[int(canid, 16)] and similarity_set[int(canid, 16)] == 1:
                    num_intersection += 1
                
            # calculate Simpson coefficient
            if 19 > W:
                SimpsonCoefficient = overlap_coefficient(num_intersection, W)
            else:
                SimpsonCoefficient = overlap_coefficient(num_intersection, 19)
            #print("[%d] SimpsonCoefficient=%f"%(w_count, SimpsonCoefficient))

            if SimpsonCoefficient < (ave-k*div) or (ave+k*div) < SimpsonCoefficient:
                # True Positive
                if True_count > False_count:
                    Da += 1
                    Ra = (float(Da)/Ta)*100
                # False Positive
                else:
                    Dn += 1
                    Rn = (float(Dn)/Tn)*100
            
            print("%d %f" % (w_count, SimpsonCoefficient))
            if SimpsonCoefficient > Max_SimpsonCoefficient:
                Max_SimpsonCoefficient = SimpsonCoefficient
            if SimpsonCoefficient < Min_SimpsonCoefficient and SimpsonCoefficient != 0.0:
                Min_SimpsonCoefficient = SimpsonCoefficient
            Ave_SimpsonCoefficient += SimpsonCoefficient

            #list clear
            num_intersection = 0
            canid_list = []
            id_i = 0
            True_count = 0
            False_count = 0

    print("Ra=%f,Rn=%f,Rt=%f"%(Ra,Rn,Rt))
    #print("Max SC=%f, Min SC=%f, Ave SC=%f" % (Max_SimpsonCoefficient, Min_SimpsonCoefficient, Ave_SimpsonCoefficient/(float(w_count))))
