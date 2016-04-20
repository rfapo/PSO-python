import numpy as np
import random
import time
import math

from Particle import Particle
from Problem import Problem
import Parameters

class Pso:

	def __init__(self):
		self.max_vel = Parameters.max_vel
		self.C1 = Parameters.C1
		self.C2 = Parameters.C2
		self.w = Parameters.w
		self.iterations = Parameters.iterations
		self.population = Parameters.population

	def search(self, iterations, population, low_bound, high_bound, max_vel, C1, C2):
		pop = create_population(population)
		gbest = update_global_best(pop)
		#ite = 1
		problem = Problem()
		for ite in xrange(iterations):
			for particle in pop:
				update_velocity(particle, gbest, max_vel, C1, C2)
				update_position(particle, low_bound, high_bound)
				particle.cost = problem.sphere(particle.position)
				update_personal_best(particle)
			gbest = update_global_best(pop, gbest)
			print "Iteration: ", ite, "Fitness: ", gbest.cost
		return gbest

	def create_population(self, population):
		pop = []
		for particle in xrange(population):
			particle = Particle()
			particle.initialize()
			pop.append(particle)
		return pop

	def update_personal_best(self, particle):
		if particle.cost > particle.best_cost:
			particle.best_cost = particle.cost
			particle.best_position = particle.position

	def update_global_best(self, population, current_best= None):
		population.sort(key=lambda k: k.cost)
		best = population[0]
		if (current_best == None or best.cost <= current_best.cost):
			current_best = Particle()
			current_best = best
			current_best.position = best.best_position
			current_best.cost = best.best_cost
		return current_best

	def update_velocity(self, particle, gbest, max_v, C1, C2):
		#Clerc constrict
		o = C1+C2
		k = 2/ abs(2 - o - math.sqrt(o**2 - o*4))
		for i, value in enumerate(particle.velocity):
			R1 = np.random.uniform(0,1)
			R2 = np.random.uniform(0,1)
			v = particle.velocity[i]	
			v1 = (C1 * R1) * (particle.best_position[i] - particle.position[i])
			v2 = (C2 * R2) * (gbest.position[i] - particle.position[i])
			particle.velocity[i] = k * (v + v1 + v2)
			if particle.velocity[i] > max_v:
				particle.velocity[i] = max_v
			if particle.velocity[i] < (-1 * max_v):
				particle.velocity[i] = -1 * max_v

	def update_position(self, particle, low_bound, high_bound):
		for i, value in enumerate(particle.position):
			particle.position[i] = (value + particle.velocity[i])
			if particle.position[i] > high_bound:
				particle.position[i] = high_bound - abs(value - high_bound)
	  			particle.velocity[i] *= -1.0
	  		if particle.position[i] < low_bound:
				particle.position[i] = low_bound + abs(value - low_bound)
	  			particle.velocity[i] *= -1.0

# if __name__ == "__main__":
# 	##Problem configurations
# 	dimensions = Parameters.dimension
# 	population = Parameters.population
# 	#search space bounds
# 	low_bound = Parameters.low_bound
# 	high_bound = Parameters.high_bound
# 	##Algorithm configurations
# 	iterations = Parameters.iterations
# 	C1 = Parameters.C1
# 	C2 = Parameters.C2
# 	w = Parameters.w
# 	min_vel = Parameters.min_vel
# 	max_v = Parameters.max_v
# 	# pop = create_population(population)
# 	# for particle in pop:
# 	# 	print particle.velocity

# 	time_init = time.time()
# 	best = search(iterations, population, max_v, low_bound, high_bound, C1, C2)
# 	time_end = time.time()
# 	print "Done!"
# 	print "Total time elapsed: %.3f seconds." % (time_end - time_init)
# 	print "Solution: "
# 	print "Best fitness: ", best.cost
# 	print "Best positions: ", best.position