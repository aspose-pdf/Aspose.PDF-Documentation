---
title: Python で PDF テーブルをデータソースと統合する方法
linktitle: 統合テーブル
type: docs
weight: 30
url: /ja/python-net/integrate-table/
description: Python で PDF テーブルをデータベースや Pandas DataFrame などのデータソースと統合する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF テーブルをデータベースやデータフレームと統合する
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF テーブルを外部データソースと統合する方法について説明します。Pandas DataFrame やその他の構造化されたソースから PDF テーブルを作成し、それらを文書に挿入し、Python で PDF ページにわたってレンダリングする際のテーブルフローを制御する方法を学びます。
---

## データフレームから PDF を作成

ザの `create_pdf_from_dataframe` 関数は新しい PDF を作成し、パンダのデータフレームから生成されたテーブルを挿入します。この方法は、データがすでに表形式で存在するレポートワークフローに役立ちます。

この関数は以下のステップを実行します。

1. で空の PDF ドキュメントを作成 `ap.Document()`.
1. 文書にページを追加します。
1. を呼び出して、データフレームを Aspose.PDF テーブルに変換します `create_table_from_dataframe(df, max_rows)`.
1. を使用してテーブルをページに追加します `page.paragraphs.add(table)`.
1. PDF を出力パスに保存します。

```python
from os import path
import sys

import pandas as pd
import aspose.pdf as ap
from config import set_license, initialize_data_dir

def create_pdf_from_dataframe(
    outfile: str, df: pd.DataFrame, max_rows: int = 20
) -> None:
    # Create new PDF document
    document = ap.Document()
    page = document.pages.add()

    table = create_table_from_dataframe(df, max_rows)

    # Add table object to first page of input document
    page.paragraphs.add(table)
    document.save(outfile)
```

## データフレームからテーブルを作成

ザの `create_table_from_dataframe` 関数はデータフレームを Aspose.PDF に変換します `Table` どのページにも追加できるオブジェクト。

次のことを行います。

1. 空欄を作成 `ap.Table()` インスタンス。
1. 表とセルの境界線を設定すると、書式の一貫性が保たれます。
1. DataFrame 列名を使用してヘッダー行を追加します。
1. からデータ行を追加 `df.head(max_rows)`.
1. 入力されたテーブルオブジェクトを返します。

```python
from os import path
import sys

import pandas as pd
import aspose.pdf as ap
from config import set_license, initialize_data_dir

def create_table_from_dataframe(df: pd.DataFrame, max_rows: int = 20) -> ap.Table:
    """Create an Aspose.PDF table from a pandas DataFrame."""
    # Initializes a new instance of the Table
    table = ap.Table()
    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1, ap.Color.light_gray)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.BOTTOM, 1, ap.Color.light_gray
    )

    # Add header row with column names
    header_row = table.rows.add()
    header_row.is_row_broken = False  # Prevent header row from being split across pages
    for column_name in df.columns:
        cell = header_row.cells.add(str(column_name))
        cell.background_color = ap.Color.light_gray

    # Add data rows
    for row_data in df.head(max_rows).itertuples(index=False):
        row = table.rows.add()
        for value in row_data:
            row.cells.add(str(value))

    return table
```

## 関連テーブルトピック

- [Python を使用して PDF 内のテーブルを操作する](/pdf/ja/python-net/working-with-tables/)
- [Python を使用して PDF にテーブルを追加します](/pdf/ja/python-net/adding-tables/)
- [PDF 文書から表を抽出](/pdf/ja/python-net/extracting-table/)
- [既存の PDF 内の表を操作](/pdf/ja/python-net/manipulating-tables/)