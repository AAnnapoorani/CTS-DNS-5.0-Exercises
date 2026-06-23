class MobileApp:
    def update(self, price):
        print("Mobile App Updated :", price)

class WebApp:
    def update(self, price):
        print("Web App Updated :", price)

class StockMarket:
    def __init__(self):
        self.observers = []
    def register(self, observer):
        self.observers.append(observer)
    def notify(self, price):
        for observer in self.observers:
            observer.update(price)


market = StockMarket()
mobile = MobileApp()
web = WebApp()
market.register(mobile)
market.register(web)
market.notify(2500)