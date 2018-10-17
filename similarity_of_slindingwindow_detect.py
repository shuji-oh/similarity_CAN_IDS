# -+- coding: utf-8 -*-
import sys
import random	#Random module
import math

# Ta is attack log total packet num, Tn is normal log total packet num
#Ta_packet = 1000
#Tn_packet = 57001
Ta_packet = 1000
Tn_packet = 1000

# Three weighted parameters
C1 = 1
C2 = 0.5
C3 = 1

def overlap_coefficient(num_intersection, WindowSize):
	return float(num_intersection)/WindowSize

# define energy function
def function_E(Ra, Rn, Rt):
	global C1
	global C2
	global C3
	return Ra*C1-Rn*C2-Rt*C3

def SimilarityBased_IntrusionDetect(Test_Data, k, div, WindowSize, similarity_set):
	
	# Ra is detection rate attack blocks 
	# Rn is detection rate normal blocks
	# Rt is detection time
	Ra = 0
	Rn = 0
	Rt = 0
	Da = 0
	Dn = 0
	ave = 0.8
	w_count = 0
	id_i = 0
	True_count = 0
	False_count = 0
	canid_list = list()
	labels = list()
	global Ta_packet
	global Tn_packet
	Ta = Ta_packet/WindowSize
	Tn = Tn_packet/WindowSize

	# proposed method
	num_intersection = 0
	id_count_prev = []
	
	with open(Test_Data) as Is:
		# calculate Ra, Rn, Rt
		for I in Is:
			# create canid list of WindowSize
			I_spt =	I.split(" ")
			canpacket = I_spt[1].split("#")
			canid_list.append(canpacket[0])
			if I_spt[0] == "1":
				True_count += 1
			else:
				False_count += 1
			#print(labels)
			#print(canpacket[0])
			id_i += 1

			# if canid_list of WindowSize is created,
			# similarity Simpson Coefficient is calculated.
			if id_i == WindowSize:
				#print(canid_list)
				w_count += 1
				id_count = [0 for i in range(2048)]
				for canid in canid_list:
					id_count[int(canid, 16)] += 1
					if w_count != 1:
						if similarity_set[int(canid, 16)] != 0 and id_count[int(canid, 16)] != 0:
							num_intersection += 1
				
				# calculate Simpson coefficient
				SimpsonCoefficient = overlap_coefficient(num_intersection, WindowSize)
				print("[%d] SimpsonCoefficient=%f"%(w_count, SimpsonCoefficient))

				# perform Intrusion Detection using Sliding Similarity
				if SimpsonCoefficient < (ave-k*div) or (ave+k*div) < SimpsonCoefficient:
					# True Positive
					if True_count >= False_count:
						Da += 1
						Ra = (float(Da)/Ta)*100
					# False Positive
					else:
						Dn += 1
						Rn = (float(Dn)/Tn)*100

				num_intersection = 0
				canid_list = []
				id_i = 0
				True_count = 0
				False_count = 0
	#print("W=%d, Ta=%d, Tn=%d, Da=%d, Dn=%d"%(WindowSize, Ta, Tn, Da, Dn))
	return Ra, Rn, Rt

def SimulatedAnnealing_Optimize(DoS_Data, T=10000, cool=0.99):
	# init random value
	#vec = random.randint(-2,2)
	k_best		= 0.8
	div_best	= random.random()
	W_best		= random.randint(5,70)
	#Ra, Rn, Rt 	= SimilarityBased_IntrusionDetect(DoS_Data, k_best, div_best, W_best)
	Ra, Rn, Rt 	= 0, 0, 0
	e_best		= function_E(Ra, Rn, Rt)
	e_prev 		= function_E(Ra, Rn, Rt)-1

	canid_list = list()
	id_i = 0

	#print("Ra=%f,Rn=%f,Rt=%f"%(Ra,Rn,Rt))
	#print("E_best=%f"%e_best)

	print("init_Param:Deviation=%f,WindowSize=%d" %(div_best, W_best))

	while T > 0.0001 and e_prev < e_best:
		# row 7 in paper
		e_next_maxima = 0.0
		W_count = 0
		best_set = [0 for i in range(2048)]
		temp_set = [0 for i in range(2048)]

		div_next = random.random()
		W_next = random.randint(W_best-10, W_best+10)

		# row 8 in paper
		with open(DoS_Data) as Is:
			for best_window in range(0, int(Tn_packet/W_next)):
				for I in Is:
					I_spt =	I.split(" ")
					canpacket = I_spt[1].split("#")
					canid_list.append(canpacket[0])

					id_i += 1

					if id_i == W_next:
						for canid in canid_list:
							# 類似度を比較する集合を算出
							temp_set[int(canid, 16)] = 1
						if best_window == W_count:
							Ra, Rn, Rt = SimilarityBased_IntrusionDetect(DoS_Data, k_best, div_next, W_next, temp_set)
							e_next = function_E(Ra, Rn, Rt)
							if e_next_maxima < e_next:
								e_next_maxima = e_next
								best_set = temp_set
						W_count += 1
						id_i = 0
						canid_list = list()
						temp_set = [0 for i in range(2048)]
		for canid in range(0, 2048):
			if best_set[canid] == 1:
				print("[WindowSize=%d], %x"%(W_next, canid))
		e_next = e_next_maxima
		print("Ra=%f,Rn=%f,Rt=%f,Precision=%f"%(Ra,Rn,Rt,float(Ra)/(Ra+Rn)))
		#print("E=%f,E_best=%f"%(e_next,e_best))

		# calcurate probability from templature.
		p = pow(math.e, -abs(e_next - e_prev)/float(T))
		#print("[%f]Probability=%f"%(T, p))

		# 変更後のコストが小さければ採用する。
		# コストが大きい場合は確率的に採用する。
		if random.random() < p:
			div_prev 	= div_next
			W_prev 		= W_next
			e_prev 		= e_next
			if e_prev > e_best:
				div_best 	= div_prev
				W_best 		= W_prev
				e_best 		= e_prev

		# cool down
		T = T * cool

	return div_best, W_best

if __name__ == '__main__':
	argvs = sys.argv
	argc = len(argvs)
	if argc < 2:
		print('Usage: python3 %s filename' % argvs[0])
		print('[filename format]\n\t[label] [CAN ID]#[PAYLOAD]\nex)\t1 000#00000000')
		quit()

	DoS_Data = argvs[1]
	div, WindowSize = SimulatedAnnealing_Optimize(DoS_Data, T=10000, cool=0.99)
	print("Optimazed Param:Deviation=%f, WindowSize=%d" %(div, WindowSize))
