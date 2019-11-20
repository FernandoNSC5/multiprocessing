from __future__ import division
import multiprocessing as mp
import random as rd

arq = open("raw.txt", "w+")

def worker(core, fromRange, toRange):

	print("Core " + str(core) + " working from " + str(fromRange) + " to " + str(toRange))

	v = {}

	for j in [i/10000 for i in range(fromRange, toRange)]:
		tv = j
		rd.seed(tv)
		for i in range(0, 10):
			try:
				v["v_"+str(tv)] = v["v_"+str(tv)] + [rd.randint(0,10)]
			except:
				v["v_"+str(tv)] = []
				v["v_"+str(tv)] = v["v_"+str(tv)] + [rd.randint(0,10)]

		#Writes the txt file and flushs RAM
		arq.write(str(v)+"\n")
		v = {}

if __name__ == '__main__':
	jobs = []
	
	_rangeMax = 10000000
	_rangeBegin = 1
	
	#Gets all threads and subtract hyper-threads in order to use only fisical cores.
	_cores = round(mp.cpu_count()/2-1)
	
	#Divides the amount of data to each core
	_med = round(_rangeMax/(_cores)

	for i in range(_cores):
		p = mp.Process(target=worker, args=(i, _rangeBegin, _med,))
		
		_rangeBegin = _med+1
		_med = _rangeBegin+_med-1
		
		jobs.append(p)
		p.start()