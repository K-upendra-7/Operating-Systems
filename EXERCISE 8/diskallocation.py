import random
import matplotlib.pyplot as plt

def plot_graph(order, title):
    plt.plot(order, range(len(order)), marker='o')
    plt.gca().invert_yaxis()
    plt.xlabel("Cylinder Number")
    plt.ylabel("Request Order")
    plt.title(title)
    plt.grid(True)
    plt.show()

def fcfs(queue, head):
    order = [head] + queue
    total = 0
    
    for i in range(len(order)-1):
        total += abs(order[i+1] - order[i])
        
    print("Service Order:", order)
    print("Total Head Movement:", total)
    
    plot_graph(order, "FCFS Disk Scheduling")

def sstf(queue, head):
    requests = queue.copy()
    current = head
    order = [head]
    total = 0

    while requests:
        nearest = min(requests, key=lambda x: abs(x-current))
        total += abs(nearest-current)
        current = nearest
        
        order.append(nearest)
        requests.remove(nearest)

    print("Service Order:", order)
    print("Total Head Movement:", total)

    plot_graph(order, "SSTF Disk Scheduling")

def scan(queue, head, start, end, direction):
    left = [x for x in queue if x < head]
    right = [x for x in queue if x >= head]

    left.sort()
    right.sort()

    order = [head]

    if direction == "left":
        left.reverse()
        order += left
        order.append(start)
        order += right

    else:
        order += right
        order.append(end)
        left.reverse()
        order += left

    total = 0
    for i in range(len(order)-1):
        total += abs(order[i+1]-order[i])

    print("Service Order:", order)
    print("Total Head Movement:", total)

    plot_graph(order, "SCAN Disk Scheduling")



# ---- Main Program ----

start = int(input("Enter start cylinder: "))
end = int(input("Enter end cylinder: "))
qsize = int(input("Enter queue size: "))

queue = [random.randint(start, end) for _ in range(qsize)]
head = random.randint(start, end)

print("\nGenerated Queue:", queue)
print("Head Position:", head)

print("\n----- Disk Scheduling Menu -----")
print("1. FCFS")
print("2. SSTF")
print("3. SCAN")
print("4. Exit")

choice = int(input("Enter choice: "))

if choice == 1:
    fcfs(queue, head)

elif choice == 2:
    sstf(queue, head)

elif choice == 3:
    direction = input("Enter direction (left/right): ")
    scan(queue, head, start, end, direction)
else:
    print("Invalid choice")
