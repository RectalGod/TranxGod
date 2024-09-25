import logging
from pathlib import Path
import time
from models.translator import translate_text
from models.utils import replace_blocks
from models.logger import log_translation
from models.config import FILE_PROCESS_DELAY

def process_markdown(file_path: Path, source_directory: Path, output_directory: Path) -> None:
    with file_path.open('r', encoding='utf-8') as file:
        content = file.read()

    patterns = [
        (r'```[\w\-]*\n[\s\S]*?```', 'CODE_BLOCK'),
        (r'!\[.*?\]\(.*?\)', 'IMAGE_BLOCK'),
        (r'`{1,3}[^`]+`{1,3}', 'INLINE_CODE'),
        (r'\[[^\]]+\]\([^)]+\)', 'LINK_URL'),
        (r'<[^>]+>', 'HTML_TAG'),
        (r'\$\$[^$]+\$\$|\$[^$]+\$', 'LATEX'),
        (r'\[\^[^\]]+\]', 'FOOTNOTE'),
        (r'&[a-zA-Z]+;', 'HTML_ENTITY'),
        (r'^-{3,}$', 'HR'),
    ]

    placeholders = {}
    for pattern, prefix in patterns:
        content, new_placeholders = replace_blocks(content, pattern, prefix)
        placeholders.update(new_placeholders)

    translated_content = translate_text(content)

    for placeholder, block in placeholders.items():
        translated_content = translated_content.replace(placeholder, block)

    if source_directory != output_directory:
        translated_file_path = output_directory / file_path.relative_to(source_directory)
    else:
        translated_file_path = file_path.with_name(f"{file_path.stem}-cn.md")

    translated_file_path.parent.mkdir(parents=True, exist_ok=True)
    with translated_file_path.open('w', encoding='utf-8') as file:
        file.write(translated_content)

    log_translation(translated_file_path, "success")

def translate_all_markdown(source_directory: Path, output_directory: Path) -> None:
    md_files = list(source_directory.rglob('*.md'))
    total_files = len(md_files)
    logging.info(f"找到 {total_files} 个 Markdown 文件需要翻译。")

    for idx, fp in enumerate(md_files, start=1):
        logging.info(f"正在翻译文件 {idx}/{total_files}: {fp}")
        try:
            process_markdown(fp, source_directory, output_directory)
        except Exception as e:
            log_translation(fp, "failure", e)
        time.sleep(FILE_PROCESS_DELAY)
