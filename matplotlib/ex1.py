import matplotlib.pyplot as plt
import numpy as np

def graphique(dataset):
    plt.figure()
    for experiment, data in dataset.items():
        plt.subplot(2, 2, int(experiment[-1]) + 1)
        plt.plot(data)
        plt.title(experiment)

    plt.show()

def main():
    dataset = {f"experiment{i}": np.random.rand(100) for i in range(4)}

    graphique(dataset)

if __name__ == "__main__":
    main()