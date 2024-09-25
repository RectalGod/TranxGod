import re
from typing import Tuple, Dict
import uuid

def generate_placeholder(prefix: str) -> str:
    return f"[[[{prefix}_{uuid.uuid4()}]]]"

def replace_blocks(content: str, pattern: str, prefix: str) -> Tuple[str, Dict[str, str]]:
    blocks = re.findall(pattern, content, re.MULTILINE)
    placeholders = {generate_placeholder(prefix): block for block in blocks}
    for placeholder, block in placeholders.items():
        content = content.replace(block, placeholder, 1)
    return content, placeholders
