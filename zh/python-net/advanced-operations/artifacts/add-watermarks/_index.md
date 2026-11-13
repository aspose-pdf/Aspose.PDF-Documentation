---
title: 在 Python 中向 PDF 添加水印
linktitle: 添加水印
type: docs
weight: 30
url: /zh/python-net/add-watermarks/
description: 在 Python 中向 PDF 页面添加样式化文本水印工件。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 在 PDF 中添加水印
Abstract: 在 Python 中向 PDF 页面添加样式化文本水印工件。
---

使用 `WatermarkArtifact` 在 PDF 的第一页添加文字水印。

## 向 PDF 添加水印

设置文本和样式，然后配置对齐、旋转和不透明度。设置 `is_background` 将水印放置在页面内容后面。

```python
import aspose.pdf as ap

def add_watermark_artifact(infile, outfile):
    with ap.Document(infile) as document:
        text_state = ap.text.TextState()
        text_state.font_size = 72
        text_state.foreground_color = ap.Color.blue_violet
        text_state.font_style = ap.text.FontStyles.BOLD
        text_state.font = ap.text.FontRepository.find_font("Arial")

        watermark = ap.WatermarkArtifact()
        watermark.set_text_and_state("WATERMARK", text_state)
        watermark.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
        watermark.artifact_vertical_alignment = ap.VerticalAlignment.CENTER
        watermark.rotation = 60
        watermark.opacity = 0.2
        watermark.is_background = True

        document.pages[1].artifacts.append(watermark)
        document.save(outfile)
```

## 相关主题

- [提取水印详细信息](/pdf/zh/python-net/extract-watermarks/)
- [移除水印](/pdf/zh/python-net/remove-watermarks/)
- [在 Python 中处理 PDF 工件](/pdf/zh/python-net/artifacts/)
