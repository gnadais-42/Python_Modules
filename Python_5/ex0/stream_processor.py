from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass
    
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid data")
            total = 0
            length = 0
            for n in data:
                total += n
                length += 1
            result = (f"Processed {length} numeric values, "
                    f"sum={total}, avg={total/length:.1f}")
            return self.format_output(result)
        except Exception as e:
            return f"Error: {e}"

    def validate(self, data: Any) -> bool:
        if type(data) != list:
            return False
        for number in data:
            if type(number) != int:
                return False
        return True


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid data")
            letters = 0
            words = 0
            previous = ' '
            for letter in data:
                letters += 1
                if letter != ' ' and previous == ' ':
                    words += 1
                previous = letter
            result = ("Processed text: "
                      f"{letters} characters, {words} words")
            return self.format_output(result)
        except Exception as e:
            return f"Error: {e}"

    def validate(self, data: Any) -> bool:
        if type(data) != str:
            return False
        return True


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid log entry")
            result = None
            if data.startswith("ERROR: "):
                result = f"Error level detected: {data[7:]}"
            else:
                result = f"INFO level detected: {data[6:]}"
            return self.format_output(result)
        except Exception as e:
            return f"Error: {e}"

    def validate(self, data: Any) -> bool:
        if type(data) != str:
            return False
        if data.startswith("ERROR: ") or data.startswith("INFO: "):
            return True
        return False
            
    def format_output(self, result: str) -> str:
        if result.startswith("ERROR"):
            return f"Output: [ALERT] {result}"
        else:
            return f"Output: [INFO] {result}"


def demo():
    processors = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]
    data = [
        [1, 2, 3],
        "Hello Nexus",
        "INFO: System ready"
    ]
    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through "
          "the same interface...")
    for i in range(3):
        print(f"Result {i + 1}:", processors[i].process(data[i]))

print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
print("Initializing Numeric Processor...")
p = NumericProcessor()
data = [1, 2, 3, 4, 5]
print("Processing data:", data)
print("Validation: "
      f"{'Numeric data verified' if p.validate(data) else 'Invalid'}")
print(p.process(data), end="\n\n")

print("Initializing Text Processor...")
p = TextProcessor()
data = "Hello Nexus World"
print(f"Processing data: \"{data}\"")
print("Validation: "
      f"{'Text data verified' if p.validate(data) else 'Invalid'}")
print(p.process(data), end="\n\n")

print("Initializing Log Processor...")
p = LogProcessor()
data = "ERROR: Connection timeout"
print(f"Processing data: \"{data}\"")
print("Validation: "
      f"{'Log entry verified' if p.validate(data) else 'Invalid'}")
print(p.process(data), end="\n\n")

demo()