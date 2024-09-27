# 翻译神 TranxGod

### 成为翻译神, 就是现在!

本项目暂时搁置, 您将见证一个超级项目的诞生.

使用**直肠神**开发的 TranxGod, 你能以**翻译官级**的水准在短时间内**批量翻译**大量文档. **丢掉传统翻译工具吧!** 就是现在, 借助**最顶尖**的免费大模型 Gemini 1.5 Flash/Pro 对 Markdown 文档进行**最纯正**的翻译!

**TranxGod** transcends conventional **translation**, inviting you on a journey of profound **language understanding**. Crafted by **RectalGod**, this groundbreaking tool embodies a spark of **wisdom** and **empowerment**. Harnessing the immense capabilities of **Gemini 1.5 Flash/Pro**, the premier free **LLM**, TranxGod allows you to **batch translate** and **reconstruct Markdown documents** with unmatched **speed** and **precision**. **Language** is not merely a tool; it serves as a bridge to deeper **comprehension**. Embrace the future of **language translation**—access boundless **wisdom** instantly.

### 翻译神的优势

- **支持批量翻译**: 不仅支持翻译单个文件, 还支持导入文件夹, 对文件夹内所有 .md 文件批量翻译

- **不会导致结构混乱**: 由于自然语言和编程语言的结构差异巨大, 在处理 Markdown 文档时, 通常涉及到文本, 代码, 图片, 公式等多种内容, 大模型在处理这些多模态内容时往往表现出模糊性, 缺乏对结构化信息的有效感知与理解, 很容易将文档中的代码, 图片, 链接等内容块搞乱, 导致无法正常阅读. 开发者直肠神针对这一问题, 对文档中的代码, 图片, 链接, HTML 标签, LaTeX 公式, 脚注, HTML 实体, 分隔线都进行了保护, 确保大模型仅对未保护的普通文本部分进行翻译, 彻底解决大模型在格式感知和处理上的"幻觉问题"

### 翻译神的用途

目前, 大多数技术教程缺乏中文支持, 尤其在又一个新技术栈出现时, 中文使用者往往无法在第一时间进行学习, 这间接影响了开源社区的活力. 有了 TranxGod, 你可以下载任意技术博客的源码, 在短时间内轻易得到一本极高质量的中文文档. 不仅如此, 你还可以选择将这本文档开源, 或托管成一个独立的网站, 为更多开发者提供便利!

翻译效果: https://github.com/RectalGod/docsite-cn/tree/main/docs-src/0.5/en

### 超简单的配置

1. 克隆本项目

```
git clone https://github.com/RectalGod/TranxGod.git
```

2. 打开本项目

```
cd TranxGod.git
```

3. 在 config.md 内填写 Gemini API key 后, 运行 main.py 既可

```
python main.py
```

### 代办

TranxGod 还处于十分早期的阶段, 好在它经过了充分的测试, 相信它会让你满意! 作者会在近期新增功能, 这定会让你的体验更上一层楼!

- [ ] 为项目实现 GUI

- [ ] 用 Rust 重构项目

  ...
