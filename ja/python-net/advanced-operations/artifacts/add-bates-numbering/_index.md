---
title: Python で PDF にベイツナンバリングを追加する方法
linktitle: ベイツ番号の追加
type: docs
weight: 10
url: /ja/python-net/add-bates-numbering/
description: Python を使用して PDF ドキュメントにベイツ番号を追加および削除する方法と、.NET 経由の Aspose.PDF for Python を使用する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python によるベイツナンバリングの追加
Abstract: ベイツ番号付けは、法律、医療、およびビジネス文書のワークフローにおける重要な機能です。これにより、セット内の各ページに一意の連続した識別子が確実に付けられ、確実に参照できるようになります。この記事では、.NET 経由の Aspose.PDF が、その柔軟な API によって Bates 番号付けの自動化をいかに簡単に行えるかを説明します。BatesAntifact クラスを使用すると、開発者は桁数、プレフィックス、サフィックス、配置、マージンなどの番号付け動作を設定し、それをプログラム的に文書全体に適用できます。アーティファクトの直接適用からデリゲートベースの構成まで、静的制御と動的制御の両方を実現する複数のアプローチが提示されています。さらに、この API では 1 回のメソッド呼び出しで Bates 番号を完全に削除できるため、ページネーションアーティファクトのライフサイクル全体を管理できます。Bates 番号の追加、カスタマイズ、削除の方法がわかりやすくステップバイステップのコード例で示されているため、このガイドは文書処理ワークフローの効率化を目指す開発者にとって実用的なリソースとなっています。
---

ベイツ番号付けは、法律、医療、ビジネスのワークフローで文書セット内のページに一意の識別子を連続して割り当てるために広く使用されています。Aspose.PDF for Python via .NET には、このプロセスを自動化するためのシンプルで柔軟な API が用意されているため、標準化された Bates 番号を任意の PDF にプログラムで適用できます。

を使用する [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) クラスでは、開発者は開始番号、桁数、接頭辞と接尾辞、配置、余白など、番号付けの動作を完全にカスタマイズできます。設定が完了すると、アーティファクトをに適用できます。 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) を通じて `add_bates_numbering` のメソッド [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) またはリストの一部として追加 [`PaginationArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paginationartifact/) オブジェクト。Aspose.PDF はデリゲートベースの構成スタイルもサポートしているため、実行時にアーティファクト設定を動的に制御できます。

ベイツ番号の作成に加えて、API ではベイツ番号を簡単に削除する方法も用意されています。 `delete_bates_numbering`、文書処理ワークフローに完全な柔軟性を提供します。

この記事では、.NET 経由の Aspose.PDF for Python を使用して PDF にベイツ番号を追加および削除する複数の方法を、アーティファクトの構成、適用、および削除の明確な例とともに説明します。

## ベイツナンバリングアーティファクトの追加

この例は、.NET 経由で Aspose.PDF for Python を使用して、プログラムで PDF ドキュメントにベイツ番号を追加する方法を示しています。を設定することにより [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) 必要な設定を行い、それをドキュメントのページに適用すると、標準化された識別子を各ページに追加するプロセスを自動化できます。

ベイツナンバリングアーティファクトをに追加するには [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)、に電話してください `AddBatesNumbering(BatesNArtifact)` の拡張メソッド [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)、渡す [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) パラメータとしてのインスタンス:

```python
import sys
from os import path
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
```

```python
import sys
from os import path
import aspose.pdf as ap

def add_bates_n_artifact(infile, outfile):
    """Add Bates numbering artifact to a PDF document."""
    with ap.Document(infile) as document:
        for _ in range(2):
            document.pages.add()

        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_bates_numbering(document.pages, bates_artifact)
        document.save(outfile)
```

## ページネーションアーティファクトを使用したベイツ番号の追加

Aspose.PDF for Python のページネーションアーティファクトコレクションを使用して PDF にベイツ番号を追加します。

1. PDF ドキュメントをロードします。
1. ナンバリングを適用する前に、必要に応じて余分なページを挿入してください。
1. ベイツアーティファクトを作る。
1. アーティファクトのプロパティを設定します。
1. アーティファクトをページネーションコレクションに追加します。
1. ページ分割をページに適用します。
1. 更新した文書を保存します。

```python
import sys
from os import path
import aspose.pdf as ap

def add_bates_n_artifact_pagination(infile, outfile):
    """Add Bates numbering using pagination artifacts collection."""
    with ap.Document(infile) as document:
        for _ in range(2):
            document.pages.add()

        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_pagination(document.pages, [bates_artifact])
        document.save(outfile)
```

## ベイツ番号を削除

からベイツ番号を削除するには [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)、を使用してください `delete_bates_numbering()` のメソッド [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/):

```python
import sys
from os import path
import aspose.pdf as ap

def delete_bates_numbering(infile, outfile):
    """Delete Bates numbering from a PDF document."""
    with ap.Document(infile) as document:
        ap.PageCollectionExtensions.delete_bates_numbering(document.pages)
        document.save(outfile)
```

## アーティファクトの関連トピック

- [Python で PDF アーティファクトを操作する](/pdf/ja/python-net/artifacts/)
- [Python で PDF にウォーターマークを追加する方法](/pdf/ja/python-net/add-watermarks/)
- [Python で PDF 背景を追加する方法](/pdf/ja/python-net/add-backgrounds/)
- [PDF ファイル内のアーティファクトタイプを数える](/pdf/ja/python-net/counting-artifacts/)