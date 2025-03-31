---
title: PDFドキュメントのフォーマットをC#で行う
linktitle: PDFドキュメントのフォーマット
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ja/net/formatting-pdf-document/
description: Aspose.PDF for .NETを使用してPDFドキュメントを作成およびフォーマットします。次のコードスニペットを使用してタスクを解決してください。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Formatting Document using C#",
    "alternativeHeadline": "Enhance PDF Formatting with Aspose.PDF for .NET",
    "abstract": "ユーザーがPDFドキュメントをシームレスに作成およびフォーマットできる強力な新機能Aspose.PDF for .NETを発見してください。ウィンドウ表示設定、フォント埋め込みオプション、カスタマイズ可能なズームファクターなどのドキュメントプロパティに対する包括的な制御を使用して、開発者はユーザーエクスペリエンスを向上させ、異なるプラットフォーム間でドキュメントの整合性を維持できます。この堅牢な機能を使用してPDF操作タスクを最適化し、.NETアプリケーションの効率を大幅に向上させます。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Formatting PDF Document, Aspose.PDF for .NET, PDF document properties, embed fonts, font substitution, set zoom factor, document window properties, PDF manipulation library, PDF document generation, C# PDF formatting",
    "wordcount": "2526",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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
    "url": "/net/formatting-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/formatting-pdf-document/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF for .NETを使用してPDFドキュメントを作成およびフォーマットします。次のコードスニペットを使用してタスクを解決してください。"
}
</script>

## PDFドキュメントのフォーマット

### ドキュメントウィンドウとページ表示プロパティの取得

このトピックでは、ドキュメントウィンドウ、ビューアアプリケーションのプロパティ、およびページの表示方法を理解するのに役立ちます。これらのプロパティを設定するには：

[Document](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document)クラスを使用してPDFファイルを開きます。これで、Documentオブジェクトのプロパティを設定できます。例えば：

- CenterWindow – ドキュメントウィンドウを画面の中央に配置します。デフォルト：false。
- Direction – 読み取り順序。これは、ページが横に並べて表示されるときのレイアウト方法を決定します。デフォルト：左から右。
- DisplayDocTitle – ドキュメントウィンドウのタイトルバーにドキュメントタイトルを表示します。デフォルト：false（タイトルが表示されます）。
- HideMenuBar – ドキュメントウィンドウのメニューバーを非表示または表示します。デフォルト：false（メニューバーが表示されます）。
- HideToolBar – ドキュメントウィンドウのツールバーを非表示または表示します。デフォルト：false（ツールバーが表示されます）。
- HideWindowUI – スクロールバーなどのドキュメントウィンドウ要素を非表示または表示します。デフォルト：false（UI要素が表示されます）。
- NonFullScreenPageMode – フルページモードで表示されていないときのドキュメントの表示方法。
- PageLayout – ページレイアウト。
- PageMode – ドキュメントが最初に開かれたときの表示方法。オプションは、サムネイルを表示、フルスクリーン、添付パネルを表示です。

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

次のコードスニペットは、[Document](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document)クラスを使用してプロパティを取得する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetDocumentWindowProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetDocumentWindow.pdf"))
    {
        // Get different document properties
        // Position of document's window - Default: false
        Console.WriteLine("CenterWindow : {0}", document.CenterWindow);

        // Predominant reading order; determines the position of page
        // When displayed side by side - Default: L2R
        Console.WriteLine("Direction : {0}", document.Direction);

        // Whether window's title bar should display document title
        // If false, title bar displays PDF file name - Default: false
        Console.WriteLine("DisplayDocTitle : {0}", document.DisplayDocTitle);

        // Whether to resize the document's window to fit the size of
        // First displayed page - Default: false
        Console.WriteLine("FitWindow : {0}", document.FitWindow);

        // Whether to hide menu bar of the viewer application - Default: false
        Console.WriteLine("HideMenuBar : {0}", document.HideMenubar);

        // Whether to hide tool bar of the viewer application - Default: false
        Console.WriteLine("HideToolBar : {0}", document.HideToolBar);

        // Whether to hide UI elements like scroll bars
        // And leaving only the page contents displayed - Default: false
        Console.WriteLine("HideWindowUI : {0}", document.HideWindowUI);

        // Document's page mode. How to display document on exiting full-screen mode.
        Console.WriteLine("NonFullScreenPageMode : {0}", document.NonFullScreenPageMode);

        // The page layout i.e. single page, one column
        Console.WriteLine("PageLayout : {0}", document.PageLayout);

        // How the document should display when opened
        // I.e. show thumbnails, full-screen, show attachment panel
        Console.WriteLine("PageMode : {0}", document.PageMode);
    }
}
```

### ドキュメントウィンドウとページ表示プロパティの設定

このトピックでは、ドキュメントウィンドウ、ビューアアプリケーション、およびページ表示のプロパティを設定する方法を説明します。これらの異なるプロパティを設定するには：

1. [Document](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document)クラスを使用してPDFファイルを開きます。
1. Documentオブジェクトのプロパティを設定します。
1. Saveメソッドを使用して更新されたPDFファイルを保存します。

利用可能なプロパティは次のとおりです：

- CenterWindow。
- Direction。
- DisplayDocTitle。
- FitWindow。
- HideMenuBar。
- HideToolBar。
- HideWindowUI。
- NonFullScreenPageMode。
- PageLayout。
- PageMode。

それぞれは、以下のコードで使用され、説明されています。次のコードスニペットは、[Document](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document)クラスを使用してプロパティを設定する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetDocumentWindowProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetDocumentWindow.pdf"))
    {
        // Set different document properties
        // Specify to position document's window - Default: false
        document.CenterWindow = true;

        // Predominant reading order; determines the position of page
        // When displayed side by side - Default: L2R
        document.Direction = Aspose.Pdf.Direction.R2L;

        // Specify whether window's title bar should display document title
        // If false, title bar displays PDF file name - Default: false
        document.DisplayDocTitle = true;

        // Specify whether to resize the document's window to fit the size of
        // First displayed page - Default: false
        document.FitWindow = true;

        // Specify whether to hide menu bar of the viewer application - Default: false
        document.HideMenubar = true;

        // Specify whether to hide tool bar of the viewer application - Default: false
        document.HideToolBar = true;

        // Specify whether to hide UI elements like scroll bars
        // And leaving only the page contents displayed - Default: false
        document.HideWindowUI = true;

        // Document's page mode. Specify how to display document on exiting full-screen mode.
        document.NonFullScreenPageMode = Aspose.Pdf.PageMode.UseOC;

        // Specify the page layout i.e. single page, one column
        document.PageLayout = Aspose.Pdf.PageLayout.TwoColumnLeft;

        // Specify how the document should display when opened
        // I.e. show thumbnails, full-screen, show attachment panel
        document.PageMode = Aspose.Pdf.PageMode.UseThumbs;

        // Save PDF document
        document.Save(dataDir + "SetDocumentWindow_out.pdf");
    }
}
```

### 既存のPDFファイルにフォントを埋め込む

PDFリーダーは、プラットフォームに関係なくドキュメントが同じように表示されるように、[14のコアフォント](https://en.wikipedia.org/wiki/PDF#Text)をサポートしています。PDFに14のコアフォントのいずれかでないフォントが含まれている場合、フォント置換を避けるためにフォントをPDFファイルに埋め込む必要があります。

Aspose.PDF for .NETは、既存のPDFファイルへのフォント埋め込みをサポートしています。完全なフォントまたはフォントのサブセットを埋め込むことができます。フォントを埋め込むには、[Document](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document)クラスを使用してPDFファイルを開きます。次に、[Aspose.Pdf.Text.Font](https://reference.aspose.com/pdf/ja/net/aspose.pdf.text)クラスを使用してフォントをPDFファイルに埋め込みます。完全なフォントを埋め込むには、FontクラスのIsEmbededプロパティを使用します。フォントのサブセットを使用するには、IsSubsetプロパティを使用します。

{{% alert color="primary" %}}

フォントのサブセットは、使用される文字のみを埋め込み、短い文やスローガンにフォントが使用される場合に便利です。たとえば、企業フォントがロゴに使用されるが、本文には使用されない場合です。サブセットを使用すると、出力PDFのファイルサイズが削減されます。ただし、本文にカスタムフォントが使用されている場合は、完全に埋め込む必要があります。

{{% /alert %}}

次のコードスニペットは、PDFファイルにフォントを埋め込む方法を示しています。

### 標準タイプ1フォントの埋め込み

一部のPDFドキュメントには、特別なAdobeフォントセットからのフォントがあります。このセットのフォントは「標準タイプ1フォント」と呼ばれます。このセットには14のフォントが含まれており、このタイプのフォントを埋め込むには特別なフラグ、すなわち[Aspose.Pdf.Document.EmbedStandardFonts](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document/properties/embedstandardfonts)を使用する必要があります。以下は、標準タイプ1フォントを含むすべてのフォントが埋め込まれたドキュメントを取得するために使用できるコードスニペットです：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EmbedFontsType1ToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Set EmbedStandardFonts property of document
        document.EmbedStandardFonts = true;

        // Iterate through each page
        foreach (var page in document.Pages)
        {
            if (page.Resources.Fonts != null)
            {
                foreach (var pageFont in page.Resources.Fonts)
                {
                    // Check if font is already embedded
                    if (!pageFont.IsEmbedded)
                    {
                        pageFont.IsEmbedded = true;
                    }
                }
            }
        }

        // Save PDF document
        document.Save(dataDir + "EmbeddedFontsUpdated_out.pdf");
    }
}
```

### PDF作成時のフォントの埋め込み

Adobe Readerがサポートする14のコアフォント以外のフォントを使用する必要がある場合、PDFファイルを生成する際にフォントの説明を埋め込む必要があります。フォント情報が埋め込まれていない場合、Adobe Readerはそれがシステムにインストールされている場合はオペレーティングシステムから取得し、そうでない場合はPDF内のフォント記述子に従って代替フォントを構築します。

>埋め込まれたフォントはホストマシンにインストールされている必要があります。つまり、次のコードでは「Univers Condensed」フォントがシステムにインストールされている必要があります。

フォント情報をPDFファイルに埋め込むために、FontクラスのIsEmbeddedプロパティを使用します。このプロパティの値を「True」に設定すると、PDFに完全なフォントファイルが埋め込まれますが、PDFファイルのサイズが増加することを考慮する必要があります。以下は、PDFにフォント情報を埋め込むために使用できるコードスニペットです。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EmbedFontWhileCreatingPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Create a section in the Pdf object
        var page = document.Pages.Add();

        // Create a TextFragment
        var fragment = new Aspose.Pdf.Text.TextFragment("");

        // Create a TextSegment with sample text
        var segment = new Aspose.Pdf.Text.TextSegment(" This is a sample text using Custom font.");

        // Create and configure TextState
        var ts = new Aspose.Pdf.Text.TextState();
        ts.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        ts.Font.IsEmbedded = true;
        segment.TextState = ts;

        // Add the segment to the fragment
        fragment.Segments.Add(segment);

        // Add the fragment to the page
        page.Paragraphs.Add(fragment);

        // Save PDF Document
        document.Save(dataDir + "EmbedFontWhileDocCreation_out.pdf");
    }
}
```

### PDF保存時のデフォルトフォント名の設定

PDFドキュメントに、ドキュメント自体およびデバイス上で利用できないフォントが含まれている場合、APIはこれらのフォントをデフォルトフォントに置き換えます。フォントが利用可能な場合（デバイスにインストールされているか、ドキュメントに埋め込まれている場合）、出力PDFは同じフォントを持つべきです（デフォルトフォントに置き換えられるべきではありません）。デフォルトフォントの値にはフォントの名前（フォントファイルへのパスではない）を含める必要があります。ドキュメントをPDFとして保存する際にデフォルトフォント名を設定する機能を実装しました。以下のコードスニペットを使用してデフォルトフォントを設定できます：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetDefaultFontOnDocumentSave(string documentName, string newName)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var fs = new FileStream(dataDir + "GetDocumentWindow.pdf", FileMode.Open))
    {
        using (var document = new Aspose.Pdf.Document(fs))
        {
            // Create PdfSaveOptions and specify Default Font Name
            var pdfSaveOptions = new Aspose.Pdf.PdfSaveOptions
            {
                DefaultFontName = newName
            };

            // Save PDF document
            document.Save(dataDir + "DefaultFont_out.pdf", pdfSaveOptions);
        }
    }
}
```

### PDFドキュメントからすべてのフォントを取得

PDFドキュメントからすべてのフォントを取得したい場合は、[Document](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document)クラスで提供されているFontUtilities.GetAllFonts()メソッドを使用できます。既存のPDFドキュメントからすべてのフォントを取得するためのコードスニペットは以下の通りです：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetAllFontsFromPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get all fonts used in the document
        var fonts = document.FontUtilities.GetAllFonts();

        // Iterate through each font and print its name
        foreach (var font in fonts)
        {
            Console.WriteLine(font.FontName);
        }
    }
}
```

### フォント置換の警告を取得

Aspose.PDF for .NETは、フォント置換の通知を取得するためのメソッドを提供しており、フォント置換のケースを処理します。以下のコードスニペットは、対応する機能を使用する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void NotificationFontSubstitution()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Attach the FontSubstitution event handler
        document.FontSubstitution += OnFontSubstitution;
        // You can use lambda
        // (oldFont, newFont) => Console.WriteLine(string.Format("Font '{0}' was substituted with another font '{1}'",
        //                                                                        oldFont.FontName, newFont.FontName));

        // Save PDF document
        document.Save(dataDir + "NotificationFontSubstitution_out.pdf");
    }
}
```

**OnFontSubstitution**メソッドは以下の通りです。

```csharp
private static void OnFontSubstitution(Aspose.Pdf.Text.Font oldFont, Aspose.Pdf.Text.Font newFont)
{
    // Handle the font substitution event here
    Console.WriteLine(string.Format("Font '{0}' was substituted with another font '{1}'",
        oldFont.FontName, newFont.FontName));
}
```

### FontSubsetStrategyを使用したフォント埋め込みの改善

フォントをサブセットとして埋め込む機能は、IsSubsetプロパティを使用して実現できますが、時には完全に埋め込まれたフォントセットをドキュメントで使用されるサブセットのみに減らしたい場合があります。Aspose.Pdf.Documentには、FontSubsetStrategyを含むFontUtilitiesプロパティがあります。SubsetFonts(FontSubsetStrategy subsetStrategy)メソッドでは、パラメータsubsetStrategyがサブセット戦略を調整するのに役立ちます。FontSubsetStrategyは、フォントサブセットの2つのバリアントをサポートしています。

- SubsetAllFonts - これは、ドキュメントで使用されるすべてのフォントをサブセット化します。
- SubsetEmbeddedFontsOnly - これは、ドキュメントに完全に埋め込まれたフォントのみをサブセット化します。

以下のコードスニペットは、FontSubsetStrategyを設定する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetFontSubsetStrategy()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // All fonts will be embedded as subset into document in case of SubsetAllFonts.
        document.FontUtilities.SubsetFonts(Aspose.Pdf.FontSubsetStrategy.SubsetAllFonts);

        // Font subset will be embedded for fully embedded fonts but fonts which are not embedded into document will not be affected.
        document.FontUtilities.SubsetFonts(Aspose.Pdf.FontSubsetStrategy.SubsetEmbeddedFontsOnly);

        // Save PDF document
        document.Save(dataDir + "SetFontSubsetStrategy_out.pdf");
    }
}
```

### PDFファイルのズームファクターの取得と設定

時には、PDFドキュメントの現在のズームファクターを確認したい場合があります。Aspose.Pdfを使用すると、現在の値を確認することも、設定することもできます。

[GoToAction](https://reference.aspose.com/pdf/ja/net/aspose.pdf.annotations/gotoaction)クラスのDestinationプロパティを使用すると、PDFファイルに関連付けられたズーム値を取得できます。同様に、ファイルのズームファクターを設定するためにも使用できます。

#### ズームファクターの設定

以下のコードスニペットは、PDFファイルのズームファクターを設定する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetZoomFactor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetZoomFactor.pdf"))
    {
        // Create GoToAction with a specific zoom factor
        var action = new Aspose.Pdf.Annotations.GoToAction(new Aspose.Pdf.Annotations.XYZExplicitDestination(1, 0, 0, 0.5));
        document.OpenAction = action;

        // Save PDF document
        document.Save(dataDir + "ZoomFactor_out.pdf");
    }
}
```

#### ズームファクターの取得

以下のコードスニペットは、PDFファイルのズームファクターを取得する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetZoomFactor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Zoomed_pdf.pdf"))
    {
        // Create GoToAction object
        if (document.OpenAction is Aspose.Pdf.Annotations.GoToAction action)
        {
            // Get the Zoom factor of PDF file
            if (action.Destination is Aspose.Pdf.Annotations.XYZExplicitDestination destination)
            {
                System.Console.WriteLine(destination.Zoom); // Document zoom value;
            }
        }
    }
}
```

### 印刷ダイアログプリセットプロパティの設定

Aspose.PDFは、PDFドキュメントの印刷ダイアログプリセットプロパティを設定することを許可します。これにより、デフォルトで単面に設定されているPDFドキュメントのDuplexModeプロパティを変更できます。これは、以下に示す2つの異なる方法論を使用して達成できます。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrintDialogPresetProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        document.Pages.Add();

        // Set duplex printing to DuplexFlipLongEdge
        document.Duplex = Aspose.Pdf.PrintDuplex.DuplexFlipLongEdge;

        // Save PDF document
        document.Save(dataDir + "SetPrintDlgPresetProperties_out.pdf", Aspose.Pdf.SaveFormat.Pdf);
    }
}
```

### PDFコンテンツエディタを使用した印刷ダイアログプリセットプロパティの設定

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrintDialogPresetPropertiesUsingPdfContentEditor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    string inputFile = dataDir + "input.pdf";

    using (var ed = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        ed.BindPdf(inputFile);

        // Check if the file has duplex flip short edge
        if ((ed.GetViewerPreference() & Aspose.Pdf.Facades.ViewerPreference.DuplexFlipShortEdge) > 0)
        {
            Console.WriteLine("The file has duplex flip short edge");
        }

        // Change the viewer preference to duplex flip short edge
        ed.ChangeViewerPreference(Aspose.Pdf.Facades.ViewerPreference.DuplexFlipShortEdge);

        // Save PDF document
        ed.Save(dataDir + "SetPrintDlgPropertiesUsingPdfContentEditor_out.pdf");
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>