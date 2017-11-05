#library.py


class BaseMeta(type):
    def __new__(cls, name, bases, body):
        if name != 'Base' and not 'bar' in body:
            raise TypeError("bad user class")
        return super().__new__(cls, name, bases, body)


class Base(metaclass=BaseMeta):
    def foo(self):
        return self.bar()

    def __init_subclass__(self, *a, **kwargs):
        print('init_subclass')
        return super().__init_subclass__(*a, **kwargs)



