class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def log(self, message):
        print("LOG:", message)


logger1 = Logger()
logger2 = Logger()
print(logger1 is logger2)
logger1.log("Application Started")