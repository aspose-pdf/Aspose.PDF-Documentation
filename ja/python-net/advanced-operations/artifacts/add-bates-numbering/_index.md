---
title: PythonでPDFにBates Numberingを追加
linktitle: Bates Numberingを追加
type: docs
weight: 10
url: /ja/python-net/add-bates-numbering/
description: PythonでPDFページに順次的なBates識別子を追加します。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PythonでPDFにBates Numberingを追加
Abstract: PythonでPDFページに順次的なBates識別子を追加します。
---

ベーツ番号付けは、ドキュメントセット内のページに連続した識別子を割り当てます。設定する `BatesNArtifact` ページ範囲、開始番号、桁数、接頭辞、接尾辞、配置を制御するために。

## Bates 番号付けアーティファクトを追加する

設定済みのアーティファクトとドキュメントのページを `PageCollectionExtensions.add_bates_numbering` に渡してください。この例では、既存のページに `000001` から始まる 6 桁の識別子を割り当てます。

```python
import aspose.pdf as ap

def _create_bates_artifact():
    """Create a Bates numbering artifact with default settings."""
    artifact = ap.BatesNArtifact()
    artifact.start_page = 1
    artifact.end_page = 0
    artifact.subset = ap.Subset.ALL
    artifact.number_of_digits = 6
    artifact.start_number = 1
    artifact.prefix = ""
    artifact.suffix = ""
    artifact.artifact_vertical_alignment = ap.VerticalAlignment.BOTTOM
    artifact.artifact_horizontal_alignment = ap.HorizontalAlignment.RIGHT
    artifact.right_margin = 72
    artifact.left_margin = 72
    artifact.top_margin = 36
    artifact.bottom_margin = 36
    return artifact


def add_bates_n_artifact(infile, outfile):
    """Add Bates numbering artifact to a PDF document."""
    with ap.Document(infile) as document:
        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_bates_numbering(document.pages, bates_artifact)
        document.save(outfile)
```

## ページネーションアーティファクトで Bates 番号を付ける

ページネーション API で Bates 番号を付けるには、前の例の `_create_bates_artifact` を再利用し、アーティファクトを含むリストを `PageCollectionExtensions.add_pagination` に渡してください。

```python
import aspose.pdf as ap

def add_bates_n_artifact_pagination(infile, outfile):
    """Add Bates numbering using pagination artifacts collection."""
    with ap.Document(infile) as document:
        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_pagination(document.pages, [bates_artifact])
        document.save(outfile)
```

## 関連トピック

- [ベーツ番号の削除](/pdf/ja/python-net/remove-bates-numbering/)
- [PythonでPDFアーティファクトを操作する](/pdf/ja/python-net/artifacts/)
