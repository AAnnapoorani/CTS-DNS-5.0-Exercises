# Exercise 49

class Converter:

    def c_to_f(self, c):
        return (c * 9/5) + 32

    def c_to_k(self, c):
        return c + 273.15

    def f_to_c(self, f):
        return (f - 32) * 5/9

    def k_to_c(self, k):
        return k - 273.15


converter = Converter()

temp = float(input("Enter Celsius: "))

print(f"Fahrenheit = {converter.c_to_f(temp):.2f}")
print(f"Kelvin = {converter.c_to_k(temp):.2f}")

