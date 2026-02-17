from typing import Any, List, Dict, Union, Optional, Protocol
from abc import ABC, abstractmethod


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


class ProcessingPipeline(ABC):

    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id: str = pipeline_id
        self.stages: List[ProcessingStage] = []
        self.metrics: Dict[str, float] = {}
        self.error_count: int = 0

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass

    def _run_stages(self, data: Any) -> Any:
        result = data

        for index, stage in enumerate(self.stages, start=1):
            try:
                result = stage.process(result)
                key = f"stage_{index}_calls"
                self.metrics[key] = self.metrics.get(key, 0) + 1
            except Exception as e:
                self.error_count += 1
                print(f"[{self.pipeline_id}] Error in Stage {index}: {e}")
                raise

        self.metrics["total_calls"] = self.metrics.get("total_calls", 0) + 1

        return result


class InputStage:
    def process(self, data: Any) -> Any:
        if not isinstance(data, dict):
            raise TypeError("InputStage expects dictionary data")
        if "type" not in data:
            raise ValueError("Missing 'type' field")
        return data


class TransformStage:
    def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if data["type"] == "sensor":
            value = data.get("value", 0)
            data["status"] = "Normal" if 0 <= value <= 50 else "Alert"
        elif data["type"] == "user_activity":
            data["count"] = len(data.get("records", []))
        elif data["type"] == "stream":
            readings = data.get("readings", [])
            data["average"] = sum(readings) / len(readings) if readings else 0
        return data


class OutputStage:
    def process(self, data: Dict[str, Any]) -> str:
        if data["type"] == "sensor":
            return f"Processed temperature reading: {data['value']}°C ({data['status']})"
        elif data["type"] == "user_activity":
            return f"User activity logged: {data['count']} actions processed"
        elif data["type"] == "stream":
            readings = data.get("readings", [])
            avg = round(data.get("average", 0), 2)
            return f"Stream summary: {len(readings)} readings, avg: {avg}°C"
        return "Unknown data type"


class JSONAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Any:
        print("Processing JSON data...")
        print("Input:", data)
        if not isinstance(data, str):
            raise TypeError("JSONAdapter expects a string")
        try:
            structured = eval(data)
        except Exception:
            raise ValueError("Invalid JSON format")
        structured["type"] = "sensor"
        return self._run_stages(structured)


class CSVAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Any:
        print("Processing CSV data...")
        print("Input:", data)
        if not isinstance(data, str):
            raise TypeError("CSVAdapter expects a string")
        records = data.split(",")
        structured = {
            "type": "user_activity",
            "records": records
        }
        return self._run_stages(structured)


class StreamAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Any:
        print("Processing Stream data...")
        print("Input:", data)
        if not isinstance(data, list):
            raise TypeError("StreamAdapter expects a list of readings")
        structured = {
            "type": "stream",
            "readings": data
        }
        return self._run_stages(structured)


class NexusManager:
    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)
        
    def process_all(self, data_list: list) -> None:
        for data, pipeline in zip(data_list, self.pipelines):
            print("Output:", self.process_data(data, pipeline) + "\n")

    def process_data(self, data: Any, pipeline: ProcessingPipeline) -> Any:
        result = data
        try:
            result = pipeline.process(result)
        except Exception:
            print(f"[NexusManager] Recovery: skipping failed pipeline {pipeline.pipeline_id}")
        return result


def main() -> None:
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")

    json_pipeline = JSONAdapter("JSON-Pipeline")
    csv_pipeline = CSVAdapter("CSV-Pipeline")
    stream_pipeline = StreamAdapter("Stream-Pipeline")

    for p in [json_pipeline, csv_pipeline, stream_pipeline]:
        p.add_stage(InputStage())
        p.add_stage(TransformStage())
        p.add_stage(OutputStage())

    manager = NexusManager()
    manager.add_pipeline(json_pipeline)
    manager.add_pipeline(csv_pipeline)
    manager.add_pipeline(stream_pipeline)

    json_data = '{"sensor": "temp", "value": 23.5, "unit": "C"}'
    csv_data = "user,action,timestamp"
    stream_data = [22.1, 23.5, 21.8, 24.0, 22.5]
    
    data = [json_data, csv_data, stream_data]
    manager.process_all(data)


if __name__ == "__main__":
    main()