class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    def __repr__(self):
        return f'<Store({self.name})>'

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        # name_store = f'{store} - franchise'
        print(store)
        return cls(f'{store} - franchise')

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return f'{store.name}, total stock price: {store.stock_price()}'

store = Store('yewale')
store2 = Store('saiba')
store2.add_item('tea', 100)
store.add_item('coffie', 10)
# class method
print(Store.franchise(store))
print(Store.franchise(store2))

#static method
print(Store.store_details(store))
print(Store.store_details(store2))