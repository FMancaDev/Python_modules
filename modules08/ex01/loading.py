#! /usr/bin/env python3

import sys
import importlib


def check_dependencies() -> dict[str, str]:
    """verifiy if library are installed and return it version"""
    dependencies = ["pandas", "numpy", "matplotlib", "requests"]
    status = {}
    for lib in dependencies:
        try:
            module = importlib.import_module(lib)
            # tenta obter a versao do modulo
            version = getattr(module, "__version__", "unknown")
            status[lib] = version
        except ImportError:
            status[lib] = "MISSING"
    return status


def analyze_data() -> None:
    "Simulates Matrix data analysis and generates a graph."
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    print("Analysing Matrix data...")
    # cria dados simulados
    data = {
        "Sector": ["Zion", "Surface", "Machine City", "Construct"],
        "Sentinels": np.random.randint(10, 100, 4)
    }
    df = pd.DataFrame(data)
    print(f"processing {len(df)} sectors...")

    # gera visualizacao
    print("Generating Visualization...")
    plt.figure(figsize=(8, 5))
    plt.bar(df["Sector"], df["Sentinels"], color="green")
    plt.title("Matrix Threat Level by Sector")
    plt.savefig("matrix_analysis.png")
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    """Função principal para carregar programas e gerir o fluxo."""
    print("\nLOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")

    status = check_dependencies()
    missing = [lib for lib, ver in status.items() if ver == "MISSING"]

    for lib, ver in status.items():
        if ver != "MISSING":
            print(f"[OK] {lib} ({ver}) - Data manipulation ready")
        else:
            print(f"[ERROR] {lib} is missing!")

    if missing:
        print("\nFATAL: Missing dependencies detected.")
        print("To fix this, run:")
        print("pip install -r requirements.txt")
        print("OR")
        print("poetry install")
        sys.exit(1)

    try:
        analyze_data()
    except Exception as e:
        print(f"An error occurred during analysis: {e}")


if __name__ == "__main__":
    main()
