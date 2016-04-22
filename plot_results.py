import matplotlib.pyplot as plt
from pylab import axes, xlim, ylim
import numpy as np

if __name__ == '__main__':
	lines_01 = [line.rstrip('\n') for line in open('saida.txt')]
	lines_02 = [line.rstrip('\n') for line in open('saida1.txt')]
	lines_03 = [line.rstrip('\n') for line in open('saida2.txt')]
	data_01 = []
	data_02 = []
	data_03 = []
	for i in lines_01:
		data_01.append(float(i))
	for i in lines_02:
		data_02.append(float(i))
	for i in lines_03:
		data_03.append(float(i))  
	# ax = axes()
	# xlim(0,11)
	# ylim(0,2)
	# ax.set_xticks([1.5, 4.5, 7.5])
	# plt.plot(data_01, 'r--', linewidth = 2, label="Global")
	# plt.plot(data_02, 'b', linewidth = 2, label="Local")
	# plt.plot(data_03, 'g--', linewidth = 2, label="Focal")
	# plt.title('Benchmark: Rastrigin')
	plt.title('Boxplot: Rosenbrock e w=0.8') 
	#plt.legend()
	#plt.xlabel(['Global', 'Local', 'Focal'])
	# #plt.yticks(np.arange(-10000, 90000, 10000))
	# plt.yticks(np.arange(-10, 190, 10))
	plt.ylabel('Fitness')
	# plt.xlabel('Iterations')
	fig = plt.figure(1, figsize=(9, 6))
	ax = fig.add_subplot(111)
	plt.hold = True
	boxes=[data_01, data_02, data_03]
	#plt.boxplot(boxes)
	bp = ax.boxplot(boxes)
	ax.set_xticklabels(['Global', 'Local', 'Focal'])
	
	plt.show(bp)
	#plt.show()
	#plt.yticks(np.arange(-10000, 90000, 10000))
	#plt.plot(data_01, 10000, 'r--', data_02, 10000, 'bs')
	#lines = plt.plot(data_01,len(data_01) , data_02, len(data_02)
	#plt.yticks(np.arange(min(data_01)-1000, max(data_01), 11000))
	#plt.show(lines)