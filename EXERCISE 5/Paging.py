import random
import math

page_size = int(input("Enter page (frame) size: "))
process_size = int(input("Enter process size: "))
memory_size = int(input("Enter main memory size: "))

if page_size <= 0 or process_size <= 0 or memory_size <= 0:
    print("Error: All inputs must be positive!")
    exit()
if (page_size & (page_size - 1)) != 0:
    print("Error: Page size must be a power of 2!")
    exit()
if memory_size % page_size != 0:
    print("Error: Memory size must be a multiple of page size!")
    exit()
if process_size > memory_size:
    print("Error: Process size should be less than or equal to main memory size!")
    exit()

num_pages = (process_size + page_size - 1) // page_size
num_frames = memory_size // page_size

if num_pages > num_frames:
    print("Error: Not enough memory to allocate all pages!")
    exit()

offset_bits = int(math.log2(page_size))
page_bits = int(math.ceil(math.log2(num_pages)))
frame_bits = int(math.ceil(math.log2(num_frames)))
physical_bits = frame_bits + offset_bits

print("\nNumber of pages:", num_pages)
print("Number of frames:", num_frames)

free_frames = list(range(num_frames))
page_table = {}

for i in range(num_pages):
    frame = random.choice(free_frames)
    page_table[i] = frame
    free_frames.remove(frame)

print("\nPage Table (Random Allocation):")
for p in page_table:
    print(f"Page {p} -> Frame {page_table[p]}")

print("\nByte -> (Page, Offset) -> Frame -> Physical Address:\n")

for byte in range(process_size):
    page_no = byte // page_size
    offset = byte % page_size
    frame_no = page_table[page_no]

    physical_address = frame_no * page_size + offset

    byte_bin = format(byte, f'0{page_bits + offset_bits}b')
    page_bin = format(page_no, f'0{page_bits}b')
    offset_bin = format(offset, f'0{offset_bits}b')
    frame_bin = format(frame_no, f'0{frame_bits}b')
    physical_bin = format(physical_address, f'0{physical_bits}b')

    print(f"Byte {byte} ({byte_bin}) -> "
          f"(Page {page_no} ({page_bin}), Offset {offset} ({offset_bin})) -> "
          f"Frame {frame_no} ({frame_bin}) -> "
          f"Physical Address {physical_address} ({physical_bin})")