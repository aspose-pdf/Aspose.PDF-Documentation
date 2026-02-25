---
title: 使用 Python 删除 PDF 文件中的图像
linktitle: 删除图像
type: docs
weight: 20
url: /zh/python-net/delete-images-from-pdf-file/
description: 本节介绍如何使用 Aspose.PDF for Python via .NET 删除 PDF 文件中的图像。
lastmod: "2025-09-27"
TechArticle: true
AlternativeHeadline: 如何使用 Python 从 PDF 中删除图像
Abstract: 本文讨论了从 PDF 文件中删除图像的各种原因，例如保护隐私、防止未授权访问敏感信息、减小文件大小以便于共享和存储，以及为压缩或文本提取准备文档。它介绍了 **Aspose.PDF for Python via .NET** 作为完成此任务的工具。文章提供了逐步说明和代码片段，演示如何使用 Aspose.PDF 删除 PDF 文件中的特定图像或全部图像。该过程包括打开现有 PDF 文档、单独或批量删除图像，并保存更新后的文件。提供的 Python 代码展示了通过访问文档资源并修改所需页面来删除图像的方法。
---

删除 PDF 中全部或特定图像的原因有很多。
有时 PDF 文件可能包含需要删除的重要图像，以保护隐私或防止未授权访问特定信息。

删除不需要或冗余的图像可以帮助减小文件大小，使 PDF 更易于共享或存储。
如有必要，您可以通过删除文档中的所有图像来减少页数。
此外，从文档中删除图像有助于为 PDF 的压缩或文本信息提取做好准备。

**Aspose.PDF for Python via .NET** 将帮助您完成此任务。

## 删除 PDF 文件中的图像

要从 PDF 文件中删除图像：

1. 打开已有的 PDF 文档。
1. 删除特定图像。
1. 保存更新后的 PDF 文件。

以下代码片段展示了如何从 PDF 文件中删除图像。

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    document = ap.Document(path_infile)
    document.pages[1].resources.images.delete(1)
    document.save(path_outfile)
```
