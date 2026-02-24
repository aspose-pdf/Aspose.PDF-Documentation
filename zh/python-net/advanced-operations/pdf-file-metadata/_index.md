---
title: 使用 Python 处理 PDF 文件元数据
linktitle: PDF 文件元数据
type: docs
weight: 200
url: /zh/python-net/pdf-file-metadata/
description: 了解如何在 Python 中使用 Aspose.PDF 提取和管理 PDF 元数据，如作者和标题。
lastmod: "2025-05-12"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 获取和设置 PDF 元数据
Abstract: 本文提供了使用 Aspose.PDF for Python via .NET 操作 PDF 元数据的完整指南。它概述了提取和设置元数据属性的方法，包括作者、创建日期、关键字等，这些对于文档目录编制、搜索优化或验证至关重要。代码片段演示了如何使用 `Document` 类和 `info` 属性从 PDF 中检索元数据，使用 `DocumentInfo` 对象设置新元数据并保存更改。此外，还展示了如何以编程方式更新 XMP 元数据，以提升文档组织和可检索性。文章还解释了通过注册命名空间 URI 插入带自定义前缀的元数据。这些功能对希望在应用程序中有效管理 PDF 文档信息的开发者来说是必不可少的。
---

## 获取 PDF 文件信息

此代码片段演示了如何使用 Aspose.PDF for Python via .NET 从 PDF 文档中提取元数据。通过访问 Document 对象的 info 属性，它检索到作者、创建日期、关键字、修改日期、主题和标题等关键信息。此功能对于需要文档目录编制、搜索优化或文档属性验证的应用程序至关重要。

1. 使用 Document 类打开 PDF 文件
1. 通过 info 属性检索文档的元数据
1. 显示元数据信息。打印所需的元数据字段

```python

    import aspose.pdf as ap

    def get_pdf_file_information():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf()

        # Open PDF document
        document = ap.Document(data_dir + "GetFileInfo.pdf")

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

Aspose.PDF for Python via .NET 允许您为 PDF 设置特定的文件信息，如作者、创建日期、主题和标题。设置这些信息的方法如下：

1. 使用 Document 类打开 PDF 文件。
1. 创建一个 [DocumentInfo]() 对象并设置所需的元数据属性。
1. 使用 save 方法将更改保存到新的 PDF 文件。

以下代码片段展示了如何设置 PDF 文件信息。

```python

    import aspose.pdf as ap
    import datetime

    def set_file_information():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_workingdocuments()

        # Open PDF document
        document = ap.Document(data_dir + "SetFileInfo.pdf")

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
        document.save(data_dir + "SetFileInfo_out.pdf")
```

## 在 PDF 文件中设置 XMP 元数据

此代码片段演示了如何使用 Aspose.PDF for Python via .NET 以编程方式在 PDF 文档中设置或更新 XMP 元数据。通过修改诸如 xmp:CreateDate、xmp:Nickname 以及自定义字段等属性，您可以将标准化的元数据嵌入 PDF 文件中。此方法对于提升文档组织、促进可检索性以及将关键信息直接嵌入文件非常有用。

Aspose.PDF 允许您在 PDF 文件中设置元数据。设置元数据的方法如下：

1. 使用 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类打开 PDF 文件。
1. 通过为特定键分配值来修改 XMP 元数据。
1. 保存已更新的 PDF 文档。

以下代码片段展示了如何在 PDF 文件中设置元数据。

```python

    import aspose.pdf as ap
    import datetime

    def set_xmp_metadata():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf()

        # Open PDF document
        document = ap.Document(data_dir + "SetXMPMetadata.pdf")

        # Set XMP metadata properties
        document.metadata["xmp:CreateDate"] = datetime.datetime.now().isoformat()
        document.metadata["xmp:Nickname"] = "Nickname"
        document.metadata["xmp:CustomProperty"] = "Custom Value"

        # Save the updated PDF document
        document.save(data_dir + "SetXMPMetadata_out.pdf")
```

## 使用前缀插入元数据

某些开发者需要使用前缀创建新的元数据命名空间。以下代码片段展示了如何使用前缀插入元数据。

```python

    import aspose.pdf as ap
    import datetime

    def set_prefix_metadata():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf()

        # Open PDF document
        document = ap.Document(data_dir + "SetXMPMetadata.pdf")

        # Register a namespace URI for the 'xmp' prefix
        document.metadata.register_namespace_uri("xmp", "http://ns.adobe.com/xap/1.0/")

        # Set the metadata property using the registered prefix
        document.metadata["xmp:ModifyDate"] = datetime.datetime.now().isoformat()  # ISO 8601 format

        # Save the updated PDF document
        document.save(data_dir + "SetPrefixMetadata_out.pdf")
```
