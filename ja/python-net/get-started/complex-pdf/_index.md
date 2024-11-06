---
title: 複雑なPDFの作成
linktitle: 複雑なPDFの作成
type: docs
weight: 30
url: ja/python-net/complex-pdf-example/
description: Aspose.PDF for Python via .NETを使用すると、画像、テキスト断片、およびテーブルを1つのドキュメントに含むより複雑なドキュメントを作成できます。
lastmod: "2022-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

[Hello, World](/pdf/python-net/hello-world-example/)の例では、PythonとAspose.PDFを使用してPDFドキュメントを作成する簡単な手順を示しました。この記事では、Aspose.PDF for Pythonを使用してより複雑なドキュメントを作成する方法を見ていきます。例として、旅客フェリーサービスを運営する架空の会社のドキュメントを取り上げます。このドキュメントには、画像、2つのテキスト断片（ヘッダーと段落）、およびテーブルが含まれます。

最初からドキュメントを作成する場合、特定の手順に従う必要があります：

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) オブジェクトをインスタンス化します。このステップでは、メタデータを含むがページのない空のPDFドキュメントを作成します。
1. ドキュメントオブジェクトに[Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)を追加します。これで、ドキュメントには1ページが含まれます。
1. ページに[Image](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/)を追加します。
1. ヘッダー用に[TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/)を作成します。ヘッダーには、フォントサイズ24ptのArialフォントを使用し、中央揃えにします。
1. ヘッダーをページの[paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties)に追加します。
1. 説明用に[TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/)を作成します。説明には、フォントサイズ24ptのArialフォントを使用し、中央揃えにします。
1. (説明)をページのParagraphsに追加します。
1. テーブルを作成し、テーブルプロパティを追加します。

1. ページに(テーブル)を追加する [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties).
1. ドキュメントを保存する "Complex.pdf".

```python

    import aspose.pdf as ap

    # ドキュメントオブジェクトを初期化
    document = ap.Document()
    # ページを追加
    page = document.pages.add()

    # 画像を追加
    page.add_image(image_file, ap.Rectangle(20, 730, 120, 830, True))

    # ヘッダーを追加
    header = ap.text.TextFragment("2020年秋の新しいフェリー航路")
    header.text_state.font = ap.text.FontRepository.find_font("Arial")
    header.text_state.font_size = 24
    header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    header.position = ap.text.Position(130, 720)
    page.paragraphs.add(header)

    # 説明を追加
    descriptionText = "訪問者はオンラインでチケットを購入する必要があり、チケットは1日5,000枚に制限されています。 \
    フェリーサービスは半分の容量で運行され、スケジュールは短縮されています。列ができることがあります。"
    description = ap.text.TextFragment(descriptionText)
    description.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    description.text_state.font_size = 14
    description.horizontal_alignment = ap.HorizontalAlignment.LEFT
    page.paragraphs.add(description)

    # テーブルを追加
    table = ap.Table()

    table.column_widths = "200"
    table.border = ap.BorderInfo(ap.BorderSide.BOX, 1.0, ap.Color.dark_slate_gray)
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.BOX, 0.5, ap.Color.black)
    table.default_cell_padding = ap.MarginInfo(4.5, 4.5, 4.5, 4.5)
    table.margin.bottom = 10
    table.default_cell_text_state.font = ap.text.FontRepository.find_font("Helvetica")

    headerRow = table.rows.add()
    headerRow.cells.add("出発都市")
    headerRow.cells.add("出発島")

    i = 0
    while i < headerRow.cells.count:
        headerRow.cells[i].background_color = ap.Color.gray
        headerRow.cells[i].default_cell_text_state.foreground_color = ap.Color.white_smoke
        i += 1

    time = timedelta(hours=6, minutes=0)
    incTime = timedelta(hours=0, minutes=30)

    i = 0
    while i < 10:
        dataRow = table.rows.add()
        dataRow.cells.add(str(time))
        time = time.__add__(incTime)
        dataRow.cells.add(str(time))
        i += 1

    page.paragraphs.add(table)

    document.save(output_pdf)
```