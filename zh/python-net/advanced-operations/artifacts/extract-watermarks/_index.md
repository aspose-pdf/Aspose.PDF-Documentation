---
title: 在 Python 中提取 PDF 水印详细信息
linktitle: 提取水印详细信息
type: docs
weight: 50
url: /zh/python-net/extract-watermarks/
description: 在 Python 中读取 PDF 首页水印工件的文本和边界矩形。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 在 PDF 中提取水印详细信息
Abstract: 在 Python 中读取 PDF 首页水印工件的文本和边界矩形。
---

在 Python 中读取 PDF 首页水印工件的文本和边界矩形。

## 读取水印文本和边界矩形

输出子类型为 `WATERMARK` 的每个分页工件的文本和边界矩形。

```python
import aspose.pdf as ap

def extract_watermark_from_pdf(infile):
    with ap.Document(infile) as document:
        watermarks = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK
        ]

        for watermark in watermarks:
            print(f"{watermark.text} {watermark.rectangle}")
```

## 相关主题

- [添加水印](/pdf/zh/python-net/add-watermarks/)
- [删除水印](/pdf/zh/python-net/remove-watermarks/)
- [在 Python 中处理 PDF 工件](/pdf/zh/python-net/artifacts/)
