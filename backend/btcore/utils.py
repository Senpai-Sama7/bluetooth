import json
from pathlib import Path
import logging

session_dir = Path.cwd() / "bt_session"
session_dir.mkdir(exist_ok=True)

logger = logging.getLogger("BT-Framework")

def save_session_json(name: str, data):
    path = session_dir / name
    path.write_text(json.dumps(data, indent=2))
