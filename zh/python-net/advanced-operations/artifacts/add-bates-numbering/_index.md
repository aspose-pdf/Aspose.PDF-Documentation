---
title: 在 Python 中为 PDF 添加 Bates 编号
linktitle: 添加 Bates 编号
type: docs
weight: 10
url: /zh/python-net/add-bates-numbering/
description: 在 Python 中为 PDF 页面添加顺序的 Bates 标识符。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 为 PDF 添加 Bates 编号
Abstract: 在 Python 中为 PDF 页面添加顺序的 Bates 标识符。
---

Bates编号为文档集合中的页面分配顺序标识符。配置一个 `BatesNArtifact` 用于控制页码范围、起始号码、数字位数、前缀、后缀以及放置位置。

## 添加 Bates 编号工件

将配置好的工件和文档页面传给 `PageCollectionExtensions.add_bates_numbering`。此示例为现有页面分配从 `000001` 开始的六位标识符。

```python
import aspose.pdf as ap

def _create_bates_artifact():
    """Create a Bates numbering artifact with default settings."""
    artifact = ap.BatesNArtifact()
    artifact.start_page = 1
    artifact.end_page = 0
    artifact.subset = ap.Subset.ALL
    artifact.number_of_digits = 6
    artifact.start_number = 1
    artifact.prefix = ""
    artifact.suffix = ""
    artifact.artifact_vertical_alignment = ap.VerticalAlignment.BOTTOM
    artifact.artifact_horizontal_alignment = ap.HorizontalAlignment.RIGHT
    artifact.right_margin = 72
    artifact.left_margin = 72
    artifact.top_margin = 36
    artifact.bottom_margin = 36
    return artifact


def add_bates_n_artifact(infile, outfile):
    """Add Bates numbering artifact to a PDF document."""
    with ap.Document(infile) as document:
        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_bates_numbering(document.pages, bates_artifact)
        document.save(outfile)
```

## 使用分页工件添加贝茨编号

如需通过分页 API 添加 Bates 编号，请复用上一个示例中的 `_create_bates_artifact`，并将包含该工件的列表传给 `PageCollectionExtensions.add_pagination`。

```python
import aspose.pdf as ap

def add_bates_n_artifact_pagination(infile, outfile):
    """Add Bates numbering using pagination artifacts collection."""
    with ap.Document(infile) as document:
        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_pagination(document.pages, [bates_artifact])
        document.save(outfile)
```

## 相关主题

- [删除贝茨编号](/pdf/zh/python-net/remove-bates-numbering/)
- [在 Python 中处理 PDF 工件](/pdf/zh/python-net/artifacts/)
