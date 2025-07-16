import time

def cpu_benchmark(iterations):
    start_time = time.time()
    
    # Perform a large number of calculations
    total = 0
    for i in range(iterations):
        total += (i * 3.14159) / (i + 1)  # Some arbitrary computation
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time, total

if __name__ == "_main_":
    iterations = 10**7  # Adjust this number for more or less intensive benchmarking
    elapsed_time, total = cpu_benchmark(iterations)
    
    print(f"Elapsed time for {iterations} iterations: {elapsed_time:.2f} seconds")
    print(f"Total result of computations: {total}")