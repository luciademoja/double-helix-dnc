
import pytest
import os
from elayra.elayra_symbolic_memory import MemoryManager

def test_memory_manager_write_and_recall(tmp_path):
    path = tmp_path / "memory.json"
    mm = MemoryManager(path=str(path))
    mm.save_memory(["E", "P"], context="test", entropy=0.5)
    assert mm.last(1)[0]["context"] == "test"
