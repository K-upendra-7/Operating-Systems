# (22PC2IT202) OPERATING SYSTEMS LABORATORY

1. Simulate the following CPU scheduling algorithms 
   - a. FCFS 
   - b. SJF Preemptive
   - c. SJF Non Preemptive
2. Simulate the following CPU scheduling algorithms 
   - a. Priority 
   - b. Round robin 
3. Simulate Bankers Algorithm for Deadlock Avoidance.
4. Implementation of the following Memory Allocation Methods for fixed partition 
   - a. First Fit 
   - b. Worst Fit 
   - c. Best Fit 
5. Implementation of Paging Technique of Memory Management 
6. Implementation of the following Page Replacement Algorithms 
   - a. FIFO 
   - b. LRU 
   - c. optimal 
7. Simulate frame allocation Methods. 
   - a. minimum number of frames 
   - b. equal allocation 
   - c. proportional allocation 
8. Simulate the following Disk scheduling algorithms.  
   - a. FCFS 
   - b. SSTF 
   - c. SCAN 
9. Simulate the following Disk scheduling algorithms.  
   - a. C-SCAN 
   - b. LOOK 
   - c. C-LOOK  
10. Simulate all file allocation strategies.  
   - a. Sequential 
   - b. Indexed 
   - c. Linked. 

---

## Python Installation and Setup Guide

### Prerequisites
This project requires Python 3.x and several Python libraries to run the Jupyter notebooks.

### Step 1: Install Python

#### For Windows:
1. **Download Python:**
   - Visit the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
   - Download the latest Python 3.x installer for Windows

2. **Run the Installer:**
   - Double-click the downloaded `.exe` file
   - **IMPORTANT:** Check the box "Add Python to PATH" at the bottom of the installer
   - Click "Install Now"
   - Wait for the installation to complete
   - Click "Close" when finished

3. **Verify Installation:**
   Open Command Prompt (cmd) and run:
   ```bash
   python --version
   ```
   You should see output like: `Python 3.x.x`

   Also verify pip (Python package manager):
   ```bash
   pip --version
   ```

### Step 2: Set Up Environment Variables (If Not Automatically Set)

If Python is not recognized in Command Prompt:

1. **Find Python Installation Path:**
   - Default location: `C:\Users\<YourUsername>\AppData\Local\Programs\Python\Python3xx\`
   - Or search for "python.exe" in File Explorer

2. **Add to PATH:**
   - Right-click "This PC" → Properties
   - Click "Advanced system settings"
   - Click "Environment Variables"
   - Under "System variables", find and select "Path"
   - Click "Edit"
   - Click "New" and add:
     - `C:\Users\<YourUsername>\AppData\Local\Programs\Python\Python3xx\`
     - `C:\Users\<YourUsername>\AppData\Local\Programs\Python\Python3xx\Scripts\`
   - Click "OK" on all windows
   - **Restart Command Prompt** for changes to take effect

3. **Verify:**
   ```bash
   python --version
   pip --version
   ```

### Step 3: Install Required Libraries

This project uses the following Python libraries:
- **matplotlib** - For creating Gantt charts and visualizations
- **pandas** - For data manipulation and displaying results in tables
- **jupyter** - For running Jupyter notebooks

#### Install all required libraries:

Open Command Prompt and run:

```bash
pip install matplotlib pandas jupyter
```

Or install them individually:

```bash
pip install matplotlib
pip install pandas
pip install jupyter
```

#### Verify Library Installation:

```bash
pip list
```

You should see `matplotlib`, `pandas`, and `jupyter` in the list.

### Step 4: Running Jupyter Notebooks

1. **Navigate to the project directory:**
   ```bash
   cd "c:\Upendra\Git Hub\Git Hub -- K-Upendra-7\Labs\Operating-Systems"
   ```

2. **Start Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```

3. **Access the notebooks:**
   - Your default browser will open automatically
   - Navigate to the exercise folders (e.g., `EXERCISE 1`)
   - Click on any `.ipynb` file to open and run it

### Step 5: Checking Python Environment

To verify everything is set up correctly, run this in Command Prompt:

```bash
python -c "import matplotlib; import pandas; print('All libraries installed successfully!')"
```

If you see "All libraries installed successfully!", you're ready to go!

### Troubleshooting

**Issue: "python is not recognized"**
- Solution: Make sure Python is added to PATH (see Step 2)
- Restart Command Prompt after adding to PATH

**Issue: "pip is not recognized"**
- Solution: Reinstall Python and ensure "Add Python to PATH" is checked

**Issue: Library import errors**
- Solution: Reinstall the library: `pip install --upgrade <library-name>`

**Issue: Permission denied during installation**
- Solution: Run Command Prompt as Administrator

### Additional Notes

- **Virtual Environment (Optional but Recommended):**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  pip install matplotlib pandas jupyter
  ```

- **Upgrade pip (if needed):**
  ```bash
  python -m pip install --upgrade pip
  ```

- **Check installed packages:**
  ```bash
  pip freeze
  ```

---

**For any issues, please ensure you have:**
- ✅ Python 3.x installed
- ✅ Python added to PATH
- ✅ pip working correctly
- ✅ All required libraries installed (matplotlib, pandas, jupyter)
