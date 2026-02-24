---
title: 使用 Python 在 PDF 中处理投资组合
linktitle: 投资组合
type: docs
weight: 20
url: /zh/python-net/portfolio/
description: 如何使用 Python 创建 PDF 投资组合。您应该使用 Microsoft Excel 文件、Word 文档和图像文件来创建 PDF 投资组合。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 在 PDF 中处理投资组合
Abstract: 本文讨论了使用 Aspose.PDF for Python via .NET 创建和管理 PDF 投资组合。PDF 投资组合能够将各种文件类型——如文本文件、图像、电子表格和演示文稿——整合到一个有序的文档中，确保所有相关材料统一存放。文章概述了创建 PDF 投资组合的过程，重点介绍了使用 `Document` 类和 `FileSpecification` 类将文件添加到文档集合中。文中提供了示例，演示将 Microsoft Excel 文件、Word 文档和图像文件加入 PDF 投资组合。此外，文章还包括创建投资组合和从中删除文件的代码片段，展示了使用 Aspose.PDF for Python 管理 PDF 投资组合的简便性和高效性。
---

创建 PDF 投资组合可以将不同类型的文件合并和存档到单一、统一的文档中。该文档可以包含文本文件、图像、电子表格、演示文稿以及其他材料，并确保所有相关材料都集中存储并有序组织。

PDF 投资组合将帮助您以高质量的方式展示您的演示文稿，无论您在何处使用它。总体而言，创建 PDF 投资组合是一项非常前沿且现代的任务。

## 如何创建 PDF 投资组合

Aspose.PDF for Python via .NET 允许使用 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类创建 PDF 投资组合文档。在获取文件后，将其添加到 document.collection 对象中，使用 [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) 类。当文件添加完毕后，使用 Document 类的 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法保存投资组合文档。

下面的示例使用 Microsoft Excel 文件、Word 文档和图像文件来创建 PDF 投资组合。

以下代码生成了如下的投资组合。

### 使用 Aspose.PDF for Python 创建的 PDF 投资组合

![使用 Aspose.PDF for Python 创建的 PDF 投资组合](working-with-pdf-portfolio_1.jpg)

```python

    import aspose.pdf as ap

    # Instantiate Document Object
    document = ap.Document()

    # Instantiate document Collection object
    document.collection = ap.Collection()

    # Get Files to add to Portfolio
    excel = ap.FileSpecification(input_excel)
    word = ap.FileSpecification(input_doc)
    image = ap.FileSpecification(input_jpg)

    # Provide description of the files
    excel.description = "Excel File"
    word.description = "Word File"
    image.description = "Image File"

    # Add files to document collection
    document.collection.append(excel)
    document.collection.append(word)
    document.collection.append(image)

    # Save Portfolio document
    document.save(output_pdf)
```

## 从 PDF 投资组合中删除文件

要从 PDF 投资组合中删除文件，请尝试使用以下代码行。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    document.collection.delete()

    # Save updated file
    document.save(output_pdf)
```


