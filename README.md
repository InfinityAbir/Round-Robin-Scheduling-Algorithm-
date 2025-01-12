# Round Robin Scheduling Algorithm

This repository contains a Python implementation of the **Round Robin Scheduling Algorithm**, a CPU scheduling technique commonly used in operating systems. It ensures fair process execution by assigning each process a fixed time quantum and cycling through them in a round-robin manner.

## Features

- Implements **Round Robin Scheduling**.
- Calculates key scheduling metrics:
  - Completion Time
  - Turnaround Time
  - Waiting Time
- Supports dynamic process arrival and burst times.
- User-friendly input and output display for process statistics.

## How It Works

1. **Input**:
   - Number of processes.
   - Burst time and arrival time for each process.
   - Time quantum for the round-robin scheduler.
   
2. **Scheduling**:
   - Processes are added to a ready queue based on their arrival times.
   - Each process is executed for a fixed time quantum, or until completion, whichever comes first.
   - Processes that aren't completed are returned to the queue.

3. **Output**:
   - Displays a tabular summary of each process's Burst Time, Arrival Time, Completion Time, Turnaround Time, and Waiting Time.
   - Calculates and displays the average Turnaround Time and Waiting Time.

## Usage

### Prerequisites
- Python 3.x installed on your system.

### Running the Code
1. Clone the repository or download the `RRS.py` file.
2. Run the script in your terminal:
   ```bash
   python RRS.py
