---
title: 添加电影批注
type: docs
weight: 10
url: /zh/python-net/add-movie-annotation/
description: 此示例绑定一个输入 PDF，在第 1 页添加电影批注，并保存更新后的 PDF。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中使用 PdfContentEditor 向 PDF 添加电影批注
Abstract: 此示例演示如何使用 Aspose.PDF for Python via the Facades API 将电影（视频）嵌入 PDF 文档。它展示了如何添加可点击的批注，以在 PDF 中直接播放视频。
---

PDF 中的电影批注允许您将多媒体内容（例如视频）嵌入文档中。使用 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)，您可以在页面上定义一个矩形区域，以显示视频。单击后，视频可直接从 PDF 播放，使您的文档更具交互性和吸引力。

1. 创建一个 PdfContentEditor 实例。
1. 绑定输入的 PDF 文档。
1. 定义一个用于电影注释的矩形。
1. 指定要嵌入的视频文件。
1. 为注释指定页码。
1. 保存更新后的 PDF 文档。

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_movie_annotation(infile, movie_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add movie annotation to page 1
    content_editor.create_movie(apd.Rectangle(80, 500, 220, 120), movie_file, 1)
    # Save updated document
    content_editor.save(outfile)
```
