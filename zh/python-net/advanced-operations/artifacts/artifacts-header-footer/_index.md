---
title: 使用 Python 管理 PDF 页眉和页脚
linktitle: 管理 PDF 页眉和页脚
type: docs
weight: 70
url: /zh/python-net/artifacts-header-footer/
description: 了解如何使用 Python 和 Aspose.PDF 管理 PDF 文档中的页眉和页脚。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 添加、定制和删除 PDF 页眉和页脚
Abstract: 在业务、出版和自动化工作流中处理 PDF 文档时，管理页眉和页脚是一项常见需求。本文演示如何使用 Aspose.PDF for Python 添加专业外观的页眉和页脚，并可自定义字体、大小、颜色和对齐方式等样式。它还展示了如何检测并删除 PDF 页面上已有的分页痕迹，如页眉和页脚。通过可复用的函数和清晰的示例，开发者可以快速将这些功能集成到文档处理系统中，用于品牌化、报告或文件清理。
---

## 创建样式化文本痕迹

此实用函数说明了如何使用 Aspose.PDF for Python 为 PDF 页面创建可重用的文本工件。它旨在生成具有一致格式的样式化页眉或页脚，包括字体设置、颜色、大小和对齐方式。该函数对工件的创建进行抽象，以便在不同的页面级文本装饰中重复使用。

1. 实例化工件对象。
1. 设置工件文本内容。
1. 应用文本样式。
1. 设置对齐。
1. 返回已配置的工件。

```python
from os import path
import aspose.pdf as ap
import sys

def _create_text_artifact(artifact_class, text):
    """Create a text artifact (header/footer) with common styling."""
    artifact = artifact_class()
    artifact.text = text
    artifact.text_state.font_size = 14
    artifact.text_state.font = ap.text.FontRepository.find_font("Arial")
    artifact.text_state.foreground_color = ap.Color.navy
    artifact.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
    return artifact

```

## 向 PDF 添加页眉

1. 打开输入的 PDF。
1. 创建一个 HeaderArtifact，文本为 "Sample Header"。
1. 将其追加到第一页。
1. 保存更新后的 PDF。

```python
from os import path
import aspose.pdf as ap
import sys

def add_header_artifact(infile, outfile):
    """Add a header artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        header = _create_text_artifact(ap.HeaderArtifact, "Sample Header")
        document.pages[1].artifacts.append(header)
        document.save(outfile)
```

## 向 PDF 添加页脚

1. 打开输入的 PDF。
1. 创建一个 FooterArtifact，文本为 "Sample Footer"。
1. 将其追加到第一页。
1. 保存输出文件。

```python
from os import path
import aspose.pdf as ap
import sys

def add_footer_artifact(infile, outfile):
    """Add a footer artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        footer = _create_text_artifact(ap.FooterArtifact, "Sample Footer")
        document.pages[1].artifacts.append(footer)
        document.save(outfile)
```

## 删除页眉或页脚工件

1. 打开 PDF。
1. 查找标记为分页页眉或页脚的伪件。
1. 将它们从首页中移除。
1. 保存已清理的文档。

```python
from os import path
import aspose.pdf as ap
import sys

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

## 相关工件主题

- [在 Python 中使用 PDF 工件](/pdf/zh/python-net/artifacts/)
- [在 Python 中添加 PDF 背景](/pdf/zh/python-net/add-backgrounds/)
- [在 Python 中为 PDF 添加 Bates 编号](/pdf/zh/python-net/add-bates-numbering/)
- [统计 PDF 文件中的工件类型](/pdf/zh/python-net/counting-artifacts/)