#Each process is an object with the following attributes
class process:
    def __init__(self, name, arrival_time, burst_time, priority, wait_time=0):
        self.name = name
        self.arrival_time = int(arrival_time)
        self.burst_time = int(burst_time)
        self.priority = int(priority)
        self.wait_time = int(wait_time)

    def print_process(self):
        print(str(self.name) + ' ' + str(self.arrival_time) + ' ' + str(self.burst_time) + ' ' + str(self.priority) + ' wait time is: ' + str(self.wait_time))
        return

#prints a list of processes
def print_process_list(arr):
    for p in arr:
        p.print_process()

#reads from a csv of processes where the order is:
# name, arrival time, burst_time, priority, wait time (optional, defaults to 0)
def get_processes(file_path):
    processes = []
    with open(file_path, 'r') as file:
        for line in file:
            contents = line.split(',')
            p = process(contents[0],contents[1],contents[2],contents[3])
            processes.append(p)
    return processes

#finds processes whos arrival time = current time from the incoming processes
def find_process(processes,time):
    found = []
    for p in processes:
        if p.arrival_time == time:
            found.append(p)

    if len(found) > 0:
        return found
    else:
        return False

#performs a shortest job first cpu scheduler simulation
def SJF(processes):
    #declare initial values
    time = 0
    incoming = processes
    ready_queue = []
    results = []
    running = []

    #while there is processes to join the ready queue, 
    #processes in the ready queue, or a process is running the scheduler must run
    while (incoming or ready_queue) or running:
        print('Current time: ' + str(time))
        #check if any processes can join the ready queue and add them
        add_to_queue = find_process(incoming,time)
        if add_to_queue:
            for p in add_to_queue:
                print (p.name + ' ADDED')
                ready_queue.append(p)
                incoming.remove(p)

        #if no process is running go find one to schedule
        if not running:
            #if we have any processes in the queue, find the shortest one
            if ready_queue:
                shortest_p = ready_queue[0]
                for p in ready_queue:
                   if p.burst_time < shortest_p.burst_time:
                       shortest_p = p

                running.append(shortest_p)
                ready_queue.remove(shortest_p)

        #if a process is currently running (or one was just added and started running)
        #decrement the remaining burst time and increase all processes in the queue wait time
        if running:
            running[0].burst_time = running[0].burst_time - 1
            print(running[0].name + ' is running, time left: ' + str(running[0].burst_time))
            for p in ready_queue:
                p.wait_time = p.wait_time + 1

            #if the process is done running add it to the results and clear running.
            if running[0].burst_time == 0:
                results.append(running[0])
                running = []

        time = time + 1

    print("Shorest Job First Simulation completed, total run time: " + str(time) + "\n")
    return results

def main():
    #get a list of processes from a txt file
    processes = get_processes('processes.txt')

    #run shortest job first simulation on the list of processes
    results = SJF(processes)

    #calculate total wait time
    total_wait = 0
    for p in results:
        total_wait = total_wait + p.wait_time

    #display results and calculate average wait time
    print('The result list is in order of when they ran. With the top being who ran first.')
    print('Final Results: ')
    print('Avg wait time: ' + str(total_wait/len(results)))
    print_process_list(results)

main()
