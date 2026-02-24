---
title: 使用 Python 从 PDF 中提取字体
linktitle: 提取 PDF 字体
type: docs
weight: 30
url: /zh/python-net/extract-fonts-from-pdf/
description: 使用 Aspose.PDF for Python 库从您的 PDF 文档中提取所有嵌入的字体。
lastmod: "2025-03-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 从 PDF 中提取字体
Abstract: 本文提供了使用 Aspose.PDF 库中特定方法从 PDF 文档中提取所有字体的指导。它介绍了 `Document` 类中可用的 `font_utilities.get_all_fonts()` 方法，该方法便于检索字体信息。文章包含了演示此过程的 Python 代码片段，涉及导入必要的模块、打开 PDF 文档以及遍历字体以打印每个字体的名称。此方法对需要分析或操作 PDF 文件中字体数据的开发者非常有用。
---

如果您想从 PDF 文档中获取所有字体，可以使用 Document 类提供的 `font_utilities.get_all_fonts()` 方法。请查看以下代码片段，以从现有 PDF 文档中获取所有字体：

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)

    # Open PDF document
    document = apdf.Document(path_infile)

    fonts = document.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)
```

