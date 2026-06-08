---
title: 使用外观文件创建橡皮图章
type: docs
weight: 20
url: /zh/python-net/create-rubber-stamp-with-appearance-file/
description: 此示例绑定输入 PDF，在第 1 页使用图像文件作为图章外观创建橡皮图章，并保存更新后的 PDF。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 PdfContentEditor 在 PDF 中创建具有自定义外观的橡皮图章
Abstract: 此示例演示如何使用 Aspose.PDF for Python via the Facades API 将具有自定义外观（图像）的橡皮图章注释添加到 PDF 文档中。自定义图章允许您将徽标、签名或品牌视觉元素作为图章的一部分。
---

橡皮图章注释不仅可以使用文本进行自定义，还可以通过使用图像文件作为其外观进行定制。这种方法对于在 PDF 页面上添加公司徽标、签名图章或任何视觉指示器非常有用。

1. 创建一个 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 实例。
1. 绑定输入的 PDF 文档。
1. 为图章定义一个矩形。
1. 使用自定义图像文件来定义橡皮图章的外观。
1. 设置图章的文本和颜色。
1. 保存更新后的 PDF 文档。

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_rubber_stamp_with_appearance_file(infile, image_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Create rubber stamp using appearance_file overload (image path)
    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(100, 400, 200, 60),
        "Stamp with custom appearance",
        apd.Color.dark_green,
        image_file,
    )
    # Save updated document
    content_editor.save(outfile)
```
