---
title: PythonでPDFにウォーターマークを追加する
linktitle: ウォーターマークを追加
type: docs
weight: 30
url: /ja/python-net/add-watermarks/
description: PythonでPDFページにスタイル付きテキストウォーターマークアーティファクトを追加する。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PythonでPDFにウォーターマークを追加する
Abstract: PythonでPDFページにスタイル付きテキストウォーターマークアーティファクトを追加する。
---

使用 `WatermarkArtifact` PDFの最初のページにテキストの透かしを追加する。

## PDF にウォーターマークを追加する

テキストとスタイルを設定し、次に配置、回転、透明度を設定します。設定 `is_background` 透かしをページコンテンツの背後に配置する

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

## 関連トピック

- [透かしの詳細を抽出](/pdf/ja/python-net/extract-watermarks/)
- [透かしを削除](/pdf/ja/python-net/remove-watermarks/)
- [PythonでPDFアーティファクトを操作](/pdf/ja/python-net/artifacts/)
