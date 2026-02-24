---
title: Python を使用した PDF ドキュメントのフォーマット
linktitle: PDF ドキュメントのフォーマット
type: docs
weight: 11
url: /ja/python-net/formatting-pdf-document/
description: Aspose.PDF for Python via .NET を使用して PDF ドキュメントを作成およびフォーマットします。次のコードスニペットを使用してタスクを解決してください。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用した PDF ドキュメントのフォーマット
Abstract: この記事は、Python の Aspose.PDF ライブラリを使用して PDF ドキュメントを操作およびフォーマットするための包括的なガイドを提供します。ウィンドウの中央揃え、読み取り方向、UI 要素の非表示など、ドキュメントウィンドウやページ表示プロパティの設定を含む、PDF カスタマイズのさまざまな側面をカバーしています。`Document` クラスを使用して、これらのプロパティをプログラムで取得および設定する方法を説明します。さらに、フォント管理についても取り上げ、Standard Type 1 フォントやその他のフォントを PDF に埋め込む方法を詳述し、ドキュメントの移植性とシステム間の視覚的一貫性を確保します。デフォルトフォント名の設定、PDF からすべてのフォントを取得する手法、`FontSubsetStrategy` を使用したフォント埋め込みの強化技術も紹介しています。また、`GoToAction` クラスを用いた PDF のズーム率調整や、両面印刷オプションを含む印刷ダイアログのプリセットプロパティの設定についても詳しく解説しています。各セクションにはコードスニペットが添付されており、これらの機能を実装するための実用的な例が示されています。
---

## PDF ドキュメントのフォーマット

### ドキュメントウィンドウとページ表示プロパティの取得

このトピックでは、ドキュメントウィンドウ、ビューア アプリケーション、およびページの表示方法に関するプロパティの取得方法を理解できます。これらのプロパティを設定するには、次のようにします。

PDF ファイルを [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラスを使用して開きます。これで、Document オブジェクトのプロパティ（例:）を設定できます。

- CenterWindow – 画面上でドキュメントウィンドウを中央に配置します。デフォルト: false.
- Direction – 読み取り順序。ページが横に並んで表示されるときの配置を決定します。デフォルト: 左から右。
- DisplayDocTitle – ドキュメントウィンドウのタイトルバーにドキュメントタイトルを表示します。デフォルト: false（タイトルが表示されます）。
- HideMenuBar – ドキュメントウィンドウのメニューバーを非表示または表示します。デフォルト: false（メニューバーが表示されます）。
- HideToolBar – ドキュメントウィンドウのツールバーを非表示または表示します。デフォルト: false（ツールバーが表示されます）。
- HideWindowUI – スクロールバーなどのドキュメントウィンドウ要素を非表示または表示します。デフォルト: false（UI 要素が表示されます）。
- NonFullScreenPageMode – フルページモードで表示されていないときのドキュメントの表示方法。
- PageLayout – ページレイアウト。
- PageMode – ドキュメントを最初に開いたときの表示方法。オプションはサムネイル表示、全画面表示、添付パネルの表示です。

以下のコードスニペットは、[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラスを使用してプロパティを取得する方法を示しています。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Get different document properties
    # Position of document's window - Default: false
    print("CenterWindow :", document.center_window)

    # Predominant reading order; determins the position of page
    # When displayed side by side - Default: L2R
    print("Direction :", document.direction)

    # Whether window's title bar should display document title
    # If false, title bar displays PDF file name - Default: false
    print("DisplayDocTitle :", document.display_doc_title)

    # Whether to resize the document's window to fit the size of
    # First displayed page - Default: false
    print("FitWindow :", document.fit_window)

    # Whether to hide menu bar of the viewer application - Default: false
    print("HideMenuBar :", document.hide_menubar)

    # Whether to hide tool bar of the viewer application - Default: false
    print("HideToolBar :", document.hide_tool_bar)

    # Whether to hide UI elements like scroll bars
    # And leaving only the page contents displayed - Default: false
    print("HideWindowUI :", document.hide_window_ui)

    # Document's page mode. How to display document on exiting full-screen mode.
    print("NonFullScreenPageMode :", document.non_full_screen_page_mode)

    # The page layout i.e. single page, one column
    print("PageLayout :", document.page_layout)

    # How the document should display when opened
    # I.e. show thumbnails, full-screen, show attachment panel
    print("pageMode :", document.page_mode)

```

### ドキュメントウィンドウとページ表示プロパティの設定

このトピックでは、ドキュメントウィンドウ、ビューア アプリケーション、およびページ表示のプロパティを設定する方法を説明します。これらのさまざまなプロパティを設定するには、次のようにします。

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラスを使用して PDF ファイルを開きます。
1. Document オブジェクトのプロパティを設定します。
1. save メソッドを使用して更新された PDF ファイルを保存します。

利用可能なプロパティは次のとおりです。

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

それぞれは以下のコードで使用され、説明されています。以下のコードスニペットは、[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラスを使用してプロパティを設定する方法を示しています。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Set different document properties
    # Sepcify to position document's window - Default: false
    document.center_window = True

    # Predominant reading order; determins the position of page
    # When displayed side by side - Default: L2R
    document.direction = ap.Direction.R2L

    # Specify whether window's title bar should display document title
    # If false, title bar displays PDF file name - Default: false
    document.display_doc_title = True

    # Specify whether to resize the document's window to fit the size of
    # First displayed page - Default: false
    document.fit_window = True

    # Specify whether to hide menu bar of the viewer application - Default: false
    document.hide_menubar = True

    # Specify whether to hide tool bar of the viewer application - Default: false
    document.hide_tool_bar = True

    # Specify whether to hide UI elements like scroll bars
    # And leaving only the page contents displayed - Default: false
    document.hide_window_ui = True

    # Document's page mode. specify how to display document on exiting full-screen mode.
    document.non_full_screen_page_mode = ap.PageMode.USE_OC

    # Specify the page layout i.e. single page, one column
    document.page_layout = ap.PageLayout.TWO_COLUMN_LEFT

    # Specify how the document should display when opened
    # I.e. show thumbnails, full-screen, show attachment panel
    document.page_mode = ap.PageMode.USE_THUMBS

    # Save updated PDF file
    document.save(output_pdf)
```

### 標準 Type 1 フォントの埋め込み

一部の PDF ドキュメントには、Adobe の特殊なフォントセットからのフォントが含まれます。このセットのフォントは「Standard Type 1 Fonts」と呼ばれます。このセットには 14 種類のフォントが含まれ、これらのフォントを埋め込むには特別なフラグ（例: [embed_standard_fonts](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties)）を使用する必要があります。以下のコードスニペットは、Standard Type 1 フォントを含むすべてのフォントが埋め込まれたドキュメントを取得するために使用できます。

```python

    import aspose.pdf as ap

    # Load an existing PDF Document
    document = ap.Document(input_pdf)
    # Set EmbedStandardFonts property of document
    document.embed_standard_fonts = True
    for page in document.pages:
        if page.resources.fonts != None:
            for page_font in page.resources.fonts:
                # Check if font is already embedded
                if not page_font.is_embedded:
                    page_font.is_embedded = True

    document.save(output_pdf)
```

### PDF 作成時のフォント埋め込み

Adobe Reader がサポートする 14 のコアフォント以外のフォントを使用する必要がある場合、PDF ファイル生成時にフォント情報を埋め込む必要があります。フォント情報が埋め込まれていない場合、Adobe Reader はシステムにインストールされていれば OS から取得するか、PDF のフォント記述子に従って代替フォントを構築します。

>埋め込まれたフォントはホストマシンにインストールされている必要があります。例えば、以下のコードで使用する ‘Univers Condensed’ フォントはシステムにインストールされています。

フォント情報を PDF に埋め込むために 'is_embedded' プロパティを使用します。このプロパティの値を 'True' に設定すると、フォントファイル全体が PDF に埋め込まれ、PDF ファイルサイズが増加することになります。以下のコードスニペットは、フォント情報を PDF に埋め込むために使用できます。

```python

    import aspose.pdf as ap

    # Instantiate Pdf object by calling its empty constructor
    doc = ap.Document()

    # Create a section in the Pdf object
    page = doc.pages.add()

    fragment = ap.text.TextFragment("")
    segment = ap.text.TextSegment(" This is a sample text using Custom font.")
    ts = ap.text.TextState()
    ts.font = ap.text.FontRepository.find_font("Arial")
    ts.font.is_embedded = True
    segment.text_state = ts
    fragment.segments.append(segment)
    page.paragraphs.add(fragment)

    # Save PDF Document
    doc.save(output_pdf)
```

### PDF を保存する際のデフォルトフォント名の設定

PDF ドキュメントに、ドキュメント自体やデバイスに存在しないフォントが含まれている場合、API はそれらのフォントをデフォルトフォントに置き換えます。フォントが利用可能（デバイスにインストールされているか、ドキュメントに埋め込まれている）場合、出力 PDF は同じフォントを使用すべきで、デフォルトフォントに置き換えられません。デフォルトフォントの値にはフォント名（フォントファイルへのパスではなく）を含める必要があります。PDF としてドキュメントを保存する際にデフォルトフォント名を設定する機能を実装しました。以下のコードスニペットを使用してデフォルトフォントを設定できます:

```python

    import aspose.pdf as ap

    # Load an existing PDF document with missing font
    document = ap.Document(input_pdf)

    pdfSaveOptions = ap.PdfSaveOptions()
    # Specify Default Font Name
    newName = "Arial"
    pdfSaveOptions.default_font_name = newName
    document.save(output_pdf, pdfSaveOptions)
```

### PDF ドキュメントからすべてのフォントを取得する

PDF ドキュメントからすべてのフォントを取得したい場合は、[font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) メソッドを [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラスで使用できます。既存の PDF ドキュメントからすべてのフォントを取得するためのコードスニペットは以下をご確認ください:

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    fonts = doc.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)
```

### FontSubsetStrategy を使用したフォント埋め込みの改善

以下のコードスニペットは、[FontSubsetStrategy](https://reference.aspose.com/pdf/python-net/aspose.pdf/fontsubsetstrategy/) を設定し、[font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) プロパティで使用する方法を示しています:

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    # All fonts will be embedded as subset into document in case of SubsetAllFonts.
    doc.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_ALL_FONTS)
    # Font subset will be embedded for fully embedded fonts but fonts which are not embedded into document will not be affected.
    doc.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_EMBEDDED_FONTS_ONLY)
    doc.save(output_pdf)
```

### PDF ファイルのズーム倍率の取得と設定

場合によっては、PDF ドキュメントの現在のズーム倍率を確認したいことがあります。Aspose.Pdf を使用すれば、現在の値を取得し、設定することができます。

[GoToAction](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/gotoaction/) クラスの Destination プロパティを使用すると、PDF ファイルに関連付けられたズーム値を取得できます。同様に、このプロパティを使用してファイルのズーム倍率を設定することも可能です。

#### ズーム倍率の設定

以下のコードスニペットは、PDF ファイルのズーム倍率を設定する方法を示しています。

```python

    import aspose.pdf as ap

    # Instantiate new Document object
    doc = ap.Document(input_pdf)

    action = ap.annotations.GoToAction(ap.annotations.XYZExplicitDestination(1, 0.0, 0.0, 0.5))
    doc.open_action = action
    # Save the document
    doc.save(output_pdf)
```

#### ズーム倍率の取得

以下のコードスニペットは、PDF ファイルのズーム倍率を取得する方法を示しています。

```python

    import aspose.pdf as ap

    # Instantiate new Document object
    doc = ap.Document(input_pdf)

    # Create GoToAction object
    action = doc.open_action

    # Get the Zoom factor of PDF file
    print(action.destination.zoom)
```

### 印刷ダイアログの事前設定プロパティの設定

Aspose.PDF は、PDF ドキュメントの [DUPLEX_FLIP_LONG_EDGE](https://reference.aspose.com/pdf/python-net/aspose.pdf/printduplex/#members) メンバーを設定することを可能にします。これにより、デフォルトでシンプルックスに設定されている PDF の DuplexMode プロパティを変更できます。以下に示す 2 つの異なる方法で実現できます。

```python

    import aspose.pdf as ap

    doc = ap.Document()
    doc.pages.add()
    doc.duplex = ap.PrintDuplex.DUPLEX_FLIP_LONG_EDGE
    doc.save(output_pdf)
```

### PDF コンテンツエディタを使用した印刷ダイアログの事前設定プロパティの設定

```python

    import aspose.pdf as ap

    ed = ap.facades.PdfContentEditor()
    ed.bind_pdf(input_pdf)
    if (ed.get_viewer_preference() & ap.facades.ViewerPreference.DUPLEX_FLIP_SHORT_EDGE) > 0:
        print("The file has duplex flip short edge")

    ed.change_viewer_preference(ap.facades.ViewerPreference.DUPLEX_FLIP_SHORT_EDGE)
    ed.save(output_pdf)
```


