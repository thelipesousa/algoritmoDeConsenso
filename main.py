from raft import Raft


def main():
    raft = Raft(num_nodes=5)
    raft.start()
    raft.simulate()


if __name__ == "__main__":
    main()
