---
title: 将PDF转换为文本在Python中
linktitle: 将PDF转换为其他格式
type: docs
weight: 90
url: /python-cpp/convert-pdf-to-other-files/
lastmod: "2022-12-23"
keywords: 转换, PDF, EPUB, LaText, 文本, XPS, Python
description: 本主题向您展示如何使用Python将PDF文件转换为其他文件格式，如文本。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## 将PDF转换为文本

**Aspose.PDF for Python** 支持将整个PDF文档和单个页面转换为文本文件。

### 将PDF文档转换为文本文件

您可以使用 'TextDevice' 类将PDF文档转换为TXT文件。

1. 创建输入和输出文件路径
1. 使用 [extractor_create](https://reference.aspose.com/pdf/python-cpp/core/extractor_create/) 创建PDF提取器外观的实例
1. 使用 [extractor_bind_pdf](https://reference.aspose.com/pdf/python-cpp/core/extractor_bind_pdf/) 将PDF文件绑定到提取器

1. 使用 [extractor_extract_text](https://reference.aspose.com/pdf/python-cpp/core/extractor_extract_text/) 从 PDF 文件中提取文本
1. 将提取的文本写入输出文件
1. 使用 'document.save' 方法保存输出 PDF。

以下代码片段说明如何从所有页面中提取文本。

```python

    from AsposePdfPython import *

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf =  DIR_OUTPUT + "convert_pdf_to_txt.txt"

    extactor = extractor_create()
    extractor_bind_pdf(extactor,input_pdf)
    text = extractor_extract_text(extactor)

    with open(output_pdf, 'w') as f:
        f.write(text)
```