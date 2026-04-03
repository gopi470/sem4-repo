from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)

        max_freq = max(freq.values())
        count_max = list(freq.values()).count(max_freq)

        return max(len(tasks), (max_freq - 1) * (n + 1) + count_max)