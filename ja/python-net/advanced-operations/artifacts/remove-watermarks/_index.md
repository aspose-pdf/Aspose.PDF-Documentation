---
title: PythonでPDFの透かしを削除する
linktitle: 透かしを削除する
type: docs
weight: 90
url: /ja/python-net/remove-watermarks/
description: PythonでPDFの最初のページから透かしアーティファクトを削除します。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Pythonを使用してPDFの透かしを削除する
Abstract: PythonでPDFの最初のページから透かしアーティファクトを削除します。
---

PythonでPDFの最初のページから透かしアーティファクトを削除します。

## 透かしアーティファクトを削除する

この例では、最初のページから、タイプが `PAGINATION` でサブタイプが `WATERMARK` のアーティファクトだけを削除します。通常のページテキスト、画像、または注釈として保存されている透かしは、PDF に残ります。

```python
import aspose.pdf as ap

def delete_watermark_artifact(infile, outfile):
    with ap.Document(infile) as document:
        watermarks = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK
        ]

        for watermark in watermarks:
            document.pages[1].artifacts.delete(watermark)

        document.save(outfile)
```

## 関連トピック

- [ウォーターマークを追加](/pdf/ja/python-net/add-watermarks/)
- [ウォーターマークの詳細を抽出](/pdf/ja/python-net/extract-watermarks/)
- [Python で PDF アーティファクトを操作](/pdf/ja/python-net/artifacts/)
