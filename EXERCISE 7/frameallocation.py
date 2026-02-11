import random
import pandas as pd
import matplotlib.pyplot as plt

# ---------- INPUT ----------
n = int(input("Enter number of processes: "))
total_frames = int(input("Enter total number of frames: "))
min_frames = int(input("Enter minimum frames per process: "))

print("\nChoose Allocation Method:")
print("1. Minimum Allocation")
print("2. Equal Allocation")
print("3. Proportional Allocation")

choice = int(input("Enter choice (1/2/3): "))

processes = [f"P{i+1}" for i in range(n)]
sizes = [random.randint(5, 25) for _ in range(n)]

# ---------- FRAME ALLOCATION ----------
if choice == 1:
    allocated = [min_frames] * n
    title = "Minimum Frame Allocation"

elif choice == 2:
    allocated = [total_frames // n] * n
    title = "Equal Frame Allocation"

elif choice == 3:
    total_size = sum(sizes)
    allocated = [(s * total_frames) // total_size for s in sizes]
    title = "Proportional Frame Allocation"

else:
    print("Invalid choice")
    exit()

used_frames = sum(allocated)
free_frames = total_frames - used_frames

# ---------- TABLE OUTPUT ----------
df = pd.DataFrame({
    "Process": processes,
    "Process_Size(Pages)": sizes,
    "Frames_Allocated": allocated
})

print("\nFrame Allocation Table:\n")
print(df.to_string(index=False))
print(f"\nUnallocated Frames: {free_frames}")

# ---------- STACKED FRAME GRAPH ----------
fig, ax = plt.subplots(figsize=(12, 3))

start = 0
colors = plt.cm.tab20.colors

for i in range(n):
    ax.barh(0, allocated[i], left=start, color=colors[i], label=processes[i])
    ax.text(start + allocated[i]/2, 0, processes[i],
            ha="center", va="center", color="white", fontsize=10)
    start += allocated[i]

# Free frames
if free_frames > 0:
    ax.barh(0, free_frames, left=start, color="gray", label="Free")
    ax.text(start + free_frames/2, 0, "Free", ha="center", va="center")

# ---------- DRAW VERTICAL LINES FOR EACH FRAME ----------
for f in range(total_frames + 1):
    ax.axvline(f, color="black", linewidth=0.3)

ax.set_xlim(0, total_frames)
ax.set_yticks([])
ax.set_xlabel("Frame Number")
ax.set_title(title)

ax.set_xticks(range(0, total_frames + 1))

plt.tight_layout()
plt.show()
