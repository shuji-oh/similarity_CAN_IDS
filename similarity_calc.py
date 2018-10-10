import math
w_count = 0

W = 10
k = 0.8
div = 0.751750
ave = 0.8

Ra = 0
Da = 0
Rn = 0
Dn = 0
Rt = 0

Ta = 1
Tn = 1000

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

def overlap_coefficient(num_intersection, WindowSize):
	return float(num_intersection)/WindowSize

def E ():
	global Ra
	global Rn
	global Rt
	return Ra*C1-Rn*C2-Rt*C3

with open("RandomDoS.log") as f:
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
				if w_count != 1:
					if id_count_prev[int(canid, 16)] != 0 and id_count[int(canid, 16)] != 0:
						num_intersection += 1
				
			# calculate Simpson coefficient
			SimpsonCoefficient = overlap_coefficient(num_intersection, W)
			print("[%d] SimpsonCoefficient=%f"%(w_count, SimpsonCoefficient))

			if SimpsonCoefficient < (ave-k*div) or (ave+k*div) < SimpsonCoefficient:
				# True Positive
				if True_count > False_count:
					Da += 1
					Ra = (float(Da)/Ta)*100
				# False Positive
				else:
					Dn += 1
					Rn = (float(Dn)/Tn)*100
			
			print("[%d] SimpsonCoefficient=%f" % (w_count, SimpsonCoefficient))
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
			id_count_prev = id_count

	print("Ra=%f,Rn=%f,Rt=%f"%(Ra,Rn,Rt))
	print("Max SC=%f, Min SC=%f, Ave SC=%f" % (Max_SimpsonCoefficient, Min_SimpsonCoefficient, Ave_SimpsonCoefficient/(float(w_count))))