---
title: 使用 Python 向 PDF 文档添加附件
linktitle: 向 PDF 文档添加附件
type: docs
weight: 10
url: /zh/python-net/add-attachment-to-pdf-document/
description: 本页描述了如何使用 Aspose.PDF for Python via .NET 库向 PDF 文件添加附件。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 向 PDF 添加附件
Abstract: 本文提供了使用 Python 和 Aspose.PDF 库向 PDF 文件添加附件的逐步指南。它详细说明了建立新 Python 项目、导入必要的 Aspose.PDF 包以及创建 `Document` 对象的过程。文章解释了如何使用所需的文件和描述创建 `FileSpecification` 对象，以及如何使用 `add` 方法将此对象添加到 PDF 文档的 `EmbeddedFileCollection` 中。`EmbeddedFileCollection` 保存了 PDF 中的所有附件。文中还包含代码片段，演示了打开文档、准备要附加的文件、将其添加到文档的附件集合以及保存更新后的 PDF 的过程。
---

附件可以包含各种信息，并且可以是多种文件类型。本文说明了如何向 PDF 文件添加附件。

1. 创建一个新的 Python 项目。
1. 导入 Aspose.PDF 包
1. 创建一个 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象。
1. 创建一个带有要添加的文件及文件描述的 [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) 对象。
1. 使用集合的 [add](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) 方法，将 [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) 对象添加到 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象的 [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) 集合中。

 [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) 集合包含 PDF 文件中的所有附件。下面的代码片段展示了如何在 PDF 文档中添加附件。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Setup new file to be added as attachment
    fileSpecification = ap.FileSpecification(attachment_file, "Sample text file")

    # Add attachment to document's attachment collection
    document.embedded_files.append(fileSpecification)

    # Save new output
    document.save(output_pdf)
```


