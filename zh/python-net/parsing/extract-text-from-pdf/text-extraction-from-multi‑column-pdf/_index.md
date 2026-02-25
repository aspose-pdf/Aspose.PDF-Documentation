---
title: 改进多列 PDF 的文本提取
linktitle: 多列 PDF 文本提取
type: docs
weight: 30
url: /zh/python-net/text-extraction-from-multi‑column-pdf/
description: 本节包含使用 Aspose.PDF 在 Python 中进行文本格式化和缩放的文章。
lastmod: "2025-11-05"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
---

## 手动减小字体大小然后提取

在多列 PDF 中，通过在提取前先减小所有文本片段的字体大小来实现提取精度。此过程有助于防止在紧凑排版或多列布局中出现的文本重叠问题。
这有助于从复杂布局（如杂志、学术论文或宣传册）中提取文本，缩放文字可以提升布局清晰度和提取效果。

1. 加载 PDF。
1. 减小现有文本片段的字体大小，保存并重新打开文档。
1. 使用 “TextAbsorber” 从页面提取文本。
1. 将提取的文本写出。

```python

import io
import aspose.pdf as ap

def extract_text_reduce_font(infile, outfile, reduce_ratio=0.7):
    """
    Extract text from a multi-column PDF by first reducing font size of all text fragments.
    Args:
        infile (str): Path to input PDF.
        outfile (str): Output text file.
        reduce_ratio (float): Ratio to reduce font size (e.g., 0.7 = 70%).
    """
    doc = ap.Document(infile)
    try:
        frag_absorber = ap.text.TextFragmentAbsorber()
        doc.pages.accept(frag_absorber)
        for frag in frag_absorber.text_fragments:
            frag.text_state.font_size = frag.text_state.font_size * reduce_ratio
        # Save to memory stream and reopen (to apply changes)
        ms = io.BytesIO()
        doc.save(ms)
        ms.seek(0)
        doc2 = ap.Document(ms)
        text_absorber = ap.text.TextAbsorber()
        doc2.pages.accept(text_absorber)
        extracted_text = text_absorber.text
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        doc.close()
```

## 使用比例因子提取文本

通过对文档应用比例因子，从具有多列布局的 PDF 中提取文本。调整比例因子可确保文本片段被正确解释，降低提取时的重叠或错位。
这对包含列、表格或密集布局的 PDF 很有用，缩放有助于在提取的文本中保持正确的阅读顺序和结构。

1. 加载 PDF。
1. 配置 “TextExtractionOptions.ScaleFactor”。
1. 使用 “TextAbsorber” 从页面提取文本。
1. 将提取的文本写出。

```python

import aspose.pdf as ap

def extract_text_with_scale_factor(infile, outfile, scale_factor=0.5):
    """
    Extract text from a PDF with multi-column layout using scale factor.
    Args:
        infile (str): Input PDF path.
        outfile (str): Output text file path.
        scale_factor (float): Scale factor between 0.1 and 1.0 or 0 for auto-scaling.
    """
    doc = ap.Document(infile)
    try:
        text_absorber = ap.text.TextAbsorber()
        ext_opts = ap.text.TextExtractionOptions(ap.text.TextExtractionOptions.TextFormattingMode.PURE)
        ext_opts.scale_factor = scale_factor
        text_absorber.extraction_options = ext_opts
        doc.pages.accept(text_absorber)
        extracted_text = text_absorber.text
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        doc.close()
```
