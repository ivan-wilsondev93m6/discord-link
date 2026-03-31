iddleware.py"""Rate limiting and permission middleware."""
import time
import logging
from collections import defaultdict

log = logging.getLogger(__name__)


class RateLimiter:
    def __init__(self, max_per_minute: int = 30):
        self.max = max_per_minute
        self._buckets: dict[str, list[float]] = defaultdict(list)

    def allow(self, user_id: str) -> bool:
        now = time.time()
        bucket = self._buckets[user_id]
        bucket[:] = [t for t in bucket if now - t < 60]
        if len(bucket) >= self.max:
            return False
        bucket.append(now)
        return True

    def reset(self, user_id: str):
        self._buckets.pop(user_id, None)
