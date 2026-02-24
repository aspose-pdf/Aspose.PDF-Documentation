---
title: 使用 Python 从 PDF 中提取图像
linktitle: 提取 PDF 中的图像
type: docs
weight: 20
url: /zh/python-net/extract-images-from-the-pdf-file/
description: 如何使用 Aspose.PDF for Python 从 PDF 中提取图像的一部分
lastmod: "2023-03-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何通过 Python 提取 PDF 中的图像
Abstract: 本文提供了一个关于使用 Python 从 PDF 文档中提取嵌入图像的简明指南。该过程包括三个主要步骤——加载 PDF 文档、访问图像资源以及将图像保存到文件。代码片段使用 Aspose.PDF 库来实现这些操作。首先，从指定路径加载 PDF 文档，并从首页的资源中访问所需图像。最后，使用文件 I/O 操作将图像保存到指定的输出文件，以便进行进一步的分析、编辑或在其他文档中复用。
---

此代码片段从 PDF 文档中提取嵌入图像，以便进行单独的分析、编辑或在其他文档中复用：

1. 加载 PDF 文档
1. 访问图像资源
1. 将图像保存到文件

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    xImage = document.pages[1].resources.images[1]
    with FileIO(path_outfile, "w") as output_image:
        xImage.save(output_image)
```

