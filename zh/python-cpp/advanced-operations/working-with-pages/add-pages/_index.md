---
title: 使用 C++ 在 Python 中添加 PDF 页面
linktitle: 添加页面
type: docs
weight: 10
url: zh/python-cpp/add-pages/
description: 本文讲解如何在 Python 中使用 C++ 在 PDF 文件的指定位置插入（添加）页面。
lastmod: "2024-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 在 PDF 文件的指定位置插入空白页面

代码片段打开一个 PDF 文档，向其添加一个空白页面，并将修改后的文档保存为一个新的 PDF 文件。

要在 PDF 文件中插入一个空白页面：

1. 打开 PDF 文档
1. 向文档添加一个新的空白页面
1. 使用 'document.save' 方法将修改后的文档保存到输出文件

以下代码片段展示了如何在 PDF 文件中插入一个页面：

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    # 设置示例 PDF 文件所在的目录路径
    dataDir = os.path.join(os.getcwd(), "samples")

    # 设置输入文件路径
    input_file = os.path.join(dataDir, "sample0.pdf")

    # 设置输出文件路径
    output_file = os.path.join(dataDir, "results", "blank_pdf_document.pdf")

    # 打开 PDF 文档
    document = apw.Document(input_file)

    # 向文档添加一个新的空白页面
    document.pages.add()

    # 将修改后的文档保存到输出文件
    document.save(output_file)
```