# The standard backtracing algorithm for the knapsack 0-1 problem.
# import numpy as np

def knapsack(i, sol, val, opt_sol, opt_val, w_left, v, w, C):
	# Base case
	if i == len(sol):
		# Check if better than current best
		if val > opt_val:
			# Update optimal value and solution
			opt_val = val
			for k in range(0, len(sol)):
				opt_sol[k] = sol[k]
	else:
		# Generate candidates
		for k in range(0, 2):
			# Check constraints (pruning)
			if k * w[i] <= w_left:
				# Expand partial solution
				sol[i] = k
				# Update remaining capacity
				w_left = w_left - k * w[i]
				# Update partial value
				val = val + k * v[i]
				# Expand partial solution
				opt_val = knapsack(i + 1, sol, val, opt_sol, opt_val, w_left, v, w, C)
	return opt_val
 
def print_solution(opt_sol, opt_val, v, w, C):
	n = len(opt_sol)
	k = 0
	while k < n and opt_sol[k] == 0:
		k = k + 1

	total_weight = 0
	if k < n:
		print ('(', w[k], ',', v[k], ')', sep='', end='')
		total_weight = total_weight + w[k]
		for i in range(k + 1, n):
			if opt_sol[i] == 1:
				total_weight = total_weight + w[i]
				print (' + ', sep='', end='')
				print ('(', w[i], ',', v[i], ')', sep='', end='')
	
	print(' => ', '(', total_weight, ',', opt_val, ')', sep='')	

def knapsack_0_1(v, w, C):
	sol = [None] * len(v)
	opt_sol = [None] * len(v)
	opt_val = knapsack(0, sol, 0, opt_sol, 0, C, v, w, C)
	print_solution(opt_sol, opt_val, v, w, C)
#	print(opt_val)

# List of item values
v = [7, 2, 10, 4]
# List of item weights
w = [3, 6, 9, 5]
# Knapsack capacity
C = 15
# v, w = np.loadtxt("knapsack_dataset.txt", unpack=True)
knapsack_0_1(v, w, C)
