---
title: 添加声音注释
type: docs
weight: 20
url: /zh/python-net/add-sound-annotation/
description: 此示例绑定一个输入 PDF，在第 1 页添加声音注释，并保存修改后的 PDF。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 PdfContentEditor 在 Python 中向 PDF 添加声音注释
Abstract: 此示例演示如何使用 Aspose.PDF for Python via the Facades API 将音频嵌入 PDF 文档。它展示了如何添加可点击的声音注释，使其在 PDF 中直接播放音频文件。
---

PDF 中的声音注释使您能够向文档添加音频内容，例如语音备注、音乐或音效。使用 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), 您可以在页面上定义一个小的可点击矩形，激活后播放指定的音频文件。

1. 创建一个 PdfContentEditor 实例。
1. 绑定输入的 PDF 文档。
1. 为声音注释定义一个矩形。
1. 指定音频文件、注释名称、页码和采样率。
1. 保存更新后的 PDF 文档。

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_sound_annotation(infile, sound_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add sound annotation to page 1
    content_editor.create_sound(
        apd.Rectangle(80, 450, 30, 30), sound_file, "Speaker", 1, "8000"
    )
    # Save updated document
    content_editor.save(outfile)
```
