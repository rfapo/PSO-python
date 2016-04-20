import numpy as np
import random
import time
import math
from itertools import cycle
import matplotlib.pyplot as plt

from Particle import Particle
from Problem import Problem
from Parameters import Parameters

def search(iterations, population, low_bound, high_bound, max_vel, C1, C2, topology, pso_type):
	problem = Problem()
	fitness = []
	pop = create_population(population)
	collection = list(enumerate(pop, start=0))
	gbest = update_global_best(pop)
	lbest = gbest
	fbest = gbest
	for ite in xrange(iterations):
		for i, particle in collection:

			if topology == "local":
				lbest = update_local_best(pop, i, lbest)
				update_velocity(particle, lbest, max_vel, C1, C2, ite, pso_type)
			elif topology == "focal":
				fbest = update_local_best(pop, i, fbest)
				update_velocity(particle, fbest, max_vel, C1, C2, ite, pso_type)
			else:
				update_velocity(particle, gbest, max_vel, C1, C2, ite, pso_type)	

			update_position(particle, low_bound, high_bound)
			particle.cost = problem.sphere(particle.position)
			update_personal_best(particle)
		gbest = update_global_best(pop, gbest)
		print "Iteration: ", ite, "Fitness: ", gbest.cost
		fitness.append(gbest.cost)
	return gbest, fitness

def create_population(population):
	pop = []
	for particle in xrange(population):
		particle = Particle()
		particle.initialize()
		pop.append(particle)
	return pop

def update_personal_best( particle):
	if particle.best_cost >= particle.cost:
		particle.best_cost = particle.cost
		particle.best_position = particle.position[:]

def update_global_best( population, current_best= None):
	population.sort(key=lambda k: k.cost)
	best = population[0]
	if (current_best == None or best.cost <= current_best.cost):
		current_best = Particle()
		current_best = best
		current_best.position = best.best_position[:]
		current_best.cost = best.cost
	return current_best

def update_local_best(pop, i, lbest):
	neighborhoods = []
	if i != len(pop) - 1:
		neighborhoods.append(pop[i-1])
		neighborhoods.append(pop[i])
		neighborhoods.append(pop[i+1])
	else:
		neighborhoods.append(pop[i-1])
		neighborhoods.append(pop[i])
		neighborhoods.append(pop[0])
	lbest = update_global_best(neighborhoods, lbest)
	return lbest

def update_focal_best(pop, i, fbest):
	neighborhoods = []
	focus_best = None
	if pop[i] == pop[0]:
		for i in xrange(len(pop)):
			neighborhoods = []
			neighborhoods.append(pop[0])
			neighborhoods.append(pop[i])
			focus_best = update_global_best(neighborhoods, lbest)
	for i in xrange(len(pop)):
		neighborhoods = []
		neighborhoods.append(focus_best)
		neighborhoods.append(pop[i])
		fbest = update_global_best(neighborhoods, lbest)
	fbest = update_global_best(neighborhoods, lbest)
	return fbest

def update_velocity(particle, gbest, max_v, C1, C2, ite, pso_type):
	
	for i, value in enumerate(particle.velocity):
		R1 = np.random.uniform(0,1)
		R2 = np.random.uniform(0,1)
		v = value	
		v1 = (C1 * R1) * (particle.best_position[i] - particle.position[i])
		v2 = (C2 * R2) * (gbest.position[i] - particle.position[i])
		if pso_type == "inertia":
			w = inertia_weight(ite)
			particle.velocity[i] = w * v + v1 + v2
		elif pso_type == "constricted":
			k = clerc_constrict(C1, C2)
			particle.velocity[i] = k * (v + v1 + v2)
		elif pso_type == "basic_with_weight":
			parameters = Parameters()
			particle.velocity[i] = parameters.w * v + v1 + v2
		else:
			particle.velocity[i] = v + v1 + v2			
		if particle.velocity[i] > max_v:
			particle.velocity[i] = max_v
		if particle.velocity[i] < (-1.0 * max_v):
			particle.velocity[i] = -1.0 * max_v

def clerc_constrict(C1, C2):
	o = C1+C2
	k = 2.0/ abs(2.0 - o - math.sqrt(o**2.0 - o*4.0))
	return k

def inertia_weight(ite):
	w_init = 0.9
	w_end = 0.4
	w = ((w_init - w_end) * (9999 - ite)/9999) + w_end
	return w 

def update_position(particle, low_bound, high_bound):
	for i, value in enumerate(particle.position):
		particle.position[i] = value + particle.velocity[i]
		if particle.position[i] > high_bound:
			particle.position[i] = high_bound - abs(particle.position[i] - high_bound)
  			particle.velocity[i] *= -1.0
  		elif particle.position[i] < low_bound:
			particle.position[i] = low_bound + abs(particle.position[i] - low_bound)
  			particle.velocity[i] *= -1.0

if __name__ == "__main__":
	## Configurations ##
	parameters = Parameters()
	dimensions = parameters.dimension
	population = parameters.population
	problem_type = parameters.problem_type
	# Search space bounds
	low_bound, high_bound = parameters.set_bounds(problem_type)
	# Algorithm configurations
	iterations = parameters.iterations
	C1 = parameters.C1
	C2 = parameters.C2
	w = parameters.w
	min_vel = parameters.min_vel
	max_v = parameters.max_v
	topology = parameters.topology
	pso_type = parameters.pso_type
	## End Configurations ##
	time_init = time.time()
	best, fitness = search(iterations, population, low_bound, high_bound, max_v, C1, C2, topology, pso_type)
	time_end = time.time()
	print "Done!"
	print "Total time elapsed: %.3f seconds." % (time_end - time_init)
	print "Solution: "
	print "low_bound: ", low_bound, " high_bound: ", high_bound
	print "Best fitness: ", best.cost
	print "Best positions: ", best.position
	# plt.plot(fitness)
	plt.boxplot(fitness)
	# plt.ylabel('Fitness')
	# plt.xlabel('Iterations')
	plt.show()