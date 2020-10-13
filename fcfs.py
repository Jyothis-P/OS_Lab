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
    def display(cls, process_list):
        print('ID\tAT\tBT\tCT\tTAT\tWT')
        for process in process_list:
            process.print()
        print('----------------------')


if __name__ == '__main__':
    # n = int(input("Enter the number of processes: "))
    # print("Enter the process and their details in the format ID AT BT")
    l = [
        [1, 5, 0],
        [2, 3, 1],
        [3, 8, 2],
        [4, 6, 3],
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

    t = processes[0].at
    for process in processes:
        t = process.fill(max(t, process.at))
        Process.display(processes)

    Process.display(processes)
