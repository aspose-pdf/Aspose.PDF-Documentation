---
title: PythonでTagged PDFを作成する
linktitle: Tagged PDFを作成する
type: docs
weight: 10
url: /ja/python-net/create-tagged-pdf/
description: Python と Aspose.PDF for Python via .NET を使用して、PDF/UA の構造要素、アクセシブルなフォーム、TOC ページ、そして自動タグ付けを含む、タグ付けされた PDF ドキュメントの作成方法を学びましょう。
lastmod: "2026-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Tagged PDF を作成することは、PDF/UA の要件に従って文書を検証できるようにするために、文書に特定の要素を追加（または作成）することを意味します。これらの要素は、しばしば Structure Elements と呼ばれます。

## Tagged PDFの作成（シンプルシナリオ）

Tagged PDF ドキュメントで構造要素を作成するために、Aspose.PDF は構造要素を作成するメソッドを使用して提供します。 [ITaggedContent](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/) インターフェース。この例では Tagged PDF ドキュメントを作成します — セマンティック構造を持つ PDF で、アクセシビリティが向上し、PDF/UA のような標準に準拠しています。
以下のコードスニペットは、ヘッダーと段落の2つの要素を含むTagged PDFの作成方法を示しています。

```python
import aspose.pdf as ap
import sys
from os import path

def create_tagged_pdf_document_simple(outfile):

    # Create PDF Document
    with ap.Document() as document:
        # Get Content for working with TaggedPdf
        tagged_content = document.tagged_content
        root_element = tagged_content.root_element

        # Set Title and Language for Document
        tagged_content.set_title("Tagged Pdf Document")
        tagged_content.set_language("en-US")
        main_header = tagged_content.create_header_element()
        main_header.set_text("Main Header")
        paragraph_element = tagged_content.create_paragraph_element()
        paragraph_element.set_text(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
            + "Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. "
            + "Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet "
            + "nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. "
            + "Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat "
            + "sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper "
            + "pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus "
            + "ac iaculis eget, tempus et magna. Sed non consectetur elit. Sed vulputate, quam sed lacinia luctus, "
            + "ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus."
        )
        root_element.append_child(main_header, True)
        root_element.append_child(paragraph_element, True)

        # Save Tagged PDF Document
        document.save(outfile)
```

## タグ付けされた PDF（高度）

```python
import aspose.pdf as ap
import sys
from os import path

def create_tagged_pdf_document_adv(outfile):
    # Create PDF Document
    with ap.Document() as document:
        # Get Content for working with TaggedPdf
        tagged_content = document.tagged_content
        root_element = tagged_content.root_element

        # Set Title and Language for Document
        tagged_content.set_title("Tagged Pdf Document")
        tagged_content.set_language("en-US")

        # Create Header Level 1
        header1 = tagged_content.create_header_element(1)
        header1.set_text("Header Level 1")

        # Create Paragraph with Quotes
        paragraph_with_quotes = tagged_content.create_paragraph_element()
        paragraph_with_quotes.structure_text_state.font = (
            ap.text.FontRepository.find_font("Arial")
        )
        position_settings = ap.tagged.PositionSettings()
        position_settings.margin = ap.MarginInfo(10, 5, 10, 5)
        paragraph_with_quotes.adjust_position(position_settings)

        # Create Span Element
        span_element1 = tagged_content.create_span_element()
        span_element1.set_text(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nec lectus ac sem faucibus imperdiet. "
            "Sed ut erat ac magna ullamcorper hendrerit. Cras pellentesque libero semper, gravida magna sed, "
            "luctus leo. Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. Interdum et malesuada "
            "fames ac ante ipsum primis in faucibus. Aliquam lacinia sit amet elit ac consectetur. Donec cursus "
            "condimentum ligula, vitae volutpat sem tristique eget. Nulla in consectetur massa. Vestibulum vitae "
            "lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. Mauris ornare eu odio non "
            "lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit."
        )

        # Create Quote Element
        quote_element = tagged_content.create_quote_element()
        quote_element.set_text(
            "Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa."
        )
        quote_element.structure_text_state.font_style = (
            ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
        )

        # Create Another Span Element
        span_element2 = tagged_content.create_span_element()
        span_element2.set_text(" Sed non consectetur elit.")

        # Append Children to Paragraph
        paragraph_with_quotes.append_child(span_element1, True)
        paragraph_with_quotes.append_child(quote_element, True)
        paragraph_with_quotes.append_child(span_element2, True)

        # Append Header and Paragraph to Root Element
        root_element.append_child(header1, True)
        root_element.append_child(paragraph_with_quotes, True)

        # Save Tagged PDF Document
        document.save(outfile)
```

作成後に以下のドキュメントが取得できます:

![2つの要素（ヘッダーと段落）を持つTagged PDFドキュメント](taggedpdf-01.png)

## テキスト構造のスタイリング

Tagged PDF は、コンテンツにアクセシビリティ機能とセマンティックな意味付けを提供する構造化文書です。

この例は、タグ付けされたコンテンツ構造を使用してアクセシビリティ機能を備えた PDF ドキュメントを作成します。カスタムスタイルと適切なドキュメントメタデータを持つ段落要素の作成方法を示しています。

```python
import aspose.pdf as ap
import sys
from os import path

def add_style(outfile):

    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with TaggedPdf
        tagged_content = document.tagged_content

        # Set Title and Language for Document
        tagged_content.set_title("Tagged Pdf Document")
        tagged_content.set_language("en-US")

        paragraph_element = tagged_content.create_paragraph_element()
        tagged_content.root_element.append_child(paragraph_element, True)

        paragraph_element.structure_text_state.font_size = 18.0
        paragraph_element.structure_text_state.foreground_color = ap.Color.red
        paragraph_element.structure_text_state.font_style = ap.text.FontStyles.ITALIC

        paragraph_element.set_text("Red italic text.")

        # Save Tagged PDF Document
        document.save(outfile)
```

## 構造要素の図示

タグ付けされた PDF はアクセシビリティコンプライアンスに不可欠であり、スクリーンリーダーやその他の支援技術によって正しく解釈できる構造化されたコンテンツを提供します。以下のコードスニペットは、埋め込み画像を含むタグ付け PDF ドキュメントの作成方法を示しています:

1. 画像を使用してタグ付きPDFを作成する。
1. ドキュメントを構成する。
1. 図を作成して設定する。
1. 配置を設定する。
1. 文書を保存する。

```python
import aspose.pdf as ap
import sys
from os import path

def illustrate_structure_elements(imagefile, outfile):
    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with TaggedPdf
        tagged_content = document.tagged_content

        # Set Title and Language for Document
        tagged_content.set_title("Tagged Pdf Document")
        tagged_content.set_language("en-US")
        figure1 = tagged_content.create_figure_element()
        tagged_content.root_element.append_child(figure1, True)
        figure1.alternative_text = "Figure One"
        figure1.title = "Image 1"
        figure1.set_tag("Fig1")
        figure1.set_image(imagefile, 300)
        # Adjust position
        position_settings = ap.tagged.PositionSettings()
        margin_info = ap.MarginInfo()
        margin_info.left = 50
        margin_info.top = 20
        position_settings.margin = margin_info
        figure1.adjust_position(position_settings)

        # Save Tagged PDF Document
        document.save(outfile)
```

## Tagged PDF を検証する

Aspose.PDF for Python via .NET は、PDF/UA タグ付けされた PDF ドキュメントを検証する機能を提供します。 \u0027validate_tagged_pdf\u0027 メソッドは、PDF 文書を PDF/UA-1 標準に対して検証します。これは、アクセシブルな PDF 文書のための ISO 14289 仕様の一部です。この機能により、PDF が障害を持つユーザーや支援技術に対してアクセス可能であることが保証されます。

- ドキュメント構造。適切なセマンティック タグ付けと論理構造。
- 代替テキスト。画像や非テキスト要素の代替テキスト。
- 読み順。スクリーンリーダーのための論理的なシーケンス。
- 色とコントラスト。十分なコントラスト比。
- フォーム。アクセシブルなフォームフィールドとラベル。
- ナビゲーション。適切なブックマークとナビゲーション構造。

```python
import aspose.pdf as ap
import sys
from os import path

def validate_tagged_pdf(infile, logfile):
    # Open PDF document
    with ap.Document(infile) as document:
        is_valid = document.validate(logfile, ap.PdfFormat.PDF_UA_1)
    print(f"Is Valid: {is_valid}")
```

## テキスト構造の位置を調整する

以下のコードスニペットは、Tagged PDF ドキュメント内のテキスト構造の位置を調整する方法を示しています：

```python
import aspose.pdf as ap
import sys
from os import path

def adjust_position(outfile):
    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with TaggedPdf
        tagged_content = document.tagged_content

        # Set Title and Language for Document
        tagged_content.set_title("Tagged Pdf Document")
        tagged_content.set_language("en-US")

        # Create paragraph
        paragraph = tagged_content.create_paragraph_element()
        tagged_content.root_element.append_child(paragraph, True)
        paragraph.set_text("Text.")

        # Adjust position
        position_settings = ap.tagged.PositionSettings()
        margin_info = ap.MarginInfo()
        margin_info.left = 300
        margin_info.top = 20
        margin_info.right = 0
        margin_info.bottom = 0
        position_settings.margin = margin_info
        position_settings.horizontal_alignment = ap.HorizontalAlignment.NONE
        position_settings.vertical_alignment = ap.VerticalAlignment.NONE
        position_settings.is_first_paragraph_in_column = False
        position_settings.is_kept_with_next = False
        position_settings.is_in_new_page = False
        position_settings.is_in_line_paragraph = False
        paragraph.adjust_position(position_settings)

        # Save Tagged PDF Document
        document.save(outfile)
```

## PDF を自動タグ付けで PDF/UA-1 に変換

このコードスニペットは、Aspose.PDF for Python via .NET を使用して、標準的な PDF を PDF/UA-1（ユニバーサルアクセシビリティ）準拠のファイルに変換する方法を説明しています。

PDF/UA は、文書が障害を持つユーザーにとってアクセス可能であり、スクリーンリーダーなどの支援技術と互換性があることを保証します。変換中に、ライブラリは組み込みの自動タグ付けと見出し認識を使用して、論理構造ツリーを自動的に生成し、セマンティックタグを適用できます。

PdfFormatConversionOptions を構成し、AutoTaggingSettings を有効にすることで、構造を手動で編集することなく、既存の PDF を効率的にアクセシブルなドキュメントに変換できます。

1. ソース文書をロードします。
1. PDF/UA 変換オプションを作成する。
1. 自動タグ付けを有効にする。
1. 見出し認識を構成する。
1. タグ付け構成を変換オプションに添付します。
1. 変換プロセスを実行します。
1. アクセシブルPDFを保存してください。

```python
import aspose.pdf as ap
import sys
from os import path

def convert_to_pdf_ua_with_automatic_tagging(infile, outfile, logfile):
    # Create PDF Document
    with ap.Document(infile) as document:
        # Create conversion options
        options = ap.PdfFormatConversionOptions(
            logfile, ap.PdfFormat.PDF_UA_1, ap.ConvertErrorAction.DELETE
        )
        # Create auto-tagging settings
        # aspose.pdf.AutoTaggingSettings.default may be used to set the same settings as given below
        auto_tagging_settings = ap.AutoTaggingSettings()
        # Enable auto-tagging during the conversion process
        auto_tagging_settings.enable_auto_tagging = True
        # Use the heading recognition strategy that's optimal for the given document structure
        auto_tagging_settings.heading_recognition_strategy = (
            ap.HeadingRecognitionStrategy.AUTO
        )
        # Assign auto-tagging settings to be used during the conversion process
        options.auto_tagging_settings = auto_tagging_settings
        # During the conversion, the document logical structure will be automatically created
        document.convert(options)
        # Save PDF document
        document.save(outfile)
```

## アクセシブルな署名フォームフィールドを含む Tagged PDF を作成する

1. 新しい PDF ドキュメントを作成します。
1. タグ付けされたコンテンツにアクセスする。
1. 署名 Form フィールドを作成してください。
1. AcroFormにフィールドを追加します。
1. タグ構造にフォーム要素を作成します。
1. Structure要素をFormフィールドにリンクしてください。
1. Form 要素を論理構造ツリーに追加します。
1. ドキュメントを保存します。

```python
import aspose.pdf as ap
import sys
from os import path

def create_pdf_with_tagged_form_field(outfile):
    # Create PDF document
    with ap.Document() as document:
        document.pages.add()
        # Get Content for work with TaggedPdf
        tagged_content = document.tagged_content
        root_element = tagged_content.root_element
        # Create a visible signature form field (AcroForm)
        signature_field = ap.forms.SignatureField(
            document.pages[1], ap.Rectangle(50, 50, 100, 100, True)
        )
        signature_field.partial_name = "Signature1"
        signature_field.alternate_name = "signature 1"

        # Add the signature field to the document's AcroForm
        document.form.add(signature_field)

        # Create a /Form structure element in the tag tree
        form = tagged_content.create_form_element()
        form.alternative_text = "form 1"

        # Link the /Form tag to the signature field via an /OBJR reference
        form.tag(signature_field)

        # Add the /Form structure element to the document’s logical structure tree
        root_element.append_child(form, True)

        # Save PDF document
        document.save(outfile)
```

## 目次（TOC）ページ付きの Tagged PDF を作成する

この例は、Aspose.PDF for Python via .NET を使用して、構造化された Table of Contents (TOC) ページを含むタグ付けされた PDF ドキュメントを作成する方法を示しています。

1. 新しい PDF ドキュメントを作成します。
1. 専用の目次ページを作成してください。
1. 論理構造ツリーに TOC 要素を作成して登録します。
1. コンテンツページを追加する。
1. ヘッダー要素を作成します。
1. /TOCI 要素を作成する。
1. ヘッダーを TOC にリンクします。
1. ドキュメントを保存します。

```python
import aspose.pdf as ap
import sys
from os import path

def create_pdf_with_toc_page(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get tagged content for the PDF structure
        content = document.tagged_content
        root_element = content.root_element
        content.set_language("en-US")
        # Add the table of contents (TOC) page
        toc_page = document.pages.add()
        toc_page.toc_info = ap.TocInfo()
        # Create a TOC structure element
        toc_element = content.create_toc_element()
        # Add the TOC element to the document structure tree
        root_element.append_child(toc_element, True)
        # Add a content page
        document.pages.add()
        # Create a header element and set its text
        header = content.create_header_element(1)
        header.set_text("1. Header")
        # Add the header to the document structure
        root_element.append_child(header, True)
        # Create a TOC item (TOCI) element
        toci = content.create_toci_element()
        # Add the TOCI element to the TOC element
        toc_element.append_child(toci, True)
        # Add an entry to the TOC page and link it to the TOCI element
        header.add_entry_to_toc_page(toc_page, toci)
        # Add a logical reference to the header within the TOCI element
        toci.add_ref(header)
        # Save PDF document
        document.save(outfile)
```

## 階層型目次（TOC）を備えた高度なタグ付きPDFを作成する

Aspose.PDF for Python via .NET を使用すると、構造化された階層的な目次 (TOC) を備えた、高度で完全にタグ付けされた PDF ドキュメントを作成できます。

1. ドキュメントを作成し、Tagged コンテンツを有効にします。
1. TOC ページを追加して設定します。
1. /TOC 構造要素を作成します。
1. 目次ページのタイトルをヘッダー要素にリンクする。
1. メインコンテンツページと最初のヘッダーを追加します。
1. ヘッダーの目次エントリを作成する。
1. リスト構造で入れ子のサブセクションを作成する。
1. トップレベルのセクションをもう1つ追加します。
1. ドキュメントを保存します。

```python
import aspose.pdf as ap
import sys
from os import path

def create_pdf_with_toc_page_advanced(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get tagged content for the PDF structure
        content = document.tagged_content
        root_element = content.root_element
        content.set_language("en-US")
        # Add the table of contents (TOC) page
        toc_page = document.pages.add()
        toc_page.toc_info = ap.TocInfo()
        toc_page.toc_info.title = ap.text.TextFragment("Table of Contents")
        # Create a TOC structure element
        toc_element = content.create_toc_element()
        # Create a header element for the TOC page title
        header_for_toc_page_title = content.create_header_element(1)
        toc_element.link_toc_page_title_to_header_element(
            toc_page, header_for_toc_page_title
        )
        # Add the TOC page title header and TOC element to the document structure tree
        root_element.append_child(header_for_toc_page_title, True)
        root_element.append_child(toc_element, True)
        # Add a content page
        document.pages.add()
        # Create a header element and set its text
        header = content.create_header_element(1)
        header.set_text("1. Header")
        # Add the header to the document structure
        root_element.append_child(header, True)
        # Create a TOC item (TOCI) element
        toci = content.create_toci_element()
        # Add the TOCI element to the TOC element
        toc_element.append_child(toci, True)
        # Add an entry to the TOC page and link it to the TOCI element
        header.add_entry_to_toc_page(toc_page, toci)
        # Add a logical reference to the header within the TOCI element
        toci.add_ref(header)
        # Create a list element for TOCI subitems
        list_element = content.create_list_element()
        for i in range(1, 4):
            # Create a list item (LI) element
            li = content.create_list_li_element()
            # Add the list item to the list element
            list_element.append_child(li, True)
            # Create a sub-header element and set its properties
            sub_header = content.create_header_element(2)
            sub_header.structure_text_state.font_size = 14
            sub_header.language = "en-US"
            sub_header.set_text(f"1.{i} subheader ")
            # Add an entry to the TOC page and link it to the LI element
            sub_header.add_entry_to_toc_page(toc_page, li)
            # Add a logical reference to the subheader element
            li.add_ref(sub_header)
            # Create a paragraph element and set its text and language
            p = content.create_paragraph_element()
            p.set_text(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
            )
            p.language = "en-US"
            # Add the sub-header and paragraph to the document structure
            root_element.append_child(sub_header, True)
            root_element.append_child(p, True)
        # Add the list element as a child to the TOCI element
        toci.append_child(list_element, True)
        # --- Additional TOC header example ---
        # Create a second header element (see comments above for header 1)
        header2 = content.create_header_element(1)
        header2.set_text("2. Header")
        root_element.append_child(header2, True)

        toci2 = content.create_toci_element()
        toc_element.append_child(toci2, True)

        header2.add_entry_to_toc_page(toc_page, toci2)
        toci2.add_ref(header2)
        # Save the PDF document
        document.save(outfile)
```

## 関連するタグ付け PDF のトピック

- [タグ付けされたPDFからタグ付けされたコンテンツを抽出する](/pdf/ja/python-net/extract-tagged-content-from-tagged-pdfs/) 作成後に論理構造ツリーを検査するために。
- [Structure Elements のプロパティ設定](/pdf/ja/python-net/setting-structure-elements-properties/) タイトル、言語、代替テキスト、拡張テキストを改良するために。
- [Tagged PDF のテーブルの操作](/pdf/ja/python-net/working-with-table-in-tagged-pdfs/) アクセシブルなドキュメントに構造化されたテーブルが含まれている場合。
