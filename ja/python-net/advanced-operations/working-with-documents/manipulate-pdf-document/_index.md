---
title: Pythonを介してPDFドキュメントを操作する
linktitle: PDFドキュメントを操作する
type: docs
weight: 20
url: /ja/python-net/manipulate-pdf-document/
description: この記事には、Pythonを使用してPDF A標準のPDFドキュメントを検証する方法、目次を操作する方法、PDFの有効期限を設定する方法などの情報が含まれています。
keywords: "manipulate pdf python"
lastmod: "2023-04-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Pythonを介してPDFドキュメントを操作する",
    "alternativeHeadline": "PythonでPDFファイルを操作する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, dotnet, python, manipulate pdf file",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
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
    "url": "/python-net/manipulate-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/manipulate-pdf-document/"
    },
    "dateModified": "2023-04-13",
    "description": "この記事には、Pythonを使用してPDF A標準のPDFドキュメントを検証する方法、目次を操作する方法、PDFの有効期限を設定する方法などの情報が含まれています。"
}
</script>


## Manipulate PDF Document in Python

## PDF A標準 (A 1AおよびA 1B) に対するPDFドキュメントの検証

PDFドキュメントをPDF/A-1aまたはPDF/A-1b互換性について検証するには、[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)クラスの[validate](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)メソッドを使用します。このメソッドを使用すると、結果を保存するファイルの名前と必要な検証タイプPdfFormat列挙型: PDF_A_1AまたはPDF_A_1Bを指定できます。

以下のコードスニペットは、PDFドキュメントをPDF/A-1Aに対して検証する方法を示しています。

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_pdf)

    # PDF/A-1aに対してPDFを検証
    document.validate(output_xml, ap.PdfFormat.PDF_A_1A)
```

以下のコードスニペットは、PDFドキュメントをPDF/A-1bに対して検証する方法を示しています。

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_pdf)

    # PDF/A-1aに対してPDFを検証
    document.validate(output_xml, ap.PdfFormat.PDF_A_1B)
```


## TOCの操作

### 既存のPDFにTOCを追加

PDFのTOCは「目次」を意味します。これは、セクションや見出しの概要を提供することで、ユーザーがドキュメントを迅速にナビゲートできるようにする機能です。

既存のPDFファイルにTOCを追加するには、[aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/)名前空間のHeadingクラスを使用します。[aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/)名前空間は、新しいPDFファイルを作成するだけでなく、既存のPDFファイルを操作することもできます。既存のPDFにTOCを追加するには、Aspose.Pdf名前空間を使用します。以下のコードスニペットは、Python経由で.NETを使用して既存のPDFファイル内に目次を作成する方法を示しています。

```python

    import aspose.pdf as ap

    # 既存のPDFファイルをロード
    doc = ap.Document(input_pdf)

    # PDFファイルの最初のページにアクセス
    tocPage = doc.pages.insert(1)

    # TOC情報を表すオブジェクトを作成
    tocInfo = ap.TocInfo()
    title = ap.text.TextFragment("目次")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD

    # TOCのタイトルを設定
    tocInfo.title = title
    tocPage.toc_info = tocInfo

    # TOC要素として使用する文字列オブジェクトを作成
    titles = ["最初のページ", "2ページ目", "3ページ目", "4ページ目"]
    for i in range(0, 2):
        # 見出しオブジェクトを作成
        heading2 = ap.Heading(1)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = tocPage
        heading2.segments.append(segment2)

        # 見出しオブジェクトの宛先ページを指定
        heading2.destination_page = doc.pages[i + 2]

        # 宛先ページ
        heading2.top = doc.pages[i + 2].rect.height

        # 宛先座標
        segment2.text = titles[i]

        # TOCを含むページに見出しを追加
        tocPage.paragraphs.add(heading2)

    # 更新されたドキュメントを保存
    doc.save(output_pdf)
```


### 異なるTOCレベルに異なるTabLeaderTypeを設定する

Aspose.PDF for Pythonは、異なるTOCレベルに異なるTabLeaderTypeを設定することもできます。[TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/)の[line_dash](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties)プロパティを設定する必要があります。

```python

    import aspose.pdf as ap

    doc = ap.Document()
    tocPage = doc.pages.add()
    toc_info = ap.TocInfo()

    # リーダータイプを設定
    toc_info.line_dash = ap.text.TabLeaderType.SOLID
    title = ap.text.TextFragment("目次")
    title.text_state.font_size = 30
    toc_info.title = title

    # Pdfドキュメントのセクションコレクションにリストセクションを追加
    tocPage.toc_info = toc_info
    # 各レベルの左マージンとテキストフォーマット設定を定義して、4レベルリストのフォーマットを定義

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

    # Pdfドキュメントにセクションを作成
    page = doc.pages.add()

    # セクションに4つの見出しを追加
    for Level in range(1, 5):
        heading2 = ap.Heading(Level)
        segment2 = ap.text.TextSegment()
        heading2.segments.append(segment2)
        heading2.is_auto_sequence = True
        heading2.toc_page = tocPage
        segment2.text = "サンプル見出し" + str(Level)
        heading2.text_state.font = ap.text.FontRepository.find_font("Arial")

        # 目次に見出しを追加
        heading2.is_in_list = True
        page.paragraphs.add(heading2)

    # Pdfを保存
    doc.save(output_pdf)
```


### TOCでページ番号を非表示にする

TOCの見出しとともにページ番号を表示したくない場合は、[TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) クラスの [is_show_page_numbers](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) プロパティを false に設定できます。以下のコードスニペットを確認して、目次でページ番号を非表示にする方法を確認してください:

```python

    import aspose.pdf as ap

    doc = ap.Document()
    toc_page = doc.pages.add()
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("目次")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    # Pdfドキュメントのセクションコレクションにリストセクションを追加
    toc_page.toc_info = toc_info
    # 左マージンを設定し、各レベルのテキストフォーマット設定を行い、4レベルリストの形式を定義

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
    # セクションに4つの見出しを追加
    for Level in range(1, 5):
        heading2 = ap.Heading(Level)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = toc_page
        heading2.segments.append(segment2)
        heading2.is_auto_sequence = True
        segment2.text = "これはレベル " + str(Level) + " の見出しです"
        heading2.is_in_list = True
        page.paragraphs.add(heading2)
    doc.save(output_pdf)

```


### TOCを追加する際のページ番号のカスタマイズ

PDFドキュメントにTOCを追加する際に、TOCのページ番号をカスタマイズすることは一般的です。例えば、ページ番号の前にP1、P2、P3などの接頭辞を追加する必要があるかもしれません。そのような場合、Aspose.PDF for Pythonは、次のコードサンプルで示されるように、[TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/)クラスの[page_numbers_prefix](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties)プロパティを使用してページ番号をカスタマイズできます。

```python

    import aspose.pdf as ap

    # 既存のPDFファイルをロード
    doc = ap.Document(input_pdf)
    # PDFファイルの最初のページにアクセス
    toc_page = doc.pages.insert(1)
    # TOC情報を表すオブジェクトを作成
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("目次")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    # TOCのタイトルを設定
    toc_info.title = title
    toc_info.page_numbers_prefix = "P"
    toc_page.toc_info = toc_info
    for i in range(len(doc.pages)):
        # 見出しオブジェクトを作成
        heading2 = ap.Heading(1)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = toc_page
        heading2.segments.append(segment2)
        # 見出しオブジェクトの宛先ページを指定
        heading2.destination_page = doc.pages[i + 1]
        # 宛先ページ
        heading2.top = doc.pages[i + 1].rect.height
        # 宛先座標
        segment2.text = "ページ " + str(i)
        # TOCを含むページに見出しを追加
        toc_page.paragraphs.add(heading2)

    # 更新されたドキュメントを保存
    doc.save(output_pdf)

```


## PDFの有効期限を設定する方法

PDFファイルにアクセス権限を適用して、特定のユーザーグループがPDFドキュメントの特定の機能/オブジェクトにアクセスできるようにします。PDFファイルのアクセスを制限するために、通常は暗号化を適用し、PDFファイルの有効期限を設定する必要がある場合があります。これにより、ドキュメントにアクセス/表示するユーザーに対してPDFファイルの有効期限に関する有効なプロンプトが表示されます。

```python

    import aspose.pdf as ap

    # Documentオブジェクトをインスタンス化
    doc = ap.Document()
    # PDFファイルのページコレクションにページを追加
    doc.pages.add()
    # ページオブジェクトの段落コレクションにテキストフラグメントを追加
    doc.pages[1].paragraphs.add(ap.text.TextFragment("Hello World..."))
    # PDFの有効期限を設定するためのJavaScriptオブジェクトを作成
    javaScript = ap.annotations.JavascriptAction(
        "var year=2017;"
        + "var month=5;"
        + "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
        + "expiry = new Date(year, month);"
        + "if (today.getTime() > expiry.getTime())"
        + "app.alert('ファイルは期限切れです。新しいものが必要です。');"
    )
    # JavaScriptをPDFのオープンアクションとして設定
    doc.open_action = javaScript

    # PDFドキュメントを保存
    doc.save(output_pdf)
```


## Pythonで記入可能なPDFをフラット化する

PDFドキュメントには、ラジオボタン、チェックボックス、テキストボックス、リストなどのインタラクティブな記入可能なウィジェットが含まれていることがよくあります。さまざまなアプリケーションの目的で編集できなくするために、PDFファイルをフラット化する必要があります。Aspose.PDFは、わずか数行のコードでPythonでPDFをフラット化する機能を提供しています。

```python
    import aspose.pdf as ap

    # ソースPDFフォームを読み込む
    doc = ap.Document(input_pdf)

    # 記入可能なPDFをフラット化する
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # 更新されたドキュメントを保存
    doc.save(output_pdf)