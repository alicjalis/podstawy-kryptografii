import hashlib
import time

def compare_hashes(file_path, algorithm, num_measurements=100):
    total_elapsed_time = 0
    for _ in range(num_measurements):
        start_time = time.time()
        with open(file_path, 'rb') as file:
            file_content = file.read()
            if algorithm == 'md5':
                hash_value = hashlib.md5(file_content).hexdigest()
            elif algorithm == 'sha1':
                hash_value = hashlib.sha1(file_content).hexdigest()
            elif algorithm == 'sha224':
                hash_value = hashlib.sha224(file_content).hexdigest()
            elif algorithm == 'sha256':
                hash_value = hashlib.sha256(file_content).hexdigest()
            elif algorithm == 'sha384':
                hash_value = hashlib.sha384(file_content).hexdigest()
            elif algorithm == 'sha512':
                hash_value = hashlib.sha512(file_content).hexdigest()
        end_time = time.time()
        elapsed_time = end_time - start_time
        total_elapsed_time += elapsed_time
    average_elapsed_time = total_elapsed_time / num_measurements
    return hash_value, average_elapsed_time

file_paths = ["text_1MB.txt", "text_3MB.txt", "text_10MB.txt"]
algorithms = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']
num_measurements = 5

total_times = {algorithm: 0 for algorithm in algorithms}

for file_path in file_paths:
    print(f"Testing for file: {file_path}")
    for algorithm in algorithms:
        _, average_elapsed_time = compare_hashes(file_path, algorithm, num_measurements)
        print(f"{algorithm}, Average Time: {average_elapsed_time:.6f} seconds")
        total_times[algorithm] += average_elapsed_time
    print()

print("Total times for each algorithm:")
for algorithm, total_time in total_times.items():
    print(f"{algorithm}, Total Time: {total_time:.6f} seconds")