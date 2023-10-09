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

def find_process(processes,time):
    found = []
    for p in processes:
        if p.arrival_time == time:
            found.append(p)

    if len(found) > 0:
        return found
    else:
        return False
    
def SJF_v2(processes,time,to_run,queue,running,results,limit):
    incoming = processes
    ready_queue = queue

    if len(results) == limit:
        return results
    if running:
        index = ready_queue.index(to_run)
        ready_queue[index].print_process()
        ready_queue[index].burst_time = ready_queue[index].burst_time - 1
        for p in ready_queue:
            p.wait_time = p.wait_time + 1
        
        if ready_queue[index].burst_time == 0:
            results.append(ready_queue[index])
            ready_queue.pop(index)
            return SJF_v2(incoming,time+1,False,ready_queue,False,results,limit)
        else:
            return SJF_v2(incoming,time+1,ready_queue[index],ready_queue,True,results,limit)
        
    else:
        add_to_queue = find_process(incoming,time)
        if add_to_queue:
            for p in add_to_queue:
                ready_queue.append(p)
                incoming.remove(p)

        shortest_p = process('dummy', 1, 1000, 0)

        if ready_queue:
            for p in ready_queue:
                if p.burst_time < shortest_p.burst_time:
                    shortest_p = p
            return SJF_v2(incoming,time+1,shortest_p,ready_queue,True,results,limit)
        else:
            return SJF_v2(incoming,time+1,False,ready_queue,False,results,limit)




    


    




def main():
    processes = get_processes('mrd_processes.txt')

    for p in processes:
        p.print_process()

    #SJF(processes)
    print('----------')
    x = find_process(processes,1)
    print_process_list(x)

    SJF_v2(processes,0,False,[],False,[],len(processes))

main()
