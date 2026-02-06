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

    @abstractmethod
    def  filter_data(self, data_batch: List[Any], 
                    criteria: Optional[str] = None) -> List[Any]:
        if not isinstance(list, data_batch):
            raise TypeError("Data must come in a List")
        elif not isinstance(str, criteria) and criteria != None:
            raise TypeError("Please enter valid criteria")
        return data_batch

    @abstractmethod
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass

    def id(self):
        return self._stream_id


class SensorStream(DataStream):
    def __init__(self, stream_id: str, type: str):
        print("Initializing Sensor Stream...")
        print(f"Stream ID: {stream_id}, Type: Environmental Data")
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[str]) -> str:
        print(f"Processing sensor batch: {data_batch}")
        try:
            batch = self.filter_data(data_batch)
            temp = 0
            temp_i = 0
            length = 0
            for data in batch:
                if data[0] == "temp":
                    temp += data[1]
                    temp_i += 1
                length += 1
            return (f"Sensor analysis: {length} readings processed"
                    f", avg temp: {temp / temp_i:.1f}")
        except Exception as e:
            return f"Error: {e}"
        
    def filter_data(self, data_batch: List[str],
                    criteria: Optional[str] = None):
        batch = super().filter_data(data_batch, criteria)
        if criteria != "Environmental":
            raise ValueError("Please enter valid criteria")
        ret_lst = []
        for x in batch:
            data = x.split(":")
            if len(data) != 2:
                raise ValueError("Invalid data")
            if data[0] not in ("temp", "humidity", "pressure"):
                raise ValueError("Invalid data")
            ret_lst.append((data[0], float(data[1])))
        return ret_lst
        


class TransactionStream(DataStream):
    def __init__(self, stream_id: str):
        print("Initializing Transaction Stream...")
        super().__init__(stream_id)


class EventStream(DataStream):
    def __init__(self, stream_id: str):
        print("Initializing Event Stream...")
        super().__init__(stream_id)


class StreamManager:
    pass
