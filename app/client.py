from __future__ import annotations

import logging
import os
from typing import Any

import ray

from app.custom_script import run_job


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)
TASK_NAME = "app.client.execute_custom_script"


def _task_metadata() -> dict[str, str | None]:
    context = ray.get_runtime_context()
    task_id_getter = getattr(context, "get_task_id", None)
    job_id_getter = getattr(context, "get_job_id", None)
    node_id_getter = getattr(context, "get_node_id", None)
    return {
        "task_id": str(task_id_getter()) if callable(task_id_getter) else None,
        "job_id": str(job_id_getter()) if callable(job_id_getter) else None,
        "node_id": str(node_id_getter()) if callable(node_id_getter) else None,
    }


@ray.remote
def execute_custom_script(name: str, count: int) -> dict[str, object]:
    task_params: dict[str, Any] = {"name": name, "count": count}
    LOGGER.info(
        "Starting Ray task task_name=%s params=%s metadata=%s",
        TASK_NAME,
        task_params,
        _task_metadata(),
    )
    return run_job(name=name, count=count)


def main() -> None:
    address = os.environ.get("RAY_CLIENT_ADDRESS", "ray://127.0.0.1:10001")
    ray.init(
        address,
        runtime_env={"working_dir": "."},
    )
    result = ray.get(execute_custom_script.remote(name="client", count=2))
    print(result)


if __name__ == "__main__":
    main()
