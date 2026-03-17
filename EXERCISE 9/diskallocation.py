import random
import matplotlib.pyplot as plt


# -------- GRAPH FUNCTION --------
def plot_graph(order, title):
    plt.figure(figsize=(12, 6))   # 2:1 ratio

    y = [i/2 for i in range(len(order))]   # scaled Y-axis
    plt.plot(order, y, marker='o')
    plt.gca().invert_yaxis()

    plt.xlabel("Cylinder Number")
    plt.ylabel("Step Number")
    plt.title(title)

    plt.grid(True)
    plt.show()


# -------- C-SCAN (Jump INCLUDED) --------
def cscan(queue, head, start, end, direction):

    left = sorted([x for x in queue if x < head])
    right = sorted([x for x in queue if x >= head])

    order = [head]

    if direction == "right":
        order += right
        order.append(end)
        order.append(start)
        order += left

    else:  # left
        order += left[::-1]
        order.append(start)
        order.append(end)
        order += right[::-1]

    # INCLUDE jump → no skipping
    total = 0
    for i in range(len(order)-1):
        total += abs(order[i+1] - order[i])

    print("\nC-SCAN (Jump Included)")
    print("Service Order:", order)
    print("Total Head Movement:", total)

    plot_graph(order, "C-SCAN Disk Scheduling")


# -------- LOOK --------
def look(queue, head, direction):

    left = sorted([x for x in queue if x < head])
    right = sorted([x for x in queue if x >= head])

    order = [head]

    if direction == "right":
        order += right
        order += left[::-1]

    else:
        order += left[::-1]
        order += right

    total = 0
    for i in range(len(order)-1):
        total += abs(order[i+1] - order[i])

    print("\nLOOK")
    print("Service Order:", order)
    print("Total Head Movement:", total)

    plot_graph(order, "LOOK Disk Scheduling")


# -------- C-LOOK (Jump INCLUDED) --------
def clook(queue, head, direction):

    left = sorted([x for x in queue if x < head])
    right = sorted([x for x in queue if x >= head])

    order = [head]

    if direction == "right":
        order += right
        order += left   # circular jump happens here

    else:
        order += left[::-1]
        order += right[::-1]  # circular jump happens here

    # INCLUDE jump
    total = 0
    for i in range(len(order)-1):
        total += abs(order[i+1] - order[i])

    print("\nC-LOOK (Jump Included)")
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

d = int(input("Enter direction: "))

if d == 1:
    direction = "left"
elif d == 2:
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