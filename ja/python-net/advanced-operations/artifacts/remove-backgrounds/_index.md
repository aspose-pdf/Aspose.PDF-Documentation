---
title: PythonでPDFの背景を削除する
linktitle: 背景を削除する
type: docs
weight: 80
url: /ja/python-net/remove-backgrounds/
description: PythonでPDFの最初のページから背景アーティファクトを削除する。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Pythonを使用してPDFの背景を削除する
Abstract: PythonでPDFの最初のページから背景アーティファクトを削除する。
---

PythonでPDFの最初のページから背景アーティファクトを削除する。

## 背景アーティファクトを削除する

削除する前に、サブタイプが `BACKGROUND` のページネーションアーティファクトを集めてください。

```python
import aspose.pdf as ap

def remove_background(infile, outfile):
    with ap.Document(infile) as document:
        backgrounds = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.BACKGROUND
        ]

        for background in backgrounds:
            document.pages[1].artifacts.delete(background)

        document.save(outfile)
```

## 関連トピック

- [背景を追加](/pdf/ja/python-net/add-backgrounds/)
- [Python で PDF アーティファクトを操作する](/pdf/ja/python-net/artifacts/)
