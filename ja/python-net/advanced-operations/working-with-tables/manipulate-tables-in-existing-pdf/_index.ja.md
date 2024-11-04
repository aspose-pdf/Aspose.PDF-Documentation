---
title: 既存のPDF内のテーブルを操作する
linktitle: テーブルの操作
type: docs
weight: 40
url: /python-net/manipulate-tables-in-existing-pdf/
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "既存のPDF内のテーブルを操作する",
    "alternativeHeadline": "既存のPDF内のテーブル内容を更新する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdfドキュメント生成",
    "keywords": "pdf, python, テーブル操作",
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
    "url": "/python-net/manipulate-tables-in-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/manipulate-tables-in-existing-pdf/"
    },
    "dateModified": "2023-02-04",
    "description": ""
}
</script>


## 既存のPDFでテーブルを操作する

Aspose.PDF for Python via .NETで最も初期にサポートされた機能の一つがテーブルの操作であり、ゼロから生成されたPDFファイルや既存のPDFファイルにテーブルを追加するための優れたサポートを提供しています。この新しいリリースでは、PDFドキュメントのページに既に存在するシンプルなテーブルを検索および解析する新機能を実装しました。[TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/)という新しいクラスがこれらの機能を提供します。TableAbsorberの使用法は既存の[TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/)クラスと非常に似ています。以下のコードスニペットは、特定のテーブルセルの内容を更新する手順を示しています。

```python

    import aspose.pdf as ap

    # 既存のPDFファイルを読み込む
    pdf_document = ap.Document(input_file)
    # テーブルを見つけるためのTableAbsorberオブジェクトを作成する
    absorber = ap.text.TableAbsorber()
    # 最初のページをアブソーバーで訪問する
    absorber.visit(pdf_document.pages[1])
    # ページ上の最初のテーブル、その最初のセル、およびその中のテキストフラグメントにアクセスする
    fragment = absorber.table_list[0].row_list[0].cell_list[0].text_fragments[1]
    # セル内の最初のテキストフラグメントのテキストを変更する
    fragment.text = "hi world"
    pdf_document.save(output_file)
```


## PDFドキュメント内の古いテーブルを新しいものに置き換える

特定のテーブルを見つけて希望のテーブルに置き換える必要がある場合は、[TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/)クラスの[replace()](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods)メソッドを使用してそれを行うことができます。以下の例は、PDFドキュメント内のテーブルを置き換える機能を示しています:

```python

    import aspose.pdf as ap

    # 既存のPDFドキュメントをロード
    pdf_document = ap.Document(input_file)
    # テーブルを見つけるためのTableAbsorberオブジェクトを作成
    absorber = ap.text.TableAbsorber()
    # 最初のページをアブソーバーで訪問
    absorber.visit(pdf_document.pages[1])
    # ページ上の最初のテーブルを取得
    table = absorber.table_list[0]
    # 新しいテーブルを作成
    new_table = ap.Table()
    new_table.column_widths = "100 100 100"
    new_table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 1)

    row = new_table.rows.add()
    row.cells.add("Col 1")
    row.cells.add("Col 2")
    row.cells.add("Col 3")

    # テーブルを新しいものに置き換える
    absorber.replace(pdf_document.pages[1], table, new_table)
    # ドキュメントを保存
    pdf_document.save(output_file)
```


## 現在のページでテーブルが壊れるかどうかを判断する方法

このコードは、テーブルを含むPDFドキュメントを生成し、ページ上の利用可能なスペースを計算し、テーブルにさらに行を追加することでスペースの制約に基づいてページが壊れるかどうかを確認します。結果は出力ファイルに保存されます。

```python

    import aspose.pdf as ap

    # PDFクラスのオブジェクトをインスタンス化する
    pdf = ap.Document()
    # PDFドキュメントのセクションコレクションにセクションを追加する
    page = pdf.pages.add()
    # テーブルオブジェクトをインスタンス化する
    table1 = ap.Table()
    table1.margin.top = 300
    # 指定したセクションの段落コレクションにテーブルを追加する
    page.paragraphs.add(table1)
    # テーブルの列幅を設定する
    table1.column_widths = "100 100 100"
    # BorderInfoオブジェクトを使用してデフォルトのセル境界線を設定する
    table1.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)
    # 別のカスタマイズされたBorderInfoオブジェクトを使用してテーブル境界線を設定する
    table1.border = ap.BorderInfo(ap.BorderSide.ALL, 1)
    # MarginInfoオブジェクトを作成し、左、下、右、上のマージンを設定する
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5
    # MarginInfoオブジェクトにデフォルトのセル余白を設定する
    table1.default_cell_padding = margin
    # カウンタを17に増やすと、テーブルが壊れます
    # これ以上このページに収容できないためです
    for row_counter in range(0, 17):
        # テーブルに行を作成し、その行にセルを作成する
        row1 = table1.rows.add()
        row1.cells.add("col " + str(row_counter) + ", 1")
        row1.cells.add("col " + str(row_counter) + ", 2")
        row1.cells.add("col " + str(row_counter) + ", 3")
    # ページの高さ情報を取得する
    page_height = pdf.page_info.height
    # ページの上部と下部のマージン、テーブルの上部マージン、テーブルの高さの
    # 合計高さ情報を取得する
    total_objects_height = page.page_info.margin.top + page.page_info.margin.bottom + table1.margin.top + \
                           table1.get_height(None)
    # ページ高さ、テーブル高さ、テーブル上部マージン、ページ上部と
    # 下部マージン情報を表示する
    print("PDFドキュメントの高さ = " + str(pdf.page_info.height) + "\n上部マージン情報 = " + str(page.page_info.margin.top)
          + "\n下部マージン情報 = " + str(page.page_info.margin.bottom) + "\n\nテーブル上部マージン情報 = "
          + str(table1.margin.top) + "\n平均行の高さ = " + str(table1.rows[0].min_row_height) + " \nテーブルの高さ "
          + str(table1.get_height(None)) + "\n ----------------------------------------" + "\n総ページの高さ ="
          + str(page_height) + "\nテーブルを含む累積の高さ =" + str(total_objects_height))
    # ページの上部マージン、ページの下部マージン +
    # テーブルの上部マージンとテーブルの高さの合計をページの高さから引いたときに
    # 10未満であるかどうかを確認する（平均行の高さは10を超える可能性があります）
    if (page_height - total_objects_height) <= 10:
        # 値が10未満の場合、メッセージを表示します。
        # これは、別の行を追加できず、新しい行を追加すると
        # テーブルが壊れることを示します。これは行の高さの値に依存します。
        print("ページの高さ - オブジェクトの高さ < 10 のため、テーブルが壊れます")
    # PDFドキュメントを保存する
    pdf.save(output_file)
```


## テーブルに繰り返し列を追加する

[Aspose.Pdf.Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) クラスでは、テーブルが縦に長すぎて次のページにオーバーフローする場合に行を繰り返す [repeating_rows_count](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) を設定できます。しかし、場合によっては、テーブルが幅広すぎて1ページに収まらず、次のページに続ける必要があります。この目的を達成するために、[Aspose.Pdf.Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) クラスに [repeating_columns_count](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) プロパティを実装しました。このプロパティを設定すると、テーブルは列ごとに次のページに分割され、指定された列数が次のページの先頭で繰り返されます。以下のコードスニペットは、[repeating_columns_count](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) プロパティの使用例を示しています:

```python

    import aspose.pdf as ap

    # 新しいドキュメントを作成
    doc = ap.Document()
    page = doc.pages.add()
    # ページ全体を占める外側のテーブルをインスタンス化
    outer_table = ap.Table()
    outer_table.column_widths = "100%"
    outer_table.horizontal_alignment = ap.HorizontalAlignment.LEFT
    # 同じページ内で分割される外側のテーブル内にネストされるテーブルオブジェクトをインスタンス化
    my_table = ap.Table()
    my_table.broken = ap.TableBroken.VERTICAL_IN_SAME_PAGE
    my_table.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_CONTENT
    # 外側のテーブルをページの段落に追加
    # 外側のテーブルに自分のテーブルを追加
    page.paragraphs.add(outer_table)
    body_row = outer_table.rows.add()
    body_cell = body_row.cells.add()
    body_cell.paragraphs.add(my_table)
    my_table.repeating_columns_count = 5
    page.paragraphs.add(my_table)
    # ヘッダー行を追加
    row = my_table.rows.add()
    row.cells.add("header 1")
    row.cells.add("header 2")
    row.cells.add("header 3")
    row.cells.add("header 4")
    row.cells.add("header 5")
    row.cells.add("header 6")
    row.cells.add("header 7")
    row.cells.add("header 11")
    row.cells.add("header 12")
    row.cells.add("header 13")
    row.cells.add("header 14")
    row.cells.add("header 15")
    row.cells.add("header 16")
    row.cells.add("header 17")
    for row_counter in range(0, 6):
        # テーブル内に行を作成し、その後行内にセルを作成
        row1 = my_table.rows.add()
        row1.cells.add("col " + str(row_counter) + ", 1")
        row1.cells.add("col " + str(row_counter) + ", 2")
        row1.cells.add("col " + str(row_counter) + ", 3")
        row1.cells.add("col " + str(row_counter) + ", 4")
        row1.cells.add("col " + str(row_counter) + ", 5")
        row1.cells.add("col " + str(row_counter) + ", 6")
        row1.cells.add("col " + str(row_counter) + ", 7")
        row1.cells.add("col " + str(row_counter) + ", 11")
        row1.cells.add("col " + str(row_counter) + ", 12")
        row1.cells.add("col " + str(row_counter) + ", 13")
        row1.cells.add("col " + str(row_counter) + ", 14")
        row1.cells.add("col " + str(row_counter) + ", 15")
        row1.cells.add("col " + str(row_counter) + ", 16")
        row1.cells.add("col " + str(row_counter) + ", 17")
    doc.save(output_file)
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "applicationCategory": "PDF操作ライブラリ for Python via .NET",
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