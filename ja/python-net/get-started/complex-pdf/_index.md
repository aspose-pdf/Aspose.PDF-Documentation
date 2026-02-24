---
title: 複雑な PDF の作成
linktitle: 複雑な PDF の作成
type: docs
weight: 30
url: /ja/python-net/complex-pdf-example/
description: Aspose.PDF for Python via .NET を使用すると、画像、テキスト フラグメント、テーブルを 1 つのドキュメントに含む、より複雑な文書を作成できます。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して複雑な PDF を作成する
Abstract: 本記事では、"Hello, World" の例で示された基本的な PDF 作成プロセスを拡張し、Python と Aspose.PDF を使用して、より複雑な PDF ドキュメントを作成する方法を解説します。例として使用するドキュメントは、架空の旅客フェリー会社向けに作成されており、画像、2 つのテキスト フラグメント（ヘッダーと段落）、およびテーブルが含まれています。プロセスは複数の手順で構成されます - 空の PDF を作成するために `Document` オブジェクトをインスタンス化し、`Page` を追加し、ページに `Image` を挿入します。ヘッダー用に Arial フォント、24pt、中央揃えで `TextFragment` を作成し、ページの段落に追加します。説明用には Times New Roman フォント、14pt、左揃えで 2 番目の `TextFragment` を追加します。その後、特定の列幅、枠線、パディングを設定してテーブルを作成・書式設定します。テーブルにはハイライトされたセルを持つヘッダー行と、反復処理によって生成される複数のデータ行が含まれます
---

この[Hello, World](/pdf/python-net/hello-world-example/) の例では、Python と Aspose.PDF を使用して PDF ドキュメントを作成するシンプルな手順を示しました。本記事では、Aspose.PDF for Python を使って、より複雑なドキュメントを作成する方法を見ていきます。例として、旅客フェリーサービスを提供する架空の企業のドキュメントを使用します。当ドキュメントには画像、2 つのテキスト フラグメント（ヘッダーと段落）、およびテーブルが含まれます。

最初からドキュメントを作成する場合、いくつかの手順に従う必要があります。

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) オブジェクトをインスタンス化します。この手順では、メタデータのみを持ちページのない空の PDF ドキュメントを作成します。
1. ドキュメントオブジェクトに[Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) を追加します。これでドキュメントに 1 ページができます。
1. ページに[Image](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/) を追加します。
1. ヘッダー用に[TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) を作成します。ヘッダーには Arial フォント、24pt、中央揃えを使用します。
1. ヘッダーをページの[paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) に追加します。
1. 説明用に[TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) を作成します。説明には Arial フォント、24pt、中央揃えを使用します。
1. (description) をページの段落に追加します。
1. テーブルを作成し、スタイル設定します。列幅、枠線、パディング、フォントを設定します。
1. (table) をページの[paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) に追加します。
1. ドキュメント "Complex.pdf" を保存します。

```python

from datetime import timedelta
import aspose.pdf as ap

def run_complex(self):

    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()

    # Add image
    imageFileName = self.data_dir + "logo.png"
    page.add_image(imageFileName, ap.Rectangle(20, 730, 120, 830, True))

    # Add Header
    header = ap.text.TextFragment("New ferry routes in Fall 2029")
    header.text_state.font = ap.text.FontRepository.find_font("Arial")
    header.text_state.font_size = 24
    header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    header.position = ap.text.Position(130, 720)
    page.paragraphs.add(header)

    # Add description
    descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. \
    Ferry service is operating at half capacity and on a reduced schedule. Expect lineups."
    description = ap.text.TextFragment(descriptionText)
    description.text_state.font = ap.text.FontRepository.find_font(
        "Times New Roman"
    )
    description.text_state.font_size = 14
    description.horizontal_alignment = ap.HorizontalAlignment.LEFT
    page.paragraphs.add(description)

    # Add table
    table = ap.Table()

    table.column_widths = "200"
    table.border = ap.BorderInfo(
        ap.BorderSide.BOX, 1.0, ap.Color.dark_slate_gray
    )
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.BOX, 0.5, ap.Color.black
    )
    table.default_cell_padding = ap.MarginInfo(4.5, 4.5, 4.5, 4.5)
    table.margin.bottom = 10
    table.default_cell_text_state.font = ap.text.FontRepository.find_font(
        "Helvetica"
    )

    headerRow = table.rows.add()
    headerRow.cells.add("Departs City")
    headerRow.cells.add("Departs Island")

    i = 0
    while i < headerRow.cells.count:
        headerRow.cells[i].background_color = ap.Color.gray
        headerRow.cells[i].default_cell_text_state.foreground_color = (
            ap.Color.white_smoke
        )
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

    document.save(self.data_dir + "Complex.pdf")
```

