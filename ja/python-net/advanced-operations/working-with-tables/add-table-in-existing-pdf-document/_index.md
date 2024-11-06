---
title: Pythonを使用してPDFにテーブルを作成または追加する 
linktitle: テーブルを作成または追加
type: docs
weight: 10
url: ja/python-net/add-table-in-existing-pdf-document/
description: Aspose.PDF for Python via .NETは、PDFテーブルを作成、読み取り、編集するためのライブラリです。このトピックの他の高度な機能を確認してください。
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Pythonを使用してPDFにテーブルを作成または追加する",
    "alternativeHeadline": ".NETを介してPythonでPDFにテーブルを追加する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdfドキュメント生成",
    "keywords": "pdf, python, pdfにテーブルを作成, テーブルを追加",
    "wordcount": "302",
    "proficiencyLevel":"初心者",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/add-table-in-existing-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-table-in-existing-pdf-document/"
    },
    "dateModified": "2023-02-04",
    "description": "Aspose.PDF for Python via .NETは、PDFテーブルを作成、読み取り、編集するためのライブラリです。このトピックの他の高度な機能を確認してください。"
}
</script>


## Pythonを使用してテーブルを作成

テーブルは、PDFドキュメントを扱う際に重要です。情報を体系的に表示するための優れた機能を提供します。Aspose.PDF名前空間には、PDFドキュメントをゼロから生成する際にテーブルを作成する機能を提供する[Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/)、[Cell](https://reference.aspose.com/pdf/python-net/aspose.pdf/cell/)、[Row](https://reference.aspose.com/pdf/python-net/aspose.pdf/row/)という名前のクラスが含まれています。

テーブルは、Tableクラスのオブジェクトを作成することで作成できます。

```python

    table = ap.Table()
```

### 既存のPDFドキュメントにテーブルを追加

Aspose.PDF for Python via .NETを使用して既存のPDFファイルにテーブルを追加するには、次の手順を実行します。

1. ソースファイルを読み込む。
1. テーブルを初期化し、その列と行を設定する。
1. テーブル設定を設定する（境界線を設定しています）。
1. テーブルを埋める。
1. ページにテーブルを追加する。
1. ファイルを保存する。

次のコードスニペットは、既存のPDFファイルにテキストを追加する方法を示しています。

```python

    import aspose.pdf as ap

    # ソースPDFドキュメントをロード
    doc = ap.Document(input_file)
    # テーブルの新しいインスタンスを初期化
    table = ap.Table()
    # テーブルの枠線の色をライトグレーに設定
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 5, ap.Color.from_rgb(apd.Color.light_gray))
    # テーブルセルの枠線を設定
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 5, ap.Color.from_rgb(apd.Color.light_gray))
    # 10行を追加するループを作成
    for row_count in range(0, 10):
        # テーブルに行を追加
        row = table.rows.add()
        # テーブルセルを追加
        row.cells.add("Column (" + str(row_count) + ", 1)")
        row.cells.add("Column (" + str(row_count) + ", 2)")
        row.cells.add("Column (" + str(row_count) + ", 3)")
    # テーブルオブジェクトを入力ドキュメントの最初のページに追加
    doc.pages[1].paragraphs.add(table)
    # テーブルオブジェクトを含む更新されたドキュメントを保存
    doc.save(output_file)
```

### テーブルにおけるColSpanとRowSpan

Aspose.PDF for Python via .NET は、テーブル内の列をマージするための[col_span](https://reference.aspose.com/pdf/python-net/aspose.pdf/cell/#properties)プロパティと、行をマージするための[row_span](https://reference.aspose.com/pdf/python-net/aspose.pdf/cell/#properties)プロパティを提供します。

`Cell`オブジェクトに対して`col_span`または`row_span`プロパティを使用し、テーブルセルを作成します。必要なプロパティを適用した後、作成されたセルをテーブルに追加できます。

```python

    import aspose.pdf as ap

    # 空のコンストラクターを呼び出してDocumentオブジェクトを初期化します
    pdf_document = ap.Document()
    pdf_document.pages.add()
    # Tableの新しいインスタンスを初期化します
    table = ap.Table()
    # テーブルの枠線の色をLightGrayに設定します
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.black)
    # テーブルセルの枠線を設定します
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.black)
    # テーブルに1行目を追加します
    row1 = table.rows.add()
    for cellCount in range(1, 5):
        # テーブルセルを追加します
        row1.cells.add("Test 1" + str(cellCount))

    # テーブルに2行目を追加します
    row2 = table.rows.add()
    row2.cells.add("Test 2 1")
    cell = row2.cells.add("Test 2 2")
    cell.col_span = 2
    row2.cells.add("Test 2 4")

    # テーブルに3行目を追加します
    row3 = table.rows.add()
    row3.cells.add("Test 3 1")
    row3.cells.add("Test 3 2")
    row3.cells.add("Test 3 3")
    row3.cells.add("Test 3 4")

    # テーブルに4行目を追加します
    row4 = table.rows.add()
    row4.cells.add("Test 4 1")
    cell = row4.cells.add("Test 4 2")
    cell.row_span = 2
    row4.cells.add("Test 4 3")
    row4.cells.add("Test 4 4")

    # テーブルに5行目を追加します
    row5 = table.rows.add()
    row5.cells.add("Test 5 1")
    row5.cells.add("Test 5 3")
    row5.cells.add("Test 5 4")

    # テーブルオブジェクトを入力ドキュメントの1ページ目に追加します
    pdf_document.pages[1].paragraphs.add(table)
    # テーブルオブジェクトを含む更新されたドキュメントを保存します
    pdf_document.save(output_file)
```


実行コードの結果は、次の画像に示されている表です:

![ColSpan and RowSpan demo](colspan_rowspan.png)

## 境界線、余白、パディングの操作

また、表の境界線スタイル、余白、セルのパディングを設定する機能もサポートしていることに注意してください。より技術的な詳細に入る前に、以下の図で示されている境界線、余白、パディングの概念を理解することが重要です:

![Borders, margins and padding](set-border-style-margins-and-padding-of-table_1.png)

上の図では、表、行、セルの境界線が重なっているのがわかります。Aspose.PDFを使用すると、表には余白があり、セルにはパディングがあります。セルの余白を設定するには、セルのパディングを設定する必要があります。

### 境界線

[Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) 、[Row](https://reference.aspose.com/pdf/python-net/aspose.pdf/row/) 、[Cell](https://reference.aspose.com/pdf/python-net/aspose.pdf/cell/) オブジェクトの境界線を設定するには、Table.border、Row.border、Cell.border プロパティを使用します。
 セルの境界線は、[Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) または Row クラスの [default_cell_border](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) プロパティを使用して設定することもできます。上記で説明したすべての境界線関連プロパティには、コンストラクタを呼び出すことで作成される Row クラスのインスタンスが割り当てられます。Row クラスには、境界線をカスタマイズするために必要なほとんどすべてのパラメータを受け取る多くのオーバーロードがあります。

### マージンまたはパディング

セルのパディングは、Table クラスの [default_cell_padding](https://reference.aspose.com/pdf/python-net/aspose.pdf/row/#properties) プロパティを使用して管理できます。すべてのパディング関連プロパティは、カスタムマージンを作成するために `left`、`right`、`top`、`bottom` パラメータに関する情報を受け取る [MarginInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) クラスのインスタンスに割り当てられます。
次の例では、セルの境界線の幅を0.1ポイント、テーブルの境界線の幅を1ポイント、セルの余白を5ポイントに設定しています。

![PDFテーブルのマージンと境界線](margin-border.png)

```python

    import aspose.pdf as ap

    # 空のコンストラクターを呼び出してDocumentオブジェクトをインスタンス化
    doc = ap.Document()
    page = doc.pages.add()
    # テーブルオブジェクトをインスタンス化
    tab1 = ap.Table()
    # 必要なセクションの段落コレクションにテーブルを追加
    page.paragraphs.add(tab1)
    # テーブルの列の幅を設定
    tab1.column_widths = "50 50 50"
    # BorderInfoオブジェクトを使用してデフォルトのセル境界線を設定
    tab1.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)
    # 別のカスタマイズされたBorderInfoオブジェクトを使用してテーブル境界線を設定
    tab1.border = ap.BorderInfo(ap.BorderSide.ALL, 1)
    # MarginInfoオブジェクトを作成し、その左、下、右、上のマージンを設定
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5
    # MarginInfoオブジェクトにデフォルトのセル余白を設定
    tab1.default_cell_padding = margin
    # テーブルに行を作成し、その行にセルを作成
    row1 = tab1.rows.add()
    row1.cells.add("col1")
    row1.cells.add("col2")
    row1.cells.add()
    my_text = ap.text.TextFragment("col3 with large text string")
    # 行1.セルに「大きなテキスト文字列をセル内に配置するためのcol3」を追加
    row1.cells[2].paragraphs.add(my_text)
    row1.cells[2].is_word_wrapped = False
    row2 = tab1.rows.add()
    row2.cells.add("item1")
    row2.cells.add("item2")
    row2.cells.add("item3")
    # Pdfを保存
    doc.save(output_file)
```


テーブルを丸い角で作成するには、[BorderInfo クラス](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/)の[rounded_border_radius](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/#properties)値を使用し、テーブルの角のスタイルを丸く設定します。

```python
    
    import aspose.pdf as ap
    
    tab1 = ap.Table()
    graph = ap.GraphInfo()
    graph.color = ap.Color.red
    # 空の BorderInfo オブジェクトを作成
    b_info = ap.BorderInfo(ap.BorderSide.ALL, graph)
    # 半径が15の丸い境界を設定
    b_info.rounded_border_radius = 15
    # テーブルの角のスタイルを丸に設定
    tab1.corner_style = ap.BorderCornerStyle.ROUND
    # テーブルの境界情報を設定
    tab1.border = b_info
```

## テーブルに異なる AutoFit 設定を適用する

Microsoft Word のようなビジュアルツールを使用してテーブルを設計する場合、テーブルのサイズを希望の幅に便利に調整するために AutoFit 機能の1つを頻繁に利用します。
 たとえば、テーブルの幅をページに合わせるために "AUTO_FIT_TO_WINDOW" オプションや AUTO_FIT_TO_CONTENT を使用できます。デフォルトでは、Aspose.Pdf を使用して新しいテーブルを作成すると、[column_adjustment](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) は "Customized" の値を使用します。次のコードスニペットでは、テーブル内で [MarginInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) と [BorderInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/) オブジェクトのパラメータを設定します。例をテストし、結果を評価してください。

```python

    import aspose.pdf as ap

    # 空のコンストラクターを呼び出して Pdf オブジェクトをインスタンス化します
    doc = ap.Document()
    # Pdf オブジェクトにセクションを作成します
    sec1 = doc.pages.add()
    # テーブルオブジェクトをインスタンス化します
    tab1 = ap.Table()
    # テーブルを目的のセクションの段落コレクションに追加します
    sec1.paragraphs.add(tab1)
    # テーブルの列幅を設定します
    tab1.column_widths = "50 50 50"
    tab1.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_WINDOW
    # BorderInfo オブジェクトを使用してデフォルトのセル境界を設定します
    tab1.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)
    # カスタマイズされた別の BorderInfo オブジェクトを使用してテーブル境界を設定します
    tab1.border = ap.BorderInfo(ap.BorderSide.ALL, 1)
    # MarginInfo オブジェクトを作成し、左、下、右、上のマージンを設定します
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5
    # デフォルトのセルパディングを MarginInfo オブジェクトに設定します
    tab1.default_cell_padding = margin
    # テーブルに行を作成し、その後行にセルを作成します
    row1 = tab1.rows.add()
    row1.cells.add("col1")
    row1.cells.add("col2")
    row1.cells.add("col3")
    row2 = tab1.rows.add()
    row2.cells.add("item1")
    row2.cells.add("item2")
    row2.cells.add("item3")
    # テーブルオブジェクトを含む更新されたドキュメントを保存します
    doc.save(output_file)
```

### テーブルの幅を取得

場合によっては、テーブルの幅を動的に取得する必要があります。Aspose.PDF.Tableクラスには、そのためのメソッド[get_width()](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#methods)があります。例えば、テーブルの列幅を明示的に設定せず、[column_adjustment](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties)を 'AUTO_FIT_TO_CONTENT' に設定した場合、以下のようにテーブルの幅を取得できます。

```python

    import aspose.pdf as ap

    # 新しいドキュメントを作成
    doc = ap.Document()
    # ドキュメントにページを追加
    page = doc.pages.add()
    # 新しいテーブルを初期化
    table = ap.Table()
    table.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_CONTENT
    # テーブルに行を追加
    row = table.rows.add()
    # テーブルにセルを追加
    cell = row.cells.add("セル1のテキスト")
    cell = row.cells.add("セル2のテキスト")
    # テーブルの幅を取得
    print(table.get_width())
```

## テーブルのセルにSVG画像を追加

Aspose.PDF for Python via .NETは、PDFファイルにテーブルセルを挿入する機能を提供します。
 テーブルを構築する際には、これらのセル内にテキストや画像を含めることができます。さらに、APIはSVGファイルをPDF形式に変換する機能を提供しています。これらの機能を組み合わせて活用することで、SVG画像を読み込み、テーブルセル内に配置することができます。

次のコード抜粋は、テーブルオブジェクトを作成し、そのセルの1つにSVG画像を埋め込むプロセスを示しています。

```python

    import aspose.pdf as ap

    # Documentオブジェクトをインスタンス化
    doc = ap.Document()
    # 画像インスタンスを作成
    img = ap.Image()
    # 画像タイプをSVGとして設定
    img.file_type = ap.ImageFileType.SVG
    # ソースファイルのパス
    img.file = DIR_INPUT_TABLE + "SVGToPDF.svg"
    # 画像インスタンスの幅を設定
    img.fix_width = 50
    # 画像インスタンスの高さを設定
    img.fix_height = 50
    # テーブルインスタンスを作成
    table = ap.Table()
    # テーブルセルの幅を設定
    table.column_widths = "100 100"
    # 行オブジェクトを作成し、テーブルインスタンスに追加
    row = table.rows.add()
    # セルオブジェクトを作成し、行インスタンスに追加
    cell = row.cells.add()
    # セルオブジェクトの段落コレクションにTextFragmentを追加
    cell.paragraphs.add(ap.text.TextFragment("First cell"))
    # 別のセルを行オブジェクトに追加
    cell = row.cells.add()
    # 最近追加したセルインスタンスの段落コレクションにSVG画像を追加
    cell.paragraphs.add(img)
    # ページオブジェクトを作成し、ドキュメントインスタンスのページコレクションに追加
    page = doc.pages.add()
    # ページオブジェクトの段落コレクションにテーブルを追加
    page.paragraphs.add(table)
    # PDFファイルを保存
    doc.save(output_file)
```

## 行の間にページ区切りを挿入する

デフォルトでは、PDFファイル内でテーブルを作成すると、テーブルが下部の余白を超える場合、複数のページにわたって展開されます。しかし、特定の行数がテーブルに追加された後にページ区切りを強制する必要がある状況もあります。以下のコード抜粋は、テーブルに10行が含まれたときにページ区切りを挿入するプロセスを示しています。

```python

    import aspose.pdf as ap

    # Documentインスタンスを作成
    doc = ap.Document()
    # PDFファイルのページコレクションにページを追加
    doc.pages.add()
    # テーブルインスタンスを作成
    tab = ap.Table()
    # テーブルの境界スタイルを設定
    tab.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)
    # 境界色を赤としてデフォルトの境界スタイルを設定
    tab.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)
    # テーブルの列幅を指定
    tab.column_widths = "100 100"
    # テーブルに200行追加するループを作成
    for counter in range(0, 201):
        row = ap.Row()
        tab.rows.add(row)
        cell1 = ap.Cell()
        cell1.paragraphs.add(ap.text.TextFragment("Cell " + str(counter) + ", 0"))
        row.cells.add(cell1)
        cell2 = ap.Cell()
        cell2.paragraphs.add(ap.text.TextFragment("Cell " + str(counter) + ", 1"))
        row.cells.add(cell2)
        # 10行が追加されると、新しい行を新しいページにレンダリング
        if counter % 10 == 0 and counter != 0:
            row.is_in_new_page = True
    # PDFファイルの段落コレクションにテーブルを追加
    doc.pages[1].paragraphs.add(tab)
    # PDFドキュメントを保存
    doc.save(output_file)
```


## 新しいページにテーブルをレンダリングする

デフォルトでは、段落はページオブジェクトのParagraphsコレクションに追加されます。しかし、ページ上で前に追加された段落レベルのオブジェクトの直後ではなく、新しいページにテーブルをレンダリングすることが可能です。

### サンプル: Pythonを使用して新しいページにテーブルをレンダリングする方法

新しいページにテーブルをレンダリングするには、[BaseParagraph](https://reference.aspose.com/pdf/python-net/aspose.pdf/baseparagraph/)クラスの[is_in_new_page](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties)プロパティを使用します。以下のコードスニペットがその方法を示しています。

```python

    import aspose.pdf as ap

    doc = ap.Document()
    page_info = doc.page_info
    margin_info = page_info.margin

    margin_info.left = 37
    margin_info.right = 37
    margin_info.top = 37
    margin_info.bottom = 37

    page_info.is_landscape = True

    table = ap.Table()
    table.column_widths = "50 100"
    # ページを追加。
    cur_page = doc.pages.add()
    for i in range(1, 121):
        row = table.rows.add()
        row.fixed_row_height = 15
        cell1 = row.cells.add()
        cell1.paragraphs.add(ap.text.TextFragment("Content 1"))
        cell2 = row.cells.add()
        cell2.paragraphs.add(ap.text.TextFragment("HHHHH"))
    paragraphs = cur_page.paragraphs
    paragraphs.add(table)

    table1 = ap.Table()
    table1.column_widths = "100 100"
    for i in range(1, 11):
        row = table1.rows.add()
        cell1 = row.cells.add()
        cell1.paragraphs.add(ap.text.TextFragment("LAAAAAAA"))
        cell2 = row.cells.add()
        cell2.paragraphs.add(ap.text.TextFragment("LAAGGGGGG"))
    table1.is_in_new_page = True
    # テーブル1を次のページに保持したい...
    paragraphs.add(table1)
    doc.save(output_file)
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Python経由で.NET用のPDF操作ライブラリ",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>