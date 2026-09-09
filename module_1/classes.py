from mailbox import NoSuchMailboxError


class Cake:
    # Measurements are in grams
    eggs = 4
    sugar = 300
    milk = 200
    butter = 50
    flour = 250
    baking_soda = 20
    vanilla = 10

    topping = None
    garnish = None

    is_baked = False

    def __init__(self, topping='No Topping', garnish='No Garnish'):
        self.topping = topping
        self.garnish = garnish

    def bake(self):
        self.is_baked = True

    def is_cake_ready(self):
        return self.is_baked

plain_cake = Cake()

chocolate_cake = Cake(topping='Chocolate Frosting')

# topping= and garnish= removed for cleaner code
lux_strawb_cake = Cake('Strawberry Frosting', 'Chocolate Shavings')

chocolate_cake.bake()
is_cake_done = chocolate_cake.is_cake_ready()
print(is_cake_done)