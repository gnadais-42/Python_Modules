from importlib import import_module


def check_dependencies():
    print("LOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")

    modules = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computations ready",
        "matplotlib": "Visualization ready",
        "requests": "Network access ready",
    }

    loaded_modules = {}
    missing = []

    for name, description in modules.items():
        try:
            module = import_module(name)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {name} ({version}) - {description}")
            loaded_modules[name] = module
        except ImportError:
            print(f"[ERROR] {name} not found")
            missing.append(name)

    return loaded_modules, missing


def generate_matrix(numpy, size=100):
    numpy.random.seed(42)
    return numpy.random.rand(size, size)


def analyze_matrix(pandas, matrix):
    df = pandas.DataFrame(matrix)
    mean_value = df.values.mean()
    std_value = df.values.std()
    return df, mean_value, std_value


def visualize_matrix(plt, matrix):
    plt.figure(figsize=(8, 6))
    plt.imshow(matrix, cmap="viridis")
    plt.colorbar(label="Value")
    plt.title("Matrix Heatmap")
    plt.xlabel("Columns")
    plt.ylabel("Rows")

    plt.savefig("matrix_analysis.png")
    plt.close()


def print_install_instructions(missing):
    print("\nMissing dependencies:", ", ".join(missing), "\n")

    print("Install with pip:")
    print("python3 -m pip install " + " ".join(missing))

    print("\nOr install from requirements.txt:")
    print("python3 -m pip install -r requirements.txt")

    print("\nUsing Poetry:")
    print("poetry add numpy@^1.24 pandas@^2.0 matplotlib@^3.7 requests@^2.31")
    print("poetry run python loading.py")


def main() -> None:
    modules, missing = check_dependencies()

    if missing:
        print_install_instructions(missing)
        return

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")

    numpy = modules["numpy"]
    pandas = modules["pandas"]
    plt = import_module("matplotlib.pyplot")

    matrix = generate_matrix(numpy)
    df, mean, std = analyze_matrix(pandas, matrix)

    visualize_matrix(plt, matrix)

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
