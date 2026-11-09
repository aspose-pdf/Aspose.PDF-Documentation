---
title: PythonでPDFの透かし詳細を抽出する
linktitle: 透かし詳細を抽出する
type: docs
weight: 50
url: /ja/python-net/extract-watermarks/
description: PythonでPDFの最初のページにある透かしアーティファクトのテキストと境界矩形を読み取ります。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Pythonを使用してPDFの透かし詳細を抽出する
Abstract: PythonでPDFの最初のページにある透かしアーティファクトのテキストと境界矩形を読み取ります。
---

PythonでPDFの最初のページにある透かしアーティファクトのテキストと境界矩形を読み取ります。

## 透かしテキストと境界を読み取る

サブタイプが `WATERMARK` のページネーションアーティファクトごとに、テキストと境界矩形を出力してください。

```python
import aspose.pdf as ap

def extract_watermark_from_pdf(infile):
    with ap.Document(infile) as document:
        watermarks = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK
        ]

        for watermark in watermarks:
            print(f"{watermark.text} {watermark.rectangle}")
```

## 関連トピック

- [透かしを追加](/pdf/ja/python-net/add-watermarks/)
- [透かしを削除](/pdf/ja/python-net/remove-watermarks/)
- [PythonでPDFアーティファクトを操作](/pdf/ja/python-net/artifacts/)
