Q_T = 2


class Process:
    def __init__(self, id, at, bt):
        self.id = id
        self.at = at
        self.bt = bt
        self.wt = -1
        self.ct = -1
        self.st = -1
        self.tat = -1
        self.rt = bt

    def fill(self):
        print('Process completed:', self.id)
        self.tat = self.ct - self.at
        self.wt = self.tat - self.bt
        return self.ct

    def execute(self, now):
        print('Current process:', self.id)
        if self.st == -1:
            self.st = now
        if self.rt <= Q_T:
            self.ct = self.rt + now
            self.rt = 0
            self.fill()
            return self.ct
        else:
            self.rt -= Q_T
            return now + Q_T

    def print(self):
        st = '\t'.join(map(str, [self.id, self.at, self.bt, self.st, self.rt, self.ct, self.tat, self.wt]))
        print(st)

    @classmethod
    def display(cls, process_list):
        print('ID\tAT\tBT\tST\tRT\tCT\tTAT\tWT')
        for process in process_list:
            process.print()
        print('----------------------')


if __name__ == '__main__':
    # n = int(input("Enter the number of processes: "))
    # print("Enter the process and their details in the format ID AT BT")
    l = [
        [1, 0, 5],
        [2, 1, 4],
        [3, 2, 2],
        [4, 3, 1],
    ]
    n = len(l)
    processes = []

    for p in l:
        processes.append(Process(*p))
    Process.display(processes)
    print('Sorting.')
    processes.sort(key=lambda x: x.at)
    Process.display(processes)
    min_at = processes[0].at
    max_at = processes[-1].at
    i = 0
    t = min_at
    flag = True
    while flag:
        flag = False
        for process in processes:
            if process.rt > 0:
                print('T =', t)
                t = process.execute(t)
                Process.display(processes)
                flag = True

    Process.display(processes)
