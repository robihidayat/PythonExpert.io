from time import sleep


class Compute:
    def __iter__(self):
        self.last = 0
        return self

    def __next__(self):
        rv = self.last
        self.last += 1
        if self.last > 10:
            raise StopIteration()
        sleep(.5)
        return rv

comput = Compute()
for val in comput:
    print(val)

def generator():
    for i in range(10):
        sleep(0.6)
        yield i
generator()