---
title: 使用 Python 从 PDF 中移除附件
linktitle: 从现有 PDF 中移除附件
type: docs
weight: 30
url: /zh/python-net/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF 可以从您的 PDF 文档中移除附件。使用 Python PDF API，通过 .NET 库的 Aspose.PDF for Python 来移除 PDF 文件中的附件。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 删除 PDF 附件
Abstract: 本文讨论如何使用 Aspose.PDF for Python 移除 PDF 文件中的附件。PDF 文档中的附件存储在 `Document` 对象的 `EmbeddedFiles` 集合中。要删除 PDF 中的所有附件，您可以对 `EmbeddedFiles` 集合调用 `delete()` 方法，然后使用 `Document` 对象的 `save()` 方法保存更新后的文档。本文提供了代码片段来演示此过程，展示打开文档、删除附件并保存修改后文件的步骤。
---

Aspose.PDF for Python 可以从 PDF 文件中移除附件。PDF 文档的附件存放在 Document 对象的 [EmbeddedFiles](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) 集合中。

要删除与 PDF 文件关联的所有附件：

1. 调用 [EmbeddedFiles](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) 集合的 [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) 方法。
1. 使用 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象的 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法保存更新后的文件。

以下代码片段展示了如何从 PDF 文档中移除附件。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Delete all attachments
    document.embedded_files.delete()

    # Save updated file
    document.save(output_pdf)
```


