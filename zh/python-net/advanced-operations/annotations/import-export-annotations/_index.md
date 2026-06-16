---
title: 使用 Python 导入和导出批注
linktitle: 导入和导出注释
type: docs
weight: 80
url: /zh/python-net/import-export-annotations/
description: 了解如何使用 Aspose.PDF for Python via .NET 从一个 PDF 导入批注并将其导出到新 PDF 文档中。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中传输 PDF 注释。
Abstract: 本文介绍了如何使用 Aspose.PDF for Python via .NET 将注释从源 PDF 复制并导出到新的 PDF 文档。该演练将过程拆分为多个小步骤，包括加载源文件、创建目标文档、添加页面、从第一页复制注释以及保存结果。
---

本文展示了如何使用 Aspose.PDF for Python via .NET 从现有 PDF 导入批注并将其导出到新 PDF 文档。

此示例从源文件的第一页读取注释，创建一个新 PDF，添加一个空白页，并将每个注释复制到该新页。此方法在需要将评论、标记或审阅笔记移至单独的输出文档时非常有用。

## 加载源 PDF

创建一个 `Document` 对象用于已经包含批注的输入文件。该对象提供对页面集合的访问以及每个页面上存储的批注。

```python
source_document = ap.Document(infile)
```

## 创建目标 PDF

接下来，创建一个空的 PDF 文档，用于接收导入的批注。此时，目标文档不包含任何页面。

```python
destination_document = ap.Document()
```

## 添加一个用于导出注释的页面

因为注释必须属于页面，在复制任何内容之前，请向目标文档添加一个新页面。

```python
page = destination_document.pages.add()
```

## 复制源页面的注释

遍历源 PDF 第一页的注释集合，并将每个注释添加到目标文档的新页面中。

第二个参数在 `page.annotations.add(annot, True)` 告诉 Aspose.PDF 将批注复制到目标页面，而不是仅仅复用现有的对象引用。

```python
for annot in source_document.pages[1].annotations:
    page.annotations.add(annot, True)
```

## 保存输出文档

在所有批注复制完成后，保存目标文档以生成最终的 PDF 文件。

```python
destination_document.save(outfile)
```

## 完整示例

以下代码将所有步骤合并为一个可重用的函数：

```python
import sys
import aspose.pdf as ap
from os import path


sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def import_export(infile, outfile):
    """
    Import annotations from one PDF document and export them to a new PDF document.
    """
    source_document = ap.Document(infile)
    destination_document = ap.Document()

    page = destination_document.pages.add()

    for annot in source_document.pages[1].annotations:
        page.annotations.add(annot, True)

    destination_document.save(outfile)
```

## 相关主题

- [交互式注释](/python-net/interactive-annotations/)
- [标记注释](/python-net/markup-annotations/)
- [媒体注释](/python-net/media-annotations/)
- [安全注释](/python-net/security-annotations/)
- [形状注释](/python-net/shape-annotations/)
- [基于文本的注释](/python-net/text-based-annotations/)
- [水印注释](/python-net/watermark-annotations/)
