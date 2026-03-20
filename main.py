import bext, random
from interval_timer import IntervalTimer

def main():
    width, height = bext.size()
    lines = []
    for i in range(50):
        line = Line('blue',
                    'black',
                    width,
                    height,
                    bext)
        lines.append(line)
    try:
        while True:
            for interval in IntervalTimer(0.03):
                for line in lines:
                    random.shuffle(lines)
                    line.printLine()
    except KeyboardInterrupt:
        pass
    
class Line:
    def __init__(self, fg, bg, width, height, bext):
        self.fg = fg
        self.bg = bg
        self.width = width
        self.height = height
        self.bext = bext
        self.pending = random.randint(4, self.width - 10)
        self.x = self.getRandomX()
        self.y = 0
        self.oldPosition = []
        self.char = [
                        'ア', 'イ', 'ウ', 'エ', 'オ',
                        'カ', 'キ', 'ク', 'ケ', 'コ',
                        'サ', 'シ', 'ス', 'セ', 'ソ',
                        'タ', 'チ', 'ツ', 'テ', 'ト',
                        'ナ', 'ニ', 'ヌ', 'ネ', 'ノ',
                        '1', '2', '3', '4', '5',
                        '6', '7', '8', '9', '0',
                        '!', '@', '#', '$', '%',
                        '&', '*', '(', ')', '-',
                        '+', '=', '[', ']', ';',
                        ':', ',', '.', '/', '?', '>'
                    ]

    def getRandomX(self):
        return random.randint(0, self.width - 1)
    
    def getRandomChar(self):
        return random.choice(self.char)
    
    def getRandomPosition(self):
        return random.randint(0, len(self.oldPosition) - 1)
    
    def draw(self):
        self.bext.fg(self.fg)
        self.bext.bg(self.bg)
        self.bext.goto(self.x, self.y)
        print(self.getRandomChar(), end='')
        self.oldPosition.append((self.x, self.y))
        if(self.y == self.height - 1):
            self.y = 0
            self.x = self.getRandomX()
        else:
            self.y += 1
        
    def removeOldPosition(self):
        self.bext.goto(self.oldPosition[0][0], self.oldPosition[0][1])
        print(' ', end='')
        self.oldPosition.pop(0)
        
    def changeOldPosition(self):
        item = self.getRandomPosition()
        self.bext.goto(self.oldPosition[item][0], self.oldPosition[item][1])
        print(self.getRandomChar(), end='')
            
    def printLine(self):
        if(self.pending <= 0):
            self.removeOldPosition()
            self.changeOldPosition()
            self.draw()
        else:
            self.pending -= 1
            self.draw()
    
if __name__ == "__main__":
    main()
