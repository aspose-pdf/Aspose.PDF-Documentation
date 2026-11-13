---
title: PythonでPDFアーティファクトをカウントする
linktitle: アーティファクトのカウント
type: docs
weight: 40
url: /ja/python-net/counting-artifacts/
description: PythonでPDFページ上のページネーションアーティファクトサブタイプ別に透かし、背景、ヘッダー、フッターをカウントする。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Pythonを使用したPDFでのアーティファクトのカウント
Abstract: PDFページ上のページネーションアーティファクトをカウントして、透かし、背景、ヘッダー、フッターを確認する。
---

PDFページ上のページネーションアーティファクトをカウントして、透かし、背景、ヘッダー、フッターを確認する。

## サブタイプ別にアーティファクトを数える

最初のページの `artifacts` コレクションを `PAGINATION` タイプで絞り込み、サブタイプごとに集計してください。該当するアーティファクトがなければ、例では 0 を出力します。

```python
from collections import Counter
import aspose.pdf as ap

def count_pdf_artifacts(infile):
    """Count and display artifacts of different types on the first page."""
    with ap.Document(infile) as document:
        pagination_artifacts = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
        ]

        subtypes = [artifact.subtype for artifact in pagination_artifacts]
        counts = Counter(subtypes)

        print(f"Watermarks: {counts.get(ap.Artifact.ArtifactSubtype.WATERMARK, 0)}")
        print(f"Backgrounds: {counts.get(ap.Artifact.ArtifactSubtype.BACKGROUND, 0)}")
        print(f"Headers: {counts.get(ap.Artifact.ArtifactSubtype.HEADER, 0)}")
        print(f"Footers: {counts.get(ap.Artifact.ArtifactSubtype.FOOTER, 0)}")
```

## 関連トピック

- [Python で PDF アーティファクトを操作する](/pdf/ja/python-net/artifacts/)
- [Watermark の詳細を抽出する](/pdf/ja/python-net/extract-watermarks/)
- [Watermark を削除する](/pdf/ja/python-net/remove-watermarks/)
- [背景を削除する](/pdf/ja/python-net/remove-backgrounds/)
- [ヘッダーとフッターを削除する](/pdf/ja/python-net/remove-headers-footers/)
