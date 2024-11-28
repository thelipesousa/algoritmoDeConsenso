import random


class Network:
    def __init__(self, nodes):
        self.nodes = nodes

    def start(self):
        """Inicia todos os nós da rede."""
        for node in self.nodes:
            node.start()

    def simulate_failure(self):
        """Simula uma falha em um nó aleatório."""
        active_nodes = [node for node in self.nodes if not node.failed]
        if active_nodes:
            node_to_fail = random.choice(active_nodes)
            node_to_fail.simulate_failure()
