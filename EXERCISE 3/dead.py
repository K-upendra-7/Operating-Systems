n = int(input("Enter number of processes (n): "))
m = int(input("Enter number of resource types (m): "))

print("\nEnter TOTAL resources in the system:")
total = list(map(int, input(f"Enter {m} values: ").split()))
if len(total) != m:
    print("ERROR: Total resource vector size must match number of resources.")
    exit()

print("\nEnter MAX matrix:")
max_matrix = []
for i in range(n):
    row = list(map(int, input(f"Enter {m} values for Process P{i}: ").split()))
    if len(row) != m:
        print("ERROR: Incorrect number of resource values.")
        exit()
    for j in range(m):
        if row[j] > total[j]:
            print(f"ERROR: Process P{i} max demand exceeds total system resources.")
            exit()
    max_matrix.append(row)

print("\nEnter ALLOCATION matrix:")
allocation = []
for i in range(n):
    row = list(map(int, input(f"Enter {m} values for Process P{i}: ").split()))
    if len(row) != m:
        print("ERROR: Incorrect number of resource values.")
        exit()
    for j in range(m):
        if row[j] > max_matrix[i][j]:
            print(f"ERROR: Allocation cannot exceed maximum demand for Process P{i}.")
            exit()
    allocation.append(row)

# Compute NEED matrix
need = []
for i in range(n):
    row = []
    for j in range(m):
        value = max_matrix[i][j] - allocation[i][j]
        if value < 0:
            print("ERROR: Need cannot be negative.")
            exit()
        row.append(value)
    need.append(row)

# Compute AVAILABLE
allocated_sum = [0] * m
for j in range(m):
    for i in range(n):
        allocated_sum[j] += allocation[i][j]

for j in range(m):
    if allocated_sum[j] > total[j]:
        print("ERROR: Allocated resources exceed total system resources.")
        exit()

available = [total[j] - allocated_sum[j] for j in range(m)]

print("\nAvailable Resources (Calculated):", available)

# Banker's Algorithm
work = available.copy()
finish = [False] * n
safe_sequence = []

print("\nInitial WORK:", work)
step = 1

while True:
    allocated_flag = False
    for i in range(n):
        if not finish[i] and all(need[i][j] <= work[j] for j in range(m)):
            print(f"\nStep {step}: Process P{i} executes")
            print("WORK before:", work)

            for j in range(m):
                work[j] += allocation[i][j]

            print("WORK after:", work)

            finish[i] = True
            safe_sequence.append(f"P{i}")
            allocated_flag = True
            step += 1

    if not allocated_flag:
        break

if all(finish):
    print("\nSYSTEM IS IN SAFE STATE")
    print("Safe Sequence:", " -> ".join(safe_sequence))
else:
    print("\nSYSTEM IS NOT IN SAFE STATE")