class Network:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        """Adiciona um nó à rede."""
        self.nodes[node.node_id] = node

    async def broadcast(self, sender_id, message):
        """Simula o envio de uma mensagem para todos os nós."""
        for node_id, node in self.nodes.items():
            if node_id != sender_id:
                await node.receive_message(message)

    async def send_message(self, sender_id, receiver_id, message):
        """Simula o envio de uma mensagem para um nó específico."""
        if receiver_id in self.nodes:
            await self.nodes[receiver_id].receive_message(message)
