import random
import matplotlib.pyplot as plt
import pandas as pd

method = input("Enter allocation method (first / best / worst): ").lower()
n_blocks = int(input("Enter number of blocks: "))
n_files  = int(input("Enter number of files: "))

block_status = [random.randint(0, 1) for _ in range(n_blocks)]
block_sizes  = [random.randint(10, 60) if b == 0 else 0 for b in block_status]
file_sizes   = [random.randint(5, 30) for _ in range(n_files)]

allocation = [-1] * n_files
fragment   = [0] * n_files
used       = [False] * n_blocks

free_blocks = [(block_sizes[i], i) for i in range(n_blocks) if block_status[i] == 0]

if method == "best":
    free_blocks.sort()
elif method == "worst":
    free_blocks.sort(reverse=True)

for i in range(n_files):
    for size, idx in free_blocks:
        if size >= file_sizes[i] and not used[idx]:
            allocation[i] = idx
            fragment[i] = size - file_sizes[i]
            used[idx] = True
            break

print("\nFile_no  File_size  Block_no  Block_size  Fragment")
print("-"*50)
for i in range(n_files):
    if allocation[i] != -1:
        print(f"{i+1:<8}{file_sizes[i]:<11}{'B'+str(allocation[i]+1):<10}{block_sizes[allocation[i]]:<12}{fragment[i]}")
    else:
        print(f"{i+1:<8}{file_sizes[i]:<11}{'NA':<10}{'NA':<12}{'NA'}")

block_to_file = {}
for i, b in enumerate(allocation):
    if b != -1:
        block_to_file[b] = f"P{i+1}"

fig, ax = plt.subplots(figsize=(4, 9))
ax.set_xlim(0, 1)
ax.set_ylim(0, n_blocks)
ax.axis("off")

for i in range(n_blocks):
    y = n_blocks - i - 1

    ax.text(-0.05, y + 0.5, f"B{i+1}", ha="right", va="center", weight="bold")

    if block_status[i] == 1:
        ax.add_patch(plt.Rectangle((0, y), 1, 1, color="yellow", ec="black"))
        ax.text(0.5, y + 0.5, "USED", ha="center", va="center", weight="bold")

    elif used[i]:
        ax.add_patch(plt.Rectangle((0, y), 1, 1, color="green", ec="black"))
        label = block_to_file.get(i, "")
        ax.text(0.5, y + 0.5, f"{label}\n{block_sizes[i]} KB",
                ha="center", va="center", fontsize=10, weight="bold")

    else:
        ax.add_patch(plt.Rectangle((0, y), 1, 1, color="white", ec="black"))
        ax.text(0.5, y + 0.5, f"{block_sizes[i]} KB", ha="center", va="center")

ax.set_title(
    f"Memory Allocation using {method.upper()} Fit (OS View)",
    fontsize=13, fontweight="bold", pad=15
)

plt.show()