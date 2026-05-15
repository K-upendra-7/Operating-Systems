# OS Lab Algorithms

An academic codebase containing Python implementations and Jupyter Notebooks for various Operating System algorithms, including CPU scheduling, deadlock detection, memory management, and disk scheduling.

## 📂 Project Structure

```text
.
├── src/                  # Pure Python implementations of OS algorithms
├── notebooks/            # Jupyter notebooks with visual outputs and step-by-step executions
├── docs/                 # Lab records and documentation
├── data/                 # Any required datasets or input files
└── scripts/              # Helper scripts
```

## 🛠️ Technologies Used

- **Python 3.x**: Core programming language.
- **Jupyter Notebook**: For interactive execution and data visualization.
- **Pandas**: Tabular representation of processes and results.
- **Matplotlib**: Generating Gantt charts and memory allocation diagrams.

## ⚙️ Setup Instructions

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd Operating-Systems
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install the required dependencies:
   ```bash
   pip install pandas matplotlib jupyter
   ```

## 🚀 How to Run

- **Python Scripts**: Navigate to the `src/` directory and execute the desired algorithm. For example:
  ```bash
  python src/exercise_1/FCFS.py
  ```
- **Jupyter Notebooks**: Start the Jupyter server and open the files in the `notebooks/` directory.
  ```bash
  jupyter notebook
  ```

## 📚 Implemented Algorithms

- **CPU Scheduling**: FCFS, SJF (Preemptive & Non-Preemptive), Priority Scheduling, Round Robin.
- **Deadlock Management**: Banker's Algorithm.
- **Memory Management**: Paging, Page Replacement Algorithms.
- **Disk Scheduling**: FCFS, C-SCAN, Disk Allocation Methods.
