class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connection = True
    
    def __str__(self):
        return f'Device {self.name!r} connected by {self.connected_by}'
    
    def disconnect(self):
        self.connection = False
        print('Disconnected device')

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f'{super().__str__()}  {self.remaining_pages} pages remaining'
    
    def print(self, pages):
        if not self.connection:
            print('Printer Disconnected')
            return
        print(f'Pages {pages} pages')
        self.remaining_pages -= pages

printer = Printer('Printer', 'USB', 500)
printer.print(20)
print(printer)
printer.disconnect()
printer.print(30)