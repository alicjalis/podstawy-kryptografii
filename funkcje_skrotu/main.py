import hashlib
import timeit


def compare_hashes(input_text):
    results = {}
    algorithms = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']
    for algorithm in algorithms:
        setup_code = f'''
from hashlib import {algorithm}
input_text = "{input_text}"
        '''
        execution_time = timeit.timeit(f'{algorithm}(input_text.encode()).hexdigest()', setup=setup_code, number=100000)
        hash_result = getattr(hashlib, algorithm)(input_text.encode()).hexdigest()
        results[algorithm.upper()] = {'hash': hash_result, 'length': len(hash_result), 'time': execution_time}
    return results


if __name__ == "__main__":
    input_data = [
        "Lorem",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus convallis arcu a enim venenatis",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus convallis arcu a enim venenatis. Fusce non urna quis nisi commodo sollicitudin",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus convallis arcu a enim venenatis. Fusce non urna quis nisi commodo sollicitudin. Donec convallis nisl vel est suscipit, nec pulvinar dui gravida Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus convallis arcu a enim venenatis. Fusce non urna quis nisi commodo sollicitudin. Donec convallis nisl vel est suscipit, nec pulvinar dui gravida."
    ]

    overall_results = {algorithm: 0 for algorithm in ['MD5', 'SHA1', 'SHA224', 'SHA256', 'SHA384', 'SHA512']}

    for data in input_data:
        print(f"Data Length: {len(data)}")
        results = compare_hashes(data)
        sorted_results = sorted(results.items(), key=lambda x: x[1]['time'])
        print("Results for current text:")
        for algorithm, result in sorted_results:
            print(f"{algorithm}: Length - {result['length']}, Time - {result['time']}, Hash - {result['hash']}")
        print("\n")
        for algorithm, result in results.items():
            overall_results[algorithm] += result['time']

    sorted_overall_results = sorted(overall_results.items(), key=lambda x: x[1])

    print("Overall ranking based on total time:")
    for algorithm, total_time in sorted_overall_results:
        print(f"{algorithm}: Total Time - {total_time}")
