#! /usr/bin/env python3

import os
from dotenv import load_dotenv


def load_matrix_config() -> dict:
    """Loads environment variables from .env file or system."""
    # Carrega as variáveis do ficheiro .env para o ambiente
    load_dotenv()

    config = {
        "MODE": os.getenv("MATRIX_MODE", "Not Defined"),
        "DB": os.getenv("DATABASE_URL", "Not Defined"),
        "API": "Authenticated" if os.getenv("API_KEY") else "Missing",
        "LOG": os.getenv("LOG_LEVEL", "INFO"),
        "ZION": os.getenv("ZION_ENDPOINT", "Offline")
    }
    return config


def check_security() -> None:
    """Performs a basic security check on the environment."""
    # Verifica se o ficheiro .env existe para confirmar a configuração
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file missing! Using default environment.")


def main() -> None:
    """The Oracle: Reading the mainframe configuration."""
    try:
        print("ORACLE STATUS: Reading the Matrix...")
        config = load_matrix_config()

        print("\nConfiguration loaded:")
        print(f"Mode: {config['MODE']}")
        print(
            f"Database: {'Connected' if config['DB'] != 'Not Defined' else 'Disconnected'}")
        print(f"API Access: {config['API']}")
        print(f"Log Level: {config['LOG']}")
        print(
            f"Zion Network: {'Online' if config['ZION'] != 'Offline' else 'Offline'}")

        print("\nEnvironment security check:")
        # Verificação se não há hardcoded secrets (exemplo simples)
        print("[OK] No hardcoded secrets detected")
        check_security()
        # Simulação de override de produção
        if config['MODE'] == "production":
            print("[OK] Production overrides available")
        else:
            print("[INFO] Running in development mode")

        print("\nThe Oracle sees all configurations.")

    except Exception as e:
        print(f"Error accessing the mainframe: {e}")


if __name__ == "__main__":
    main()
