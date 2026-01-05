import random
import matplotlib.pyplot as plt
import pandas as pd

# Input
processes = []

n = int(input("Enter number of processes: "))
for i in range(n):
    bt = random.randint(1, 10)
    processes.append({
        'PID': f'P{i+1}',
        'AT': random.randint(0, 10),
        'BT': bt,
        'RT': bt, 
        'Completed': False
    })

# Calculation 
current_time = 0
completed_count = 0
n = len(processes)
timeline = [] 
total_tat = 0
total_wt = 0

def record_history(label, start, end):
    if not timeline:
        timeline.append((label, start, end))
        return
    last_lbl, last_start, last_end = timeline[-1]
    if last_lbl == label and last_end == start:
        timeline[-1] = (label, last_start, end) 
    else:
        timeline.append((label, start, end))

while completed_count < n:
    available = [p for p in processes if p['AT'] <= current_time and not p['Completed']]

    if not available:
        record_history('Idle', current_time, current_time + 1)
        current_time += 1
        continue

    shortest_job = min(available, key=lambda x: (x['RT'], x['AT']))

    shortest_job['RT'] -= 1
    record_history(shortest_job['PID'], current_time, current_time + 1)
    
    current_time += 1

    if shortest_job['RT'] == 0:
        shortest_job['Completed'] = True
        completed_count += 1
        
        shortest_job['CT'] = current_time
        shortest_job['TAT'] = shortest_job['CT'] - shortest_job['AT']
        shortest_job['WT'] = shortest_job['TAT'] - shortest_job['BT']
        
        total_tat += shortest_job['TAT']
        total_wt += shortest_job['WT']

avg_tat = total_tat / n
avg_wt = total_wt / n

# Output
df = pd.DataFrame(processes)
df = df[['PID', 'AT', 'BT', 'CT','WT','TAT']].sort_values(by='PID')

print("Preemptive SJF Results")
print(df.to_string(index=False))
print(f"Average Waiting Time:    {avg_wt:.2f}")
print(f"Average Turnaround Time: {avg_tat:.2f}")

# Plotting
fig, ax = plt.subplots(figsize=(10, 5))
unique_pids = df['PID'].unique()
y_pos = {pid: i for i, pid in enumerate(unique_pids)}

for label, start, end in timeline:
    duration = end - start
    if duration <= 0: continue
    
    if label == 'Idle':
        ax.broken_barh([(start, duration)], (-0.5, len(unique_pids)), facecolors='tab:red', alpha=0.5)
        if duration > 0.5:
            ax.text(start + duration/2, len(unique_pids)/2 - 0.5, "Idle", ha='center', va='center', rotation=90, color='white', fontweight='bold')
    else:
        y = y_pos[label]
        ax.broken_barh([(start, duration)], (y - 0.4, 0.8), facecolors='tab:blue', edgecolor='black')
        if duration >= 1:
            ax.text(start + duration/2, y, label, ha='center', va='center', color='white', fontweight='bold')
    
    ax.text(start, -0.6, str(start), ha='center', va='top', fontsize=8)
    ax.text(end, -0.6, str(end), ha='center', va='top', fontsize=8)

ax.set_yticks(range(len(unique_pids)))
ax.set_yticklabels(unique_pids)
ax.set_xlabel('Time')
ax.set_ylabel('Processes')
ax.set_title('Preemptive SJF Gantt Chart')
ax.grid(True, axis='x', linestyle='--', alpha = 0.6)
plt.tight_layout()
plt.show()




