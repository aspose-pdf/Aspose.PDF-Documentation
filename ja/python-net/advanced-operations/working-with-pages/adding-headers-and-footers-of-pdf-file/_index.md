---
title: Python での PDF ヘッダーとフッターの追加
linktitle: PDF へのヘッダーとフッターの追加
type: docs
weight: 50
url: /ja/python-net/add-headers-and-footers-of-pdf-file/
description: テキスト、画像、構造化コンテンツを使用して Python で PDF ファイルにヘッダーとフッターを追加する方法を学びます。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python で PDF ファイルにヘッダーとフッターを追加する
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメントにヘッダーとフッターを追加する方法を説明します。テキスト、ページ番号、HTML、画像、表、LaTeX ベースのヘッダーとフッターのコンテンツについて説明します。
---

このページを使用して、**.NET 経由の Python 用 Aspose.PDF ** を使用して PDF ページ全体に一貫したヘッダーとフッターのコンテンツを追加できます。

ヘッダーとフッターは次の方法で作成できます [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/), [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/), [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/), [`Image`](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/)、および [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) オブジェクトを経由して適用する [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) 各ページに。

## ヘッダーとフッターをテキストフラグメントとして追加

PDF のすべてのページにシンプルなテキストヘッダーとフッターを追加します。これにより、次のようになります。 [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) オブジェクト、インサート [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/) それらに含まれる要素、セット [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) 適切な位置に配置し、ドキュメントの各ページに添付します。その結果、すべてのページに一貫したヘッダーとフッターのテキストが表示される PDF が作成されます。

次のコードスニペットは、Python を使用してヘッダーとフッターをテキストフラグメントとして PDF に追加する方法を示しています。

1. ヘッダーとフッターのテキストフラグメントを作成します。
1. HeaderFooter オブジェクトを作成し、それらにテキストフラグメントを追加します。
1. 余白設定を定義して、ヘッダーとフッターの配置を制御します。
1. 入力ファイルから PDF ドキュメントをロードします。
1. 文書内のすべてのページを繰り返し処理します。
1. ヘッダーとフッターを各ページに割り当てます。
1. 変更した PDF を出力ファイルに保存します。

```python
import aspose.pdf as ap

def add_header_and_footer_as_text(input_file, output_file):
    # Create header text
    header_text = ap.text.TextFragment("Demo header")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_text)

    # Create footer text
    footer_text = ap.text.TextFragment("Demo footer")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_text)

    # Set header margin
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20
    header.margin = margin

    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

この方法は、各ページの上部と下部に一貫したタイトル、ページインジケーター、または法的免責事項を追加する場合に便利です。また、画像やページ番号などの動的コンテンツを含めるように拡張することもできます。

## ページ番号付け用のヘッダーとフッターの追加

Aspose.PDF for Python を使用して PDF ドキュメントのヘッダーとフッターに自動ページ番号を追加します。このスクリプトは、組み込み変数 $p (現在のページ番号) と $P (合計ページ数) を使用して、すべてのページにページ番号を動的に挿入します。ヘッダーは「Y ページから Y ページ」という形式で、フッターには「X/Y ページ」という形式が表示されます。は [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) 各ページに正しく配置されるようにします。

1. 「Page $p from $P」を使用してヘッダー用のテキストフラグメントを作成し、現在のページと合計ページ数を表示します。
1. HeaderFooter オブジェクトを作成し、それにヘッダーテキストを追加します。
1. 別の番号付けスタイルとして「Page $p/$P」を使用してフッター用のテキストフラグメントを作成します。
1. Footer オブジェクトを作成し、フッターテキストを追加します。
1. 余白設定 (左 = 50、上 = 20) を定義し、ヘッダーとフッターの両方に適用します。
1. 入力ファイルから PDF ドキュメントを開きます。
1. すべてのページをループ処理し、各ページにヘッダーとフッターを割り当てます。
1. 更新した PDF を出力パスに保存します。

```python
import aspose.pdf as ap

def using_header_and_footer_for_page_numbering(input_file, output_file):
    # Create header text
    header_text = ap.text.TextFragment("Page $p from $P")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_text)

    # Create footer text
    footer_text = ap.text.TextFragment("Page $p / $P")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_text)

    # Create margins
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20

    # Set header margin
    header.margin = margin
    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## ヘッダーとフッターを HTML フラグメントとして追加

Aspose.PDF for Python を使用して、HTML 形式のヘッダーとフッターを PDF ドキュメントのすべてのページに適用します。を使用して [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/)このスクリプトでは、太字や斜体などのリッチテキストスタイルをヘッダーとフッターに表示できます。 [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) が適切に配置されるように適用され、同じ形式の要素が文書内の各ページに添付されます。

次のコードスニペットは、Python を使用してヘッダーとフッターを HTML フラグメントとして PDF に追加する方法を示しています。

1. HTMLFragment を使用して、'などのスタイル付きテキストを含む HTML ヘッダースニペットを作成します。<strong>'は太字を表します。
1. HeaderFooter オブジェクトを作成し、それに HTML ヘッダーを追加します。
1. 'を使用して HTML フッタースニペットを作成する<i>'は斜体スタイルに適しています。
1. フッターオブジェクトを作成し、それにフッター HTML を追加します。
1. 余白 (左 = 50、上 = 20) を設定し、ヘッダーとフッターの両方に割り当てます。
1. 「AP.Document ()」を使用して PDF ドキュメントをロードします。
1. すべてのページをループ処理し、それぞれにヘッダーとフッターを割り当てます。
1. 変更した PDF を指定した出力パスに保存します。

```python
import aspose.pdf as ap

def add_header_and_footer_as_html(input_file, output_file):
    # Create header HTML
    header_html = ap.HtmlFragment("This is an HTML <strong>Header</strong>")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_html)

    # Create footer HTML
    footer_html = ap.HtmlFragment("Powered by <i>Aspose.PDF</i>")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_html)

    # Set header margin
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20
    header.margin = margin

    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

HTMLFragment を使用すると、インラインスタイルや HTML マークアップによるリッチフォーマットが可能になり、プレーンテキストよりも柔軟なデザインが可能になります。

## ヘッダーとフッターを画像として追加

Aspose.PDF for Python を使用して、PDF ドキュメントの各ページに画像ベースのヘッダーとフッターを追加します。すべてのページのヘッダーとフッターに同じ画像ファイルが使用されます。 [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) 画像を配置すると、画像はヘッダー/フッター領域に収まるように自動的に調整されます。

次のコードスニペットは、Python を使用してヘッダーとフッターを画像として PDF に追加する方法を示しています。

1. 画像を 'AP.Image' オブジェクトに読み込み、ヘッダーとして使用できるように準備します。
1. HeaderFooter オブジェクトを作成し、そのオブジェクトにヘッダー画像を添付します。
1. 同じ画像を再度読み込んで、フッターとして使用します。
1. フッターオブジェクトを作成し、それにフッター画像を追加します。
1. 'AP.Document () 'を使用して入力 PDF ドキュメントをロードします。
1. 文書のすべてのページを繰り返し処理します。
1. ヘッダーとフッターの両方の位置にマージン (左 = 50) を適用します。
1. PDF の各ページにヘッダーとフッターを割り当てます。
1. 更新した PDF を指定した出力ファイルに保存します。

この手法は、ヘッダー/フッター領域にロゴやウォーターマークがあるブランディング文書に最適です。

```python
import aspose.pdf as ap

def add_header_and_footer_as_image(input_file, image_file, output_file):
    # Create header image
    header_image = ap.Image()
    header_image.file = image_file
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_image)

    # Create footer image
    footer_image = ap.Image()
    footer_image.file = image_file

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_image)

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Set header margin
            margin = ap.MarginInfo()
            margin.left = 50
            header.margin = margin

            # Set footer margin
            footer.margin = margin

            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## ヘッダーとフッターをテーブルとして追加

Aspose.PDF for Python を使用して、構造化されたテーブルベースのヘッダーとフッターを PDF 文書のすべてのページに追加します。 [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) オブジェクトを使用すると、複雑なヘッダーやフッターのレイアウト制御、配置、一貫した書式設定がしやすくなります。ヘッダーテキストは中央に配置され、フッターテキストは左揃えで、どちらも Arial 12pt フォントを使用しています。列幅はページサイズに基づいて動的に計算され、正しく配置されます。

このコードスニペットは、.NET 経由の Aspose.PDF for Python を使用して PDF ドキュメントの各ページにヘッダーとフッター (テーブルを使用) を追加します。

1. を使用してテキストスタイルを定義します [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) ヘッダーとフッター (フォント、サイズ、配置) 用。
1. 作成 [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) ヘッダーとフッターのオブジェクト。
1. ヘッダーを作成 [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) 行が 1 つと、ヘッダーテキストを含むセルが 1 つあります。
1. フッターを作成 [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) 1 行と 1 つのセルにフッターテキストが含まれます。
1. 対応するテーブルにテーブルを追加します [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) オブジェクト。
1. フッターを設定 [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) 適切な水平位置に配置するため。
1. を開きます [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 適切な方法を使用する。
1. すべてのページを繰り返し処理し、テーブルベースのヘッダーとフッターを各ページに割り当てます。
1. 変更を保存する [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 出力ファイルへ。

```python
import aspose.pdf as ap

def add_header_and_footer_as_table(input_file, output_file):
    text_state_header = ap.text.TextState()
    text_state_header.font = ap.text.FontRepository.find_font("Arial")
    text_state_header.font_size = 12
    text_state_header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    text_state_footer = ap.text.TextState()
    text_state_footer.font = ap.text.FontRepository.find_font("Arial")
    text_state_footer.font_size = 12
    text_state_footer.horizontal_alignment = ap.HorizontalAlignment.LEFT
    # Create header
    header = ap.HeaderFooter()
    # Create footer
    footer = ap.HeaderFooter()
    # Create header Table
    table_header = ap.Table()
    table_header.column_widths = str(594 - header.margin.left - header.margin.right)
    header_row = table_header.rows.add()
    header_row.cells.add("This is a Table Header", text_state_header)
    # Create footer Table
    table = ap.Table()
    table.column_widths = str(594 - footer.margin.left - footer.margin.right)
    table.rows.add().cells.add("Powered by Aspose.PDF", text_state_footer)
    header.paragraphs.add(table_header)
    footer.paragraphs.add(table)
    # Set footer margin
    footer.margin.left = 150

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## ヘッダーとフッターを LaTeX として追加

Aspose.PDF for Python を使用して、LaTeX 形式のコンテンツを含むヘッダーとフッターを PDF ドキュメントのすべてのページに追加します。LaTeX では、数学記号、日付、著作権マーク、その他の高度なフォーマットをレンダリングできます。ヘッダーには動的な日付が含まれ、フッターには現在のページ番号と総ページ数とともに著作権記号が表示されます。

次のコードスニペットは使用方法を示しています [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) .NET 経由で Aspose.PDF for Python を使用して PDF のヘッダーとフッターに配置します。

1. を開きます [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 適切な方法を使用する。
1. 動的フッターに使用する合計ページ数を決定します。
1. 文書のすべてのページを繰り返し処理します。
1. を作成 [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) ヘッダーのオブジェクト。
1. を作成 [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) LaTeX コマンドを含むヘッダーテキスト用 (例: `\\today\\`).
1. を作成 [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) フッターのオブジェクト。
1. を作成 [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) LaTeX シンボルとページ番号を含むフッターテキスト用。
1. を追加 [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) 対応するヘッダー/フッターオブジェクトに移動します。
1. ヘッダーとフッターを現在のページにバインドします。
1. 変更を保存する [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 出力ファイルへ。

```python
import aspose.pdf as ap

def add_header_and_footer_as_latex(input_file, output_file):
    # Open PDF document
    with ap.Document(input_file) as document:
        page_count = len(document.pages)
        for i in range(1, page_count + 1):
            # Create header
            header = ap.HeaderFooter()
            h_latex_text = "This is a LaTeX Header. \\today\\"
            h_l_text = ap.TeXFragment(h_latex_text, True)
            # Create footer
            footer = ap.HeaderFooter()
            f_latex_text = (
                f"\\copyright\\ 2025 My Company -- Page \\thepage\\ is {page_count}"
            )
            f_l_text = ap.TeXFragment(f_latex_text, True)

            header.paragraphs.add(h_l_text)
            footer.paragraphs.add(f_l_text)
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## 関連ページトピック

- [Python で PDF ページを操作する](/pdf/ja/python-net/working-with-pages/)
- [Python で PDF にページ番号を追加する方法](/pdf/ja/python-net/add-page-number/)
- [Python で PDF ページにスタンプを付ける](/pdf/ja/python-net/stamping/)
- [Python で PDF ドキュメントをフォーマットする](/pdf/ja/python-net/formatting-pdf-document/)