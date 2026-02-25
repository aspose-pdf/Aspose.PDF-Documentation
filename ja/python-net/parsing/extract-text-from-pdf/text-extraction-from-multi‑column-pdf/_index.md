---
title: マルチカラムPDFからのテキスト抽出の改善
linktitle: マルチカラムPDFからのテキスト抽出
type: docs
weight: 30
url: /ja/python-net/text-extraction-from-multi‑column-pdf/
description: このセクションには、PythonでAspose.PDFを使用したテキストの書式設定とスケーリングに関する記事が含まれています。
lastmod: "2025-11-05"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
---

## 手動でフォントサイズを縮小してから抽出

マルチカラムPDFにおける抽出精度は、抽出前にすべてのテキストフラグメントのフォントサイズをまず縮小することで達成されます。このプロセスは、密に配置されたレイアウトやマルチカラムレイアウトで発生し得るテキストの重なり問題を防止します。
テキストのサイズ変更がレイアウトの明瞭さと抽出結果を向上させるため、雑誌、学術論文、パンフレットなどの複雑なレイアウトからのテキスト抽出に役立ちます。

1. PDFをロードします。
1. 既存のテキストフラグメントのフォントサイズを縮小し、保存してドキュメントを再度開きます。
1. 'TextAbsorber' を使用してページからテキストを抽出します。
1. 抽出されたテキストを書き出します。

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

## スケールファクターでテキストを抽出

文書にスケールファクターを適用して、マルチカラムレイアウトのPDFからテキストを抽出します。スケールファクターを調整することで、テキストフラグメントが正しく解釈され、抽出時の重なりや位置ずれが減少します。
列やテーブル、密なレイアウトを持つPDFに有用で、スケーリングにより抽出されたテキストの正しい読み順と構造を維持できます。

1. PDFをロードします。
1. 'TextExtractionOptions.ScaleFactor' を設定します。
1. 'TextAbsorber' を使用してページからテキストを抽出します。
1. 抽出されたテキストを書き出します。

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
