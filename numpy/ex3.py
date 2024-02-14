import numpy as np

def main():
    np.random.seed(0)
    matrix = np.random.randint(0, 100, [10,5])

    resultMatrix = (matrix - np.mean(matrix, axis=0)) / np.std(matrix, axis=0)

    print(resultMatrix)

if __name__ == "__main__":
    main()