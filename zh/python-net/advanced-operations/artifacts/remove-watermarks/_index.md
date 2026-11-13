---
title: 在 Python 中移除 PDF 水印
linktitle: 移除水印
type: docs
weight: 90
url: /zh/python-net/remove-watermarks/
description: 在 Python 中移除 PDF 第一页的水印伪影。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 移除 PDF 中的水印
Abstract: 在 Python 中移除 PDF 第一页的水印伪影。
---

在 Python 中移除 PDF 第一页的水印工件。

## 移除水印工件

此示例仅删除第一页中类型为 `PAGINATION`、子类型为 `WATERMARK` 的工件。以普通页面文本、图像或注释形式保存的可见水印仍保留在 PDF 中。

```python
import aspose.pdf as ap

def delete_watermark_artifact(infile, outfile):
    with ap.Document(infile) as document:
        watermarks = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK
        ]

        for watermark in watermarks:
            document.pages[1].artifacts.delete(watermark)

        document.save(outfile)
```

## 相关主题

- [添加水印](/pdf/zh/python-net/add-watermarks/)
- [提取水印详细信息](/pdf/zh/python-net/extract-watermarks/)
- [在 Python 中处理 PDF 工件](/pdf/zh/python-net/artifacts/)
