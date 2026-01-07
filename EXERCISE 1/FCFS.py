import random
import matplotlib.pyplot as plt
import pandas as pd

# Input
num_processes = int(input("Enter number of processes: "))
processes = []

for i in range(num_processes):
    processes.append({
        'PID': f'P{i+1}',
        'AT': random.randint(0, 10),
        'BT': random.randint(1, 10)
    })

# Calculation 
processes.sort(key=lambda x: x['AT'])

current_time = 0
total_tat = 0
total_wt = 0
timeline = [] 

for p in processes:

    if current_time < p['AT']:
        timeline.append(('Idle', current_time, p['AT']))
        current_time = p['AT']
    
    p['Start'] = current_time
    p['CT'] = current_time + p['BT']
    p['TAT'] = p['CT'] - p['AT']
    p['WT'] = p['TAT'] - p['BT']
    
    total_tat += p['TAT']
    total_wt += p['WT']
    timeline.append((p['PID'], p['Start'], p['CT']))
    
    current_time = p['CT']

avg_tat = total_tat / len(processes)
avg_wt = total_wt / len(processes)

# Output
df = pd.DataFrame(processes).sort_values(by='PID')
print("FCFS Scheduler")
print(df.to_string(index=False))
print(f"Average Waiting Time:    {avg_wt:.2f}")
print(f"Average Turnaround Time: {avg_tat:.2f}")

# Plot
fig, ax = plt.subplots(figsize=(10, 5))

unique_pids = df['PID'].unique()
y_positions = {pid: i for i, pid in enumerate(unique_pids)}

mid_y = len(unique_pids) / 2 - 0.5

for label, start, end in timeline:
    duration = end - start

    if duration == 0: continue
        
    if label == 'Idle':
        ax.broken_barh([(start, duration)], (-0.5, len(unique_pids)), facecolors='tab:red', alpha=0.5)
        ax.text(start + duration/2, mid_y, "Idle", ha='center', va='center', color='white', fontweight='bold', rotation=90)
    else:
        y = y_positions[label]
        ax.broken_barh([(start, duration)], (y - 0.4, 0.8), facecolors='tab:blue', edgecolor='black')
        ax.text(start + duration/2, y, label, ha='center', va='center', color='white', fontweight='bold')

ax.set_yticks(range(len(unique_pids)))
ax.set_yticklabels(unique_pids)
ax.set_xlabel('Time')
ax.set_ylabel('Process ID')
ax.set_title('Gantt Chart - FCFS')
ax.grid(True, axis='x', linestyle = '--', alpha=0.6)

plt.tight_layout()
plt.show()