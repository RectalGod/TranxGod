import yaml

with open('config.md', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    config_lines = []
    for line in lines:
        if line.strip() and not line.startswith('#'):
            config_lines.append(line)
    config_content = ''.join(config_lines)

config = yaml.safe_load(config_content)

GEMINI_API_URL = config.get('GEMINI_API_URL')
API_KEY = config.get('API_KEY')
TRANSLATE_PROMPT = config.get('TRANSLATE_PROMPT')
MAX_RETRIES = config.get('MAX_RETRIES')
RETRY_DELAY = config.get('RETRY_DELAY')
FILE_PROCESS_DELAY = config.get('FILE_PROCESS_DELAY')
LOG_LEVEL = config.get('LOG_LEVEL')
LOG_SUCCESS_MESSAGE = config.get('LOG_SUCCESS_MESSAGE')
LOG_FAILURE_MESSAGE = config.get('LOG_FAILURE_MESSAGE')
