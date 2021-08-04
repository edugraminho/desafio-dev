from pathlib import Path
import os

ROOT = Path(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(ROOT, "data")


EXTENSIONS = {'txt'}