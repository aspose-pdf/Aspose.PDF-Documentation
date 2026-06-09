---
title: 使用 Python 提取 PDF 中的图像
linktitle: 从 PDF 中提取图像
type: docs
weight: 20
url: /zh/python-net/extract-images-from-the-pdf-file/
description: 了解如何使用 Aspose.PDF for Python 提取 PDF 文件中嵌入的图像。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何通过 Python 提取 PDF 中的图像
Abstract: 本文阐述了如何使用 Aspose.PDF for Python 从 PDF 文档中提取嵌入的图像。内容包括使用 Document 类打开源 PDF、从页面资源集合中访问图像，以及将提取的 XImage 保存到外部文件，以便重新使用、检查或后续处理。
---

使用 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 打开 PDF，然后访问页面资源以检索一个 [XImage](https://reference.aspose.com/pdf/python-net/aspose.pdf/ximage/) 对象并将其另存为单独的文件。此方法在需要重复使用图像、检查提取的资源或从 PDF 内容构建图像处理工作流时非常有用。

1. 将 PDF 打开为 `Document`.
1. 从目标页面访问图像资源。
1. 检索所需的 `XImage` 来自页面图像集合。
1. 将提取的图像保存到输出文件。

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    xImage = document.pages[1].resources.images[1]
    with FileIO(path_outfile, "w") as output_image:
        xImage.save(output_image)
```
