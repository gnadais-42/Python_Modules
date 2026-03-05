from importlib import import_module


def main() -> None:
    print("LOADING STATUS: Loading programs..."
          "\n\nChecking dependencies:")

    required: dict = {
        "numpy": "Advanced calculus",
        "pandas": "Data manipulation",
        "matplotlib": "Visualization",
        "requests": "Network access"
    }

    missing: list = []
    for package in required:
        try:
            module = import_module(package)
            version = module.__version__
            print(f"[OK] {package} ({version}) - {required[package]} ready")
        except ImportError:
            print(f"[KO] {package} is not installed")
            missing.append(package)

    if missing:
        print("Missing dependencies:", missing, end="\n\n")
        print("To install these dependencies through pip\n"
              "first make sure you're in a safe environment, then run:")
        print("python3 -m pip install -r requirements.txt")
        print("\nTo install and run this program using poetry, just run:")
        print("poetry run python3 loading.py\n")
        print("Poetry will automatically create a safe"
              " environment with your dependencies\n"
              "installed as long as they are properly "
              "listed in a pyproject.toml file")
        return

    import numpy
    import pandas
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...\n")

    numpy.random.seed(42)
    matrix = numpy.random.normal(loc=50, scale=15, size=(1000, 1000))

    df = pandas.DataFrame(matrix)

    print("Matrix Shape:", df.shape)

    matrix_mean = numpy.mean(matrix)
    matrix_std = numpy.std(matrix)
    matrix_sum = numpy.sum(matrix)
    print("Global Mean:", matrix_mean)
    print("Global Std Dev:", matrix_std)
    print("Global Sum:", matrix_sum)

    row_means = df.mean(axis=1)

    product_matrix = numpy.dot(matrix, matrix.T)

    print("Product Matrix Shape:", product_matrix.shape)

    plt.figure(figsize=(14, 6))

    downsampled = matrix[::20, ::20]

    plt.subplot(1, 2, 1)
    plt.imshow(downsampled, cmap="viridis", aspect="auto")
    plt.colorbar()
    plt.title("Heatmap (Downsampled 1000x1000 Matrix)")
    plt.subplot(1, 2, 2)
    plt.hist(row_means, bins=50)
    plt.title("Distribution of Row Means")
    plt.xlabel("Mean Value")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("matrix_analysis.png", dpi=300)
    plt.close()
    print("\nGenerating visualization...")


if __name__ == "__main__":
    main()
