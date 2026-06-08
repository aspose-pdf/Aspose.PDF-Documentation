---
title: 在 Python 中删除 PDF 附件
linktitle: 从现有 PDF 中删除附件
type: docs
weight: 30
url: /zh/python-net/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF 可以从您的 PDF 文档中删除附件。使用 Python PDF API，通过 Aspose.PDF for Python via .NET 库来删除 PDF 文件中的附件。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 删除 PDF 附件
Abstract: 本文讨论了如何使用 Aspose.PDF for Python 删除 PDF 文件中的附件。PDF 文档中的附件存储在 `Document` 对象的 `EmbeddedFiles` 集合中。要删除 PDF 中的所有附件，您可以对 `EmbeddedFiles` 集合调用 `delete()` 方法，然后使用 `Document` 对象的 `save()` 方法保存更新后的文档。文中提供了代码片段来演示此过程，展示了打开文档、删除附件并保存修改后文件的步骤。
---

Aspose.PDF for Python 可以删除 PDF 文件中的附件。PDF 文档的附件存放在 Document 对象的 [EmbeddedFiles](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) 集合。

此工作流在您需要清理过时的嵌入文件、减小包大小或准备不附带源材料的 PDF 进行再分发时非常有用。

要删除与 PDF 文件关联的所有附件：

1. 调用 [EmbeddedFiles](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) collection 的 [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) 方法。
1. 使用以下方式保存已更新的文件 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象的 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法。

下面的代码片段展示了如何从 PDF 文档中删除附件。

```python

import aspose.pdf as ap

def remove_attachment(infile, outfile):
    # Open PDF document
    with ap.Document(infile) as document:
        document.embedded_files.delete()
        document.save(outfile)
```

## 按名称删除特定附件

如果您只需删除一个附件并保留其他附件，请使用 [delete_by_key()](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/delete_by_key/) 方法并传递附件名称。

删除特定附件：

1. 打开源 PDF 文件。
1. 调用 `document.embedded_files.delete_by_key(attachment_name)`.
1. 保存更新后的 PDF 文件。

以下代码片段通过名称删除一个附件。

```python

import aspose.pdf as ap

def remove_attachment(infile, attachment_name, outfile):
    # Open PDF document
    with ap.Document(infile) as document:
        document.embedded_files.delete_by_key(attachment_name)
        document.save(outfile)
```

## 相关附件主题

- [在 Python 中处理 PDF 附件](/pdf/zh/python-net/attachments/)
- [在 Python 中向 PDF 添加附件](/pdf/zh/python-net/add-attachment-to-pdf-document/)
- [在 Python 中创建和管理 PDF 组合文件](/pdf/zh/python-net/portfolio/)

