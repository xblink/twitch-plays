class Graph:
    def __init__(self, title):
        self.title = title
        self.valueBuffer = []
        self.currentCount = 0
        
    def update(self, count):
        self.currentCount = count
    
    def get_ascii(self):
        count = self.currentCount
        hCount = 0
        while count > 250:
            count -= 250
            hCount += 250
        return '   {0:>9}|{1:-<25}|{2:<2}{3:<3}'.format(self.title,'#' * int(self.currentCount/10), 'R' * hCount ,count)
    