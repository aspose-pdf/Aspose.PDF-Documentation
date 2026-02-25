---
title: Python を使用した PDF へのテーブル追加
linktitle: テーブルの追加
type: docs
weight: 10
url: /ja/python-net/adding-tables/
description: Aspose.PDF for Python via .NET は、PDF テーブルの作成、読み取り、編集に使用されるライブラリです。このトピックの他の高度な機能をご確認ください。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF にテーブルを追加する方法
Abstract: この記事では、Aspose.PDF for Python via .NET ライブラリを使用して PDF ドキュメント内でテーブルを作成および操作するための包括的なガイドを提供します。テーブルの枠線、余白、パディングの設定を含め、既存の PDF ファイルにテーブルを追加する手順を詳しく解説します。さらに、`col_span` と `row_span` を使用した列や行の結合、さまざまな AutoFit 設定の適用、テーブル幅の動的取得などの高度な機能についても検討します。この記事では、テーブルセルに SVG 画像を挿入し、改ページを強制するか新しいページにテーブルを描画する方法も示します。コードスニペットは各機能を示し、PDF ドキュメントでテーブルのレイアウトとコンテンツを効果的に管理する方法を紹介します。
---

既存の PDF ドキュメントにテーブルを追加することは、データの提示を強化したり、情報を構造化したり、レポートを作成したりするための一般的なニーズです。**Aspose.PDF for Python via .NET** はこのタスクに対する包括的なソリューションを提供し、開発者が既存の PDF にシームレスにテーブルを挿入できるようにします。

このガイドは、Aspose.PDF for Python via .NET を使用して既存の PDF ドキュメントにテーブルを追加するための段階的なアプローチを提供します。テーブルの初期化、列幅の設定、枠線の定義、行とセルへのデータ入力、変更されたドキュメントの保存について説明します。さらに、セル枠線の処理、余白とパディングの適用、AutoFit 設定を利用したテーブル寸法の動的調整といった高度な機能も取り上げます。

PDF の視覚的魅力を高めたり、データをより効果的に整理したりしたい場合、このガイドは Aspose.PDF for Python の強力なテーブル操作機能を活用するための貴重なリソースとなります。

## 基本的なテーブルの作成

## テーブルの作成

この例は、枠線と複数行を持つ PDF ドキュメント内のテーブルの作成方法を示します。

1. 新しい PDF ドキュメントを作成します。
1. ドキュメントに空白ページを追加します。
1. テーブルを初期化します。
1. テーブル全体の枠線を設定します。
1. 各セルの枠線を設定します。
1. 行とセルを追加します。
1. ページにテーブルを挿入します。
1. 指定されたパスに PDF を保存します。

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Load source PDF document
    document = ap.Document()
    page = document.pages.add()
    # Initializes a new instance of the Table
    table = ap.Table()
    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 5, ap.Color.light_gray)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.ALL, 5, ap.Color.light_gray
    )
    # Create a loop to add 10 rows
    for row_count in range(0, 10):
        # Add row to table
        row = table.rows.add()
        # Add table cells
        row.cells.add("Column (" + str(row_count) + ", 1)")
        row.cells.add("Column (" + str(row_count) + ", 2)")
        row.cells.add("Column (" + str(row_count) + ", 3)")
    # Add table object to first page of input document
    page.paragraphs.add(table)

    # Save updated document containing table object
    document.save(path_outfile)
```

### テーブルセルへの画像追加

このコードスニペットは、PDF ドキュメントのテーブルセルに画像を挿入する方法を示します。

1. 新しい PDF ドキュメントを作成します。
1. テーブルを初期化します。
1. 列幅をポイント単位で設定します。
1. 最初のセルにテキストフラグメントが追加されます。
1. 'ap.Image()' インスタンスが2番目のセルに追加されます。
1. 'img.file' で画像ファイルへのパスを設定します。
1. 'img.fix_width' と 'img.fix_height' がセル内の画像サイズを制御します。
1. テーブルを PDF ページに挿入します。
1. PDF を保存します。

```python

    import aspose.pdf as ap
    from os import path

    # Instantiate Document object
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    table = ap.Table()
    # Set width for table cells
    table.column_widths = "200 100"

    # Create row object and add it to table instance
    row = table.rows.add()
    # Create cell object and add it to row instance
    cell = row.cells.add()
    # Add textfragment to paragraphs collection of cell object
    cell.paragraphs.add(ap.text.TextFragment(image))
    # Create an image instance
    img = ap.Image()
    # Set image type as SVG
    # Path for source file
    img.file = path.join(self.data_dir, image)
    # Set width for image instance
    img.fix_width = 50
    # Set height for image instance
    img.fix_height = 50
    # Add another cell to row object
    cell = row.cells.add()
    # Add SVG image to paragraphs collection of recently added cell instance
    cell.paragraphs.add(img)

    # Add table to paragraphs collection of page object
    page.paragraphs.add(table)
    # Save PDF file
    document.save(path_outfile)
```

PDF ドキュメントのテーブルセルに SVG 画像を追加できます：

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Instantiate Document object
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    table = ap.Table()
    # Set width for table cells
    table.column_widths = "200 100"
    for image in images:
        # Create row object and add it to table instance
        row = table.rows.add()
        # Create cell object and add it to row instance
        cell = row.cells.add()
        # Add textfragment to paragraphs collection of cell object
        cell.paragraphs.add(ap.text.TextFragment(image))
        # Create an image instance
        img = ap.Image()
        # Set image type as SVG
        img.file_type = ap.ImageFileType.SVG
        # Path for source file
        img.file = path.join(self.data_dir, image)
        # Set width for image instance
        img.fix_width = 50
        # Set height for image instance
        img.fix_height = 50
        # Add another cell to row object
        cell = row.cells.add()
        # Add SVG image to paragraphs collection of recently added cell instance
        cell.paragraphs.add(img)

    # Add table to paragraphs collection of page object
    page.paragraphs.add(table)
    # Save PDF file
    document.save(path_outfile)
```

### テーブルの ColSpan と RowSpan

この例は、テーブルセルを垂直および水平に結合して複雑なテーブルレイアウトを作成する方法を示します。

1. テーブル全体の枠線を設定します。
1. デフォルトのセル枠線を設定します。
1. 2つのセルを水平に結合して1つにします。
1. セルを2行にわたって垂直に結合します。
1. 行 5 は、結合された列をスキップすることで rowspan を考慮します。
1. テーブルをページに挿入します。
1. PDF を保存します。

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Load source PDF document
    document = ap.Document()
    page = document.pages.add()

    # Initializes a new instance of the Table
    table = ap.Table()
    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.black)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.ALL, 0.5, ap.Color.black
    )
    # Add 1st row to table
    row1 = table.rows.add()
    for cellCount in range(1, 5):
        # Add table cells
        row1.cells.add("Test 1" + str(cellCount))

    # Add 2nd row to table
    row2 = table.rows.add()
    row2.cells.add("Test 2 1")
    cell = row2.cells.add("Test 2 2")
    cell.col_span = 2
    row2.cells.add("Test 2 4")

    # Add 3rd row to table
    row3 = table.rows.add()
    row3.cells.add("Test 3 1")
    row3.cells.add("Test 3 2")
    row3.cells.add("Test 3 3")
    row3.cells.add("Test 3 4")

    # Add 4th row to table
    row4 = table.rows.add()
    row4.cells.add("Test 4 1")
    cell = row4.cells.add("Test 4 2")
    cell.row_span = 2
    row4.cells.add("Test 4 3")
    row4.cells.add("Test 4 4")

    # Add 5th row to table
    row5 = table.rows.add()
    row5.cells.add("Test 5 1")
    row5.cells.add("Test 5 3")
    row5.cells.add("Test 5 4")

    # Add table object to first page of input document
    page.paragraphs.add(table)
    # Save updated document containing table object
    document.save(path_outfile)
```

![ColSpan と RowSpan のデモ](colspan_rowspan.png)

### テーブルとセルへの枠線の適用

この例は、セルのパディング、テーブルの余白を設定し、テーブルセル内のテキストのワードラップを制御する方法を示しています。

1. 列の幅を設定します。
1. テーブルとセルの境界線を定義します。
1. セル内のパディングを設定し、一貫した間隔を確保します。
1. デフォルトで全てのセルにパディングを適用します。
1. テキストを追加し、ラップを制御します。
1. 行とセルを追加します。
1. PDFを保存します。

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)
    # Load source PDF document
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    tab1 = ap.Table()
    # Add the table in paragraphs collection of the desired section
    page.paragraphs.add(tab1)
    # Set with column widths of the table
    tab1.column_widths = "50 50 50"
    # Set default cell border using BorderInfo object
    tab1.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)
    # Set table border using another customized BorderInfo object
    tab1.border = ap.BorderInfo(ap.BorderSide.ALL, 1)
    # Create MarginInfo object and set its left, bottom, right and top margins
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5
    # Set the default cell padding to the MarginInfo object
    tab1.default_cell_padding = margin
    # Create rows in the table and then cells in the rows
    row1 = tab1.rows.add()
    row1.cells.add("col1")
    row1.cells.add("col2")
    row1.cells.add()
    text = ap.text.TextFragment("col3 with large text string")
    # Row1.Cells.Add("col3 with large text string to be placed inside cell")
    row1.cells[2].paragraphs.add(text)
    row1.cells[2].is_word_wrapped = False
    row2 = tab1.rows.add()
    row2.cells.add("item1")
    row2.cells.add("item2")
    row2.cells.add("item3")
    # Save updated document containing table object
    document.save(path_outfile)
```

![PDFテーブルの余白と境界](margin-border.png)

## テーブルレイアウトとサイズ設定

### 列と行の自動調整

このコードスニペットは、ページに合わせてテーブルの列幅を自動的に調整する方法を示しています。
パラメータ table.column_widths = "50 50 50" はポイントであることに注意してください。但し、センチメートル (cm)、インチ、または % でも指定可能です。

1. 初期の列幅を設定します。
1. ページ幅に合わせて列を自動的に調整します。
1. セルとテーブルの境界線を定義します。
1. 'table.default_cell_padding' はセル内の一貫した間隔のために 'MarginInfo()' を使用します。
1. 'table.rows.add()' で行を追加し、'row.cells.add()' でセルを追加します。
1. PDFを保存します。

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Load source PDF document
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    table = ap.Table()

    page.paragraphs.add(table)

    table.column_widths = "50 50 50"
    table.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_WINDOW

    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)

    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1)

    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5

    table.default_cell_padding = margin

    row1 = table.rows.add()
    row1.cells.add("col1")
    row1.cells.add("col2")
    row1.cells.add("col3")
    row2 = table.rows.add()
    row2.cells.add("item1")
    row2.cells.add("item2")
    row2.cells.add("item3")

    document.save(path_outfile)
```

### コンテンツ周辺の間隔調整

この例は、複数ページにまたがるテーブルを作成し、セル内の長文を処理し、パディングと境界線を適用する方法を示しています。

1. 'page.paragraphs.add(table)' を使用してページに新しいテーブルを追加します。
1. 'table.column_widths' で列の幅を定義します。
1. 'table.default_cell_border' を使用して個々のセル境界線を設定します。
1. 'table.border' でテーブル全体の境界線を設定します。
1. 'MarginInfo()' を使用してセルのデフォルトパディングを定義します。
1. 'TextFragment' を使用してテキストを追加します。
1. 別の行を追加します。
1. PDFを保存します。

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Instantiate a table object that will be nested inside outerTable that will break inside the same page
    table = ap.Table()
    # Add page
    page = document.pages.add()

    # Instantiate a table object
    table = ap.Table()

    # Add the table in paragraphs collection of the desired section
    page.paragraphs.add(table)

    # Set column widths of the table
    table.column_widths = "50 50 50"

    # Set default cell border using BorderInfo object
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)

    # Set table border using another customized BorderInfo object
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1)

    # Create MarginInfo object and set its left, bottom, right and top margins
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5

    # Set the default cell padding to the MarginInfo object
    table.default_cell_padding = margin

    # Create rows and cells
    row1 = table.rows.add()
    row1.cells.add("col1")
    row1.cells.add("col2")
    row1.cells.add()

    # Add a long text fragment into the third cell
    text = ap.text.TextFragment("col3 with large text string")
    row1.cells[2].paragraphs.add(text)
    row1.cells[2].is_word_wrapped = False

    # Add another row
    row2 = table.rows.add()
    row2.cells.add("item1")
    row2.cells.add("item2")
    row2.cells.add("item3")

    # Save PDF document
    document.save(path_outfile)
```

![境界線、余白、パディング](set-border-style-margins-and-padding-of-table_1.png)

### テーブルコーナーのスタイリング

Aspose.PDF for Python via .NET は、テーブルに丸みを帯びたコーナーを適用し、境界線の半径をカスタマイズする方法を示しています。

1. 新しいテーブルインスタンスを作成します。
1. すべての面に対して境界線を初期化します。
1. コーナーの半径を設定します。
1. 丸みを帯びたコーナースタイルを適用します。
1. 行とセルを追加します。
1. 'page.paragraphs.add(table)' でテーブルをPDFページに挿入します。
1. PDFドキュメントを保存します。

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Load source PDF document
    document = ap.Document()
    page = document.pages.add()
    # Initializes a new instance of the Table
    table = ap.Table()

    # Create a table
    table = ap.Table()

    # Create a blank BorderInfo object
    b_info = ap.BorderInfo(ap.BorderSide.ALL)

    # Set the border a rounded border where radius of round is 15
    b_info.rounded_border_radius = 15

    # Set the table corner style as Round
    table.corner_style = ap.BorderCornerStyle.ROUND

    # Set the table border information
    table.border = b_info

    # Create a loop to add 10 rows
    for row_count in range(0, 10):
        # Add row to table
        row = table.rows.add()
        # Add table cells
        row.cells.add("Column (" + str(row_count) + ", 1)")
        row.cells.add("Column (" + str(row_count) + ", 2)")
        row.cells.add("Column (" + str(row_count) + ", 3)")

    # Add table object to first page of input document
    page.paragraphs.add(table)
    # Save updated document containing table object
    document.save(path_outfile)
```

## テーブルへのコンテンツ追加

### セル内でHTMLフラグメントを使用する

この例は、HTML形式のコンテンツをテーブルセルに挿入する方法を示しています。

1. テーブルとセルの境界線を定義します。
1. HTMLコンテンツを追加します。
1. 行を追加します。ループで各セルにHTML形式のコンテンツを持つ複数の行を追加します。
1. 'page.paragraphs.add(table)' でテーブルをPDFページに挿入します。
1. PDFドキュメントを保存します。

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Instantiate Document object
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    table = ap.Table()

    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.light_gray)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.ALL, 0.5, ap.Color.light_gray
    )
    # Create a loop to add 10 rows
    row_count = 1
    while row_count < 10:
        # Add row to table
        row = table.rows.add()
        # Add table cells
        cell = row.cells.add()
        cell.paragraphs.add(
            ap.HtmlFragment(f"Column <strong>({row_count}, 1)</strong>")
        )

        cell = row.cells.add()
        cell.paragraphs.add(
            ap.HtmlFragment(
                f"Column <span style='color:red'>({row_count}, 2)</span>"
            )
        )

        cell = row.cells.add()
        cell.paragraphs.add(
            ap.HtmlFragment(
                f"Column <span style='text-decoration: underline'>({row_count}, 3)</span>"
            )
        )
        row_count += 1

    # Add table object to first page of input document
    page.paragraphs.add(table)
    # Save updated document containing table object
    document.save(path_outfile)
```

### セル内でLaTeXフラグメントを使用する

この例は、数式やスタイル化された表現のために、LaTeX形式のコンテンツをテーブルセルに挿入する方法を示しています。

1. テーブルとセルの境界線を定義します。
1. LaTeX コンテンツを追加します。
1. 行を追加します。ループで各セルに LaTeX 形式のコンテンツを持つ複数の行を追加します。
1. 'page.paragraphs.add(table)' を使用してテーブルを PDF ページに挿入します。
1. PDF ドキュメントを保存します。

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Instantiate Document object
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    table = ap.Table()

    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.light_gray)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.ALL, 0.5, ap.Color.light_gray
    )
    # Create a loop to add 10 rows
    row_count = 1
    while row_count < 10:
        # Add row to table
        row = table.rows.add()
        # Add table cells
        cell = row.cells.add()
        cell.paragraphs.add(
            ap.LatexFragment(f"Column $\\mathbf{{({row_count}, 1)}}$")
        )

        cell = row.cells.add()
        cell.paragraphs.add(
            ap.LatexFragment(
                f"Column $\\textcolor{{red}}{{({row_count}, 2)}}$"
            )
        )

        cell = row.cells.add()
        cell.paragraphs.add(
            ap.LatexFragment(
                f"Column $\\underline{{({row_count}, 3)}}$"
            )
        )
        row_count += 1

    # Add table object to first page of input document
    page.paragraphs.add(table)
    # Save updated document containing table object
    document.save(path_outfile)
```

## 高度なテーブル機能

### ページをまたぐテーブルの挿入

この例では、PDF に複数のテーブルを作成し、ページ余白を設定し、テーブルを新しいページで開始させる方法を示します。

1. 'page_info.margin' を使用してページ余白を設定します。
1. 'page_info.is_landscape' でページの向きを横向きに設定します。
1. 最初のテーブル:
- 指定された幅で2列を定義します。
- 'row.fixed_row_height' を使用してループで行を追加します。
- セルにテキストフラグメントを入力します。
1. 2番目のテーブル:
- 'table1.column_widths' を使用して新しいテーブルを作成します。
- テーブルが新しいページで開始するように強制します。
1. 最初のテーブルを追加します。
1. 新しいページに2番目のテーブルを追加します。
1. ドキュメントを保存します

```python

    import aspose.pdf as ap
    from os import path

    # The path to the documents directory
    path_outfile = path.join(self.data_dir, outfile)

    # Create PDF document
    document = ap.Document()

    # Set page and margin information
    page_info = document.page_info
    margin_info = page_info.margin

    margin_info.left = 37
    margin_info.right = 37
    margin_info.top = 37
    margin_info.bottom = 37
    page_info.is_landscape = True

    # First table with 120 rows
    table = ap.Table()
    table.column_widths = "50 100"

    cur_page = document.pages.add()

    for i in range(1, 121):
        row = table.rows.add()
        row.fixed_row_height = 15
        cell1 = row.cells.add()
        cell1.paragraphs.add(ap.text.TextFragment("Content 1"))
        cell2 = row.cells.add()
        cell2.paragraphs.add(ap.text.TextFragment("Content 2"))

    cur_page.paragraphs.add(table)

    # Second table with 10 rows
    table1 = ap.Table()
    table1.column_widths = "100 100"

    for i in range(1, 11):
        row = table1.rows.add()
        cell1 = row.cells.add()
        cell1.paragraphs.add(ap.text.TextFragment("Content 3"))
        cell2 = row.cells.add()
        cell2.paragraphs.add(ap.text.TextFragment("Content 4"))

    table1.is_in_new_page = True  # Force table to new page
    cur_page.paragraphs.add(table1)

    # Save updated document containing table object
    document.save(path_outfile)
```

### 境界線なしテーブルの作成

この例では、ページをまたいで縦に分割可能な大きなテーブルを作成し、列を繰り返し、ヘッダーセルに異なる背景色を適用する方法を示します。

1. テーブルを初期化します。
1. すべてのセルにデフォルトの枠線を設定します。
1. ヘッダーセルは 'col_span' を使用して複数列を結合します。
1. 'background_color set' を使用して、視覚的区別を高めるためにセルの背景を設定します
1. 行を追加します。
1. 'page.paragraphs.add(table)' を使用してテーブルを PDF ページに挿入します。
1. PDF ドキュメントを保存します。

```python

    import aspose.pdf as ap
    from os import path

    # The path to the documents directory
    path_outfile = path.join(self.data_dir, outfile)

    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    table = ap.Table()
    table.broken = ap.TableBroken.VERTICAL
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL)
    table.repeating_columns_count = 2
    page.paragraphs.add(table)

    # Add header Row
    row = table.rows.add()
    cell = row.cells.add("header 1")
    cell.col_span = 2
    cell.background_color = ap.Color.light_gray
    row.cells.add("header 3")

    cell2 = row.cells.add("header 4")
    cell2.col_span = 2
    cell2.background_color = ap.Color.light_blue
    row.cells.add("header 6")

    cell3 = row.cells.add("header 7")
    cell3.col_span = 2
    cell3.background_color = ap.Color.light_green
    cell4 = row.cells.add("header 9")

    cell4.col_span = 3
    cell4.background_color = ap.Color.light_coral
    row.cells.add("header 12")
    row.cells.add("header 13")
    row.cells.add("header 14")
    row.cells.add("header 15")
    row.cells.add("header 16")
    row.cells.add("header 17")

    row_counter = 0
    while row_counter < 3:
        # Create rows in the table and then cells in the rows
        row1 = table.rows.add()
        row1.cells.add("col " + str(row_counter) + ", 1")
        row1.cells.add("col " + str(row_counter) + ", 2")
        row1.cells.add("col " + str(row_counter) + ", 3")
        row1.cells.add("col " + str(row_counter) + ", 4")
        row1.cells.add("col " + str(row_counter) + ", 5")
        row1.cells.add("col " + str(row_counter) + ", 6")
        row1.cells.add("col " + str(row_counter) + ", 7")
        row1.cells.add("col " + str(row_counter) + ", 8")
        row1.cells.add("col " + str(row_counter) + ", 9")
        row1.cells.add("col " + str(row_counter) + ", 10")
        row1.cells.add("col " + str(row_counter) + ", 11")
        row1.cells.add("col " + str(row_counter) + ", 12")
        row1.cells.add("col " + str(row_counter) + ", 13")
        row1.cells.add("col " + str(row_counter) + ", 14")
        row1.cells.add("col " + str(row_counter) + ", 15")
        row1.cells.add("col " + str(row_counter) + ", 16")
        row1.cells.add("col " + str(row_counter) + ", 17")
        row_counter += 1

    document.save(path_outfile)
```

### 複数ページにわたるヘッダー行の繰り返し

この例では、ヘッダー行を各ページに表示させたまま、複数ページにまたがるテーブルを作成する方法を示します。

1. テーブルを初期化します。
1. フォント、サイズ、色を含めてヘッダー行を繰り返します。
1. 列幅を設定し、テーブルに枠線を適用します。
1. ヘッダー行を追加します。
1. 多数のデータ行を追加してテーブルが複数ページにまたがるようにします。
1. 'page.paragraphs.add(table)' を使用してテーブルを PDF ページに挿入します。
1. PDF ドキュメントを保存します。

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Instantiate a table object
    table = ap.Table()

    # Set the table to break across pages
    table.broken = ap.TableBroken.VERTICAL

    # Set number of repeating header rows
    table.repeating_rows_count = 2

    text_state = ap.text.TextState()
    text_state.font_size = 12
    text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_state.foreground_color = ap.Color.red
    table.repeating_rows_style =  text_state

    # Set column widths
    table.column_widths = "100 100 100"

    # Set borders
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.black)
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1, ap.Color.black)

    # Add header rows that will repeat on each page
    header_row1 = table.rows.add()
    header_row1.cells.add("Header 1-1")
    header_row1.cells.add("Header 1-2")
    header_row1.cells.add("Header 1-3")

    # Set background color for header rows
    for cell in header_row1.cells:
        cell.background_color = ap.Color.light_gray

    header_row2 = table.rows.add()
    header_row2.cells.add("Header 2-1")
    header_row2.cells.add("Header 2-2")
    header_row2.cells.add("Header 2-3")

    for cell in header_row2.cells:
        cell.background_color = ap.Color.light_blue

    # Add many data rows to force table across multiple pages
    for i in range(1, 101):
        row = table.rows.add()
        row.cells.add(f"Data {i}-1")
        row.cells.add(f"Data {i}-2")
        row.cells.add(f"Data {i}-3")

    # Add table to page
    page.paragraphs.add(table)

    # Save document
    document.save(path_outfile)
```

### 列の繰り返し

'add_repeating_columns' 関数は、列が繰り返されるテーブルを持つ PDF ドキュメントを作成します。枠線付きテーブルを設定し、ヘッダーを追加し、データ行を埋め、生成された PDF ファイルを指定された場所に保存します。このプロパティを設定すると、テーブルは次のページで列単位に改ページされ、次のページの先頭で指定された列数が繰り返されます。

1. 新しい PDF ドキュメントを初期化します。
1. カスタム寸法のページを追加します。
1. テーブルの枠線スタイルを設定します。
1. テーブルを初期化します。
1. テーブルを PDF ページに追加します。
1. ヘッダー行を追加します。
1. データ行を追加します。
1. PDF ドキュメントを保存します。

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()
    page.set_page_size(ap.PageSize.A5.height, ap.PageSize.A5.width)

    # Define border
    border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.light_gray)

    # Create table
    table = ap.Table()
    table.broken = ap.TableBroken.VERTICAL
    table.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_CONTENT
    table.repeating_columns_count = 5
    table.border = border
    table.default_cell_border = border

    # Add table to page
    page.paragraphs.add(table)

    # Add header row
    row = table.rows.add()
    for i in range(1, 6):
        cell = row.cells.add(f"header {i}")
        cell.background_color = ap.Color.light_gray

    for i in range(6, 18):
        row.cells.add(f"header {i}")

    # Add data rows
    for row_counter in range(1, 6):
        row = table.rows.add()
        for i in range(1, 6):
            cell = row.cells.add(f"cell {row_counter},{i}")
            cell.background_color = ap.Color.light_gray
        for i in range(6, 18):
            row.cells.add(f"cell {row_counter},{i}")

    # Save PDF document
    document.save(path_outfile)
    print(f"File saved at: {path_outfile}")
```
