## Felipe Sousa de Almeida RA: 22018160
## Guilherme Domingues de Sousa RA: 22013871


# **Algoritmo de Consenso Raft - Simulação**

Este projeto é uma simulação do algoritmo de consenso **Raft** em um ambiente distribuído. Ele implementa as fases principais do algoritmo, incluindo a eleição de líderes e a replicação de logs, enquanto simula falhas e recuperação de nós em um cluster distribuído.

---

## **Descrição do Projeto**

O objetivo deste projeto é demonstrar o funcionamento do algoritmo de consenso Raft, amplamente utilizado em sistemas distribuídos para garantir consistência de dados. A implementação simula um ambiente de rede onde vários nós trocam mensagens para alcançar consenso.

---

## **Funcionalidades**

1. **Nós distribuídos**: Cada nó pode estar em um dos estados:
   - **Follower**: Ouve mensagens de um líder ou inicia uma eleição se o líder estiver ausente.
   - **Candidate**: Tenta se eleger líder após o término do temporizador de eleição.
   - **Leader**: Coordena o cluster, garantindo a replicação consistente dos logs.

2. **Comunicação em rede**:
   - Simulação de mensagens entre nós para eleições e replicação.
   - Temporizadores aleatórios para evitar conflitos durante eleições.

3. **Simulação de falhas**:
   - Os nós podem falhar ou se recuperar dinamicamente durante a execução.
   - O sistema reage às falhas, elegendo um novo líder quando necessário.

---

## **Estrutura do Projeto**

- **`node.py`**: Implementa o comportamento de cada nó (follower, candidate, leader).
- **`network.py`**: Simula a rede que conecta os nós.
- **`raft.py`**: Lógica principal para criar e gerenciar o cluster de nós.
- **`main.py`**: Ponto de entrada para executar a simulação.

---

## **Como Executar**

### **Pré-requisitos**
1. **Python 3.9+**: Certifique-se de ter o Python instalado. Para verificar:
   ```bash
   python3 --version
