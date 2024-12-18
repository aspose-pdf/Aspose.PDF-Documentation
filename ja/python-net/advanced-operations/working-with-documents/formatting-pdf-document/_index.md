---
title: Pythonを使用したPDFドキュメントのフォーマット
linktitle: PDFドキュメントのフォーマット
type: docs
weight: 11
url: /ja/python-net/formatting-pdf-document/
description: Aspose.PDF for Python via .NETを使用してPDFドキュメントを作成およびフォーマットします。次のコードスニペットを使用してタスクを解決してください。
lastmod: "2023-04-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Pythonを使用したPDFドキュメントのフォーマット",
    "alternativeHeadline": "Python via .NETでPDFドキュメントをフォーマットする方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, dotnet, python, pdfドキュメントのフォーマット",
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
    "url": "/python-net/formatting-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/formatting-pdf-document/"
    },
    "dateModified": "2023-04-13",
    "description": "Aspose.PDF for Python via .NETを使用してPDFドキュメントを作成およびフォーマットします。次のコードスニペットを使用してタスクを解決してください。"
}
</script>


## PDFドキュメントのフォーマット

### ドキュメントウィンドウとページ表示プロパティの取得

このトピックでは、ドキュメントウィンドウ、ビューアアプリケーションのプロパティ、およびページがどのように表示されるかを取得する方法について説明します。これらのプロパティを設定するには:

[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラスを使用してPDFファイルを開きます。これで、ドキュメントオブジェクトのプロパティを設定できます。例えば、

- CenterWindow – ドキュメントウィンドウを画面の中央に配置します。デフォルト: false。
- Direction – 読み順。これは、ページを並べて表示する際のレイアウト方法を決定します。デフォルト: 左から右。
- DisplayDocTitle – ドキュメントウィンドウのタイトルバーにドキュメントのタイトルを表示します。デフォルト: false (タイトルが表示されます)。
- HideMenuBar – ドキュメントウィンドウのメニューバーを非表示または表示します。デフォルト: false (メニューバーが表示されます)。
- HideToolBar – ドキュメントウィンドウのツールバーを非表示または表示します。デフォルト: false (ツールバーが表示されます)。
- HideWindowUI – スクロールバーなどのドキュメントウィンドウ要素を非表示または表示します。
 デフォルト: false (UI要素が表示される)。
- NonFullScreenPageMode – ドキュメントがフルページモードで表示されていないときの表示方法。
- PageLayout – ページのレイアウト。
- PageMode – ドキュメントが最初に開かれたときの表示方法。オプションは、サムネイルを表示、フルスクリーン、添付ファイルパネルを表示。

以下のコードスニペットは、[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラスを使用してプロパティを取得する方法を示しています。

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_pdf)

    # 異なるドキュメントプロパティを取得
    # ドキュメントのウィンドウの位置 - デフォルト: false
    print("CenterWindow :", document.center_window)

    # 主な読み取り順序; ページの位置を決定する
    # 並べて表示されるとき - デフォルト: L2R
    print("Direction :", document.direction)

    # ウィンドウのタイトルバーにドキュメントのタイトルを表示するかどうか
    # falseの場合、タイトルバーにはPDFファイル名が表示される - デフォルト: false
    print("DisplayDocTitle :", document.display_doc_title)

    # ドキュメントのウィンドウを
    # 最初に表示されるページのサイズに合わせてリサイズするかどうか - デフォルト: false
    print("FitWindow :", document.fit_window)

    # ビューアアプリケーションのメニューバーを隠すかどうか - デフォルト: false
    print("HideMenuBar :", document.hide_menubar)

    # ビューアアプリケーションのツールバーを隠すかどうか - デフォルト: false
    print("HideToolBar :", document.hide_tool_bar)

    # スクロールバーなどのUI要素を隠すかどうか
    # ページ内容のみを表示する - デフォルト: false
    print("HideWindowUI :", document.hide_window_ui)

    # ドキュメントのページモード。フルスクリーンモードを終了したときのドキュメントの表示方法。
    print("NonFullScreenPageMode :", document.non_full_screen_page_mode)

    # ページのレイアウト、つまりシングルページ、1列
    print("PageLayout :", document.page_layout)

    # ドキュメントを開いたときの表示方法
    # 例えば、サムネイルを表示、フルスクリーン、添付ファイルパネルを表示
    print("pageMode :", document.page_mode)

```

### ドキュメントウィンドウとページ表示プロパティの設定

このトピックでは、ドキュメントウィンドウ、ビューアアプリケーション、およびページ表示のプロパティを設定する方法を説明します。これらの異なるプロパティを設定するには:

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラスを使用してPDFファイルを開きます。
1. Documentオブジェクトのプロパティを設定します。
1. 保存メソッドを使用して更新されたPDFファイルを保存します。

利用可能なプロパティは次のとおりです:

- CenterWindow
- Direction
- DisplayDocTitle
- FitWindow
- HideMenuBar
- HideToolBar
- HideWindowUI
- NonFullScreenPageMode
- PageLayout
- PageMode

以下のコードスニペットで、[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラスを使用してプロパティを設定する方法を示します。

```python

    import aspose.pdf as ap

    # ドキュメントを開く
    document = ap.Document(input_pdf)

    # 異なるドキュメントプロパティを設定する
    # ドキュメントウィンドウの位置を指定 - デフォルト: false
    document.center_window = True

    # 主な読み取り順序を指定; ページの位置を決定する
    # 並べて表示する場合 - デフォルト: L2R
    document.direction = ap.Direction.R2L

    # ウィンドウのタイトルバーにドキュメントのタイトルを表示するか指定
    # falseの場合、タイトルバーにはPDFファイル名が表示されます - デフォルト: false
    document.display_doc_title = True

    # ドキュメントウィンドウのサイズを変更して最初に表示されるページのサイズに合わせるか指定
    # デフォルト: false
    document.fit_window = True

    # ビューアアプリケーションのメニューバーを隠すか指定 - デフォルト: false
    document.hide_menubar = True

    # ビューアアプリケーションのツールバーを隠すか指定 - デフォルト: false
    document.hide_tool_bar = True

    # スクロールバーなどのUI要素を隠して
    # ページの内容のみを表示するか指定 - デフォルト: false
    document.hide_window_ui = True

    # ドキュメントのページモード。全画面モードを終了したときの表示方法を指定します。
    document.non_full_screen_page_mode = ap.PageMode.USE_OC

    # ページレイアウトを指定、すなわち単一ページ、1カラム
    document.page_layout = ap.PageLayout.TWO_COLUMN_LEFT

    # ドキュメントを開いたときの表示方法を指定
    # 例えば、サムネイルを表示、全画面表示、添付ファイルパネルを表示
    document.page_mode = ap.PageMode.USE_THUMBS

    # 更新されたPDFファイルを保存
    document.save(output_pdf)
```


### 標準タイプ1フォントの埋め込み

一部のPDF文書には、特別なAdobeフォントセットからのフォントがあります。このセットからのフォントは「標準タイプ1フォント」と呼ばれます。このセットには14のフォントが含まれており、このタイプのフォントを埋め込むには、特別なフラグ、例えば [embed_standard_fonts](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) を使用する必要があります。以下は、標準タイプ1フォントを含むすべてのフォントが埋め込まれた文書を取得するために使用できるコードスニペットです:

```python

    import aspose.pdf as ap

    # 既存のPDFドキュメントを読み込む
    document = ap.Document(input_pdf)
    # ドキュメントのEmbedStandardFontsプロパティを設定する
    document.embed_standard_fonts = True
    for page in document.pages:
        if page.resources.fonts != None:
            for page_font in page.resources.fonts:
                # フォントがすでに埋め込まれているか確認する
                if not page_font.is_embedded:
                    page_font.is_embedded = True

    document.save(output_pdf)
```

### PDF作成時のフォントの埋め込み

もし、Adobe Readerでサポートされている14のコアフォント以外のフォントを使用する必要がある場合は、PDFファイルを生成する際にフォントの説明を埋め込まなければなりません。フォント情報が埋め込まれていない場合、Adobe Readerはオペレーティングシステムからそれを取得します（システムにインストールされている場合）か、PDFのフォント記述子に基づいて代替フォントを構築します。

>埋め込まれるフォントはホストマシンにインストールされている必要があります。つまり、以下のコードで「Univers Condensed」フォントがシステムにインストールされているケースです。

フォント情報をPDFファイルに埋め込むためにプロパティ「is_embedded」を使用します。このプロパティの値を「True」に設定すると、PDFに完全なフォントファイルが埋め込まれますが、これによりPDFファイルのサイズが増加することを知っておいてください。以下はフォント情報をPDFに埋め込むために使用できるコードスニペットです。

```python

    import aspose.pdf as ap

    # 空のコンストラクタを呼び出してPdfオブジェクトをインスタンス化する
    doc = ap.Document()

    # Pdfオブジェクトにセクションを作成する
    page = doc.pages.add()

    fragment = ap.text.TextFragment("")
    segment = ap.text.TextSegment(" This is a sample text using Custom font.")
    ts = ap.text.TextState()
    ts.font = ap.text.FontRepository.find_font("Arial")
    ts.font.is_embedded = True
    segment.text_state = ts
    fragment.segments.append(segment)
    page.paragraphs.add(fragment)

    # PDFドキュメントを保存する
    doc.save(output_pdf)
```


### PDFを保存する際にデフォルトフォント名を設定する

PDFドキュメントに、ドキュメント自体やデバイスに存在しないフォントが含まれている場合、APIはこれらのフォントをデフォルトフォントに置き換えます。フォントが利用可能な場合（デバイスにインストールされているか、ドキュメントに埋め込まれている場合）、出力PDFは同じフォントを持つべきです（デフォルトフォントに置き換えられるべきではありません）。デフォルトフォントの値には、フォントファイルへのパスではなくフォントの名前が含まれている必要があります。ドキュメントをPDFとして保存する際にデフォルトフォント名を設定する機能を実装しました。デフォルトフォントを設定するには、次のコードスニペットを使用できます。

```python

    import aspose.pdf as ap

    # フォントが欠落している既存のPDFドキュメントをロードする
    document = ap.Document(input_pdf)

    pdfSaveOptions = ap.PdfSaveOptions()
    # デフォルトフォント名を指定する
    newName = "Arial"
    pdfSaveOptions.default_font_name = newName
    document.save(output_pdf, pdfSaveOptions)
```

### PDFドキュメントからすべてのフォントを取得する

PDFドキュメントからすべてのフォントを取得したい場合、[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)クラスで提供されている[font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties)メソッドを使用できます。
 既存のPDFドキュメントからすべてのフォントを取得するには、次のコードスニペットを確認してください。

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    fonts = doc.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)
```

### FontSubsetStrategyを使用したフォント埋め込みの改善

以下のコードスニペットは、[font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties)プロパティで使用する[FontSubsetStrategy](https://reference.aspose.com/pdf/python-net/aspose.pdf/fontsubsetstrategy/)を設定する方法を示しています。

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    # SubsetAllFontsの場合、すべてのフォントはサブセットとしてドキュメントに埋め込まれます。
    doc.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_ALL_FONTS)
    # 完全に埋め込まれたフォントのためにフォントサブセットが埋め込まれますが、ドキュメントに埋め込まれていないフォントには影響しません。
    doc.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_EMBEDDED_FONTS_ONLY)
    doc.save(output_pdf)
```

### PDFファイルのズームファクターの取得と設定

時には、PDFドキュメントの現在のズームファクターを確認したいことがあります。Aspose.Pdfを使用すると、現在の値を確認することができ、また、設定することもできます。

[GoToAction](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/gotoaction/) クラスの Destination プロパティを使用すると、PDFファイルに関連付けられたズーム値を取得できます。同様に、ファイルのズームファクターを設定するためにも使用できます。

#### ズームファクターの設定

次のコードスニペットは、PDFファイルのズームファクターを設定する方法を示しています。

```python

    import aspose.pdf as ap

    # 新しいDocumentオブジェクトをインスタンス化
    doc = ap.Document(input_pdf)

    action = ap.annotations.GoToAction(ap.annotations.XYZExplicitDestination(1, 0.0, 0.0, 0.5))
    doc.open_action = action
    # ドキュメントを保存
    doc.save(output_pdf)
```

#### ズームファクターの取得

次のコードスニペットは、PDFファイルのズームファクターを取得する方法を示しています。

```python

    import aspose.pdf as ap

    # 新しいDocumentオブジェクトをインスタンス化
    doc = ap.Document(input_pdf)

    # GoToActionオブジェクトを作成
    action = doc.open_action

    # PDFファイルのズームファクターを取得
    print(action.destination.zoom)
```


### 印刷ダイアログプリセットプロパティの設定

Aspose.PDFを使用すると、PDFドキュメントの[DUPLEX_FLIP_LONG_EDGE](https://reference.aspose.com/pdf/python-net/aspose.pdf/printduplex/#members)メンバーを設定できます。これにより、デフォルトではシンプルモードに設定されているPDFドキュメントのDuplexModeプロパティを変更することができます。これは、以下に示す2つの異なる方法で実現できます。

```python

    import aspose.pdf as ap

    doc = ap.Document()
    doc.pages.add()
    doc.duplex = ap.PrintDuplex.DUPLEX_FLIP_LONG_EDGE
    doc.save(output_pdf)
```

### PDFコンテンツエディターを使用して印刷ダイアログプリセットプロパティを設定

```python

    import aspose.pdf as ap

    ed = ap.facades.PdfContentEditor()
    ed.bind_pdf(input_pdf)
    if (ed.get_viewer_preference() & ap.facades.ViewerPreference.DUPLEX_FLIP_SHORT_EDGE) > 0:
        print("ファイルは両面短辺反転が設定されています")

    ed.change_viewer_preference(ap.facades.ViewerPreference.DUPLEX_FLIP_SHORT_EDGE)
    ed.save(output_pdf)
```