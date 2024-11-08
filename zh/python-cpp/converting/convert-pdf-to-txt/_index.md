---
title: 将 PDF 转换为 TXT 在 Python 中
linktitle: 将 PDF 转换为 TXT
type: docs
weight: 20
url: /zh/python-cpp/convert-pdf-to-txt/
lastmod: "2024-04-23"
description: Aspose.PDF for Python via C++ 库允许您使用 Python 将 PDF 转换为 TXT 格式。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 将 PDF 转换为 TXT

Aspose.PDF for Python via C++ 支持通过以下步骤将 PDF 文档转换为文本文件：

1. 创建输入和输出文件路径
1. 使用 [extractor_create](https://reference.aspose.com/pdf/python-cpp/core/extractor_create/) 创建 PDF 提取器外观的实例
1. 使用 [extractor_bind_pdf](https://reference.aspose.com/pdf/python-cpp/core/extractor_bind_pdf/) 将 PDF 文件绑定到提取器
1. 使用 [extractor_extract_text](https://reference.aspose.com/pdf/python-cpp/core/extractor_extract_text/) 从 PDF 文件中提取文本
1. 将提取的文本写入输出文件
1. 使用 'document.save' 方法保存输出 PDF。

下面的代码片段展示了如何使用 Python via C++ 将 JPG 图像转换为 PDF：

```python

    import AsposePDFPython as apCore
    import os
    import os.path

    # 创建数据目录路径
    dataDir = os.path.join(os.getcwd(), "samples")

    # 创建输入文件路径
    input_file = os.path.join(dataDir, "sample.pdf")

    # 创建输出文件路径
    output_file = os.path.join(dataDir, "results", "pdf-to-txt.txt")

    # 创建PDF提取器外观的实例
    extactor = apCore.facades_pdf_extractor_create()

    # 绑定PDF文件到提取器
    apCore.facades_facade_bind_pdf(extactor, input_file)

    # 从PDF文件中提取文本
    text = apCore.facades_pdf_extractor_extract_text(extactor)

    # 将提取的文本写入输出文件
    with open(output_file, 'w') as f:
        f.write(text)
```