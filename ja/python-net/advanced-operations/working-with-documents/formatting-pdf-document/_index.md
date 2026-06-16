---
title: Python で PDF ドキュメントをフォーマットする
linktitle: PDF ドキュメントのフォーマット
type: docs
weight: 11
url: /ja/python-net/formatting-pdf-document/
description: Python で PDF 文書の書式設定、フォントの埋め込み、ビューア設定の制御、表示オプションの調整を行う方法を学びます。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF ドキュメントをフォーマットする
Abstract: この記事では、Python の Aspose.PDF ライブラリを使用した PDF ドキュメントの操作と書式設定に関する包括的なガイドを提供します。ドキュメントウィンドウとページ表示プロパティの設定 (ウィンドウの中央配置、読み上げ方向、UI 要素の非表示など) を含む PDF カスタマイズのさまざまな側面について説明しています。この記事では、`Document` クラスを使用してこれらのプロパティをプログラムで取得および設定する方法について説明します。さらに、フォント管理についても説明し、Standard Type 1 フォントやその他のフォントを PDF に埋め込んで、システム間で文書の移植性と表示の一貫性を確保する方法についても詳しく説明しています。また、デフォルトのフォント名を設定する方法、PDF からすべてのフォントを取得する方法、「FontSubsetStrategy」を使用してフォントの埋め込みを強化する方法についても説明します。さらに、この記事では、`GoToAction` クラスを使用して PDF ドキュメントのズーム率を調整する方法と、両面印刷オプションを含む印刷ダイアログプリセットのプロパティを設定する方法について詳しく説明します。各セクションにはコードスニペットが付属しており、これらの機能を実装するための実用的な例が示されています。
---

このガイドは、Python で生成されたドキュメントの PDF ビューアの動作、フォントの埋め込み、デフォルトの表示設定、または印刷設定を制御する必要がある場合に役立ちます。

## PDF ドキュメントのフォーマット

### ドキュメントウィンドウとページ表示プロパティを取得

このトピックは、ドキュメントウィンドウ、ビューアアプリケーションのプロパティを取得する方法、およびページの表示方法を理解するのに役立ちます。これらのプロパティを設定するには:

を使用して PDF ファイルを開きます [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラス。これで、Document オブジェクトのプロパティを次のように設定できるようになりました。

- CenterWindow — ドキュメントウィンドウを画面の中央に配置します。デフォルト:false。
- 方向 — 読み取り順序。これにより、ページを並べて表示するときのレイアウトが決まります。デフォルト:左から右。
- DisplayDocTitle — ドキュメントウィンドウのタイトルバーにドキュメントタイトルを表示します。デフォルト:false (タイトルが表示されます)。
- HideMenuBar — ドキュメントウィンドウのメニューバーを表示または非表示にします。デフォルト:false (メニューバーが表示されます)。
- HideToolbar — ドキュメントウィンドウのツールバーを表示または非表示にします。デフォルト:false (ツールバーが表示されます)。
- HideWindowUI — スクロールバーなどのドキュメントウィンドウ要素を表示または非表示にします。デフォルト:false (UI 要素が表示されます)。
- NonFullScreenPageMode — ドキュメントがフルページモードで表示されていないときに表示されます。
- ページレイアウト — ページレイアウト。
- PageMode — ドキュメントを初めて開いたときの表示方法。オプションには、サムネイル表示、全画面表示、添付パネル表示があります。

次のコードスニペットは、を使用してプロパティを取得する方法を示しています [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラス。

```python
import aspose.pdf as ap


def get_document_window(input_pdf, output_pdf):
    """Print document window metadata for inspection."""
    document = ap.Document(input_pdf)

    print("CenterWindow:", document.center_window)
    print("Direction:", document.direction)
    print("DisplayDocTitle:", document.display_doc_title)
    print("FitWindow:", document.fit_window)
    print("HideMenuBar:", document.hide_menubar)
    print("HideToolBar:", document.hide_tool_bar)
    print("HideWindowUI:", document.hide_window_ui)
    print("NonFullScreenPageMode:", document.non_full_screen_page_mode)
    print("PageLayout:", document.page_layout)
    print("PageMode:", document.page_mode)
```

### ドキュメントウィンドウとページ表示プロパティの設定

このトピックでは、ドキュメントウィンドウ、ビューアアプリケーション、およびページ表示のプロパティを設定する方法について説明します。これらのさまざまなプロパティを設定するには:

1. を使用して PDF ファイルを開きます [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラス。
1. Document オブジェクトのプロパティを設定します。
1. save メソッドを使用して、更新した PDF ファイルを保存します。

使用可能なプロパティは以下のとおりです。

- センターウィンドウ
- 方向
- ドキュメントタイトルを表示
- フィットウィンドウ
- メニューバーを非表示
- ツールバーを非表示
- ウィンドウ UI を非表示
- 非全画面ページモード
- ページレイアウト
- ページモード

それぞれが使用され、以下のコードで説明されています。次のコードスニペットは、を使用してプロパティを設定する方法を示しています。 [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラス。

```python
import aspose.pdf as ap


def set_document_window(input_pdf, output_pdf):
    """Set document window properties and save the result."""
    document = ap.Document(input_pdf)

    document.center_window = True
    document.direction = ap.Direction.R2L
    document.display_doc_title = True
    document.fit_window = True
    document.hide_menubar = True
    document.hide_tool_bar = True
    document.hide_window_ui = True
    document.non_full_screen_page_mode = ap.PageMode.USE_OC
    document.page_layout = ap.PageLayout.TWO_COLUMN_LEFT
    document.page_mode = ap.PageMode.USE_THUMBS

    document.save(output_pdf)
```

### 標準タイプ 1 フォントの埋め込み

一部の PDF ドキュメントには、アドビの特別なフォントセットのフォントが含まれています。このセットのフォントは「標準 Type 1 フォント」と呼ばれます。このセットには 14 種類のフォントが含まれており、このタイプのフォントを埋め込むには特別なフラグを使用する必要があります。 [標準フォントを埋め込む](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties)。以下は、Standard Type 1 フォントを含むすべてのフォントが埋め込まれたドキュメントを取得するために使用できるコードスニペットです。

```python
import aspose.pdf as ap


def embedded_fonts(input_pdf, output_pdf):
    """Ensure fonts in an existing PDF are embedded."""
    document = ap.Document(input_pdf)
    document.embed_standard_fonts = True

    for page in document.pages:
        if page.resources.fonts:
            for page_font in page.resources.fonts:
                if not page_font.is_embedded:
                    page_font.is_embedded = True

    document.save(output_pdf)
```

### PDF 作成中のフォントの埋め込み

Adobe Reader がサポートする 14 種類のコアフォント以外のフォントを使用する必要がある場合は、PDF ファイルの生成時にフォントの説明を埋め込む必要があります。フォント情報が埋め込まれていない場合、Adobe Reader がシステム上にインストールされている場合はオペレーティングシステムからフォント情報を取得するか、PDF 内のフォント記述子に従って代替フォントを作成します。

>埋め込みフォントはホストマシンにインストールする必要があることに注意してください。つまり、次のコードの場合、「Univers Condensed」フォントがシステム上にインストールされます。

プロパティ「is_embedded」を使用して、フォント情報をPDFファイルに埋め込みます。このプロパティの値を 'True' に設定すると、PDF ファイルのサイズが大きくなることを認識した上で、フォントファイル全体が PDF に埋め込まれます。PDF にフォント情報を埋め込むために使用できるコードスニペットを次に示します。

```python
import aspose.pdf as ap


def embedded_fonts_in_new_document(input_pdf, output_pdf):
    """Embed fonts while generating a document from scratch."""
    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment("")
    segment = ap.text.TextSegment(" This is a sample text using Custom font.")
    text_state = ap.text.TextState()
    text_state.font = ap.text.FontRepository.find_font("Arial")
    text_state.font.is_embedded = True
    segment.text_state = text_state
    fragment.segments.append(segment)
    page.paragraphs.add(fragment)

    document.save(output_pdf)
```

### PDF の保存時にデフォルトフォント名を設定

PDF ドキュメントに、ドキュメント自体やデバイスでは使用できないフォントが含まれている場合、API はこれらのフォントをデフォルトのフォントに置き換えます。フォントが使用できる（デバイスにインストールされている、または文書に埋め込まれている）場合、出力 PDF も同じフォントである必要があります（デフォルトのフォントに置き換えないでください）。デフォルトフォントの値には、（フォントファイルへのパスではなく）フォントの名前が含まれている必要があります。文書を PDF として保存する際にデフォルトのフォント名を設定する機能が実装されました。以下のコードスニペットを使用してデフォルトフォントを設定できます。

```python
import aspose.pdf as ap


def set_default_font(input_pdf, output_pdf):
    """Assign a fallback font when saving a PDF."""
    document = ap.Document(input_pdf)

    save_options = ap.PdfSaveOptions()
    save_options.default_font_name = "Arial"
    document.save(output_pdf, save_options)
```

### PDF ドキュメントからすべてのフォントを取得

PDF文書からすべてのフォントを取得したい場合は、以下を使用できます [フォント_ユーティリティ](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) で提供されるメソッド [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラス。既存の PDF ドキュメントからすべてのフォントを取得するには、次のコードスニペットを確認してください。

```python
import aspose.pdf as ap


def get_all_fonts(input_pdf, output_pdf):
    """Print all fonts referenced by a document."""
    document = ap.Document(input_pdf)
    for font in document.font_utilities.get_all_fonts():
        print(font.font_name)
```

### フォントサブセットストラテジーを使用してフォントの埋め込みを改善する

次のコードスニペットは、設定方法を示しています [フォントサブセット戦略](https://reference.aspose.com/pdf/python-net/aspose.pdf/fontsubsetstrategy/) 使用されています [フォント_ユーティリティ](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) プロパティ:

```python
import aspose.pdf as ap


def improve_fonts_embedding(input_pdf, output_pdf):
    """Apply different font subset strategies to reduce file size."""
    document = ap.Document(input_pdf)

    document.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_ALL_FONTS)
    document.font_utilities.subset_fonts(
        ap.FontSubsetStrategy.SUBSET_EMBEDDED_FONTS_ONLY
    )

    document.save(output_pdf)
```

### PDF ファイルのズーム係数の取得/設定

PDF ドキュメントの現在のズーム倍率を確認したい場合があります。Aspose.Pdf では、現在の値を確認できるだけでなく、設定することもできます。

ザの [アクションに移動](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/gotoaction/) class Destination プロパティを使用すると、PDF ファイルに関連付けられているズーム値を取得できます。同様に、ファイルのズーム係数を設定するのにも使用できます。

#### ズーム倍率を設定

次のコードスニペットは、PDF ファイルのズーム係数を設定する方法を示しています。

```python
import aspose.pdf as ap


def set_zoom_factor(input_pdf, output_pdf):
    """Set an initial zoom level via document open action."""
    document = ap.Document(input_pdf)

    action = ap.annotations.GoToAction(
        ap.annotations.XYZExplicitDestination(1, 0.0, 0.0, 0.5)
    )
    document.open_action = action
    document.save(output_pdf)
```

#### ズームファクターを取得

次のコードスニペットは、PDF ファイルのズーム係数を取得する方法を示しています。

```python
import aspose.pdf as ap


def get_zoom_factor(input_pdf, output_pdf):
    """Print the zoom level configured in the document open action."""
    document = ap.Document(input_pdf)

    action = document.open_action
    if action and action.destination:
        print("Zoom:", action.destination.zoom)
    else:
        print("Zoom: not set")
```

## 関連ドキュメントトピック

- [Python で PDF ドキュメントを操作する](/pdf/ja/python-net/working-with-documents/)
- [Python で PDF ファイルを作成](/pdf/ja/python-net/create-pdf-document/)
- [Python で PDF ドキュメントを操作する方法](/pdf/ja/python-net/manipulate-pdf-document/)
- [Python で PDF ファイルを最適化する方法](/pdf/ja/python-net/optimize-pdf/)
