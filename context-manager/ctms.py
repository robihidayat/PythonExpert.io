from sqlite3 import connect

class contexmanger:
    def __init__(self, gen):
        self.gen = gen

    def __call__(self, *args, **kwargs):
        self.args, self.kwargs = args, kwargs
        return self

    def __enter__(self):
        print('__enter__')
        self.gen_inst = self.gen(*self.args, **self.kwargs)
        next(self.gen_inst)

    def __exit__(self, *args):
        print('__exit__')
        next(self.gen_inst, None)

def temptable(cur):
    print('create table')
    cur.execute('CREATE TABLE points(x int, y int)')
    yield
    cur.execute('drop table points')
    print('drop table')


temptable = contexmanger(temptable)

with connect('test.db') as conn:
    cur = conn.cursor()
    with temptable(cur):
        cur.execute('insert into points (x,y) VALUES (123,2)')
        cur.execute('insert into points (x,y) VALUES (12,3)')
        cur.execute('insert into points (x,y) VALUES (4,5)')
        cur.execute('insert into points (x,y) VALUES (3,6)')
        cur.execute('insert into points (x,y) VALUES (2,9)')
        for row in cur.execute('select x, y from points'):
            print(row)
        for rows in cur.execute('select sum(x*y) from points'):
            print(rows)
