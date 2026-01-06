import random
import matplotlib.pyplot as plt
import pandas as pd

# Input
processes = []

n = int(input("Enter number of processes: "))
for i in range(n):
    processes.append({
        'PID': f'P{i+1}',
        'AT': random.randint(0, 10),
        'BT': random.randint(1, 10),
        'Completed': False
    })

# Calculation
processes.sort(key=lambda x: x['AT'])

current_time = 0
completed_count = 0
timeline = [] 
total_tat = 0
total_wt = 0

while completed_count < n:
    available = []

    for p in processes:
        if p['AT'] <= current_time:
            if not p['Completed']:
                available.append(p)

    if not available:
        remaining = []

        for p in processes:
            if not p['Completed']:
                remaining.append(p)

        next_arrival = min(p['AT'] for p in remaining)
        
        timeline.append(('Idle', current_time, next_arrival))
        current_time = next_arrival
    else:
        shortest_job = min(available, key=lambda x: x['BT'])
        
        start_time = current_time
        completion_time = current_time + shortest_job['BT']
        
        shortest_job['Start'] = start_time
        shortest_job['CT'] = completion_time
        shortest_job['TAT'] = completion_time - shortest_job['AT']
        shortest_job['WT'] = shortest_job['TAT'] - shortest_job['BT']
        shortest_job['Completed'] = True
        
        timeline.append((shortest_job['PID'], start_time, completion_time))
        total_tat += shortest_job['TAT']
        total_wt += shortest_job['WT']
        current_time = completion_time
        completed_count += 1

avg_tat = total_tat / n
avg_wt = total_wt / n

# Output
df = pd.DataFrame(processes)
df = df[['PID', 'AT', 'BT', 'CT','WT','TAT']].sort_values(by='PID')

print("Non Preemptive SJF Results")
print(df.to_string(index=False))
print(f"Average Waiting Time:    {avg_wt: .2f}")
print(f"Average Turnaround Time: {avg_tat: .2f}")

# Plot
fig, ax = plt.subplots(figsize=(10, 5))
unique_pids = df['PID'].unique()
y_pos = {pid: i for i, pid in enumerate(unique_pids)}

for label, start, end in timeline:
    duration = end - start
    if duration <= 0: continue
    
    if label == 'Idle':
        ax.broken_barh([(start, duration)], (-0.5, len(unique_pids)), facecolors='tab:red', alpha=0.5)
        ax.text(start + duration/2, len(unique_pids)/2 - 0.5, "Idle", ha='center', va='center', rotation=90, color='white', fontweight='bold')
    else:
        y = y_pos[label]
        ax.broken_barh([(start, duration)], (y - 0.4, 0.8), facecolors='tab:blue', edgecolor='black')
        ax.text(start + duration/2, y, label, ha='center', va='center', color='white', fontweight='bold')
    
    ax.text(start, -0.6, str(start), ha='center', va='top', fontsize=8)
    ax.text(end, -0.6, str(end), ha='center', va='top', fontsize=8)

ax.set_yticks(range(len(unique_pids)))
ax.set_yticklabels(unique_pids)
ax.set_xlabel('Time')
ax.set_ylabel('Processes')
ax.set_title('Non Preemptive SJF Gantt Chart')
ax.grid(True, axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()



