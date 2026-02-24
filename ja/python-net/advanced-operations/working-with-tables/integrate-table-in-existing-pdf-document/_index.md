---
title: データソースPDFとテーブルを統合
linktitle: テーブルを統合
type: docs
weight: 30
url: /ja/python-net/integrate-table/
description: この記事では、PDFテーブルの統合方法を示します。データベースとテーブルを統合し、テーブルが現在のページで分割されるかどうかを判断します。
lastmod: "2025-09-17"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## DataFrameからPDFを作成

関数 'create_pdf_from_dataframe' は DataFrame を受け取り、新しい PDF 内のテーブルに変換します。新しい PDF ドキュメントを作成し、ページを追加し、DataFrame からテーブルを生成（ヘルパーメソッドを使用）し、結果を指定されたファイルパスに保存します。そして、これは可能なだけでなく、とても簡単です。

1. 'ap.Document()' を使用して空の PDF ドキュメントを初期化します。
1. 'self.create_table_from_dataframe(df, max_rows)' 関数は DataFrame を Aspose.PDF のテーブルオブジェクトに変換します。
1. テーブルを PDF ページに挿入します。生成されたテーブルを最初のページのコンテンツに追加します（page.paragraphs.add(table)）。
1. PDF ドキュメントを保存します。

```python

from os import path
import pandas as pd
import aspose.pdf as ap

# Example DataFrame
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Paris", "London"]
})

max_rows = 3  # Number of rows to include in the table
path_outfile = "output.pdf"

# Define the function to create a table from DataFrame
def create_table_from_dataframe(df, max_rows):
    table = ap.Table()
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1, ap.Color.light_gray)
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.BOTTOM, 1, ap.Color.light_gray
    )
    # Add header row with column names
    header_row = table.rows.add()
    header_row.is_row_broken = False
    for column_name in df.columns:
        cell = header_row.cells.add(str(column_name))
        cell.background_color = ap.Color.light_gray
    # Add data rows
    for row_data in df.head(max_rows).itertuples(index=False):
        row = table.rows.add()
        for value in row_data:
            row.cells.add(str(value))
    return table

# Load source PDF document
document = ap.Document()
page = document.pages.add()

table = create_table_from_dataframe(df, max_rows)

# Add table object to first page of input document
page.paragraphs.add(table)
document.save(path_outfile)
```

## DataFrameからテーブルを作成

このコードは DataFrame を Aspose.PDF の Table オブジェクトに変換します。テーブルの枠線を設定し、列名のヘッダー行を追加し、DataFrame の最初の max_rows 行でテーブルを埋めます。結果として得られた Table は PDF ドキュメントに追加できます。

1. 空の 'ap.Table()' オブジェクトを作成します。
1. テーブルの枠線を設定します。
1. デフォルトのセル枠線を設定します。
1. ヘッダー行を追加します。
1. データ行を追加します。
1. テーブルを返します。

```python

    from os import path
    import pandas as pd
    import aspose.pdf as ap

    
    table = ap.Table()  # Initializes a new instance of the Table
    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1, ap.Color.light_gray)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.BOTTOM, 1, ap.Color.light_gray
    )

    # Add header row with column names
    header_row = table.rows.add()
    header_row.is_row_broken = (
        False  # Prevent header row from being split across pages
    )
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
