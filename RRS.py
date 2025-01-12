from collections import deque

class Process:
    def __init__(self, id, burst_time, arrival_time):
        self.id = id
        self.burst_time = burst_time
        self.arrival_time = arrival_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def round_robin(processes, time_quantum):
    """
    Simulates Traditional Round Robin Scheduling.

    Args:
        processes: A list of Process objects.
        time_quantum: The time quantum for each process.
    """
    time = 0
    ready_queue = deque()

    # Add processes arriving at time 0 to the ready queue
    for i, process in enumerate(processes):
        if process.arrival_time <= time:
            ready_queue.append(i)

    while any(process.remaining_time > 0 for process in processes):  # Continue until all processes are finished
        if not ready_queue:
            # If no processes are ready, increment time until the next arrival
            next_arrival_time = min(process.arrival_time for process in processes if process.remaining_time > 0)
            time = next_arrival_time
            for i, process in enumerate(processes):
                if process.arrival_time <= time and i not in ready_queue:
                    ready_queue.append(i)
            continue

        process_index = ready_queue.popleft()
        current_process = processes[process_index]

        if current_process.remaining_time <= time_quantum:
            time += current_process.remaining_time
            current_process.remaining_time = 0
            current_process.completion_time = time
        else:
            time += time_quantum
            current_process.remaining_time -= time_quantum

        # Add processes that arrive during the time quantum to the ready queue
        for i, process in enumerate(processes):
            if process.arrival_time <= time and i not in ready_queue:
                ready_queue.append(i)

        # If the current process is not finished, add it back to the queue
        if current_process.remaining_time > 0:
            ready_queue.append(process_index)

    # Calculate turnaround and waiting times after all processes are completed
    for process in processes:
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time

def display_results(processes):
    """
    Displays the results of the scheduling algorithm.
    """
    total_turnaround_time = 0
    total_waiting_time = 0

    print("PID\tBurst\tArrival\tCompletion\tTurnaround\tWaiting")
    for process in processes:
        print(f"{process.id}\t{process.burst_time}\t{process.arrival_time}\t{process.completion_time}\t\t{process.turnaround_time}\t\t{process.waiting_time}")
        total_turnaround_time += process.turnaround_time
        total_waiting_time += process.waiting_time

    print(f"\nAverage Turnaround Time: {total_turnaround_time / len(processes)}")
    print(f"Average Waiting Time: {total_waiting_time / len(processes)}")

if __name__ == "__main__":
    num_processes = int(input("Enter the number of processes: "))
    processes = []

    for i in range(num_processes):
        burst_time = int(input(f"Enter burst time for process {i+1}: "))
        arrival_time = int(input(f"Enter arrival time for process {i+1}: "))
        processes.append(Process(i+1, burst_time, arrival_time))

    time_quantum = int(input("Enter the time quantum: "))

    round_robin(processes, time_quantum)
    display_results(processes)