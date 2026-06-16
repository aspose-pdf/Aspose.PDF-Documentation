---
title: 複雑な PDF の作成
linktitle: 複雑な PDF の作成
type: docs
weight: 30
url: /ja/python-net/complex-pdf-example/
description: .NET 経由の Aspose.PDF for Python では、画像、テキストフラグメント、およびテーブルを 1 つのドキュメントに含む、より複雑なドキュメントを作成できます。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して複雑な PDF を作成する
Abstract: この記事では、「Hello, World」の例で示した基本的な PDF 作成プロセスを拡張し、Python と Aspose.PDF を使用してより複雑な PDF ドキュメントを作成する方法を示します。このサンプル文書は、架空の旅客フェリーサービス会社向けに作成されたもので、画像、2 つのテキストフラグメント (ヘッダーと段落)、および表が含まれています。このプロセスにはいくつかのステップがあります。たとえば、「Document」オブジェクトをインスタンス化して空の PDF を作成し、「Page」を追加し、ページに「Image」を挿入します。ヘッダー用の「TextFragment」は、サイズが 24pt で中央揃えの Arial フォントを使用して作成され、ページの段落に追加されます。説明用に 2 つ目の「TextFragment」が追加されました。サイズが 14 ポイントで、左揃えの Times New Roman フォントが使用されています。その後、テーブルが作成され、特定の列幅、境界線、パディングでフォーマットされます。テーブルには、強調表示されたセルを含むヘッダー行と、反復処理によって生成された複数のデータ行が含まれます。
---

ザの [ハロー・ワールド](/pdf/ja/python-net/hello-world-example/) 例では、Python と Aspose.PDF を使用して PDF ドキュメントを作成する簡単な手順を示しました。この記事では、Aspose.PDF for Python を使用してさらに複雑なドキュメントを作成する方法を見ていきます。例として、旅客フェリーサービスを運営する架空の会社の文書を取り上げます。この文書には、画像 1 つ、テキストフラグメント 2 つ (ヘッダーと段落)、1 つの表が含まれます。

ドキュメントを最初から作成する場合、特定の手順に従う必要があります。

1. をインスタンス化する [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 対象。このステップでは、メタデータはあるがページは含まない空の PDF ドキュメントを作成します。
1. を追加 [ページ](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 文書オブジェクトへ。これで、文書は 1 ページになります。
1. を追加 [[イメージ]](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/) ページへ。
1. を作成 [テキストフラグメント](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) ヘッダー用。ヘッダーには、フォントサイズが24ptで中央揃えのArialフォントを使用します。
1. ページへのヘッダーの追加 [段落](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties).
1. を作成 [テキストフラグメント](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) 説明用。説明には、フォントサイズが24ptで中央揃えのArialフォントを使用します。
1. 「段落」ページに説明を追加します。
1. テーブルの作成とスタイル設定列の幅、境界線、パディング、フォントを設定します。
1. ページへの表の追加 [段落](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties).
1. ドキュメント「Complex.pdf」を保存します。

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
    description.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    description.text_state.font_size = 14
    description.horizontal_alignment = ap.HorizontalAlignment.LEFT
    page.paragraphs.add(description)

    # Add table
    table = ap.Table()

    table.column_widths = "200"
    table.border = ap.BorderInfo(ap.BorderSide.BOX, 1.0, ap.Color.dark_slate_gray)
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.BOX, 0.5, ap.Color.black)
    table.default_cell_padding = ap.MarginInfo(4.5, 4.5, 4.5, 4.5)
    table.margin.bottom = 10
    table.default_cell_text_state.font = ap.text.FontRepository.find_font("Helvetica")

    headerRow = table.rows.add()
    headerRow.cells.add("Departs City")
    headerRow.cells.add("Departs Island")

    i = 0
    while i < headerRow.cells.count:
        headerRow.cells[i].background_color = ap.Color.gray
        headerRow.cells[
            i
        ].default_cell_text_state.foreground_color = ap.Color.white_smoke
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
