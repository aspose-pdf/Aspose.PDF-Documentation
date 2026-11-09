---
title: 在 Python 中统计 PDF 工件
linktitle: 统计工件
type: docs
weight: 40
url: /zh/python-net/counting-artifacts/
description: 在 Python 中按分页工件子类型统计 PDF 页面上的水印、背景、页眉和页脚。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 在 PDF 中统计工件
Abstract: 统计 PDF 页面上的分页工件，以检查水印、背景、页眉和页脚。
---

统计 PDF 页面上的分页工件，以检查水印、背景、页眉和页脚。

## 按子类型统计分页工件

按 `PAGINATION` 类型筛选第一页的 `artifacts` 集合，然后按子类型统计工件数量。没有相应子类型的工件时，示例输出 0。

```python
from collections import Counter
import aspose.pdf as ap

def count_pdf_artifacts(infile):
    """Count and display artifacts of different types on the first page."""
    with ap.Document(infile) as document:
        pagination_artifacts = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
        ]

        subtypes = [artifact.subtype for artifact in pagination_artifacts]
        counts = Counter(subtypes)

        print(f"Watermarks: {counts.get(ap.Artifact.ArtifactSubtype.WATERMARK, 0)}")
        print(f"Backgrounds: {counts.get(ap.Artifact.ArtifactSubtype.BACKGROUND, 0)}")
        print(f"Headers: {counts.get(ap.Artifact.ArtifactSubtype.HEADER, 0)}")
        print(f"Footers: {counts.get(ap.Artifact.ArtifactSubtype.FOOTER, 0)}")
```

## 相关主题

- [在 Python 中处理 PDF 工件](/pdf/zh/python-net/artifacts/)
- [提取水印详细信息](/pdf/zh/python-net/extract-watermarks/)
- [删除水印](/pdf/zh/python-net/remove-watermarks/)
- [删除背景](/pdf/zh/python-net/remove-backgrounds/)
- [删除页眉和页脚](/pdf/zh/python-net/remove-headers-footers/)
