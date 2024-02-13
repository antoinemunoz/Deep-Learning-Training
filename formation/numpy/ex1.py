import numpy as np

def initialisation(m, n):
    matrix = np.random.rand(m, n + 1)
    biais = np.ones((m, 1))

    return np.concatenate((matrix, biais), axis=1)

def main():
    print(initialisation(3, 2))

if __name__ == "__main__":
    main()