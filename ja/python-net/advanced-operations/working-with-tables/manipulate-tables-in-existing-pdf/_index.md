---
title: 既存の PDF ドキュメント内の表の操作
linktitle: テーブルを操作
type: docs
weight: 40
url: /ja/python-net/manipulating-tables/
description: Python を使用して既存の PDF ドキュメント内のテーブルを検査および変更する方法を学びます。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して既存の PDF テーブルを検査および変更する
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメントにすでに存在するテーブルを操作する方法について説明します。TableAbsorber を使用してテーブルを検索する方法、特定の行やセルにアクセスする方法、テーブルテキストの内容を更新する方法、変更した PDF を Python で保存する方法について説明します。
---

## 既存の PDF 内の表を操作

.NET 経由の Python 用の Aspose.PDF では、PDF ドキュメントにすでに存在するテーブルを更新できます。次のものを使用できます。 [テーブルアブソーバー](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) クラスを使用すると、ページ上の表を検索したり、行やセルにアクセスしたり、テキストの内容を変更したり、更新されたファイルを保存したりできます。

このページは、文書レイアウト全体を再作成せずに PDF 内の既存の表の内容を更新する必要がある場合に使用します。

## PDF テーブルセル内のテキストの検索と置換

次の使用例は、1 ページ目の最初の表を検索し、最初のセルにアクセスし、そのテキストを置換して、出力 PDF を保存します。

1. 入力 PDF を開きます。
1. テーブルアブソーバーを作成し、1ページ目にアクセスしてください。
1. 少なくとも 1 つのテーブルが検出されていることを確認します。
1. 最初の表の最初の行の最初のセルにアクセスします。
1. セルにテキストフラグメントが含まれていることを確認し、最初のフラグメントを更新します。
1. 変更した PDF を保存します。

```python
import aspose.pdf as ap

def replace_cell_text(infile: str, outfile: str) -> None:
    """Replace text in the first cell of the first detected table."""
    # Open PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    if len(absorber.table_list) == 0:
        raise ValueError("No tables were found on page 1.")

    first_cell = absorber.table_list[0].row_list[0].cell_list[0]
    if len(first_cell.text_fragments) == 0:
        raise ValueError("The target cell has no text fragments.")

    # Change text of the first text fragment in the cell
    first_cell.text_fragments[0].text = "New Value"

    # Save PDF document
    document.save(outfile)
```

## 既存のテーブルを新しいテーブルに置き換える

検出されたテーブルを新しく作成されたテーブルに置き換えることもできます。この方法は、構造と内容の両方を変更する必要がある場合に役立ちます。

以下のコードは PDF を開き、1 ページ目の最初のテーブルを見つけ、代替テーブルを作成し、古いテーブルを新しいテーブルと入れ替えて、結果を保存します。

```python
import aspose.pdf as ap

def replace_table(infile: str, outfile: str) -> None:
    """Replace an entire table with a new one."""
    # Open PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    if len(absorber.table_list) == 0:
        raise ValueError("No tables were found on page 1.")

    # Get first table on the page
    old_table = absorber.table_list[0]

    # Create new table
    new_table = ap.Table()
    new_table.column_widths = "100 100 100"
    new_table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 1.0)

    row = new_table.rows.add()
    row.cells.add("Col 1")
    row.cells.add("Col 2")
    row.cells.add("Col 3")
    row = new_table.rows.add()
    row.cells.add("Col 12")
    row.cells.add("Col 22")
    row.cells.add("Col 32")

    # Replace the old table with the new one
    absorber.replace(document.pages[1], old_table, new_table)

    # Save PDF document
    document.save(outfile)
```

## 関連テーブルトピック

- [Python を使用して PDF 内のテーブルを操作する](/pdf/ja/python-net/working-with-tables/)
- [Python を使用して PDF にテーブルを追加します](/pdf/ja/python-net/adding-tables/)
- [PDF 文書から表を抽出](/pdf/ja/python-net/extracting-table/)
- [既存の PDF から表を削除する](/pdf/ja/python-net/removing-tables/)
