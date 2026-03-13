# Ray Client Python Proof of Concept

This project shows how to run a custom Python script on a remote Ray cluster through Ray Client.

## Prerequisites

- [Pixi](https://pixi.sh/latest/) installed
- Access to a remote Ray cluster with Ray Client enabled

## Install dependencies

```powershell
pixi install
```

## Configure the remote cluster address

Set the Ray Client endpoint before running the example.

```powershell
$env:RAY_CLIENT_ADDRESS = "ray://your-ray-head.example.com:10001"
```

If `RAY_CLIENT_ADDRESS` is not set, the client falls back to `ray://127.0.0.1:10001`.

## Run the custom script through Ray Client

```powershell
pixi run client
```

That command:

1. Connects to the remote cluster through Ray Client
2. Ships the local project as the Ray runtime working directory
3. Executes the custom Python logic as a remote Ray task

## Project structure

```text
app/
  custom_script.py  # custom business logic
  client.py         # Ray Client example
```
