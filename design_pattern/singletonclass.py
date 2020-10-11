class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        # import pdb;pdb.set_trace()
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Logger(metaclass=Singleton):
    
    def logger(self):
        print(self)


v = Logger()
v.logger()
s = Logger()
s.logger()