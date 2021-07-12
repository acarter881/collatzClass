class Collatz:
    def __init__(self, number) -> None:
        self.number = number
        self.iterate = 0
        if self.number < 1:
            raise ValueError('Please enter an integer greater than or equal to 1.')
    
    def myIter(self):
        while self.number != 1:
            self.iterate += 1
            self.number = self.maker(self.number)

        return self.iterate

    def maker(self, number):
        self.number = number

        if self.number % 2 == 0:
            return self.number // 2
        return (self.number * 3) + 1

c = Collatz(225543634343432221254645634343343543442512235345346346346346346232352523434345735346347324624624357357373534634734) 
print(c.myIter()) #2535
