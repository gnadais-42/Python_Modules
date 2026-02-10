from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod

class DataStream(ABC):
    def __init__(self, stream_id: str):
        print("Initializing Stream...")
        print(f"Stream ID: {stream_id}")
        self._stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def  filter_data(self, data_batch: List[Any], 
                    criteria: Optional[str] = None) -> List[Any]:
        if not isinstance(data_batch, list):
            raise TypeError("Data must come in a List")
        elif not isinstance(criteria, str) and criteria != None:
            raise TypeError("Please enter valid criteria")
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "Stream_id": self._stream_id
        }

    def id(self):
        return self._stream_id


class SensorStream(DataStream):
    def __init__(self, stream_id: str):
        print("Initializing Sensor Stream...")
        print(f"Stream ID: {stream_id}, Type: Environmental Data")
        super().__init__(stream_id)
        self.readings = 0
        self.total_temp = 0
        self.count_temp = 0

    def process_batch(self, data_batch: List[str]) -> str:
        print(f"Processing sensor batch: {data_batch}")
        try:
            batch = self.filter_data(data_batch, "Environmental")
            for data in batch:
                if data[0] == "temp":
                    self.total_temp += data[1]
                    self.count_temp += 1
                self.readings += 1
            return (f"Sensor analysis: {self.readings} readings processed"
                    f", avg temp: {self.total_temp / self.count_temp:.1f}ºC")
        except Exception as e:
            return f"Error: {e}"
        
    def filter_data(self, data_batch: List[str],
                    criteria: Optional[str] = None):
        if not isinstance(data_batch, list):
            raise TypeError("Data must come in a List")
        elif not isinstance(criteria, str) and criteria != None:
            raise TypeError("Please enter valid criteria")
        if criteria != "Environmental":
            raise ValueError("Please enter valid criteria")
        ret_lst = []
        for x in data_batch:
            data = x.split(":")
            if len(data) != 2:
                raise ValueError("Invalid data")
            if data[0] not in ("temp", "humidity", "pressure"):
                raise ValueError("Invalid data")
            ret_lst.append((data[0], float(data[1])))
        return ret_lst
    
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        avg_temp = 0
        if self.count_temp != 0:
            avg_temp = self.total_temp / self.count_temp
        return {
            "Stream_id": self._stream_id,
            "Readings": self.readings,
            "Total _temp": self.total_temp,
            "Average_temp": avg_temp
        }
        

class TransactionStream(DataStream):
    def __init__(self, stream_id: str):
        print("Initializing Transaction Stream...")
        print(f"Stream ID: {stream_id}, Type: Financial Data")
        super().__init__(stream_id)
        self.operations = 0
        self.net_flow = 0

    def  filter_data(self, data_batch: List[Any], 
                    criteria: Optional[str] = None) -> List[Any]:
        if not isinstance(data_batch, list):
            raise TypeError("Data must come in a List")
        elif not isinstance(criteria, str) and criteria != None:
            raise TypeError("Please enter valid criteria")
        if criteria != "Financial":
            raise ValueError("Please enter valid criteria")
        ret_lst = []
        for x in data_batch:
            data = x.split(":")
            if len(data) != 2:
                raise ValueError("Invalid data")
            if data[0] not in ("buy", "sell"):
                raise ValueError("Invalid data")
            ret_lst.append((data[0], float(data[1])))
        return ret_lst
    
    def process_batch(self, data_batch: List[str]) -> str:
        print(f"Processing transaction batch: {data_batch}")
        try:
            batch = self.filter_data(data_batch, "Financial")
            for data in batch:
                if data[0] == "buy":
                    self.net_flow += data[1]
                elif data[0] == "sell":
                    self.net_flow -= data[1]
                self.operations += 1
            return (f"Transaction analysis: {self.operations} operations"
                    f", net flow: {self.net_flow:+} units")
        except Exception as e:
            return f"Error: {e}"
        
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "Stream_id": self._stream_id,
            "Operations": self.operations,
            "Net_flow": self.net_flow
        }


class EventStream(DataStream):
    def __init__(self, stream_id: str):
        print("Initializing Event Stream...")
        print(f"Stream ID: {stream_id}, Type: System Events")
        super().__init__(stream_id)
        self.events = 0
        self.errors = 0

    def  filter_data(self, data_batch: List[Any], 
                    criteria: Optional[str] = None) -> List[Any]:
        if not isinstance(data_batch, list):
            raise TypeError("Data must come in a List")
        elif not isinstance(criteria, str) and criteria != None:
            raise TypeError("Please enter valid criteria")
        if criteria != "Event":
            raise ValueError("Please enter valid criteria")
        ret_lst = []
        for x in data_batch:
            if x not in ("login", "logout", "error"):
                raise ValueError("Invalid data")
            ret_lst.append(x)
        return ret_lst

    def process_batch(self, data_batch: List[str]) -> str:
        print(f"Processing event batch: {data_batch}")
        try:
            batch = self.filter_data(data_batch, "Event")
            for data in batch:
                if data == "error":
                    self.errors += 1
                self.events += 1
            return (f"Event analysis: {self.events} events"
                    f", {self.errors} error detected")
        except Exception as e:
            return f"Error: {e}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "Stream_id": self._stream_id,
            "Errors": self.errors
        }


class StreamManager:
    def __init__(self):
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream):
        if not isinstance(stream, DataStream):
            raise TypeError("Only DataStream objects allowed")
        self.streams.append(stream)

    def process_all(self, batches: Dict[str, List[Any]]):
        print("=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...\n")

        for stream in self.streams:
            try:
                stream_id = stream.id()
                if stream_id in batches:
                    result = stream.process_batch(batches[stream_id])
                    print(f"- {result}")
                else:
                    print(f"- No batch for stream {stream_id}")
            except Exception as e:
                print(f"- Error processing stream {stream.id()}: {e}")


print("=== CODE NEXUS- POLYMORPHIC STREAM SYSTEM ===\n")
sensor = SensorStream("SENSOR_001")
print(sensor.process_batch(["temp:22.5", "humidity:65", "pressure:1013"]))
print()
transaction = TransactionStream("TRANS_001")
print(transaction.process_batch(["buy:100", "sell:150", "buy:75"]))
print()
event = EventStream("EVENT_001")
print(event.process_batch(["login", "error", "logout"]))
print()
manager = StreamManager()
manager.add_stream(sensor)
manager.add_stream(transaction)
manager.add_stream(event)
batches = {
    "SENSOR_001": ["temp:25.0", "temp:20.0"],
    "TRANS_001": ["buy:200", "sell:50", "buy:25", "sell:100"],
    "EVENT_001": ["login", "error", "error"]
}
manager.process_all(batches)

