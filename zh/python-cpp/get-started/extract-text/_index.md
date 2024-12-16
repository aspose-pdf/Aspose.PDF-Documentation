---
title: 使用 Python 从 PDF 中提取文本
linktitle: 从 PDF 中提取文本
type: docs
weight: 10
url: /zh/python-cpp/extract-text/
description: 本节介绍如何使用 Python 库从 PDF 文档中提取文本。
lastmod: "2024-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 从 PDF 文档的所有页面提取文本

从 PDF 中提取文本并不容易。许多 PDF 阅读器无法从 PDF 图像或扫描的 PDF 中提取文本。但是，**Aspose.PDF for Python via C++** 工具可以轻松地从所有 PDF 文件中提取文本。

查看代码片段并按照以下步骤从 PDF 中提取文本：

1. 导入 Aspose.PDF for Python 库
1. 创建一个新的提取器对象，用于从 PDF 文档中提取文本和图像。
1. 将提取器对象绑定到 PDF 文件，该文件是提取的来源。
1. 从 PDF 文档中提取所有文本并将其放入某个变量中。

1. 做任何事情，将提取的文本打印到控制台，搜索一些片段等

```python
from AsposePdfPython import *

extactor = Extract()
extractor_bind_pdf(extactor,"blank_pdf_document.pdf")
text = extractor_extract_text(extactor)

print(text)
```