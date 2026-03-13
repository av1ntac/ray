from __future__ import annotations

import os

import ray

from app.custom_script import run_job


@ray.remote
def execute_custom_script(name: str, count: int) -> dict[str, object]:
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
