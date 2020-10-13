import random


class Process:
    def __init__(self, id, at, bt):
        self.id = id
        self.at = at
        self.bt = bt
        self.wt = 0
        self.ct = 0
        self.st = 0
        self.tat = 0

    def fill(self, st):
        print('Current process:', self.id)
        self.st = st
        self.ct = self.st + self.bt
        self.tat = self.ct - self.at
        self.wt = self.tat - self.bt
        return self.ct

    def print(self):
        st = '\t'.join(map(str, [self.id, self.at, self.bt, self.ct, self.tat, self.wt]))
        print(st)

    @classmethod
    def min(cls, process_list):
        """
        A class function to find the process with the minimum BT given a list of processes.
        """
        least = process_list[0]
        for process in process_list:
            if process.bt < least.bt:
                least = process
        return least

    @classmethod
    def display(cls, process_list):
        print('ID\tAT\tBT\tCT\tTAT\tWT')
        for process in process_list:
            process.print()
        print('----------------------')


# n = int(input("Enter the number of processes: "))
# print("Enter the process and their details in the format ID AT BT")
l = [
    [1, 1, 7],
    [2, 2, 5],
    [3, 3, 1],
    [4, 4, 2],
    [5, 5, 8]
]
n = len(l)
processes = []

for p in l:
    processes.append(Process(*p))
# for i in range(n):
#     processes.append(Process(random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)))
    # processes.append(Process(*[int(x.strip()) for x in input().split(' ')]))
Process.display(processes)
print('Sorting.')
processes.sort(key=lambda x: x.at)
Process.display(processes)

t = processes[0].fill(processes[0].at)
print('First one. t =', t)
Process.display(processes)
offset = 1

waiting_list = []

while offset < n - 1:
    for process in processes[offset:]:
        if process.at < t:
            waiting_list.append(process)
        else:
            break

    if len(waiting_list) == 0:
        t += 1
        continue

    offset = processes.index(waiting_list[-1]) + 1

    next_process = Process.min(waiting_list)
    waiting_list.remove(next_process)
    t = next_process.fill(t)
    print('Waiting list:', end=' ')
    for p in waiting_list:
        print(p.id, end=' ')
    print('\nt =', t, 'offset =', offset)
    Process.display(processes)

while len(waiting_list) > 0:
    next_process = Process.min(waiting_list)
    waiting_list.remove(next_process)
    t = next_process.fill(t)
    print('Waiting list:', end=' ')
    for p in waiting_list:
        print(p.id, end=' ')
    print('\nt =', t)
    Process.display(processes)

print('Final')
processes.sort(key=lambda x: x.id)
Process.display(processes)
