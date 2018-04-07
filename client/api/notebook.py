class EmptyClass:
    def __init__(self, *args, **kwargs):
        pass

    def empty_function(self, *args, **kwargs):
        return self

    def __getattr__(self, attr):
        return self.empty_function

class Notebook(EmptyClass):
    pass
