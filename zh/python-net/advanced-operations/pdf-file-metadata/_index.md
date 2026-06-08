---
title: 在 Python 中处理 PDF 文件元数据
linktitle: PDF 文件元数据
type: docs
weight: 200
url: /zh/python-net/pdf-file-metadata/
description: 学习如何在 Python 中使用 Aspose.PDF 提取、更新和管理 PDF 文件元数据及 XMP 属性。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中获取和设置 PDF 文档信息及 XMP 元数据
Abstract: 本文解释了如何在 Aspose.PDF for Python via .NET 中处理 PDF 元数据。了解如何读取文档信息，如作者、标题和关键字，更新文件属性，设置 XMP 元数据字段，以及在 Python 中为 PDF 文件注册自定义元数据前缀。
---

当您需要检查文档属性、更新 PDF 文件信息以用于搜索或编目，或在 Python 中以编程方式管理 XMP 元数据时，请使用本指南。

## 获取 PDF 文件信息

此代码片段演示了如何使用 Aspose.PDF for Python via .NET 从 PDF 文档中提取元数据。通过访问 Document 对象的 info 属性，它检索关键信息，如作者、创建日期、关键字、修改日期、主题和标题。此功能对于需要文档编目、搜索优化或文档属性验证的应用程序至关重要。

1. 使用 Document 类打开 PDF 文件
1. 通过 info 属性检索文档的元数据
1. 显示元数据信息。打印所需的元数据字段

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def get_pdf_file_information(infile):
    # Open PDF document
    document = ap.Document(infile)

    # Get document information
    doc_info = document.info

    # Display document information
    print(f"Author: {doc_info.author}")
    print(f"Creation Date: {doc_info.creation_date}")
    print(f"Keywords: {doc_info.keywords}")
    print(f"Modify Date: {doc_info.mod_date}")
    print(f"Subject: {doc_info.subject}")
    print(f"Title: {doc_info.title}")
```

## 设置 PDF 文件信息

Aspose.PDF for Python via .NET 允许您为 PDF 设置特定文件信息，例如作者、创建日期、主题和标题。要设置这些信息：

1. 使用 Document 类打开 PDF 文件。
1. 创建一个 [DocumentInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/documentinfo/) 对象并设置所需的元数据属性。
1. 使用 save 方法将更改保存为一个新 PDF 文件。

下面的代码片段展示了如何设置 PDF 文件信息。

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def set_file_information(infile, outfile):

    # Open PDF document
    document = ap.Document(infile)

    # Specify document information
    doc_info = ap.DocumentInfo(document)
    doc_info.author = "Aspose"
    doc_info.creation_date = datetime.datetime.now()
    doc_info.keywords = "Aspose.Pdf, DOM, API"
    doc_info.mod_date = datetime.datetime.now()
    doc_info.subject = "PDF Information"
    doc_info.title = "Setting PDF Document Information"
    doc_info.producer = "Custom producer"
    doc_info.creator = "Custom creator"

    # Save PDF document
    document.save(outfile)
```

## 在 PDF 文件中设置 XMP 元数据

此代码片段演示了如何使用 Aspose.PDF for Python via .NET 以编程方式设置或更新 PDF 文档中的 XMP 元数据。通过修改诸如 xmp:CreateDate、xmp:Nickname 和自定义字段等属性，您可以将标准化的元数据嵌入 PDF 文件中。此方法特别适用于提升文档组织、方便搜索以及将关键信息直接嵌入文件中。

Aspose.PDF 允许您在 PDF 文件中设置元数据。要设置元数据：

1. 使用以下方式打开 PDF 文件 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类。
1. 通过为特定键分配值来修改 XMP 元数据。
1. 保存已更新的 PDF 文档。

以下代码片段展示了如何在 PDF 文件中设置元数据。

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def set_xmp_metadata(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Set XMP metadata properties
    document.metadata.add("xmp:CreateDate", datetime.datetime.now().isoformat())
    document.metadata.add("xmp:Nickname", "Nickname")
    document.metadata.add("xmp:CustomProperty", "Custom Value")

    # Save the updated PDF document
    document.save(outfile)
```

## 插入带前缀的元数据

一些开发人员需要使用前缀创建新的元数据命名空间。下面的代码片段展示了如何插入带前缀的元数据。

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def set_prefix_metadata(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Register a namespace URI for the 'xmp' prefix
    document.metadata.register_namespace_uri("xmp", "http://ns.adobe.com/xap/1.0/")

    # Set the metadata property using the registered prefix
    document.metadata.add(
        "xmp:ModifyDate", datetime.datetime.now().isoformat()
    )  # ISO 8601 format

    # Save the updated PDF document
    document.save(outfile)
```

## 相关主题

- [Python中的高级PDF操作](/pdf/zh/python-net/advanced-operations/)
- [使用 Python 处理 PDF 文档](/pdf/zh/python-net/working-with-documents/)
- [在 Python 中处理 PDF 附件](/pdf/zh/python-net/attachments/)
- [在 Python 中比较 PDF 文档](/pdf/zh/python-net/compare-pdf-documents/)
