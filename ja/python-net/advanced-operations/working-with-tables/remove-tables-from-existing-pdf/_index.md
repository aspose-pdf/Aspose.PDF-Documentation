---
title: 既存の PDF ドキュメントから表を削除
linktitle: テーブルを削除
description: Python で既存の PDF ドキュメントから 1 つまたは複数のテーブルを削除する方法を学びます。
lastmod: "2026-06-09"
type: docs
weight: 50
url: /ja/python-net/removing-tables/
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF ファイルから 1 つまたは複数のテーブルを削除する
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して既存の PDF ドキュメントからテーブルを削除する方法について説明します。テーブルを検索するための「TableAmsorber」を紹介し、1 つのテーブルを削除する方法、または検出されたすべてのテーブルをページから削除する方法を示します。
---

## PDF ドキュメントから表を削除

Python 用 Aspose.PDF では、PDF からテーブルを削除できます。既存の PDF を開き、最初のページにある最初の表を検出します。 `TableAbsorber`、を使用してそのテーブルを削除します `remove()`そして、更新された PDF を新しいファイルに保存します。

このページは、表形式の多いPDFをクリーンアップしたり、古い表形式のコンテンツを削除したり、再配布する前に文書を簡略化したりする必要がある場合に使用します。

```python
import aspose.pdf as ap
from os import path
import sys

def remove_one_table(infile: str, outfile: str) -> None:
    # Load existing PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit first page with absorber
    absorber.visit(document.pages[1])
    # Get first table on the page
    table = absorber.table_list[0]
    # Remove the table
    absorber.remove(table)
    # Save PDF
    document.save(outfile)
```

## PDF ドキュメントからすべてのテーブルを削除

ライブラリを使用すると、PDFの特定のページからすべての表を削除できます。このコードは既存の PDF を開き、2 ページ目にあるすべての表を TableAbsorber で検出し、検出された表を繰り返し処理して各表を削除し、変更した PDF を新しいファイルに保存します。PDF コンテンツの残りはそのまま残したまま、ページから表を一括削除する必要がある場合に便利です。

```python
import aspose.pdf as ap
from os import path
import sys

def remove_all_tables(infile: str, outfile: str) -> None:
    # Load existing PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit first page with absorber
    absorber.visit(document.pages[1])
    #  Loop through the copy of collection and removing tables
    tables = list(absorber.table_list)
    for table in tables:
        absorber.remove(table)

    # Save document
    document.save(outfile)
```

## 関連テーブルトピック

- [Python を使用して PDF 内のテーブルを操作する](/pdf/ja/python-net/working-with-tables/)
- [Python を使用して PDF にテーブルを追加します](/pdf/ja/python-net/adding-tables/)
- [PDF 文書から表を抽出](/pdf/ja/python-net/extracting-table/)
- [既存の PDF 内の表を操作](/pdf/ja/python-net/manipulating-tables/)