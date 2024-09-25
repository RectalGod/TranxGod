# Gemini 配置
GEMINI_API_URL: "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"
API_KEY: "在此填写您的 Gemini API key"  # Gemini API 密钥

# 翻译提示语
TRANSLATE_PROMPT: "请将以下英文文本翻译成中文，同时保持Markdown语法和代码块不变："  # 翻译提示语

# 重试机制
MAX_RETRIES: 3  # 请求失败时的最大重试次数
RETRY_DELAY: 5  # 每次重试之间的等待时间（秒）

# 处理延迟
FILE_PROCESS_DELAY: 2  # 每处理一个文件后的延迟时间（秒）

# 日志配置
LOG_LEVEL: "INFO"  # 日志级别
LOG_SUCCESS_MESSAGE: "已翻译并保存: {file_path}"  # 成功日志消息模板
LOG_FAILURE_MESSAGE: "处理文件 {file_path} 失败: {error}"  # 失败日志消息模板
