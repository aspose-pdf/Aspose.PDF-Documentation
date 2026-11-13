---
title: PythonでPDFのベーツ番号付けを削除する
linktitle: ベーツ番号付けを削除する
type: docs
weight: 100
url: /ja/python-net/remove-bates-numbering/
description: PythonでPDFのすべてのページからベーツ番号付けを削除します。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Pythonを使用してPDFのベーツ番号付けを削除する
Abstract: PythonでPDFのすべてのページからベーツ番号付けを削除します。
---

PythonでPDFのすべてのページからベーツ番号付けを削除します。

## ベーツ番号付けを削除する

ドキュメントのページを `PageCollectionExtensions.delete_bates_numbering` に渡し、PDF を保存してください。

```python
import aspose.pdf as ap

def delete_bates_numbering(infile, outfile):
    """Delete Bates numbering from a PDF document."""
    with ap.Document(infile) as document:
        ap.PageCollectionExtensions.delete_bates_numbering(document.pages)
        document.save(outfile)
```

## 関連トピック

- [ベーツ番号の追加](/pdf/ja/python-net/add-bates-numbering/)
- [Python で PDF アーティファクトを扱う](/pdf/ja/python-net/artifacts/)
