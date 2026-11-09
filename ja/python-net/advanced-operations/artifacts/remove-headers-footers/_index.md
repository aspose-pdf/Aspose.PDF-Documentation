---
title: PythonでPDFのヘッダーとフッターを削除する
linktitle: ヘッダーとフッターを削除する
type: docs
weight: 110
url: /ja/python-net/remove-headers-footers/
description: PythonでPDFの最初のページからヘッダーとフッターのアーティファクトを削除する。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PythonでPDFのヘッダーとフッターを削除する
Abstract: PythonでPDFの最初のページからヘッダーとフッターのアーティファクトを削除する。
---

PythonでPDFの最初のページからヘッダーとフッターのアーティファクトを削除する。

## ヘッダーとフッターのアーティファクトを削除する

削除する前に、サブタイプが `HEADER` または `FOOTER` のページネーションアーティファクトを集めてください。

```python
import aspose.pdf as ap

def delete_header_footer_artifact(infile, outfile):
    with ap.Document(infile) as document:
        header_footers = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and (
                artifact.subtype == ap.Artifact.ArtifactSubtype.HEADER
                or artifact.subtype == ap.Artifact.ArtifactSubtype.FOOTER
            )
        ]

        for art in header_footers:
            document.pages[1].artifacts.delete(art)

        document.save(outfile)
```

## 関連トピック

- [ヘッダーとフッターを追加する](/pdf/ja/python-net/artifacts-header-footer/)
- [PythonでPDFアーティファクトを操作する](/pdf/ja/python-net/artifacts/)
