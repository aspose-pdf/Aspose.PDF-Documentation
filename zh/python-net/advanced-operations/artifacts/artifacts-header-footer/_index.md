---
title: 在 Python 中添加 PDF 页眉和页脚
linktitle: 添加页眉和页脚
type: docs
weight: 70
url: /zh/python-net/artifacts-header-footer/
description: 在 Python 中向 PDF 页面添加带样式的页眉和页脚元素。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 在 PDF 中添加页眉和页脚
Abstract: 在 Python 中向 PDF 页面添加带样式的页眉和页脚元素。
---

使用 `HeaderArtifact` 和 `FooterArtifact` 向 PDF 页面添加滚动文字。这些示例在第一页添加了伪影。

## 创建样式化文本工件

运行任一添加示例前，请先定义此辅助函数。该函数为页眉和页脚使用相同的字体、大小、颜色和对齐方式。

```python
import aspose.pdf as ap

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

将 `HeaderArtifact` 传给辅助函数，然后将返回的工件添加到页面。

```python
import aspose.pdf as ap

def add_header_artifact(infile, outfile):
    """Add a header artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        header = _create_text_artifact(ap.HeaderArtifact, "Sample Header")
        document.pages[1].artifacts.append(header)
        document.save(outfile)
```

## 在 PDF 中添加页脚

将 `FooterArtifact` 传给辅助函数，然后将返回的工件添加到页面。

```python
import aspose.pdf as ap

def add_footer_artifact(infile, outfile):
    """Add a footer artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        footer = _create_text_artifact(ap.FooterArtifact, "Sample Footer")
        document.pages[1].artifacts.append(footer)
        document.save(outfile)
```

## 相关主题

- [删除页眉和页脚](/pdf/zh/python-net/remove-headers-footers/)
- [在 Python 中使用 PDF 工件](/pdf/zh/python-net/artifacts/)
