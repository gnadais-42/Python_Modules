import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time


def check_dependencies():
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    print(f"[OK] pandas ({pd.__version__}) - Data manipulation ready")
    print(f"[OK] numpy ({np.__version__}) - Numerical computations ready")
    print(f"[OK] matplotlib ({plt.matplotlib.__version__}) - Visualization ready")

    time.sleep(1)


def generate_matrix(size=100):
    """
    Generate a square matrix with random values.
    100x100 = 10,000 data points
    """
    np.random.seed(42)
    return np.random.rand(size, size)


def analyze_matrix(matrix):
    df = pd.DataFrame(matrix)

    mean_value = df.values.mean()
    std_value = df.values.std()

    return df, mean_value, std_value


def visualize_matrix(matrix):
    plt.figure(figsize=(8, 6))
    plt.imshow(matrix, cmap='viridis')
    plt.colorbar(label="Value")
    plt.title("Matrix Heatmap")
    plt.xlabel("Columns")
    plt.ylabel("Rows")

    plt.savefig("matrix_analysis.png")
    plt.close()


def main():
    check_dependencies()

    print("Analyzing Matrix data...")
    time.sleep(1)

    matrix = generate_matrix(100)  # 100x100 matrix
    print(f"Processing {matrix.size} data points...")
    time.sleep(1)

    df, mean_value, std_value = analyze_matrix(matrix)

    print("Generating visualization...")
    visualize_matrix(matrix)
    time.sleep(1)

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()