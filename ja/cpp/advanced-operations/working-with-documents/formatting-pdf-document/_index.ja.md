---
title: C++を使用したPDFドキュメントのフォーマット
linktitle: PDFドキュメントのフォーマット
type: docs
weight: 20
url: /cpp/formatting-pdf-document/
description: Aspose.PDF for C++を使用してPDFドキュメントを作成およびフォーマットします。タスクを解決するために次のコードスニペットを使用してください。
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDFドキュメントのフォーマット

### ドキュメントウィンドウとページ表示プロパティの取得

このトピックでは、ドキュメントウィンドウ、ビューアアプリケーションのプロパティ、およびページがどのように表示されるかを理解するのに役立ちます。これらのプロパティを設定するには、[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) クラスを使用してPDFファイルを開きます。これで、ドキュメントオブジェクトのプロパティを設定できます。例えば：

- CenterWindow – ドキュメントウィンドウを画面の中央に配置します。デフォルト: false。
- Direction – 読み取り順序。これは、ページが並べて表示されるときにどのように配置されるかを決定します。デフォルト: 左から右。
- DisplayDocTitle – ドキュメントウィンドウのタイトルバーにドキュメントのタイトルを表示します。 Default: false (タイトルが表示されます)。
- HideMenuBar – ドキュメントウィンドウのメニューバーを非表示または表示します。Default: false (メニューバーが表示されます)。
- HideToolBar – ドキュメントウィンドウのツールバーを非表示または表示します。Default: false (ツールバーが表示されます)。
- HideWindowUI – スクロールバーなどのドキュメントウィンドウ要素を非表示または表示します。Default: false (UI要素が表示されます)。
- NonFullScreenPageMode – ドキュメントがフルページモードで表示されていないときの状態。
- PageLayout – ページレイアウト。
- PageMode – ドキュメントを最初に開いたときの表示方法。オプションはサムネイル表示、フルスクリーン、添付ファイルパネル表示です。

次のコードスニペットは、[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) クラスを使用してプロパティを取得する方法を示しています。

```cpp
void GetDocumentWindowAndPageDisplayProperties()
{
    // パス名の文字列。
    String _dataDir("C:\\Samples\\");
    // ファイル名の文字列。
    String inputFileName("sample.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // 異なるドキュメントプロパティを取得
    // ドキュメントウィンドウの位置 - Default: false
    Console::WriteLine(u"CenterWindow : {0}", document->get_CenterWindow());

    // 主要な読み順; ページの位置を決定します
    // 並べて表示されるとき - Default: L2R
    Console::WriteLine(u"Direction : {0}", document->get_Direction());

    // ウィンドウのタイトルバーにドキュメントタイトルを表示するかどうか
    // falseの場合、タイトルバーにはPDFファイル名が表示されます - Default: false
    Console::WriteLine(u"DisplayDocTitle : {0}", document->get_DisplayDocTitle());

    // ドキュメントウィンドウのサイズを最初に表示されるページのサイズに合わせて
    // 調整するかどうか - Default: false
    Console::WriteLine(u"FitWindow : {0}", document->get_FitWindow());

    // ビューアーアプリケーションのメニューバーを非表示にするかどうか - Default: false
    Console::WriteLine(u"HideMenuBar : {0}", document->get_HideMenubar());

    // ビューアーアプリケーションのツールバーを非表示にするかどうか - Default: false
    Console::WriteLine(u"HideToolBar : {0}", document->get_HideToolBar());

    // スクロールバーのようなUI要素を非表示にするかどうか
    // ページコンテンツのみを表示します - Default: false
    Console::WriteLine(u"HideWindowUI : {0}", document->get_HideWindowUI());

    // ドキュメントのページモード。フルスクリーンモードを終了したときの表示方法。
    Console::WriteLine(u"NonFullScreenPageMode : {0}", document->get_NonFullScreenPageMode());

    // ページレイアウト、つまりシングルページ、1カラム
    Console::WriteLine(u"PageLayout : {0}", document->get_PageLayout());

    // ドキュメントを開いたときの表示方法
    // つまり、サムネイル表示、フルスクリーン、添付ファイルパネル表示
    Console::WriteLine(u"pageMode : {0}", document->get_PageMode());
}
```
### ドキュメントウィンドウとページ表示プロパティの設定

このトピックでは、ドキュメントウィンドウ、ビューアーアプリケーション、およびページ表示のプロパティを設定する方法を説明します。これらの異なるプロパティを設定するには、以下の手順に従います。

1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) クラスを使用してPDFファイルを開きます。
1. 異なるドキュメントプロパティを設定します：

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

1. Saveメソッドを使用して更新されたPDFファイルを[保存](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/#ac082fe8e67b25685fc51d33e804269fa)します。

利用可能なプロパティは以下の通りです：

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

それぞれのプロパティは以下のコードで使用され、説明されています。 以下のコードスニペットは、[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) クラスを使用してプロパティを設定する方法を示しています。

```cpp
void SetDocumentWindowAndPageDisplayProperties()
{
    // パス名の文字列。
    String _dataDir("C:\\Samples\\");
    // ファイル名の文字列。
    String inputFileName("sample.pdf");
    String outputFileName("sample_page_display_properties.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // 異なるドキュメントプロパティを設定する
    // ドキュメントのウィンドウの位置を指定する - デフォルト: false
    document->set_CenterWindow(true);

    // 主な読み取り順序を設定する; ページの位置を決定する
    // 並べて表示される時 - デフォルト: L2R
    document->set_Direction(Direction::R2L);

    // ウィンドウのタイトルバーにドキュメントタイトルを表示するかどうかを指定する
    // false の場合、タイトルバーはPDFファイル名を表示する - デフォルト: false
    document->set_DisplayDocTitle(true);

    // ドキュメントのウィンドウをサイズに合わせてリサイズするかどうかを指定する
    // 最初に表示されるページ - デフォルト: false
    document->set_FitWindow(true);

    // ビューアアプリケーションのメニューバーを非表示にするかどうかを指定する - デフォルト: false
    document->set_HideMenubar(true);

    // ビューアアプリケーションのツールバーを非表示にするかどうかを指定する - デフォルト: false
    document->set_HideToolBar(true);

    // スクロールバーのようなUI要素を非表示にするかどうかを指定する
    // ページ内容のみを表示する - デフォルト: false
    document->set_HideWindowUI(true);

    // ドキュメントのページモード。フルスクリーンモードを終了した際の表示方法を指定する。
    document->set_NonFullScreenPageMode(PageMode::UseOC);

    // ページレイアウトを指定する、すなわちシングルページ、一列
    document->set_PageLayout(PageLayout::TwoColumnLeft);

    // ドキュメントを開いた時の表示方法を指定する
    // すなわち、サムネイルを表示、フルスクリーン、添付パネルを表示
    document->set_PageMode(PageMode::UseThumbs);

    // 更新されたPDFファイルを保存する
    document->Save(_dataDir + outputFileName);
}
```
### 既存のPDFファイルにフォントを埋め込む

PDFリーダーは、ドキュメントが表示されるプラットフォームに関係なく同じ方法で表示できるように[14のコアフォント](https://en.wikipedia.org/wiki/PDF#Text)をサポートしています。PDFに14のコアフォントのいずれでもないフォントが含まれている場合、フォント置き換えを避けるためにフォントをPDFファイルに埋め込む必要があります。

Aspose.PDF for C++は、既存のPDFファイルへのフォント埋め込みをサポートしています。完全なフォントまたはフォントのサブセットを埋め込むことができます。フォントを埋め込むには、[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)クラスを使用してPDFファイルを開きます。その後、[Aspose.Pdf.Text.Font](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.font)クラスを使用してフォントをPDFファイルに埋め込みます。完全なフォントを埋め込むには、FontクラスのIsEmbededプロパティを使用します。フォントのサブセットを使用するには、IsSubsetプロパティを使用します。

{{% alert color="primary" %}}

フォントのサブセットは使用される文字のみを埋め込み、短い文章やスローガンにフォントが使用される場合に便利です。例えば、企業のロゴにフォントが使用されるが、本文には使用されない場合などです。 
サブセットを使用すると、出力PDFのファイルサイズが小さくなります。ただし、本文にカスタムフォントを使用する場合は、それを完全に埋め込んでください。

{{% /alert %}}

次のコードスニペットは、PDFファイルにフォントを埋め込む方法を示しています。

### 標準Type 1フォントの埋め込み

特別なセットからフォントを使用するPDFドキュメントがあり、これらは「標準Type 1フォント」と呼ばれます。このセットには14のフォントが含まれており、このタイプのフォントを埋め込むには特別なフラグを使用する必要があります。すなわち、[Aspose.Pdf.Document.EmbedStandardFonts](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a8f1a88eef22e05ee9ee22a79db9cb9f6)。

以下は、標準Type 1フォントを含むすべてのフォントが埋め込まれたドキュメントを取得するために使用できるコードスニペットです：

```cpp
void EmbeddingStandardType1Fonts()
{

    // パス名の文字列
    String _dataDir("C:\\Samples\\");
    // ファイル名の文字列
    String inputFileName("sample.pdf");
    String outputFileName("embedded-fonts-updated_out.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // ドキュメントのEmbedStandardFontsプロパティを設定
    document->set_EmbedStandardFonts(true);
    for (auto page : document->get_Pages())
    {
        auto fonts = page->get_Resources()->get_Fonts();
        if (fonts != nullptr)
        {
            for (auto pageFont : fonts)
            {
                // フォントが既に埋め込まれているか確認
                if (!pageFont->get_IsEmbedded())
                {
                    pageFont->set_IsEmbedded(true);
                }
            }
        }
    }
    document->Save(_dataDir + outputFileName);
}
```
```
### PDF作成時のフォント埋め込み

Adobe Readerがサポートする14のコアフォント以外のフォントを使用する必要がある場合、Pdfファイルを生成する際にフォントの説明を埋め込む必要があります。フォント情報が埋め込まれていない場合、Adobe Readerはそれをオペレーティングシステムから取得します（システム上にインストールされている場合）、またはPdfのフォント記述子に従って代替フォントを構築します。

>埋め込まれるフォントはホストマシンにインストールされている必要があることに注意してください。以下のコードの場合、『Univers Condensed』フォントがシステム上にインストールされています。

フォント情報をPdfファイルに埋め込むために、FontクラスのプロパティIsEmbeddedを使用します。このプロパティの値を『True』に設定すると、Pdfに完全なフォントファイルが埋め込まれます。このことはPdfファイルのサイズを増加させることを知っておいてください。以下は、フォント情報をPdfに埋め込むために使用できるコードスニペットです。

```cpp
void EmbeddingFontsWhileCreatingPDF()
{
    // パス名の文字列。
    String _dataDir("C:\\Samples\\");
    // ファイル名の文字列。
    String inputFileName("sample.pdf");
    String outputFileName("EmbedFontWhileDocCreation_out.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // Pdfオブジェクトにセクションを作成
    auto page = document->get_Pages()->Add();

    auto fragment = MakeObject<TextFragment>("");
    auto segment = MakeObject <TextSegment>(u"このサンプルテキストはカスタムフォントを使用しています。");

    auto ts = MakeObject<TextState>();

    ts->set_Font(FontRepository::FindFont(u"Arial"));
    ts->get_Font()->set_IsEmbedded(true);
    segment->set_TextState(ts);
    fragment->get_Segments()->Add(segment);
    page->get_Paragraphs()->Add(fragment);

    // PDFドキュメントを保存
    document->Save(_dataDir);
}
```

### PDFを保存する際のデフォルトフォント名の設定

PDFドキュメントにフォントが含まれているが、そのフォントがドキュメント自体やデバイスに存在しない場合、APIはこれらのフォントをデフォルトフォントに置き換えます。フォントが利用可能な場合（デバイスにインストールされているかドキュメントに埋め込まれている場合）、出力PDFは同じフォントを持つべきです（デフォルトフォントに置き換えられるべきではありません）。デフォルトフォントの値にはフォントのパスではなくフォントの名前が含まれている必要があります。Apose.PDF for C++は、ドキュメントをPDFとして保存する際にデフォルトフォント名を設定する機能を実装しました。以下のコードスニペットを使用して、デフォルトフォントを設定できます。

```cpp
void SetDefaultFontNameWhileSavingPDF()
{
    // パス名のための文字列。
    String _dataDir("C:\\Samples\\");
    // ファイル名のための文字列。
    String inputFileName("sample.pdf");
    String outputFileName("output_out.pdf");
    String newName("Arial");

    auto document = MakeObject<Document>(inputFileName);

    auto pdfSaveOptions = MakeObject<PdfSaveOptions>();

    // デフォルトフォント名を指定
    pdfSaveOptions->set_DefaultFontName(newName);
    document->Save(_dataDir + outputFileName, pdfSaveOptions);
}
```

### PDFドキュメントからすべてのフォントを取得

PDFドキュメントからすべてのフォントを取得したい場合は、[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)クラスで提供されている[FontUtilities](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a2e22a508e8baef176dfc34734cf0def9).GetAllFonts()メソッドを使用できます。

既存のPDFドキュメントからすべてのフォントを取得するための以下のコードスニペットを確認してください：

```cpp
void GetAllFontsFromPDFdocument()
{
    // パス名用の文字列。
    String _dataDir("C:\\Samples\\");
    // ファイル名用の文字列。
    String inputFileName("sample.pdf");
    String outputFileName("output_out.pdf");
    String newName("Arial");

    auto document = MakeObject<Document>(inputFileName);
    auto fonts = document->get_FontUtilities()->GetAllFonts();
    for (auto font : fonts)
    {
        std::cerr << font->get_FontName() << std::endl;
    }
}
```

### フォント置換の警告を取得

Aspose.PDF for C++は、フォント置換のケースを処理するためのフォント置換に関する通知を取得するメソッドを提供します。 対応する機能を使用する方法を示すコードスニペットは以下の通りです。

```cpp
void GetWarningsForFontSubstitution()
{
    // パス名のための文字列。
    String _dataDir("C:\\Samples\\");

    // ファイル名のための文字列。
    String inputFileName("sample.pdf");
    String outputFileName("output_out.pdf");

    auto document = MakeObject<Document>(inputFileName);

    document->FontSubstitution = Aspose::Pdf::Document::FontSubstitutionHandler(OnFontSubstitution);
}
```

[OnFontSubstitution](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac776d8736d430532bdaa530a36eb51a0) メソッドは以下の通りです。

```cpp
void OnFontSubstitution(Aspose::Pdf::Text::Font &font, Aspose::Pdf::Text::Font& newFont) {
    std::cout << "Warning: Font " << font.get_FontName() 
            << " was substituted with another font -> " 
            << newFont.get_FontName() << std::endl;
}
```

### FontSubsetStrategyを使用してフォント埋め込みを改善する

フォントをサブセットとして埋め込む機能は、IsSubsetプロパティを使用して達成できますが、時折、完全に埋め込まれたフォントセットを文書で使用されるサブセットに限定したい場合があります。 [Aspose.Pdf.Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)には、SubsetFonts(FontSubsetStrategy subsetStrategy)メソッドを含む[FontUtilities](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document.i_document_font_utilities/)プロパティがあります。メソッドSubsetFonts()では、パラメータsubsetStrategyを使用してサブセット戦略を調整します。FontSubsetStrategyは、フォントサブセットの次の2つのバリエーションをサポートしています。

- SubsetAllFonts - これは、ドキュメント内で使用されているすべてのフォントをサブセット化します。
- SubsetEmbeddedFontsOnly - これは、ドキュメントに完全に埋め込まれているフォントのみをサブセット化します。

次のコードスニペットは、FontSubsetStrategyを設定する方法を示しています：

```cpp
void ImproveFontsEmbeddingUsingFontSubsetStrategy()
{
    // パス名の文字列。
    String _dataDir("C:\\Samples\\");

    // ファイル名の文字列。
    String inputFileName("sample.pdf");
    // ファイル名の文字列。
    String outputFileName("sample_out.pdf");

    auto document = MakeObject<Document>(inputFileName);
    // SubsetAllFontsの場合、すべてのフォントはドキュメントにサブセットとして埋め込まれます。
    document->get_FontUtilities()->SubsetFonts(FontSubsetStrategy::SubsetAllFonts);
    // フォントサブセットは完全に埋め込まれたフォントに対してのみ埋め込まれますが、ドキュメントに埋め込まれていないフォントには影響しません。
    document->get_FontUtilities()->SubsetFonts(FontSubsetStrategy::SubsetEmbeddedFontsOnly);
    document->Save(_dataDir + outputFileName);
}
```
### PDFファイルのズームファクターの取得と設定

時々、PDFドキュメントのズームファクターを設定したいことがあります。Aspose.PDF for C++を使用すると、Documentクラスの[set_OpenAction(…) メソッド](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#abb5c84979077034d06a673409b666e21)でズームファクターの値を設定できます。

[GoToAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_action/)クラスのDestinationプロパティを使用すると、PDFファイルに関連付けられたズーム値を取得できます。同様に、ファイルのズームファクターを設定するためにも使用できます。

#### ズームファクターの設定

以下のコードスニペットは、PDFファイルのズームファクターを設定する方法を示しています。

```cpp
void SetZoomFactor() {
    // パス名の文字列。
    String _dataDir("C:\\Samples\\");

    // ファイル名の文字列。
    String inputFileName("sample.pdf");
    // ファイル名の文字列。
    String outputFileName("Zoomed_pdf_out.pdf");

    auto document = MakeObject<Document>(inputFileName);
    auto action = MakeObject<Aspose::Pdf::Annotations::GoToAction>(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(1, 0, 0, .5));

    document->set_OpenAction(action);
    // ドキュメントを保存します
    document->Save(_dataDir + outputFileName);
}
```

#### ズームファクターを取得する

Aspose.PDF for C++を使用してPDFファイルのズームファクターを取得します。

次のコードスニペットは、PDFファイルのズームファクターを取得する方法を示しています:

```cpp
void GetZoomFactor() 
{
    // パス名のための文字列。
    String _dataDir("C:\\Samples\\");

    // ファイル名のための文字列。
    String inputFileName("sample.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // GoToActionオブジェクトを作成
    auto action = System::DynamicCast<Aspose::Pdf::Annotations::GoToAction>(document->get_OpenAction());

    // PDFファイルのズームファクターを取得
    auto zoom = System::DynamicCast<Aspose::Pdf::Annotations::XYZExplicitDestination>(action->get_Destination());
    Console::WriteLine(zoom->get_Zoom()); // ドキュメントのズーム値;
}
```

### 印刷ダイアログプリセットプロパティの設定

Aspose.PDF for C++は、PDFドキュメントの印刷ダイアログプリセットプロパティを設定することができます。 PDF ドキュメントの DuplexMode プロパティを変更することができます。デフォルトでは simplex に設定されています。以下に示すように、2つの異なる方法でこれを達成できます。

```cpp
void SettingPrintDialogPresetProperties()
{
    // パス名の文字列。
    String _dataDir("C:\\Samples\\");
    // ファイル名の文字列。
    String outputFileName("SettingPrintDialogPresetProperties.pdf");

    auto document = MakeObject<Document>();
    document->get_Pages()->Add();
    document->set_Duplex(PrintDuplex::DuplexFlipLongEdge);
    document->Save(_dataDir + outputFileName);
}
```

### PDF コンテンツエディターを使用して印刷ダイアログのプリセットプロパティを設定する

```cpp
void SettingPrintDialogPresetPropertiesUsingContentEditor() {
    // パス名の文字列。
    String _dataDir("C:\\Samples\\");

    // ファイル名の文字列。
    String inputFileName("sample.pdf");
    String outputFileName("SetPrintDlgPropertiesUsingPdfContentEditor_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto contentEditor = MakeObject<Aspose::Pdf::Facades::PdfContentEditor>();

    contentEditor->BindPdf(outputFileName);
    if ((contentEditor->GetViewerPreference() & Aspose::Pdf::Facades::ViewerPreference::DuplexFlipShortEdge) > 0)
    {
    std::cout << "ファイルには短辺の両面印刷が設定されています" << std::endl;
    }

    contentEditor->ChangeViewerPreference(Aspose::Pdf::Facades::ViewerPreference::DuplexFlipShortEdge);
    contentEditor->Save(_dataDir + outputFileName);
}
```