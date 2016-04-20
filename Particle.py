import numpy as np
from Problem import Problem
from Parameters import Parameters
class Particle(Problem):

	def __init__(self):

		self.position = []
		self.velocity = []
		self.cost = 0.0
		self.best_position = []
		self.best_cost = 0.0
	 
	def set_position(self, position):
		self.position = position

	def set_best_position(self, best_position):
		self.best_position = best_position

	def set_cost(self, cost):
		self.cost = cost

	def set_best_cost(self, best_cost):
		self.best_cost = best_cost

	def set_velocity(self, velocity):
		self.velocity = velocity

	def initialize(self):
		problem = Problem()
		parameters = Parameters()
		problem_type = parameters.problem_type
		low_bound, high_bound = parameters.set_bounds(problem_type)
		self.position = np.random.uniform(low_bound, high_bound, parameters.dimension)
		self.velocity = np.random.uniform(parameters.min_vel, parameters.max_vel, parameters.dimension)
		self.cost = problem.cost_function(self.position)
		self.best_position = self.position[:]
		self.best_cost = self.cost

