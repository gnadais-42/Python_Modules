from typing import Any, List, Dict, Union, Optional, Protocol
from abc import ABC, abstractmethod


class ProcessingPipeline(ABC):
	stages: List[ProcessingStage] = []

	@abstractmethod
	def process(self, data: Any) -> Any:
		pass

	def add_stage(cls, stage: ProcessingStage) -> None:
		cls.stages.append(stage)


class ProcessingStage(Protocol):
	def process(self, data: Any) -> Any:
        pass


class InputStage():
	def process(self, data: Any) -> Dict:
        pass


class TransformStage():
	def process(self, data: Any) -> Dict:
        pass


class OutputStage():
	def process(self, data: Any) -> str:
        pass


class JSONAdapter():
	def __init__(self, pipeline_id):
		self.pipeline_id = pipeline_id

	def process(self, data: Any) -> Any:
        pass


class CSVAdapter():
	def __init__(self, pipeline_id):
        self.pipeline_id = pipeline_id

	def process(self, data: Any) -> Any:
        pass


class StreamAdapter():
	def __init__(self, pipeline_id):
        self.pipeline_id = pipeline_id

	def process(self, data: Any) -> Any:
        pass


class NexusManager():
	pipelines: List[ProcessingPipeline]

	def add_pipeline(cls, pipeline: ProcessingPipeline) -> None:
		cls.pipelines.append(pipeline)

	def process_data() -> Any:
		pass
	pass
