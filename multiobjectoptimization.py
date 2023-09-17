from Benchmark.Prototype import FunctionOptimization


print("Hello world")

funcTest = FunctionOptimization(10,5)
population = funcTest.generate()

print(funcTest.eveluate(population[0]))
