# cs431program1
Hello, this is my program 1 where I implemented a shortest job first cpu scheduler simulation using python.

My idea while writing was this to just have a loop running handling incoming processes and the scheduler itself.
So the entire SJF function handles the scheduling and the processes joining the ready queue. I also made each
process into an object that handles its arrival time, burst time, wait time, and priority.

To add processes edit 'processes.txt' and enter them in csv format in the following order
process name, arrival time, burst time, priority, wait time (optional, default is 0)

Simply run the program and you can then view the results!
I hope you enjoy my program!
