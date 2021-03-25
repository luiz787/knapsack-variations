class BranchAndBoundNode:

    # O nó guarda o array de itens e a restrição da mochila para facilitar a computação do limite
    def __init__(self, items, W, level, item) -> None:
        self.items = items
        self.W = W
        self.level = level
        self.item = item
        self.bound = self.compute_bound()

    def compute_bound(self):
        bound = self.item.value
        total_weight = self.item.weight
        child = self.level + 1

        while child < len(self.items) and total_weight + self.items[child].weight <= self.W:
            total_weight += self.items[child].weight
            bound += self.items[child].value
            child += 1

        if child < len(self.items):
            remaining_capacity = self.W - total_weight
            bound += remaining_capacity * self.items[child].proportional_value

        return bound

    # Métodos de comparação definidos para permitir a inserção
    # de objetos na fila de prioridade
    def __lt__(self, other):
        return self.bound < other.bound

    def __le__(self, other):
        return self.bound <= other.bound
