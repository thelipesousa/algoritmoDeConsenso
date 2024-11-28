import threading
import time
import random


class Node:
    def __init__(self, id, nodes):
        self.id = id
        self.nodes = nodes  # Lista de nós na rede
        self.state = "follower"
        self.term = 0
        self.votes = 0
        self.failed = False
        self.is_leader = False
        self.lock = threading.Lock()

    def start(self):
        """Inicia o nó e seu comportamento em uma thread separada."""
        threading.Thread(target=self.run, daemon=True).start()

    def run(self):
        """Executa o ciclo de um nó no algoritmo Raft."""
        while not self.failed:
            if self.state == "follower":
                self.wait_for_leader()
            elif self.state == "candidate":
                self.start_election()
            time.sleep(1)

    def wait_for_leader(self):
        """Espera por um líder ou inicia uma eleição."""
        timeout = random.uniform(2, 5)
        time.sleep(timeout)

        if not self.is_leader and not any(node.is_leader for node in self.nodes if not node.failed):
            self.state = "candidate"

    def start_election(self):
        """Inicia uma eleição."""
        with self.lock:
            self.term += 1
            self.votes = 1  # Vota em si mesmo
            print(f"Nó {self.id} iniciou uma eleição (Termo: {self.term}).")

            for node in self.nodes:
                if node.id != self.id and not node.failed:
                    node.receive_vote(self)

            if self.votes > len(self.nodes) // 2:
                self.become_leader()

    def receive_vote(self, candidate):
        """Recebe uma solicitação de voto."""
        with self.lock:
            if candidate.term >= self.term and not self.failed:
                candidate.votes += 1
                print(f"Nó {self.id} votou no nó {candidate.id}.")

    def become_leader(self):
        """Assume o papel de líder."""
        self.is_leader = True
        self.state = "leader"
        print(f"Nó {self.id} tornou-se o líder (Termo: {self.term}).")
        self.send_heartbeats()

    def send_heartbeats(self):
        """Envia batimentos cardíacos para os seguidores."""
        while self.is_leader and not self.failed:
            print(f"Nó {self.id} enviando batimentos cardíacos.")
            time.sleep(2)

    def simulate_failure(self):
        """Simula a falha do nó."""
        self.failed = True
        print(f"Nó {self.id} falhou.")
