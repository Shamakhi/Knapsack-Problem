# The dynamic programming algorithm for the knapsack 0-1 problem.


import numpy as np

def knapsack_0_1_dp(v, w, C):
	n = len(v)
	cmax = C
	# Subproblem solutions (two-dimensional array (n + 1)x(C + 1))
	opt = [[0] * (cmax + 1) for _ in range(n + 1)]
	# Base case (i = 0)
	for c in range(0, cmax + 1):
		opt[0][c] = 0
	# Systematically solve all subproblems
	for i in range(0, n):
		for c in range(0, cmax + 1):
			# Use recursion formula
			if w[i] > c:
				# Case 1
				opt[i][c] = opt[i - 1][c]
			else:
				# max(Case 1, Case 2)
				opt[i][c] = max(opt[i - 1][c], v[i] + opt[i - 1][c - w[i]])
	# Solution to largest subproblem
	return opt

def reconstruct(v, w, C, opt):
	n = len(v)
	# Remaining capacity
	cmax = C
	# Items included/excluded
	opt_sol = [None] * n
	# Trace back through the two-dimensional array
	i = n - 1
	while i >= 0:
		if (w[i] <= cmax) and (v[i] + opt[i - 1][cmax - w[i]] >= opt[i - 1][cmax]):
			# Case 2, include item i
			opt_sol[i] = True
			# Reserve space for included item
			cmax = cmax - w[i]
		else: 
			# Exclude item i, capacity unchanged
			opt_sol[i] = False
		i = i - 1
	# Process optimal solution
	print_solution(opt_sol, opt[n - 1][C], v, w, C)

def print_solution(opt_sol, opt_val, v, w, C):
	n = len(opt_sol)
	k = 0
	while k < n and opt_sol[k] == 0:
		k = k + 1

	total_weight = 0
	if k < n:
		print ('(', k, ',', w[k], ',', v[k], ')', sep='', end='')
		total_weight = total_weight + w[k]
		for i in range(k + 1, n):
			if opt_sol[i] == 1:
				total_weight = total_weight + w[i]
				print (' + ', sep='', end='')
				print ('(', i, ',', w[i], ',', v[i], ')', sep='', end='')
	
	print(' => ', '(', total_weight, ',', opt_val, ')', sep='')	

# List of item values
v = [7, 2, 10, 4]
# List of item weights
w = [3, 6, 9, 5]
# Knapsack capacity
C = 15
# opt = knapsack_0_1_dp(v, w, C)
# reconstruct(v, w, C, opt)
v, w = np.loadtxt("knapsack_dataset.txt", dtype=int, unpack=True)
opt = knapsack_0_1_dp(v[1:], w[1:], v[0])
reconstruct(v[1:], w[1:], v[0], opt)

