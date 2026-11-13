---
title: 在 Python 中删除 PDF 背景
linktitle: 删除背景
type: docs
weight: 80
url: /zh/python-net/remove-backgrounds/
description: 在 Python 中删除 PDF 第一页的背景伪影。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 删除 PDF 中的背景
Abstract: 在 Python 中删除 PDF 第一页的背景伪影。
---

在 Python 中删除 PDF 第一页的背景工件。

## 删除背景工件

删除前，先收集子类型为 `BACKGROUND` 的分页工件。

```python
import aspose.pdf as ap

def remove_background(infile, outfile):
    with ap.Document(infile) as document:
        backgrounds = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.BACKGROUND
        ]

        for background in backgrounds:
            document.pages[1].artifacts.delete(background)

        document.save(outfile)
```

## 相关主题

- [添加背景](/pdf/zh/python-net/add-backgrounds/)
- [在 Python 中使用 PDF 工件](/pdf/zh/python-net/artifacts/)
