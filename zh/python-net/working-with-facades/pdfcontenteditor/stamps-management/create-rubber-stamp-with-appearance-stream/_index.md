---
title: 使用外观流创建橡皮图章
type: docs
weight: 30
url: /zh/python-net/create-rubber-stamp-with-appearance-stream/
description: 此示例加载 PDF，在第 1 页使用图像文件作为外观创建橡皮图章，并保存修改后的文档。 ✨
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 PdfContentEditor 在 Python 中创建自定义图像外观的橡皮图章
Abstract: 此示例展示了如何使用 Aspose.PDF for Python 通过 Facades API 在 PDF 中创建带自定义图像外观的橡皮图章注释。此方法允许您应用品牌化或视觉丰富的图章，如徽标、印章或签名。
---

可以使用外部图像文件自定义橡皮图章注释。与仅依赖基于文本的图章不同，您可以定义视觉外观（例如公司徽标或批准徽章），并将其放置在页面上。

1. 创建一个 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 实例。
1. 绑定输入的 PDF 文档。
1. 为图章位置定义一个矩形。
1. 使用图像文件作为印章外观。
1. 应用文本和颜色设置。
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
