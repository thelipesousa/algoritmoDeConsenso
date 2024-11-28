import asyncio
from raft import Raft

async def main():
    """Cria e inicia o cluster Raft."""
    num_nodes = 5
    raft = Raft(num_nodes)
    await raft.start_cluster()

if __name__ == "__main__":
    asyncio.run(main())
