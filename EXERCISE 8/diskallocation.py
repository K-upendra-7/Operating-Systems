import random
import matplotlib.pyplot as plt


# -------- GRAPH FUNCTION --------
def plot_graph(order, title):
    plt.figure(figsize=(12,6))   # 2:1 ratio

    plt.plot(order, range(len(order)), marker='o')
    plt.gca().invert_yaxis()

    plt.xlabel("Cylinder Number")
    plt.ylabel("Step Number")
    plt.title(title)
    
    plt.show()


# -------- FCFS --------
def fcfs(queue, head):
    order = [head] + queue
    total = 0
    
    for i in range(len(order)-1):
        total += abs(order[i+1] - order[i])
        
    print("\nFCFS")
    print("Service Order:", order)
    print("Total Head Movement:", total)
    
    plot_graph(order, "FCFS Disk Scheduling")


# -------- SSTF --------
def sstf(queue, head):
    requests = queue.copy()
    current = head
    order = [head]
    total = 0

    for _ in range(len(requests)):
        nearest = requests[0]
        min_dist = abs(nearest - current)

        for r in requests:
            if abs(r - current) < min_dist:
                nearest = r
                min_dist = abs(r - current)

        total += min_dist
        current = nearest

        order.append(nearest)
        requests.remove(nearest)

    print("\nSSTF")
    print("Service Order:", order)
    print("Total Head Movement:", total)

    plot_graph(order, "SSTF Disk Scheduling")


# -------- SCAN --------
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
        total += abs(order[i+1] - order[i])

    print("\nSCAN")
    print("Service Order:", order)
    print("Total Head Movement:", total)

    plot_graph(order, "SCAN Disk Scheduling")


# -------- MAIN --------
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

choice = int(input("Enter choice: "))


if choice == 1:
    fcfs(queue, head)

elif choice == 2:
    sstf(queue, head)

elif choice == 3:
    print("\nDirection:")
    print("1. Left")
    print("2. Right")

    d = input("Enter direction: ")

    if d == "1":
        direction = "left"
    elif d == "2":
        direction = "right"
    else:
        print("Invalid direction")
        exit()

    scan(queue, head, start, end, direction)

else:
    print("Invalid choice")