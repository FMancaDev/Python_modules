#! /usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """
    Abstract Base Class representing a generic data stream.
    """

    def __init__(self, stream_id: str) -> None:
        """Initialize stream with an ID using super."""
        super().__init__()
        self.stream_id = stream_id
        self.processed_count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Process a batch of data. Must be overridden.
        """
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """
        Filter data based on criteria.
        Default implementation returns data as-is.
        """
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return basic stream statistics."""
        return {
            "id": self.stream_id,
            "processed": self.processed_count,
            "type": self.__class__.__name__
        }


class SensorStream(DataStream):
    """Stream handler for numerical sensor data."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        """Calculates average of numeric sensor readings."""
        try:
            valid_readings = [
                x for x in data_batch
                if isinstance(x, (int, float))
            ]
            count = len(valid_readings)
            self.processed_count += count
            if count == 0:
                return f"Sensor {self.stream_id}: No valid readings"

            avg = sum(valid_readings) / count
            return (f"Sensor analysis: {count} readings processed, "
                    f"avg temp: {avg:.1f}°C")
        except Exception as e:
            return f"Error processing sensor batch: {e}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter logic: if criteria is 'high', keep values > 20."""
        if criteria == "high":
            return [x for x in data_batch
                    if isinstance(x, (int, float)) and x > 20]
        return data_batch


class TransactionStream(DataStream):
    """Stream handler for financial transaction tuples."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        """Calculates net flow from (type, amount) tuples."""
        try:
            valid = [
                x for x in data_batch
                if isinstance(x, tuple) and len(x) == 2
                and isinstance(x[1], (int, float))
            ]
            self.processed_count += len(valid)
            net_flow = sum(
                amt if op == 'buy' else -amt
                for op, amt in valid
            )
            return (f"Transaction analysis: {len(valid)} operations, "
                    f"net flow: {net_flow:+} units")
        except Exception as e:
            return f"Error processing transactions: {e}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter logic: if criteria is 'large', keep amounts > 100."""
        if criteria == "large":
            return [x for x in data_batch
                    if isinstance(x, tuple) and len(x) == 2
                    and x[1] > 100]
        return data_batch


class EventStream(DataStream):
    """Stream handler for system event strings."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        """Analyzes event strings."""
        try:
            valid_events = [
                x for x in data_batch
                if isinstance(x, str)
            ]
            self.processed_count += len(valid_events)
            errors = len([e for e in valid_events if "error" in e.lower()])
            return (f"Event analysis: {len(valid_events)} events, "
                    f"{errors} error detected")
        except Exception as e:
            return f"Error processing events: {e}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter logic: if criteria is 'critical', keep only errors."""
        if criteria == "critical":
            return [x for x in data_batch
                    if isinstance(x, str) and "error" in x.lower()]
        return data_batch


class StreamProcessor:
    """
    Manager class to handle multiple streams polymorphically.
    """

    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        """Adds a stream to the processor."""
        if isinstance(stream, DataStream):
            self.streams.append(stream)

    def process_streams(self, data_map: Dict[str, List[Any]]) -> None:
        """
        Polymorphically processes all streams.
        data_map: Dictionary linking stream_id to data batches.
        """
        for stream in self.streams:
            if stream.stream_id in data_map:
                try:
                    result = stream.process_batch(data_map[stream.stream_id])
                    print(result)
                except Exception as e:
                    print(f"Stream {stream.stream_id} failed: {e}")


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    sensor = SensorStream("SENSOR_001")
    trans = TransactionStream("TRANS_001")
    event = EventStream("EVENT_001")
    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(trans)
    processor.add_stream(event)

    sensor_data = [22.5, 65, 1013]
    trans_data = [('buy', 100), ('sell', 150), ('buy', 75)]
    event_data = ["login", "error: timeout", "logout"]

    print("Initializing Sensor Stream...")
    print(f"Stream ID: {sensor.stream_id}, Type: Environmental Data")
    print(f"Processing sensor batch: {sensor_data}")
    print(sensor.process_batch(sensor_data))

    print("\nInitializing Transaction Stream...")
    print(f"Stream ID: {trans.stream_id}, Type: Financial Data")
    print(f"Processing transaction batch: {trans_data}")
    print(trans.process_batch(trans_data))

    print("\nInitializing Event Stream...")
    print(f"Stream ID: {event.stream_id}, Type: System Events")
    print(f"Processing event batch: {event_data}")
    print(event.process_batch(event_data))

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    all_data = {
        "SENSOR_001": sensor_data,
        "TRANS_001": trans_data,
        "EVENT_001": event_data
    }
    print("Batch 1 Results:")
    print(f"- Sensor data: {sensor.processed_count} readings processed")
    print(f"- Transaction data: {trans.processed_count} operations processed")
    print(f"- Event data: {event.processed_count} events processed")

    print("\nStream filtering active: High-priority data only")
    f_sensor = sensor.filter_data(sensor_data, "high")
    f_trans = trans.filter_data(trans_data, "large")
    f_event = event.filter_data(event_data, "critical")
    print(f"Filtered results: {len(f_event)} critical sensor alerts, "
          f"{len(f_trans)} large transaction")
    print("All streams processed successfully. Nexus throughput optimal.")
