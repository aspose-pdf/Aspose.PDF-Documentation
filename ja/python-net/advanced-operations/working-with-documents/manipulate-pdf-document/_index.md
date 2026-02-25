---
title: Python を介した .NET で PDF ドキュメントを操作する
linktitle: PDF ドキュメントを操作する
type: docs
weight: 20
url: /ja/python-net/manipulate-pdf-document/
description: この記事では、Python を使用して PDF/A 標準の PDF ドキュメントを検証する方法、TOC の操作方法、PDF の有効期限を設定する方法などについて説明しています。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用した PDF ドキュメント操作ガイド
Abstract: この記事では、Python と Aspose.PDF ライブラリを使用して PDF ドキュメントを操作するための包括的なガイドを提供します。`Document` クラスの `validate` メソッドを使用した PDF/A-1a および PDF/A-1b 準拠の検証を含む複数の機能を扱います。また、PDF ファイル内で目次 (TOC) を追加、カスタマイズ、管理する方法について、異なる TabLeaderTypes の設定、ページ番号の非表示、プレフィックスを使用したページ番号のカスタマイズなどを詳しく説明します。さらに、アクセス制限のために JavaScript を埋め込んで PDF の有効期限を設定する方法と、PDF の入力可能なフォームを編集不可にするフラット化手順についても解説します。各セクションには、Aspose.PDF を Python で使用する実装例を示すコードスニペットが添えられています。
---

## Python で PDF ドキュメントを操作する

## PDF/A 標準 (A 1A と A 1B) 用に PDF ドキュメントを検証する

PDF/A-1a または PDF/A-1b 互換性のために PDF ドキュメントを検証するには、[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラスの [validate](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドを使用します。このメソッドでは、結果を保存するファイル名と必要な検証タイプである PdfFormat 列挙体：PDF_A_1A または PDF_A_1B を指定できます。

次のコードスニペットは、PDF/A-1A 用に PDF ドキュメントを検証する方法を示しています。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Validate PDF for PDF/A-1a
    document.validate(output_xml, ap.PdfFormat.PDF_A_1A)
```

次のコードスニペットは、PDF/A-1b 用に PDF ドキュメントを検証する方法を示しています。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Validate PDF for PDF/A-1a
    document.validate(output_xml, ap.PdfFormat.PDF_A_1B)
```

## TOC の操作

### 既存の PDF に TOC を追加する

PDF の TOC は「目次 (Table of Contents)」を意味します。この機能は、セクションや見出しの概要を提供することで、ユーザーが文書を迅速にナビゲートできるようにします。

既存の PDF ファイルに TOC を追加するには、[aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) 名前空間の Heading クラスを使用します。[aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) 名前空間は、新規作成と既存 PDF の操作の両方が可能です。既存の PDF に TOC を追加するには、Aspose.Pdf 名前空間を使用します。次のコードスニペットは、Python via .NET を使用して既存の PDF ファイル内に目次を作成する方法を示しています。

```python

    import aspose.pdf as ap

    # Load an existing PDF files
    doc = ap.Document(input_pdf)

    # Get access to first page of PDF file
    tocPage = doc.pages.insert(1)

    # Create object to represent TOC information
    tocInfo = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD

    # Set the title for TOC
    tocInfo.title = title
    tocPage.toc_info = tocInfo

    # Create string objects which will be used as TOC elements
    titles = ["First page", "Second page", "Third page", "Fourth page"]
    for i in range(0, 2):
        # Create Heading object
        heading2 = ap.Heading(1)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = tocPage
        heading2.segments.append(segment2)

        # Specify the destination page for heading object
        heading2.destination_page = doc.pages[i + 2]

        # Destination page
        heading2.top = doc.pages[i + 2].rect.height

        # Destination coordinate
        segment2.text = titles[i]

        # Add heading to page containing TOC
        tocPage.paragraphs.add(heading2)

    # Save the updated document
    doc.save(output_pdf)
```

### 異なる TOC レベルごとに異なる TabLeaderType を設定する

Python 用 Aspose.PDF でも、異なる TOC レベルごとに異なる TabLeaderType を設定できます。[TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) の [line_dash](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) プロパティを設定する必要があります。

```python

    import aspose.pdf as ap

    doc = ap.Document()
    tocPage = doc.pages.add()
    toc_info = ap.TocInfo()

    # set LeaderType
    toc_info.line_dash = ap.text.TabLeaderType.SOLID
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 30
    toc_info.title = title

    # Add the list section to the sections collection of the Pdf document
    tocPage.toc_info = toc_info
    # Define the format of the four levels list by setting the left margins
    # and
    # text format settings of each level

    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.left = 0
    toc_info.format_array[0].margin.right = 30
    toc_info.format_array[0].line_dash = ap.text.TabLeaderType.DOT
    toc_info.format_array[0].text_state.font_style = ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
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

    # Create a section in the Pdf document
    page = doc.pages.add()

    # Add four headings in the section
    for Level in range(1, 5):
        heading2 = ap.Heading(Level)
        segment2 = ap.text.TextSegment()
        heading2.segments.append(segment2)
        heading2.is_auto_sequence = True
        heading2.toc_page = tocPage
        segment2.text = "Sample Heading" + str(Level)
        heading2.text_state.font = ap.text.FontRepository.find_font("Arial")

        # Add the heading into Table Of Contents.
        heading2.is_in_list = True
        page.paragraphs.add(heading2)

    # save the Pdf
    doc.save(output_pdf)
```

### TOC のページ番号を非表示にする

TOC の見出しと一緒にページ番号を表示したくない場合は、[TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) クラスの [is_show_page_numbers](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) プロパティを false に設定できます。目次のページ番号を非表示にするコードスニペットは以下をご確認ください。

```python

    import aspose.pdf as ap

    doc = ap.Document()
    toc_page = doc.pages.add()
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    # Add the list section to the sections collection of the Pdf document
    toc_page.toc_info = toc_info
    # Define the format of the four levels list by setting the left margins and
    # text format settings of each level

    toc_info.is_show_page_numbers = False
    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.right = 0
    toc_info.format_array[0].text_state.font_style = ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    toc_info.format_array[1].margin.left = 30
    toc_info.format_array[1].text_state.underline = True
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD
    page = doc.pages.add()
    # Add four headings in the section
    for Level in range(1, 5):
        heading2 = ap.Heading(Level)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = toc_page
        heading2.segments.append(segment2)
        heading2.is_auto_sequence = True
        segment2.text = "this is heading of level " + str(Level)
        heading2.is_in_list = True
        page.paragraphs.add(heading2)
    doc.save(output_pdf)

```

### TOC 追加時にページ番号をカスタマイズする

PDF 文書に TOC を追加する際に、ページ番号をカスタマイズすることは一般的です。例えば、ページ番号の前に P1、P2、P3 などのプレフィックスを付ける必要がある場合があります。そのような場合、Python 用 Aspose.PDF は [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) クラスの [page_numbers_prefix](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) プロパティを提供しており、以下のコードサンプルのようにページ番号をカスタマイズできます。

```python

    import aspose.pdf as ap

    # Load an existing PDF files
    doc = ap.Document(input_pdf)
    # Get access to first page of PDF file
    toc_page = doc.pages.insert(1)
    # Create object to represent TOC information
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    # Set the title for TOC
    toc_info.title = title
    toc_info.page_numbers_prefix = "P"
    toc_page.toc_info = toc_info
    for i in range(len(doc.pages)):
        # Create Heading object
        heading2 = ap.Heading(1)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = toc_page
        heading2.segments.append(segment2)
        # Specify the destination page for heading object
        heading2.destination_page = doc.pages[i + 1]
        # Destination page
        heading2.top = doc.pages[i + 1].rect.height
        # Destination coordinate
        segment2.text = "Page " + str(i)
        # Add heading to page containing TOC
        toc_page.paragraphs.add(heading2)

    # Save the updated document
    doc.save(output_pdf)

```

## PDF の有効期限の設定方法

PDF ファイルにアクセス権限を設定し、特定のユーザーグループが PDF ドキュメントの特定の機能やオブジェクトにアクセスできるようにします。PDF のアクセスを制限するために、通常は暗号化を適用し、さらに PDF ファイルの有効期限を設定する必要がある場合があります。これにより、ドキュメントにアクセスまたは閲覧するユーザーに PDF の有効期限に関する適切な通知が表示されます。

```python

    import aspose.pdf as ap

    # Instantiate Document object
    doc = ap.Document()
    # Add page to pages collection of PDF file
    doc.pages.add()
    # Add text fragment to paragraphs collection of page object
    doc.pages[1].paragraphs.add(ap.text.TextFragment("Hello World..."))
    # Create JavaScript object to set PDF expiry date
    javaScript = ap.annotations.JavascriptAction(
        "var year=2017;"
        + "var month=5;"
        + "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
        + "expiry = new Date(year, month);"
        + "if (today.getTime() > expiry.getTime())"
        + "app.alert('The file is expired. You need a new one.');"
    )
    # Set JavaScript as PDF open action
    doc.open_action = javaScript

    # Save PDF Document
    doc.save(output_pdf)
```

## Python で記入可能な PDF をフラット化する

PDF ドキュメントには、ラジオボタン、チェックボックス、テキストボックス、リストなどのインタラクティブな記入可能ウィジェットを含むフォームが含まれることが多いです。さまざまなアプリケーション目的で編集不可にするためには、PDF ファイルをフラット化する必要があります。
Aspose.PDF は、数行のコードだけで Python で PDF をフラット化する機能を提供します。

```python

    import aspose.pdf as ap

    # Load source PDF form
    doc = ap.Document(input_pdf)

    # Flatten Flatten Fillable PDF
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # Save the updated document
    doc.save(output_pdf)
```


