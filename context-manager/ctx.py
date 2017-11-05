from sqlite3 import connect

class temptable:
    def __init__(self, cur):
        self.cur = cur

    def __enter__(self):
        print('__enter__')
        self.cur.execute('CREATE TABLE points(x int, y int)')

    def __exit__(self, *args):
        print('__exit__')
        self.cur.execute('drop table points')


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
