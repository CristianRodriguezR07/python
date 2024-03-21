class Pizza:
    def __init__(self, tamaño, salsa, ingredientes):
        self.tamaño = tamaño
        self.salsa = salsa
        self.ingredientes = ingredientes

    def __str__(self):
        return f"Pizza: {self.tamaño}, {self.salsa}, {self.ingredientes}"

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza(None, None, [])

    def set_tamaño(self, tamaño):
        self.pizza.tamaño = tamaño

    def set_salsa(self, salsa):
        self.pizza.salsa = salsa

    def agregar_ingrediente(self, ingrediente):
        self.pizza.ingredientes.append(ingrediente)

    def get_pizza(self):
        return self.pizza
    
class Director:
    def __init__(self, builder):
        self.builder = builder

    def construir_pizza_vegetariana(self):
        self.builder.set_tamaño("mediana")
        self.builder.set_salsa("tomate")
        self.builder.agregar_ingrediente("pimiento")
        self.builder.agregar_ingrediente("cebolla")
        self.builder.agregar_ingrediente("champiñones")

    def construir_pizza_carnivora(self):
        self.builder.set_tamaño("grande")
        self.builder.set_salsa("barbacoa")
        self.builder.agregar_ingrediente("pepperoni")
        self.builder.agregar_ingrediente("jamón")
        self.builder.agregar_ingrediente("salchicha")

director = Director(PizzaBuilder())
director.construir_pizza_vegetariana()
pizza_vegetariana = director.builder.get_pizza()
director.construir_pizza_carnivora()
pizza_carnivora = director.builder.get_pizza()

print(pizza_vegetariana)
print(pizza_carnivora)
