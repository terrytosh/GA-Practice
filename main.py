import random

# Algorithm Parameters
population_size = 10
bit_length = 8
target_value = 150
num_generations = 10
mutation_rate = 0.01

# Generate a random bit string "individual" of length 8
def generate_random_individual():
    return ''.join(random.choice('01') for _ in range(bit_length))

# Generate an initial random population of size 10
def generate_initial_population():
    return [generate_random_individual() for _ in range(population_size)]

initial_population = generate_initial_population()
for individual in initial_population:
    print(individual)