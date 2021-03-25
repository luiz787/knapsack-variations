class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.proportional_value = 0 if weight == 0 else value / weight
