#! /usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """
    Abstract Base Class for data processing.
    Defines the contract that all processors must follow.
    """

    def __init__(self) -> None:
        """Initializes the processor using super."""
        super().__init__()

    @abstractmethod
    def process(self, data: Any) -> str:
        """
        Abstract method to process data.
        Must be overridden by subclasses.
        """
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """
        Abstract method to validate input data.
        Must be overridden by subclasses.
        """
        pass

    def format_output(self, result: str) -> str:
        """Standard formatting for all processors."""
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """Processor specialized for handling numeric lists."""

    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        """Checks if data is a list of numbers using type()."""
        if type(data) is not list:
            return False

        for x in data:
            if type(x) is not int and type(x) is not float:
                return False
        return True

    def process(self, data: Any) -> str:
        """Calculates sum and average of the numbers."""
        if not self.validate(data):
            return "Error: Invalid numeric data"

        try:
            total = sum(data)
            count = len(data)
            if count == 0:
                average = 0.0
            else:
                average = total / count

            return (f"Processed {count} numeric values, "
                    f"sum={total}, avg={average}")
        except Exception:
            return "Error processing numeric data"


class TextProcessor(DataProcessor):
    """Processor specialized for handling text strings."""

    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        """Checks if data is a string."""
        return type(data) is str

    def process(self, data: Any) -> str:
        """Counts characters and words in the text."""
        if not self.validate(data):
            return "Error: Invalid text data"

        try:
            length = len(data)
            words = len(data.split())
            return f"Processed text: {length} characters, {words} words"
        except Exception:
            return "Error processing text data"


class LogProcessor(DataProcessor):
    """Processor specialized for handling log messages."""

    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        """Checks if data is a string and contains a colon."""
        if type(data) is not str:
            return False
        return ":" in data

    def process(self, data: Any) -> str:
        """Parses log level and message."""
        if not self.validate(data):
            return "Error: Invalid log data"

        try:
            parts = data.split(": ", 1)

            if len(parts) < 2:
                parts = data.split(":", 1)

            level = parts[0]
            message = parts[1]

            if level == "ERROR":
                return f"[ALERT] {level} level detected: {message}"
            else:
                return f"[INFO] {level} level detected: {message}"
        except Exception:
            return "Error processing log"


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    num_proc = NumericProcessor()
    txt_proc = TextProcessor()
    log_proc = LogProcessor()

    # --- Teste Numeric ---
    print("Initializing Numeric Processor...")
    data_num = [1, 2, 3, 4, 5]
    print(f"Processing data: {data_num}")
    if num_proc.validate(data_num):
        print("Validation: Numeric data verified")
        res = num_proc.process(data_num)
        print(num_proc.format_output(res))

    # --- Teste Text ---
    print("Initializing Text Processor...")
    data_txt = "Hello Nexus World"
    print(f"Processing data: \"{data_txt}\"")
    if txt_proc.validate(data_txt):
        print("Validation: Text data verified")
        res = txt_proc.process(data_txt)
        print(txt_proc.format_output(res))

    # --- Teste Log ---
    print("Initializing Log Processor...")
    data_log = "ERROR: Connection timeout"
    print(f"Processing data: \"{data_log}\"")
    if log_proc.validate(data_log):
        print("Validation: Log entry verified")
        res = log_proc.process(data_log)
        print(log_proc.format_output(res))

    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    res1 = num_proc.process([1, 2, 3])
    print(f"Result 1: {res1}")

    res2 = txt_proc.process("Hello World")
    print(f"Result 2: {res2}")

    res3 = log_proc.process("INFO: System ready")
    print(f"Result 3: {res3}")

    print("Foundation systems online. Nexus ready for advanced streams.")
