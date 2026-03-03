from typing import List, Dict, Set, Tuple

class TimeMap:

    def __init__(self):
        self.store: Dict[str, List[Tuple[int, str]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.store.get(key) is None:
            self.store.setdefault(key, [])
        self.store.get(key).append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        print()
