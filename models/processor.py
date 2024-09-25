import argparse
import sys
from pathlib import Path
import logging
from models.logger import setup_logging
from models.markdown import translate_all_markdown, process_markdown
from models.config import LOG_LEVEL

def main() -> None:
    setup_logging(LOG_LEVEL)

    parser = argparse.ArgumentParser(description="TranxGod")
    parser.add_argument("path", nargs='?', help="请输入你需要翻译的文件夹或文件的路径")
    args = parser.parse_args()

    input_path_str = args.path or input("请输入需要翻译的文件夹或文件的路径: ").strip()
    if not input_path_str:
        logging.error("未提供需要翻译的文件夹或文件的路径, 程序将退出")
        sys.exit(1)
    input_path = Path(input_path_str)

    if input_path.is_dir():
        output_directory = input_path.parent / f"{input_path.name}-cn"
        translate_all_markdown(input_path, output_directory)
    elif input_path.is_file() and input_path.suffix == '.md':
        output_file = input_path.with_name(f"{input_path.stem}-cn.md")
        process_markdown(input_path, source_directory=input_path.parent, output_directory=input_path.parent)
    else:
        logging.error("请输入有效的 Markdown 文件或含有 Markdown 文件的目录路径")

if __name__ == "__main__":
    main()
