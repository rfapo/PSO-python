class Parameters:
	def __init__(self):
		self.topology = "global"
		'''Set problem: sphere, rotated rastrigin, rosenbrock'''
		self.problem_type = "rastrigin"
		# low_bound = -100.0
		# high_bound = 100.0
		self.low_bound = None
		self.high_bound = None
		self.dimension = 30
		self.min_vel = -1.0
		self.max_vel = 1.0

		## PSO parameters ##
		# PSO Types: basic, basic_with_weight, inertia or constricted
		self.pso_type = "inertia"
		#max_v = 0.054705633519
		#max_v = 0.053141592653589793
		self.max_v = 0.053141592653589793
		self.C1 = 2.05
		self.C2 = 2.05
		self.w = 0.8
		self.iterations = 10000
		self.population = 30

	def set_bounds(self, problem_type):
		if problem_type == "rastrigin":
			self.low_bound = -5.2
			self.high_bound = 5.0
		else:
			self.low_bound = -100.0
			self.high_bound = 100.0
		return self.low_bound, self.high_bound