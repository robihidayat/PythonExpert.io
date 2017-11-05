class Api:
    def run_this_first(self):
        first()
    def run_this_seconds(self):
        second()
    def run_this_last(self):
        last()

def api():
    first()
    yield
    second()
    yield
    last()