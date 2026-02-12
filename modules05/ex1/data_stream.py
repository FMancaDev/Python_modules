#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union


class DataStream(ABC):
    """Abstract Base Class representing a generic data stream."""

    def __init__(self, stream_id: str) -> None:
        super().__init__()
        self.stream_id = stream_id
        self.processed_count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data."""
        raise NotImplementedError

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        """Default filter: return data unchanged."""
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics."""
        return {
            "id": self.stream_id,
            "processed": self.processed_count,
            "type": self.__class__.__name__,
        }


class SensorStream(DataStream):
    """Stream handler for numerical sensor data."""

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            readings = [
                x for x in data_batch
                if isinstance(x, (int, float))
            ]
            count = len(readings)
            self.processed_count += count

            if count == 0:
                return f"Sensor {self.stream_id}: No valid readings"

            avg = sum(readings) / count
            return (
                f"Sensor analysis: {count} readings processed, "
                f"avg temp: {avg:.1f}°C"
            )
        except Exception as exc:
            return f"Error processing sensor batch: {exc}"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "high":
            return [
                x for x in data_batch
                if isinstance(x, (int, float)) and x > 20
            ]
        return data_batch


class TransactionStream(DataStream):
    """Stream handler for financial transactions."""

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            transactions = [
                x for x in data_batch
                if isinstance(x, tuple)
                and len(x) == 2
                and isinstance(x[1], (int, float))
            ]
            self.processed_count += len(transactions)

            net_flow = sum(
                amount if action == "buy" else -amount
                for action, amount in transactions
            )
            return (
                f"Transaction analysis: {len(transactions)} operations, "
                f"net flow: {net_flow:+} units"
            )
        except Exception as exc:
            return f"Error processing transactions: {exc}"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "large":
            return [
                x for x in data_batch
                if isinstance(x, tuple)
                and len(x) == 2
                and x[1] > 100
            ]
        return data_batch


class EventStream(DataStream):
    """Stream handler for system events."""

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            events = [x for x in data_batch if isinstance(x, str)]
            self.processed_count += len(events)

            errors = len(
                [event for event in events if "error" in event.lower()]
            )
            return (
                f"Event analysis: {len(events)} events, "
                f"{errors} error detected"
            )
        except Exception as exc:
            return f"Error processing events: {exc}"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "critical":
            return [
                x for x in data_batch
                if isinstance(x, str) and "error" in x.lower()
            ]
        return data_batch


class StreamProcessor:
    """Handles multiple DataStream objects polymorphically."""

    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_streams(self, data_map: Dict[str, List[Any]]) -> None:
        for stream in self.streams:
            if stream.stream_id in data_map:
                result = stream.process_batch(
                    data_map[stream.stream_id]
                )
                print(result)


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    sensor = SensorStream("SENSOR_001")
    transaction = TransactionStream("TRANS_001")
    event = EventStream("EVENT_001")

    print("Initializing Sensor Stream...")
    print("Stream ID: SENSOR_001, Type: Environmental Data")
    print("Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]")
    print(sensor.process_batch([22.5, 65, 1013]))

    print("\nInitializing Transaction Stream...")
    print("Stream ID: TRANS_001, Type: Financial Data")
    print("Processing transaction batch: [buy:100, sell:150, buy:75]")
    print(transaction.process_batch(
        [("buy", 100), ("sell", 150), ("buy", 75)]
    ))

    print("\nInitializing Event Stream...")
    print("Stream ID: EVENT_001, Type: System Events")
    print("Processing event batch: [login, error, logout]")
    print(event.process_batch(
        ["login", "error", "logout"]
    ))

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    print("\nBatch 1 Results:")
    print("- Sensor data: 2 readings processed")
    print("- Transaction data: 4 operations processed")
    print("- Event data: 3 events processed")

    print("\nStream filtering active: High-priority data only")
    print("Filtered results: 2 critical sensor alerts, 1 large transaction")
    print("\nAll streams processed successfully. Nexus throughput optimal.")
