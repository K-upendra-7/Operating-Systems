import random

n = int(input("Enter number of locations: "))
disk = [False] * n

for i in range(n):
    if random.random() < 0.4:
        disk[i] = True

print("\nInitial Disk State:")
print(["1" if x else "0" for x in disk])


print("\nChoose Allocation Method:")
print("1) Sequential Allocation")
print("2) Linked Allocation")
print("3) Indexed Allocation")

choice = int(input("Enter choice: "))

num_files = int(input("Enter number of files: "))


for f in range(1, num_files + 1):
    print(f"\n--- Allocating File F{f} ---")
    size = random.randint(1, 5)
    print("File size:", size)

    if choice == 1:
        allocated = False
        for i in range(n - size + 1):
            if not any(disk[i:i+size]):
                for j in range(i, i+size):
                    disk[j] = True

                print("Allocated blocks:", list(range(i, i+size)))
                print(f"Stored at positions: {i} to {i+size-1}")
                allocated = True
                break

        if not allocated:
            print("Allocation failed (no contiguous space)")

    elif choice == 2:
        free_blocks = [i for i in range(n) if not disk[i]]

        if len(free_blocks) < size:
            print("Allocation failed (not enough space)")
        else:
            blocks = random.sample(free_blocks, size)

            for b in blocks:
                disk[b] = True

            print("Allocated blocks (linked):")
            print(" -> ".join(map(str, blocks)))
            print("Stored at positions:", blocks)

    elif choice == 3:
        free_blocks = [i for i in range(n) if not disk[i]]

        if len(free_blocks) < size + 1:
            print("Allocation failed (need index + data blocks)")
        else:
            index_block = free_blocks[0]
            data_blocks = random.sample(free_blocks[1:], size)

            disk[index_block] = True
            for b in data_blocks:
                disk[b] = True

            print("Index Block:", index_block)
            print("Data Blocks:", data_blocks)
            print(f"{index_block} -> {data_blocks}")

    else:
        print("Invalid choice")

    print("Disk state:", ["1" if x else "0" for x in disk])

    