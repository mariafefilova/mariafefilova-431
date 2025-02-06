def prime_generator(n):
    mas = [1 for i in range(n)]
    mas[0],mas[1]=0,0
    for i in range(n):
        if mas[i]:
            yield i
            for m in range(i*2,n,i):
                mas[m]=0
 
#пример применения:
for prime in prime_generator(15):
    print(prime)
    

class CycleIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0
        self.lenght= len(iterable)
    def __iter__(self):
        return self
    def __next__(self):
        current = self.iterable[self.index] 
        self.index = (self.index+1)%(self.lenght)
        return current


it = CycleIterator([1, 2, 3])
for _ in range(7):
    print(next(it)) # 1, 2, 3, 1, 2, 3, 1
