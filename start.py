import numpy as np

state = np.array([1, 1j])

norm = np.linalg.norm(state)
state = state / norm

prob_0 = np.abs(state[0])**2
prob_1 = np.abs(state[1])**2

print("Quantum state:", state)
print("Probability of measuring |0>:", prob_0)
print("Probability of measuring |1>:", prob_1)
print("Check total probability =", prob_0 + prob_1)
