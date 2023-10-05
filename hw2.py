class process:
    def __init__(self, name, arrival_time, burst_time, priority):
        self.name = name
        self.arrival_time = int(arrival_time)
        self.burst_time = int(burst_time)
        self.priority = int(priority)

    def print_process(self):
        print(str(self.name) + ' ' + str(self.arrival_time) + ' ' + str(self.burst_time) + ' ' + str(self.priority))
        return

    def run_process(self,time):
        return process(self.name,self.arrival_time,self.burst_time - time, self.priority)

def print_process_list(arr):
    for p in arr:
        p.print_process()

def get_processes(file_path):

    processes = []
    with open(file_path, 'r') as file:
        for line in file:
            contents = line.split(',')
            p = process(contents[0],contents[1],contents[2],contents[3])
            processes.append(p)
    return processes

def SJF(processes):
    incoming = processes
    ready_queue = []
    time = 0
    flag = True

    while incoming or ready_queue:
        for p in incoming:
            if p.arrival_time <= time:
                ready_queue.append(p)
                incoming.remove(p)

        shortest_time = ready_queue[0].burst_time
        shortest_process = ready_queue[0]

        for p in ready_queue:
            if p.burst_time < shortest_time:
                shortest_process = p

        if shortest_process:
            ready_queue.remove(shortest_process)
            time_needed = shortest_process.burst_time
            ran_process = shortest_process.run_process(shortest_process.burst_time)
            time = time + time_needed
        else:
            time = time + 1

        print('This process ran: ')
        shortest_process.print_process()


    print(time)

def main():
    processes = get_processes('mrd_processes.txt')

    for p in processes:
        p.print_process()

    SJF(processes)

main()