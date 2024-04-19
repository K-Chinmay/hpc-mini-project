import time
import multiprocessing

# Simulated function to perform heavy computation (simulating a database query)
def heavy_computation(data_chunk):
    # Simulating heavy computation by sleeping for a random time
    time.sleep(2)
    result = sum(data_chunk)  # Perform some computation on the data chunk
    return result

# Function to divide the data into chunks for parallel processing
def chunk_data(data, num_chunks):
    chunk_size = len(data) // num_chunks
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
    return chunks

if __name__ == "__main__":
    # Simulating a large dataset
    data = list(range(1000000))

    # Number of processes for parallel execution
    num_processes = multiprocessing.cpu_count()

    # Divide the data into chunks
    chunks = chunk_data(data, num_processes)

    # Create a pool of worker processes
    pool = multiprocessing.Pool(processes=num_processes)

    # Perform parallel execution of heavy_computation function on each data chunk
    start_time = time.time()
    results = pool.map(heavy_computation, chunks)
    end_time = time.time()

    # Close the pool of worker processes
    pool.close()
    pool.join()

    # Calculate the total execution time
    total_time = end_time - start_time

    # Output the results and total execution time
    print("Results:", results)
    print("Total Execution Time:", total_time, "seconds")
