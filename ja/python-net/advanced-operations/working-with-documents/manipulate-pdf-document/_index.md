---
title: Python で PDF ドキュメントを操作する方法
linktitle: PDF ドキュメントを操作
type: docs
weight: 20
url: /ja/python-net/manipulate-pdf-document/
description: 目次管理や PDF/A チェックを含む、Python で PDF ドキュメントを検証、構造化、変更する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用した PDF ドキュメントの操作に関するガイド
Abstract: この記事では、Python、特に Aspose.PDF ライブラリを使用して PDF 文書を操作するための包括的なガイドを提供します。このガイドでは、「Document」クラスの「validate」メソッドを使用して PDF ドキュメントが PDF/A-1a および PDF/A-1b に準拠しているかどうかを検証するなど、いくつかの機能について説明しています。また、さまざまな TabLeader タイプの設定、ページ番号の非表示、プレフィックス付きのページ番号のカスタマイズなど、PDF ファイルの目次 (TOC) を追加、カスタマイズ、および管理する方法についても詳しく説明します。さらに、アクセス制限用に JavaScript を埋め込んで PDF ドキュメントに有効期限を設定する方法と、PDF 内の入力可能なフォームをフラット化して編集できないようにする方法についても説明しています。各セクションには、Python で Aspose.PDF を使用してこれらの機能を実装する方法を示すコードスニペットが付属しています。
---

このページは、PDF の準拠性を検証したり、目次を作成またはカスタマイズしたり、文書の有効期限の動作を設定したり、Python ワークフローで入力可能な PDF をフラット化したりする必要がある場合に役立ちます。

## Python で PDF ドキュメントを操作する方法

## PDF ドキュメントが PDF A 規格 (A 1A および A 1B) に適合しているかどうかを検証します

PDF ドキュメントの PDF/A-1a または PDF/A-1b との互換性を検証するには、以下を使用してください。 [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラス [検証します](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法。このメソッドでは、結果を保存するファイルの名前と、必要な検証タイプ PDFFormat 列挙型 (PDF_A_1A または PDF_A_1B) を指定できます。

次のコードスニペットは、PDF ドキュメントの PDF/A-1A を検証する方法を示しています。

```python
import sys
from os import path
import aspose.pdf as ap


def validate_pdfa_standard_a1a(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.validate(output_pdf, ap.PdfFormat.PDF_A_1A)
```

次のコードスニペットは、PDF ドキュメントの PDF/A-1b を検証する方法を示しています。

```python
import sys
from os import path
import aspose.pdf as ap


def validate_pdfa_standard_a1b(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.validate(output_pdf, ap.PdfFormat.PDF_A_1B)
```

## 目次での作業

### 目次を既存の PDF に追加

PDFの目次は「目次」の略です。これは、セクションや見出しの概要を表示することで、ユーザーが文書内をすばやく移動できるようにする機能です。 

既存の PDF ファイルに目次を追加するには、の Heading クラスを使用します。 [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) 名前空間。ザブ [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) 名前空間は、新しい PDF ファイルの作成と既存の PDF ファイルの操作の両方が可能です。既存の PDF に目次を追加するには、Aspose.Pdf 名前空間を使用してください。次のコードスニペットは、.NET 経由で Python を使用して既存の PDF ファイル内に目次を作成する方法を示しています。

```python
import sys
from os import path
import aspose.pdf as ap


def add_table_of_contents(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.insert(1)
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    toc_page.toc_info = toc_info

    titles = ["First page", "Second page"]
    for index, title_text in enumerate(titles[:2]):
        heading = ap.Heading(1)
        segment = ap.text.TextSegment(title_text)
        heading.toc_page = toc_page
        heading.segments.append(segment)
        destination_page = document.pages[index + 2]
        heading.destination_page = destination_page
        heading.top = destination_page.rect.height
        toc_page.paragraphs.add(heading)

    document.save(output_pdf)
```

### 目次レベルごとに異なるタブリーダータイプを設定

Aspose.PDF for Python では、目次レベルごとに異なるタブリーダータイプを設定することもできます。以下を設定する必要があります。 [ラインダッシュ](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) のプロパティ [目次情報](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/).

```python
import sys
from os import path
import aspose.pdf as ap


def set_toc_levels(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.add()
    toc_info = ap.TocInfo()
    toc_info.line_dash = ap.text.TabLeaderType.SOLID
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 30
    toc_info.title = title
    toc_page.toc_info = toc_info

    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.left = 0
    toc_info.format_array[0].margin.right = 30
    toc_info.format_array[0].line_dash = ap.text.TabLeaderType.DOT
    toc_info.format_array[0].text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    toc_info.format_array[1].margin.left = 10
    toc_info.format_array[1].margin.right = 30
    toc_info.format_array[1].line_dash = 3
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].margin.left = 20
    toc_info.format_array[2].margin.right = 30
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].line_dash = ap.text.TabLeaderType.SOLID
    toc_info.format_array[3].margin.left = 30
    toc_info.format_array[3].margin.right = 30
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD

    page = document.pages.add()
    for level in range(1, 5):
        heading = ap.Heading(level)
        heading.is_auto_sequence = True
        heading.toc_page = toc_page
        heading.text_state.font = ap.text.FontRepository.find_font("Arial")
        segment = ap.text.TextSegment(f"Sample Heading{level}")
        heading.segments.append(segment)
        heading.is_in_list = True
        page.paragraphs.add(heading)

    document.save(output_pdf)
```

### 目次のページ番号を非表示にする

目次の見出しと一緒にページ番号を表示したくない場合は、次のようにします。 [ページ番号を表示](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) のプロパティ [目次情報](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) クラスは false です。目次のページ番号を非表示にするには、次のコードスニペットを確認してください。

```python
import sys
from os import path
import aspose.pdf as ap


def hide_page_numbers_in_toc(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.add()
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    toc_info.is_show_page_numbers = False
    toc_page.toc_info = toc_info

    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.right = 0
    toc_info.format_array[0].text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    toc_info.format_array[1].margin.left = 30
    toc_info.format_array[1].text_state.underline = True
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD

    page = document.pages.add()
    for level in range(1, 2):
        heading = ap.Heading(level)
        heading.toc_page = toc_page
        heading.is_auto_sequence = True
        heading.is_in_list = True
        segment = ap.text.TextSegment(f"this is heading of level {level}")
        heading.segments.append(segment)
        page.paragraphs.add(heading)

    document.save(output_pdf)
```

### 目次を追加しながらページ番号をカスタマイズ

PDF ドキュメントに目次を追加するときに、目次のページ番号をカスタマイズするのが一般的です。例えば、ページ番号の前に P1、P2、P3 などのプレフィックスを追加する必要がある場合があります。このような場合、Python 用の Aspose.PDF は次のような機能を提供します。 [ページ番号プレフィックス](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) のプロパティ [目次情報](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) 次のコードサンプルに示すように、ページ番号をカスタマイズするために使用できるクラス。

```python
import sys
from os import path
import aspose.pdf as ap


def customize_page_numbers_in_toc(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.insert(1)
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    toc_info.page_numbers_prefix = "P"
    toc_page.toc_info = toc_info

    for index, page in enumerate(document.pages, start=1):
        heading = ap.Heading(1)
        heading.toc_page = toc_page
        heading.destination_page = page
        heading.top = page.rect.height
        segment = ap.text.TextSegment(f"Page {index}")
        heading.segments.append(segment)
        toc_page.paragraphs.add(heading)

    document.save(output_pdf)
```

## PDF の有効期限を設定する方法

特定のユーザーグループがPDFドキュメントの特定の機能/オブジェクトにアクセスできるように、PDFファイルにアクセス権限を適用します。PDF ファイルへのアクセスを制限するために、通常は暗号化を適用しますが、PDF ファイルの有効期限を設定する必要がある場合もあります。これにより、ユーザーがドキュメントにアクセス/閲覧したときに PDF ファイルの有効期限に関する有効なプロンプトが表示されるようになります。

```python
import sys
from os import path
import aspose.pdf as ap


def set_pdf_expiry_date(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.pages.add()
    document.pages[1].paragraphs.add(ap.text.TextFragment("Hello World..."))
    script = ap.annotations.JavascriptAction(
        "var year=2017;"
        "var month=5;"
        "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
        "expiry = new Date(year, month);"
        "if (today.getTime() > expiry.getTime())"
        "app.alert('The file is expired. You need a new one.');"
    )
    document.open_action = script
    document.save(output_pdf)
```

## 入力可能な PDF を Python でフラット化する方法

PDF ドキュメントには、ラジオボタン、チェックボックス、テキストボックス、リストなどのインタラクティブに入力可能なウィジェットを含むフォームが含まれていることがよくあります。さまざまな用途で編集できないようにするには、PDF ファイルをフラット化する必要があります。
Aspose.PDF には、わずか数行のコードで Python で PDF をフラット化するための関数が用意されています。

```python
import sys
from os import path
import aspose.pdf as ap


def flatten_fillable_pdf(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    if document.form and document.form.fields:
        for field in document.form.fields:
            field.flatten()
    document.save(output_pdf)
```

## 関連ドキュメントトピック

- [Python で PDF ドキュメントを操作する](/pdf/ja/python-net/working-with-documents/)
- [Python で PDF ドキュメントをフォーマットする](/pdf/ja/python-net/formatting-pdf-document/)
- [Python で PDF ファイルを作成](/pdf/ja/python-net/create-pdf-document/)
- [Python で PDF ファイルを最適化する方法](/pdf/ja/python-net/optimize-pdf/)
