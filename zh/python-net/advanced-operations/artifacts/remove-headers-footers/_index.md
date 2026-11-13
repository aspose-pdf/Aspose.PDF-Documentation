---
title: 在 Python 中删除 PDF 页眉和页脚
linktitle: 删除页眉和页脚
type: docs
weight: 110
url: /zh/python-net/remove-headers-footers/
description: 在 Python 中删除 PDF 第一页的页眉和页脚伪影。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 删除 PDF 的页眉和页脚
Abstract: 在 Python 中删除 PDF 第一页的页眉和页脚伪影。
---

在 Python 中删除 PDF 第一页的页眉和页脚伪影。

## 删除页眉和页脚工件

删除前，先收集子类型为 `HEADER` 或 `FOOTER` 的分页工件。

```python
import aspose.pdf as ap

def delete_header_footer_artifact(infile, outfile):
    with ap.Document(infile) as document:
        header_footers = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and (
                artifact.subtype == ap.Artifact.ArtifactSubtype.HEADER
                or artifact.subtype == ap.Artifact.ArtifactSubtype.FOOTER
            )
        ]

        for art in header_footers:
            document.pages[1].artifacts.delete(art)

        document.save(outfile)
```

## 相关主题

- [添加页眉和页脚](/pdf/zh/python-net/artifacts-header-footer/)
- [在 Python 中处理 PDF 构件](/pdf/zh/python-net/artifacts/)
