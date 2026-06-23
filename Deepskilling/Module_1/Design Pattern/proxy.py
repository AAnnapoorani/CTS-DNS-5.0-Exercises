class RealImage:
    def __init__(self, filename):
        self.filename = filename
        print("Loading image from server...")
    def display(self):
        print("Displaying", self.filename)


class ProxyImage:
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None
    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        self.real_image.display()

image = ProxyImage("sample.jpg")
print("Image object created")
image.display()
image.display()