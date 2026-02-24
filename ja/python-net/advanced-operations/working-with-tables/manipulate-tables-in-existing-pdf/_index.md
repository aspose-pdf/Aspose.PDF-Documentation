---
title: 既存PDFのテーブルを操作する
linktitle: テーブルを操作する
type: docs
weight: 40
url: /ja/python-net/manipulating-tables/
description: Aspose.PDF for Python via .NET を使用して、既存の PDF のテーブルを操作する方法を学び、ドキュメントの変更に柔軟性を提供します。
lastmod: "2025-09-27"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## 既存PDFのテーブルを操作する

Aspose.PDF for Python は、PDF ドキュメント内のテーブルの特定のセルの内容を変更する方法を示します。TableAbsorber クラスを使用して最初のページのテーブルを検出し、最初のテーブルの最初のセル内の特定のテキストフラグメントにアクセスし、そのテキストを更新し、変更された PDF を新しいファイルに保存します。

1. 'ap.Document()' を使用して PDF ファイルを開きます。
1. PDF 内のテーブルを検出するために TableAbsorber オブジェクトを作成します。
1. absorber.visit() を呼び出して、最初のページのすべてのテーブルを見つけます。
1. 特定のテキストフラグメントにアクセスします：
- 最初のテーブルを取得します。
- テーブルの最初の行を取得します。
- セル内の2番目のテキストフラグメントを選択します。
1. テキストを変更します。
1. 更新された PDF を保存します。
1. 保存されたファイルの確認を出力します。

```python

    import aspose.pdf as ap
    from os import path

    # Define file names and data directory
    data_dir = "."  # or specify your data directory
    infile = "input.pdf"   # replace with your input PDF file name
    outfile = "output.pdf" # replace with your desired output PDF file name

    # Open PDF document
    path_infile = path.join(data_dir, infile)
    path_outfile = path.join(data_dir, outfile)
    document = ap.Document(path_infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    # Get access to first table on page, their first cell and text fragments in it
    fragment = absorber.table_list[0].row_list[0].cell_list[0].text_fragments[1]

    # Change text of the first text fragment in the cell
    fragment.text = "hi world"

    # Save PDF document

    document.save(path_outfile)
    print(f"File saved at: {path_outfile}")
```

## PDF ドキュメント内の古いテーブルを新しいものに置き換える

Aspose.PDF は、PDF 内の既存のテーブルを新しいテーブルに置き換えることを可能にします。コードスニペットは PDF を開き、TableAbsorber を使用して最初のページの最初のテーブルを特定し、カスタムの列幅と内容を持つ新しいテーブルを作成し、元のテーブルを新しいテーブルに置き換えます。最後に、更新された PDF を新しいファイルに保存します。

文書の他の部分を変更せずに、PDF のテーブル構造と内容を変更する方法を示しています。

```python

    import aspose.pdf as ap
    from os import path

    # Open PDF document
    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)
    document = ap.Document(path_infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    # Get first table on the page
    table = absorber.table_list[0]

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

    # Replace the table with new one
    absorber.replace(document.pages[1], table, new_table)

    # Save PDF document
    document.save(path_outfile)
    print(f"File saved at: {path_outfile}")
```
