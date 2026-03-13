from __future__ import annotations

from datetime import UTC, datetime


def run_job(name: str, count: int = 1) -> dict[str, object]:
    """Stand-in for user-defined business logic."""
    normalized = name.strip() or "world"
    return {
        "message": f"Hello, {normalized}!",
        "count": count,
        "processed_at": datetime.now(UTC).isoformat(),
    }
