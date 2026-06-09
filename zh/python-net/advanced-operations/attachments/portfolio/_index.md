---
title: 在 Python 中创建 PDF 作品集
linktitle: 作品集
type: docs
weight: 20
url: /zh/python-net/portfolio/
description: 了解如何使用 Aspose.PDF for Python via .NET 在 Python 中创建和管理 PDF 作品集。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中构建和编辑包含嵌入文件的 PDF 作品集
Abstract: 本文解释了如何使用 Aspose.PDF for Python via .NET 创建和管理 PDF 作品集。了解如何将多种文件类型打包到单个 PDF 作品集、将文件添加到文档集合，以及使用 Python 以编程方式删除作品集项目。
---

创建 PDF 作品集可以将不同类型的文件整合并归档到单个一致的文档中。此类文档可以包括文本文件、图像、电子表格、演示文稿以及其他材料，并确保所有相关资料都存储并组织在同一位置。

PDF 作品集将帮助您在任何使用场景中以高质量的方式展示您的演示文稿。总体而言，创建 PDF 作品集是一项非常前沿且现代的任务。

当您希望将一组相关文件一起分发，同时保持每个文件在一个 PDF 容器内保持原始格式时，请使用 PDF 作品集。

## 如何创建 PDF 作品集

Aspose.PDF for Python via .NET 允许使用 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class. 在使用该类获取后，将文件添加到 a\u00A0document.collection\u00A0object 中 [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) class. 当文件已添加后，使用\u00A0Document\u00A0class\u0027 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 用于保存作品集文档的方法。

以下示例使用 Microsoft Excel 文件、Word 文档和图像文件来创建 PDF 作品集。

以下代码生成如下作品集。

### 使用 Aspose.PDF for Python 创建的 PDF 作品集

![使用 Aspose.PDF for Python 创建的 PDF 作品集](working-with-pdf-portfolio_1.jpg)

```python
import aspose.pdf as ap

def create_pdf_portfolio(input_files, outfile):
    # Instantiate Document Object
    document = ap.Document()

    # Instantiate document Collection object
    document.collection = ap.Collection()

    # Get Files to add to Portfolio
    excel = ap.FileSpecification(input_files[0])
    word = ap.FileSpecification(input_files[1])
    image = ap.FileSpecification(input_files[2])

    # Provide description of the files
    excel.description = "Excel File"
    word.description = "Word File"
    image.description = "Image File"

    # Add files to document collection
    document.collection.append(excel)
    document.collection.append(word)
    document.collection.append(image)

    # Save Portfolio document
    document.save(outfile)
```

## 从 PDF Portfolio 中删除文件

要从 PDF 组合文档中删除/移除文件，请尝试使用以下代码行。

```python
import aspose.pdf as ap

def remove_files_from_pdf_portfolio(infile, outfile):
    # Open document
    document = ap.Document(infile)
    document.collection.delete()

    # Save updated file
    document.save(outfile)
```

## 相关附件主题

- [在 Python 中处理 PDF 附件](/pdf/zh/python-net/attachments/)
- [在 Python 中向 PDF 添加附件](/pdf/zh/python-net/add-attachment-to-pdf-document/)
- [在 Python 中删除 PDF 附件](/pdf/zh/python-net/removing-attachment-from-an-existing-pdf/)

