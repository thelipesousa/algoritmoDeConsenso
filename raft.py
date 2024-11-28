import time
from node import Node
from network import Network


class Raft:
    def __init__(self, num_nodes=5):
        self.nodes = [Node(i, []) for i in range(num_nodes)]
        for node in self.nodes:
            node.nodes = self.nodes
        self.network = Network(self.nodes)

    def start(self):
        """Inicia a simulação da rede."""
        self.network.start()

    def simulate(self):
        """Simula o comportamento da rede com falhas."""
        for _ in range(5):  # Simular cinco falhas
            time.sleep(5)
            self.network.simulate_failure()
        print("Simulação concluída.")
