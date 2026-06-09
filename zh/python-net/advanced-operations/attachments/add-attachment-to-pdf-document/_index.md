---
title: 在 Python 中向 PDF 添加附件
linktitle: 向 PDF 文档添加附件
type: docs
weight: 10
url: /zh/python-net/add-attachment-to-pdf-document/
description: 了解如何在 Python 中使用 Aspose.PDF for Python via .NET 向 PDF 文档添加文件附件。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 向 PDF 添加附件的方法
Abstract: 本文提供了使用 Python 和 Aspose.PDF 库向 PDF 文件添加附件的分步指南。它详细说明了建立新 Python 项目、导入必要的 Aspose.PDF 包以及创建 `Document` 对象的过程。文章解释了如何使用所需的文件和描述创建 `FileSpecification` 对象，以及如何使用 `add` 方法将该对象添加到 PDF 文档的 `EmbeddedFileCollection` 中。`EmbeddedFileCollection` 保存了 PDF 中的所有附件。文中还包含了一段代码示例，演示了打开文档、设置附件文件、将其追加到文档的附件集合以及保存更新后的 PDF 的过程。
---

附件可以包含各种信息，且可以是多种文件类型。本文解释了如何向 PDF 文件添加附件。

当需要将支持的源文件、电子表格、图像或相关文档与主 PDF 一起打包时，使用嵌入式 PDF 附件。

1. 创建一个新的 Python 项目。
1. 导入 Aspose.PDF 包
1. 创建一个 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象。
1. 创建一个 [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) 包含您正在添加的文件及文件描述的对象。
1. 添加 [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) 对象到 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象的 [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) 集合，带有集合的 [添加](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) 方法。

这 [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) 集合包含 PDF 文件中的所有附件。以下代码片段向您展示如何在 PDF 文档中添加附件。

```python
from os import path
import aspose.pdf as ap

def add_attachments(infile, attachment_path, outfile):
    with ap.Document(infile) as document:
        file_spec = ap.FileSpecification(attachment_path, "Sample text file")
        document.embedded_files.add(path.basename(attachment_path), file_spec)
        document.save(outfile)
```

## 相关附件主题

- [在 Python 中处理 PDF 附件](/pdf/zh/python-net/attachments/)
- [在 Python 中删除 PDF 附件](/pdf/zh/python-net/removing-attachment-from-an-existing-pdf/)
- [在 Python 中创建和管理 PDF 组合文件](/pdf/zh/python-net/portfolio/)

