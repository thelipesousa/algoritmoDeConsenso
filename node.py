import random
import asyncio

class Node:
    def __init__(self, node_id, peers):
        self.node_id = node_id
        self.peers = peers  # Lista de IDs dos outros nós
        self.state = "follower"  # Estados: follower, candidate, leader
        self.current_term = 0
        self.voted_for = None
        self.logs = []  # Simulação de um log
        self.election_timer = None

    async def start(self):
        """Inicia o nó como um seguidor."""
        print(f"Nó {self.node_id} iniciado como {self.state}.")
        await self.run_follower()

    async def run_follower(self):
        """Comportamento do nó como seguidor."""
        self.reset_election_timer()
        while self.state == "follower":
            await asyncio.sleep(0.1)

    def reset_election_timer(self):
        """Reinicia o temporizador de eleição."""
        timeout = random.uniform(1.0, 2.0)  # Temporizador aleatório
        self.election_timer = asyncio.get_event_loop().call_later(
            timeout, self.start_election
        )

    def start_election(self):
        """Inicia uma eleição como candidato."""
        print(f"Nó {self.node_id} iniciou uma eleição.")
        self.state = "candidate"
        self.current_term += 1
        self.voted_for = self.node_id
        # Lógica para pedir votos será implementada aqui
