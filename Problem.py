from Parameters import Parameters
import numpy as np
from numpy import cos, pi
#from numpy import asfarray

class Problem:

	def cost_function(self, vector):
		parameters = Parameters()
		if parameters.problem_type == "rastrigin":
			result = self.rastrigin(vector)
		elif parameters.problem_type == "rosenbrock":
			result = self.rosenbrock(vector)
		else:
			result = self.sphere(vector)
		return result

	def sphere(self, position):
		n = len(position)
		total = 0.0
		for i in xrange(n):
			total += (position[i] ** 2.0)
		return total

	def rastrigin(self, position):
		n = len(position)
		A=10.
		total = 0.0
		for i in xrange(n):
			parcela = position[i]**2-(A*cos(2*pi*position[i]))
			total = A * n + parcela
		return total
	
	def rosenbrock(self, position):
		''' Search space suggested: -100 to 1000'''	 
	 	x = np.asfarray(position)
	 	total = np.sum(100.0*(x[1:]-x[:-1]**2.0)**2.0) 
	 	return total