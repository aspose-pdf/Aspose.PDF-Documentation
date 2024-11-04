---
title: 如何通过 C++ 使用 Python 合并 PDF
linktitle: 合并 PDF 文件
type: docs
weight: 10
url: /python-cpp/merge-pdf-documents/
keywords: "合并多个 pdf 成为单个 pdf python, 合并多个 pdf 为一个 python, 合并多个 pdf 到一个 python"
description: 本页面解释如何使用 Python 将 PDF 文档合并为单个 PDF 文件。
lastmod: "2024-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 通过 C++ 在 Python 中将多个 PDF 合并或组合成单个 PDF

通过利用 Python 和 Aspose 的 C++ 库，你可以轻松高效地将多个 PDF 文件合并成一个 PDF。

要连接两个 PDF 文件：

1. 打开第一个文档
1. 然后将第二个文档的页面添加到第一个文档
1. 使用 'document.save' 方法保存连接后的输出文件。

以下代码片段展示了如何连接 PDF 文件。

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    dataDir = os.path.join(os.getcwd(), "samples")
    input_file= os.path.join(dataDir , "sample0.pdf")
    output_file = os.path.join(dataDir , "results", "concatenated-files.pdf")

    # 打开第一个文档
    document1 = apw.Document(inputFile)
    document2 = apw.Document(inputFile)

    # 将第二个文档的页面添加到第一个文档
    document1.pages.add(document2.pages)

    # 保存连接后的输出文件
    document1.save(output_file)
```