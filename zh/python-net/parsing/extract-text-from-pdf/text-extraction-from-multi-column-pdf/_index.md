---
title: 改进多列 PDF 的文本提取
linktitle: 多列 PDF 的文本提取
type: docs
weight: 30
url: /zh/python-net/text-extraction-from-multi-column-pdf/
description: 了解使用 Aspose.PDF for Python 改进多列 PDF 布局中文本提取的技术。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 手动减小字体大小后再提取

在某些多列布局中，提取前减小文本片段的字体大小可以改善阅读顺序并减少重叠问题。此技术有助于处理布局紧凑的文档，如杂志、研究论文、宣传册或包含密集文本列的报告。

1. 加载 PDF。
1. 使用 [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) 收集文本片段。
1. 将每个片段的字体大小减小，然后保存并重新打开文档。
1. 使用 [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/) 提取文本。
1. 将提取的文本写入输出文件。

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
```

## 使用比例因子提取文本

多列提取的另一种选项是配置 [TextExtractionOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textextractionoptions/) 使用比例因子。调整比例因子可以改善对紧密排列片段的解释，并有助于在密集布局、表格或基于列的文档中保持更准确的阅读顺序。

1. 加载 PDF。
1. 创建一个 [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/).
1. 配置 `TextExtractionOptions.scale_factor`.
1. 将提取选项分配给 absorber。
1. 提取页面文本并将结果写入输出文件。

```python
import aspose.pdf as ap


def extract_text_scale_factor(infile, outfile, scale_factor=0.5):
    """
    Extract text from a PDF with multi-column layout using scale factor.
    Args:
        infile (str): Input PDF path.
        outfile (str): Output text file path.
        scale_factor (float): Scale factor between 0.1 and 1.0 or 0 for auto-scaling.
    """
    doc = ap.Document(infile)
    text_absorber = ap.text.TextAbsorber()
    ext_opts = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    ext_opts.scale_factor = scale_factor
    text_absorber.extraction_options = ext_opts
    doc.pages.accept(text_absorber)
    extracted_text = text_absorber.text
    with open(outfile, "w", encoding="utf-8") as tw:
        tw.write(extracted_text)
```
