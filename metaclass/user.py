# user.py
# u can use library, but u can change it,
# u have controll all in this script.


from library import Base
"""
check karakteristik dari function
"""
assert hasattr(Base, 'fo'),"you broke it, you fool !"

class Drived(Base):
    def bar(self):
        return self.foo()