import matplotlib.pyplot as plt

class Category:

    def __init__(
        self,
        name,
        limit
    ):
        self.name = name
        self.limit = limit
        self.spent = 0

    def add_expense(self, amount):

        self.spent += amount

        if self.spent > self.limit:
            print(
                f"Alert: {self.name} budget exceeded!"
            )


food = Category("Food", 5000)
travel = Category("Travel", 3000)

food.add_expense(3500)
food.add_expense(2000)

travel.add_expense(1500)

labels = [
    food.name,
    travel.name
]

values = [
    food.spent,
    travel.spent
]

plt.pie(
    values,
    labels=labels,
    autopct="%1.1f%%"
)

plt.title("Monthly Budget Usage")
plt.show()

