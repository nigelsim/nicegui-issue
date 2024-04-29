import example
from nicegui import ui
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, default=8080)
parser.add_argument(
    "--host",
    type=str,
    default="127.0.0.1",
)
args = parser.parse_args()

ui.run(
    title="Dock Simulator",
    port=args.port,
    host=args.host,
    reload=False,
    workers=1
)
