---
title: 在 Python 中移除 PDF 的 Bates 编号
linktitle: 移除 Bates 编号
type: docs
weight: 100
url: /zh/python-net/remove-bates-numbering/
description: 在 Python 中从 PDF 的所有页面移除 Bates 编号。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 在 PDF 中移除 Bates 编号
Abstract: 在 Python 中从 PDF 的所有页面移除 Bates 编号。
---

在 Python 中从 PDF 的所有页面移除 Bates 编号。

## 删除 Bates 编号

将文档的页面传给 `PageCollectionExtensions.delete_bates_numbering`，然后保存 PDF。

```python
import aspose.pdf as ap

def delete_bates_numbering(infile, outfile):
    """Delete Bates numbering from a PDF document."""
    with ap.Document(infile) as document:
        ap.PageCollectionExtensions.delete_bates_numbering(document.pages)
        document.save(outfile)
```

## 相关主题

- [添加 Bates 编号](/pdf/zh/python-net/add-bates-numbering/)
- [在 Python 中处理 PDF 工件](/pdf/zh/python-net/artifacts/)
