---
title: 按索引删除印章
type: docs
weight: 50
url: /zh/python-net/delete-stamp-by-index/
description: 此示例在第2页创建两个橡皮图章。之后，可通过指定其索引来删除印章。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 中的 PdfContentEditor 按索引删除 PDF 中的橡皮图章
Abstract: 此示例演示如何使用 Aspose.PDF for Python via the Facades API，通过索引删除 PDF 中的橡皮图章注释。它展示了如何添加多个印章，然后根据它们在页面上的顺序删除其中一个。
---

当页面上存在多个橡皮图章时，您可以使用其索引删除特定的图章。delete_stamp() 方法允许按照顺序删除注释，这在您不跟踪印章 ID 但知道其顺序时非常有用。

1. 创建一个 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 实例。
1. 绑定输入的 PDF 文档。
1. 使用 bind_pdf(infile) 将输入 PDF 文件绑定到 PdfContentEditor 实例。
1. 调用 'delete_stamp(1, [2, 3])' 来删除索引为 1 的印章，在第 2 页和第 3 页。
1. 使用 save(outfile) 将修改后的 PDF 文档保存到输出文件。

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_stamp_by_index(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    content_editor.delete_stamp(1, [2, 3])
    # Save updated document
    content_editor.save(outfile)
```
