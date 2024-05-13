import sys
import random
def read_requests(file_path):
    with open(file_path, 'r') as file:
        requests = [int(line.strip()) for line in file.readlines()]
    return requests

def fcfs(requests, start):
    head_movements = 0
    current_position = start
    for request in requests:
        head_movements += abs(current_position - request)
        current_position = request
    return head_movements
def scan(requests, start):
    head_movements = 0
    current_position = start
    requests.sort()
    upper_requests = [r for r in requests if r >= current_position]
    lower_requests = [r for r in requests if r < current_position][::-1]
    for request in upper_requests:
        head_movements += abs(current_position - request)
        current_position = request
    if lower_requests:
        head_movements += abs(current_position - 0) 
        current_position = 0
    for request in lower_requests:
        head_movements += abs(current_position - request)
        current_position = request
    return head_movements

def optimized_scan(requests, start, total_cylinders):
    head_movements = 0
    current_position = start
    requests.sort()
    
    if start - 0 < total_cylinders - start:
        lower_requests = [r for r in requests if r <= current_position]
        upper_requests = [r for r in requests if r > current_position]
        
        for request in reversed(lower_requests):
            head_movements += abs(current_position - request)
            current_position = request
        if upper_requests:
            head_movements += abs(current_position - 0) 
            current_position = 0
        for request in upper_requests:
            head_movements += abs(current_position - request)
            current_position = request
    else:
        upper_requests = [r for r in requests if r >= current_position]
        lower_requests = [r for r in requests if r < current_position]
        
        for request in upper_requests:
            head_movements += abs(current_position - request)
            current_position = request
        if lower_requests:
            head_movements += abs(current_position - total_cylinders)
            current_position = total_cylinders
            for request in reversed(lower_requests):
                head_movements += abs(current_position - request)
                current_position = request

    return head_movements

def c_scan(requests, start):
    head_movements = 0
    current_position = start
    requests.sort()
    upper_requests = [r for r in requests if r >= current_position]
    lower_requests = [r for r in requests if r < current_position]

    for request in upper_requests:
        head_movements += abs(current_position - request)
        current_position = request
    if lower_requests:
        head_movements += abs(current_position - 4999) + 4999  
        current_position = 0
    for request in lower_requests:
        head_movements += abs(current_position - request)
        current_position = request
    return head_movements

def optimized_c_scan(requests, start, total_cylinders):
    head_movements = 0
    current_position = start
    requests.sort()
    if start - 0 > total_cylinders - start:
        head_movements += abs(current_position - 0)  
        current_position = 0
    upper_requests = [r for r in requests if r >= current_position]
    lower_requests = [r for r in requests if r < current_position]
    for request in upper_requests:
        head_movements += abs(current_position - request)
        current_position = request
    if lower_requests: 
        head_movements += abs(current_position - total_cylinders)  
        current_position = 0
        for request in lower_requests:
            head_movements += abs(current_position - request)
            current_position = request

    return head_movements

def genereate_requests_file(file_path, num_requests):
    with open(file_path, 'w') as file:
        for _ in range(num_requests):
            file.write(str(random.randint(0, 4999)) + "\n")

def main():
    genereate_requests_file("requests.txt", 5000)
    if len(sys.argv) != 3:
        print("Usage: python script.py <start_position> <file_path>")
        return
    start_position = int(sys.argv[1])
    file_path = sys.argv[2]

    requests = read_requests(file_path)
    total_cylinders = 4999  
    print("\noriginal Algorithms: ")
    print("FCFS Total Head Movements:", fcfs(requests, start_position))
    print("SCAN Total Head Movements:", scan(requests, start_position))
    print("C-SCAN Total Head Movements:", c_scan(requests, start_position))
    print("\nOptimized Algorithms: ")
    print("Optimized FCFS Total Head Movements:", fcfs(sorted(requests.copy()), start_position))
    print("Optimized SCAN Total Head Movements:", optimized_scan(requests, start_position, total_cylinders))
    print("Optimized C-SCAN Total Head Movements:", optimized_c_scan(requests, start_position, total_cylinders))



if __name__ == "__main__":
    main()
