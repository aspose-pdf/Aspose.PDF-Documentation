---
title: Python で PDF からテーブルを抽出する方法
linktitle: テーブルを抽出
type: docs
weight: 20
url: /ja/python-net/extracting-table/
description: Python で既存の PDF ドキュメントからテーブルデータを抽出する方法を学びます。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF ファイルからテーブルデータを抽出する
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメントからテーブルを抽出する方法について説明します。「TableAbsorber」を使用してページごとにテーブルを検出し、行とセルを反復処理し、分析やダウンストリームデータ処理のためにセルテキストを取得する方法を示します。
---

## PDF から表を抽出

PDF からの表の抽出は、レポート、データ移行、分析のワークフローに役立ちます。.NET 経由の Aspose.PDF for Python を使用すると、既存の PDF ドキュメントから表の内容を効率的に検出して読み取ることができます。

このコードスニペットは、既存の PDF ファイルを開き、各ページの表をスキャンして、セルテキストの内容を抽出します。以下を使用します。 `TableAbsorber` テーブルを検出し、行とセルを反復処理して抽出されたテキストを出力します。

1. PDF を AP.Document オブジェクトにロードします。
1. ページをループ処理します。
1. テーブルアブソーバーオブジェクトを作成します。
1. テーブルを反復処理します。
1. 行とセルを繰り返し処理します。
1. セルからテキストを抽出して印刷します。

次の使用例は、PDF を読み取り、すべてのテーブルを検索し、セルの内容を 1 行ずつ出力します。

```python
import aspose.pdf as ap
from os import path
import sys

def extract(infile: str) -> None:
    """Extract and print all tables from a PDF file."""
    document = ap.Document(infile)
    for page in document.pages:
        absorber = ap.text.TableAbsorber()
        absorber.visit(page)
        for table in absorber.table_list:
            print("Table ----")
            for row in table.row_list:
                print("Row:")
                row_txt = ""
                for cell in row.cell_list:
                    cell_txt = ""
                    text_fragment_collection = cell.text_fragments
                    for fragment in text_fragment_collection:
                        for seg in fragment.segments:
                            cell_txt += seg.text
                    row_txt += " | "
                    row_txt += cell_txt
                print(row_txt)
```

## 関連テーブルトピック

- [Python を使用して PDF 内のテーブルを操作する](/pdf/ja/python-net/working-with-tables/)
- [Python を使用して PDF にテーブルを追加します](/pdf/ja/python-net/adding-tables/)
- [PDF テーブルとデータソースの統合](/pdf/ja/python-net/integrate-table/)
- [既存の PDF から表を削除する](/pdf/ja/python-net/removing-tables/)