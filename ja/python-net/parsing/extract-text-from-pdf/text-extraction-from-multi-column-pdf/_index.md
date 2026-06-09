---
title: 複数列の PDF からのテキスト抽出の改善
linktitle: 複数列の PDF からのテキスト抽出
type: docs
weight: 30
url: /ja/python-net/text-extraction-from-multi-column-pdf/
description: Aspose.PDF for Python を使用して、複数列の PDF レイアウトからのテキスト抽出を改善する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## フォントサイズを手動で縮小してから抽出する

複数列のレイアウトでは、抽出前にテキストフラグメントのフォントサイズを小さくすると、読み上げ順序が改善され、重複の問題が軽減されます。この手法は、雑誌、研究論文、パンフレット、またはテキスト列が密集したレポートなど、フォーマットの厳しい文書に役立ちます。

1. PDF をロードします。
1. 使用 [テキストフラグメントアブソーバー](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) テキストの断片を集めるためだ
1. 各フラグメントのフォントサイズを小さくしてから、ドキュメントを保存して再度開きます。
1. 使用 [テキストアブソーバー](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/) テキストを抽出します。
1. 抽出したテキストを出力ファイルに書き込みます。

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

## スケールファクターを使用してテキストを抽出

複数列抽出のもう1つのオプションは、構成することです [テキスト抽出オプション](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textextractionoptions/) スケールファクター付き。スケールファクターを調整すると、密集したフラグメントの解釈が改善され、密集したレイアウト、表、または列ベースの文書でもより正確な読み上げ順序を維持できます。

1. PDF をロードします。
1. を作成 [テキストアブソーバー](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/).
1. 環境設定 `TextExtractionOptions.scale_factor`.
1. 抽出オプションをアブソーバーに割り当てます。
1. ページテキストを抽出し、結果を出力ファイルに書き込みます。

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
