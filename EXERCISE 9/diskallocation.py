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

    plt.grid(True)
    plt.show()


# -------- C-SCAN --------
def cscan(queue, head, start, end, direction):

    left = [x for x in queue if x < head]
    right = [x for x in queue if x >= head]

    left.sort()
    right.sort()

    order = [head]

    if direction == "right":
        order += right
        order.append(end)
        order.append(start)
        order += left

    else:  # left
        left.reverse()
        order += left
        order.append(start)
        order.append(end)
        right.reverse()
        order += right

    # movement (ignore jump)
    total = 0
    for i in range(len(order)-1):
        if (order[i] == end and order[i+1] == start) or \
           (order[i] == start and order[i+1] == end):
            continue
        total += abs(order[i+1] - order[i])

    print("\nC-SCAN")
    print("Service Order:", order)
    print("Total Head Movement:", total)

    plot_graph(order, "C-SCAN Disk Scheduling")


# -------- LOOK --------
def look(queue, head, direction):

    left = [x for x in queue if x < head]
    right = [x for x in queue if x >= head]

    left.sort()
    right.sort()

    order = [head]

    if direction == "right":
        order += right
        left.reverse()
        order += left

    else:
        left.reverse()
        order += left
        order += right

    total = 0
    for i in range(len(order)-1):
        total += abs(order[i+1] - order[i])

    print("\nLOOK")
    print("Service Order:", order)
    print("Total Head Movement:", total)

    plot_graph(order, "LOOK Disk Scheduling")


# -------- C-LOOK --------
def clook(queue, head, direction):

    left = [x for x in queue if x < head]
    right = [x for x in queue if x >= head]

    left.sort()
    right.sort()

    order = [head]

    if direction == "right":
        order += right
        order += left

    else:
        left.reverse()
        order += left
        right.reverse()
        order += right

    # ignore circular jump
    total = 0
    for i in range(len(order)-1):
        if (order[i] > order[i+1] and direction == "right") or \
           (order[i] < order[i+1] and direction == "left"):
            continue
        total += abs(order[i+1] - order[i])

    print("\nC-LOOK")
    print("Service Order:", order)
    print("Total Head Movement:", total)

    plot_graph(order, "C-LOOK Disk Scheduling")


# -------- MAIN --------
start = int(input("Enter start cylinder: "))
end = int(input("Enter end cylinder: "))
qsize = int(input("Enter queue size: "))

queue = [random.randint(start, end) for _ in range(qsize)]
head = random.randint(start, end)

print("\nQueue:", queue)
print("Head:", head)

print("\n----- MENU -----")
print("1. C-SCAN")
print("2. LOOK")
print("3. C-LOOK")

choice = int(input("Enter choice: "))

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

if choice == 1:
    cscan(queue, head, start, end, direction)

elif choice == 2:
    look(queue, head, direction)

elif choice == 3:
    clook(queue, head, direction)

else:
    print("Invalid choice")