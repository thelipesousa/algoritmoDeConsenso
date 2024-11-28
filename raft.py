from node import Node
from network import Network
import asyncio

class Raft:
    def __init__(self, num_nodes):
        self.nodes = []
        self.network = Network()
        for i in range(num_nodes):
            peers = [j for j in range(num_nodes) if j != i]
            node = Node(node_id=i, peers=peers)
            self.nodes.append(node)
            self.network.add_node(node)

    async def start_cluster(self):
        """Inicia todos os nós do cluster."""
        tasks = [node.start() for node in self.nodes]
        await asyncio.gather(*tasks)
