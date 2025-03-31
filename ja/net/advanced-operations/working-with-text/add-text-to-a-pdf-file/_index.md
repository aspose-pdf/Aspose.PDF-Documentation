---
title: PDFにテキストを追加する方法（C#を使用）
linktitle: PDFにテキストを追加
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ja/net/add-text-to-pdf-file/
description: Aspose.PDFを使用して.NETでPDFドキュメントにテキストを追加する方法を学び、コンテンツの強化とドキュメントの編集を行います。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Text to PDF using C#",
    "alternativeHeadline": "Add Custom Text to Existing PDFs with C#",
    "abstract": "Aspose.PDFのC#を使用したPDFにテキストを追加する機能により、開発者は既存のPDFドキュメント内でテキストをシームレスに統合および操作できます。テキストフラグメントの追加、カスタムOTFフォントの利用、HTMLコンテンツの追加などの機能により、この機能はドキュメントのフォーマットとプレゼンテーションを強化し、プログラム的にプロフェッショナルでカスタマイズされたPDFを作成しやすくします。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "5625",
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
    "url": "/net/add-text-to-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-text-to-pdf-file/"
    },
    "dateModified": "2024-11-26",
    "description": "この記事では、Aspose.PDFでのテキスト操作のさまざまな側面について説明します。PDFにテキストを追加する方法、HTMLフラグメントを追加する方法、またはカスタムOTFフォントを使用する方法を学びます。"
}
</script>

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも機能します。

既存のPDFファイルにテキストを追加するには：

1. Documentオブジェクトを使用して入力PDFを開きます。
2. テキストを追加したい特定のページを取得します。
3. 入力テキストと他のテキストプロパティを使用してTextFragmentオブジェクトを作成します。テキストを追加したい特定のページから作成されたTextBuilderオブジェクトを使用して、AppendTextメソッドを使用してTextFragmentオブジェクトをページに追加します。
4. DocumentオブジェクトのSaveメソッドを呼び出し、出力PDFファイルを保存します。

## テキストの追加

次のコードスニペットは、既存のPDFファイルにテキストを追加する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Get particular page
        var page = document.Pages.Add();

        // Create text fragment
        var textFragment = new Aspose.Pdf.Text.TextFragment("main text");
        textFragment.Position = new Aspose.Pdf.Text.Position(100, 600);

        // Set text properties
        textFragment.TextState.FontSize = 12;
        textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
        textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray);
        textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Red);

        // Create TextBuilder object
        var textBuilder = new Aspose.Pdf.Text.TextBuilder(page);

        // Append the text fragment to the PDF page
        textBuilder.AppendText(textFragment);

        // Save PDF document
        document.Save(dataDir + "AddText_out.pdf");
    }
}
```

## ストリームからフォントを読み込む

次のコードスニペットは、PDFドキュメントにテキストを追加する際にストリームオブジェクトからフォントを読み込む方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void LoadingFontFromStream()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();
    var fontFile = dataDir + "HPSimplified.ttf";

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "LoadFonts.pdf"))
    {
        // Create text builder object for first page of document
        var textBuilder = new Aspose.Pdf.Text.TextBuilder(document.Pages[1]);
        // Create text fragment with sample string
        var textFragment = new Aspose.Pdf.Text.TextFragment("Hello world");

        if (File.Exists(fontFile))
        {
            // Load the TrueType font into stream object
            using (FileStream fontStream = File.OpenRead(fontFile))
            {
                // Set the font name for text string
                textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.OpenFont(fontStream, Aspose.Pdf.Text.FontTypes.TTF);
                // Specify the position for Text Fragment
                textFragment.Position = new Aspose.Pdf.Text.Position(10, 10);
                // Add the text to TextBuilder so that it can be placed over the PDF file
                textBuilder.AppendText(textFragment);
            }

            // Save PDF document
            document.Save(dataDir + "LoadingFontFromStream_out.pdf");
        }
    }
}
```

## TextParagraphを使用してテキストを追加

次のコードスニペットは、[TextParagraph](https://reference.aspose.com/pdf/ja/net/aspose.pdf.text/textparagraph)クラスを使用してPDFドキュメントにテキストを追加する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextWithTextParagraph()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page to pages collection of Document object
        var page = document.Pages.Add();
        var builder = new Aspose.Pdf.Text.TextBuilder(page);
        // Create text paragraph
        var paragraph = new Aspose.Pdf.Text.TextParagraph();
        // Set subsequent lines indent
        paragraph.SubsequentLinesIndent = 20;
        // Specify the location to add TextParagraph
        paragraph.Rectangle = new Aspose.Pdf.Rectangle(100, 300, 200, 700);
        // Specify word wraping mode
        paragraph.FormattingOptions.WrapMode = Aspose.Pdf.Text.TextFormattingOptions.WordWrapMode.ByWords;
        // Create text fragment
        var fragment = new Aspose.Pdf.Text.TextFragment("the quick brown fox jumps over the lazy dog");
        fragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Times New Roman");
        fragment.TextState.FontSize = 12;
        // Add fragment to paragraph
        paragraph.AppendLine(fragment);
        // Add paragraph
        builder.AppendParagraph(paragraph);

        // Save PDF document
        document.Save(dataDir + "AddTextUsingTextParagraph_out.pdf");
    }
}
```

## TextSegmentにハイパーリンクを追加

PDFページは1つ以上のTextFragmentオブジェクトで構成される場合があり、各TextFragmentオブジェクトには1つ以上のTextSegmentインスタンスを持つことができます。TextSegmentにハイパーリンクを設定するには、[TextSegment](https://reference.aspose.com/pdf/ja/net/aspose.pdf.text/textsegment)クラスのHyperlinkプロパティを使用し、Aspose.Pdf.WebHyperlinkインスタンスのオブジェクトを提供します。次のコードスニペットを使用してこの要件を達成してください。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHyperlinkToTextSegment()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create TextFragment instance
        var fragment = new Aspose.Pdf.Text.TextFragment("Sample Text Fragment");
        // Set horizontal alignment for TextFragment
        fragment.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
        // Create a textsegment with sample text
        var segment = new Aspose.Pdf.Text.TextSegment(" ... Text Segment 1...");
        // Add segment to segments collection of TextFragment
        fragment.Segments.Add(segment);
        // Create a new TextSegment
        segment = new Aspose.Pdf.Text.TextSegment("Link to Google");
        // Add segment to segments collection of TextFragment
        fragment.Segments.Add(segment);
        // Set hyperlink for TextSegment
        segment.Hyperlink = new Aspose.Pdf.WebHyperlink("www.google.com");
        // Set forground color for text segment
        segment.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
        // Set text formatting as italic
        segment.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Italic;
        // Create another TextSegment object
        segment = new Aspose.Pdf.Text.TextSegment("TextSegment without hyperlink");
        // Add segment to segments collection of TextFragment
        fragment.Segments.Add(segment);
        // Add TextFragment to paragraphs collection of page object
        page.Paragraphs.Add(fragment);

        // Save PDF document
        document.Save(dataDir + "AddHyperlinkToTextSegment_out.pdf");
    }
}
```

## OTFフォントを使用

Aspose.PDF for .NETは、PDFファイルのコンテンツを作成/操作する際にカスタム/TrueTypeフォントを使用する機能を提供し、ファイルの内容がデフォルトのシステムフォント以外の内容で表示されるようにします。Aspose.PDF for .NETのリリース10.3.0以降、Open Type Fontsのサポートが提供されています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UseOTFFont()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create TextFragment instnace with sample text
        var fragment = new Aspose.Pdf.Text.TextFragment("Sample Text in OTF font");
        // Find font inside system font directory
        // Fragment.TextState.Font = FontRepository.FindFont("HelveticaNeueLT Pro 45 Lt");
        // Or you can even specify the path of OTF font in system directory
        fragment.TextState.Font = Aspose.Pdf.Text.FontRepository.OpenFont(dataDir + "space age.otf");
        // Specify to emend font inside PDF file, so that its displayed properly,
        // Even if specific font is not installed/present over target machine
        fragment.TextState.Font.IsEmbedded = true;
        // Add TextFragment to paragraphs collection of Page instance
        page.Paragraphs.Add(fragment);

        // Save PDF document
        document.Save(dataDir + "OTFFont_out.pdf");
    }
}
```

## DOMを使用してHTML文字列を追加

Aspose.Pdf.Generator.Textクラスには、PDFファイルにHTMLタグ/コンテンツを追加できるIsHtmlTagSupportedというプロパティがあります。追加されたコンテンツは、単純なテキスト文字列として表示されるのではなく、ネイティブHTMLタグでレンダリングされます。Aspose.Pdf名前空間の新しいドキュメントオブジェクトモデル（DOM）で同様の機能をサポートするために、HtmlFragmentクラスが導入されました。

[HtmlFragment](https://reference.aspose.com/pdf/ja/net/aspose.pdf/htmlfragment)インスタンスを使用して、PDFファイル内に配置するHTMLコンテンツを指定できます。TextFragmentと同様に、HtmlFragmentは段落レベルのオブジェクトであり、Pageオブジェクトの段落コレクションに追加できます。次のコードスニペットは、DOMアプローチを使用してPDFファイル内にHTMLコンテンツを配置する手順を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHTMLStringUsingDOM()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add a page to pages collection of PDF file
        var page = document.Pages.Add();
        // Instantiate HtmlFragment with HTML contnets
        var title = new Aspose.Pdf.HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>");
        // Set bottom margin information
        title.Margin.Bottom = 10;
        // Set top margin information
        title.Margin.Top = 200;
        // Add HTML Fragment to paragraphs collection of page
        page.Paragraphs.Add(title);

        // Save PDF document
        document.Save(dataDir + "AddHTMLUsingDOM_out.pdf");
    }
}
```

次のコードスニペットは、ドキュメントにHTMLの順序付きリストを追加する手順を示しています：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHTMLOrderedListIntoDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Instantiate HtmlFragment object with corresponding HTML fragment 
        var fragment = new Aspose.Pdf.HtmlFragment("`<body style='line-height: 100px;'><ul><li>First</li><li>Second</li><li>Third</li><li>Fourth</li><li>Fifth</li></ul>Text after the list.<br/>Next line<br/>Last line</body>`");
        // Add Page in Pages Collection 
        var page = document.Pages.Add();
        // Add HtmlFragment inside page 
        page.Paragraphs.Add(fragment);

        // Save PDF document
        document.Save(dataDir + "AddHTMLOrderedListIntoDocuments_out.pdf");
    }
}
```

TextStateオブジェクトを使用してHTML文字列のフォーマットを設定することもできます：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetHTMLStringFormatting()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var fragment = new Aspose.Pdf.HtmlFragment("some text");
        fragment.TextState = new Aspose.Pdf.Text.TextState();
        fragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Calibri");
        // Add Page in Pages Collection 
        var page = document.Pages.Add();
        // Add HtmlFragment inside page 
        page.Paragraphs.Add(fragment);

        // Save PDF document
        document.Save(dataDir + "SetHTMLStringFormatting_out.pdf");
    }
}
```

HTMLマークアップを介してテキスト属性値を設定し、その後TextStateプロパティに同じ値を提供した場合、TextStateインスタンスのプロパティによってHTMLパラメータが上書きされます。次のコードスニペットは、説明された動作を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHTMLUsingDOMAndOverwrite()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add a page to pages collection of PDF file
        var page = document.Pages.Add();
        // Instantiate HtmlFragment with HTML contnets
        var title = new Aspose.Pdf.HtmlFragment("<p style='font-family: Verdana'><b><i>Table contains text</i></b></p>");
        //Font-family from 'Verdana' will be reset to 'Arial'
        title.TextState = new Aspose.Pdf.Text.TextState("Arial");
        title.TextState.FontSize = 20;
        // Set bottom margin information
        title.Margin.Bottom = 10;
        // Set top margin information
        title.Margin.Top = 400;
        // Add HTML Fragment to paragraphs collection of page
        page.Paragraphs.Add(title);
        
        // Save PDF document
        document.Save(dataDir + "AddHTMLUsingDOMAndOverwrite_out.pdf");
    }
}
```

## フットノートとエンドノート（DOM）

フットノートは、連続した上付き数字を使用して論文のテキスト内のノートを示します。実際のノートはインデントされ、ページの下部にフットノートとして表示されることがあります。

### フットノートの追加

フットノート参照システムでは、次のように参照を示します：

- ソース資料に直接続く行の上に小さな数字を置きます。この数字はノート識別子と呼ばれ、テキストの行の少し上に位置します。
- ページの下部に同じ数字を置き、その後にソースの引用を記載します。フットノートは数値的かつ年代順であるべきです：最初の参照は1、次は2、そしてその後も続きます。

フットノートの利点は、読者がページの下に目を向けるだけで、興味のある参照の出所を発見できることです。

フットノートを作成するために、以下の手順に従ってください：

- Documentインスタンスを作成します。
- Pageオブジェクトを作成します。
- TextFragmentオブジェクトを作成します。
- Noteインスタンスを作成し、その値をTextFragment.FootNoteプロパティに渡します。
- TextFragmentをページインスタンスの段落コレクションに追加します。

### フットノートのカスタムラインスタイル

次の例は、PDFページの下部にフットノートを追加し、カスタムラインスタイルを定義する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CustomLineStyleForFootNote()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create GraphInfo object
        var graph = new Aspose.Pdf.GraphInfo();
        // Set line width as 2
        graph.LineWidth = 2;
        // Set the color for graph object
        graph.Color = Aspose.Pdf.Color.Red;
        // Set dash array value as 3
        graph.DashArray = new int[] { 3 };
        // Set dash phase value as 1
        graph.DashPhase = 1;
        // Set footnote line style for page as graph
        page.NoteLineStyle = graph;
        // Create TextFragment instance
        var text = new Aspose.Pdf.Text.TextFragment("Hello World");
        // Set FootNote value for TextFragment
        text.FootNote = new Aspose.Pdf.Note("foot note for test text 1");
        // Add TextFragment to paragraphs collection of first page of document
        page.Paragraphs.Add(text);
        // Create second TextFragment
        text = new Aspose.Pdf.Text.TextFragment("Aspose.PDF for .NET");
        // Set FootNote for second text fragment
        text.FootNote = new Aspose.Pdf.Note("foot note for test text 2");
        // Add second text fragment to paragraphs collection of PDF file
        page.Paragraphs.Add(text);

        // Save PDF document
        document.Save(dataDir + "CustomLineStyleForFootNote_out.pdf");
    }
}
```

フットノートラベル（ノート識別子）のフォーマットをTextStateオブジェクトを使用して次のように設定できます：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FormattingUsingTextStateObject()
{
    var text = new Aspose.Pdf.Text.TextFragment("test text 1");
    text.FootNote = new Aspose.Pdf.Note("foot note for test text 1");
    text.FootNote.Text = "21";
    text.FootNote.TextState = new Aspose.Pdf.Text.TextState();
    text.FootNote.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    text.FootNote.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Italic;
}
```

### フットノートラベルのカスタマイズ

デフォルトでは、フットノート番号は1から始まる増分です。ただし、カスタムフットノートラベルを設定する必要がある場合があります。この要件を達成するために、次のコードスニペットを使用してください。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CustomizeFootNoteLabel()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create GraphInfo object
        var graph = new Aspose.Pdf.GraphInfo();
        // Set line width as 2
        graph.LineWidth = 2;
        // Set the color for graph object
        graph.Color = Aspose.Pdf.Color.Red;
        // Set dash array value as 3
        graph.DashArray = new int[] { 3 };
        // Set dash phase value as 1
        graph.DashPhase = 1;
        // Set footnote line style for page as graph
        page.NoteLineStyle = graph;
        // Create TextFragment instance
        var text = new Aspose.Pdf.Text.TextFragment("Hello World");
        // Set FootNote value for TextFragment
        text.FootNote = new Aspose.Pdf.Note("foot note for test text 1");
        // Specify custom label for FootNote
        text.FootNote.Text = " Aspose(2015)";
        // Add TextFragment to paragraphs collection of first page of document
        page.Paragraphs.Add(text);

        // Save PDF document
        document.Save(dataDir + "CustomizeFootNoteLabel_out.pdf");
    }
}
```

## フットノートに画像とテーブルを追加

以前のリリースバージョンでは、フットノートのサポートが提供されていましたが、これはTextFragmentオブジェクトにのみ適用されていました。しかし、Aspose.PDF for .NETのリリース10.7.0以降、テーブル、セルなどのPDFドキュメント内の他のオブジェクトにもフットノートを追加できるようになりました。次のコードスニペットは、TextFragmentオブジェクトにフットノートを追加し、その後フットノートセクションの段落コレクションに画像とテーブルオブジェクトを追加する手順を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageAndTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        var text = new Aspose.Pdf.Text.TextFragment("some text");
        page.Paragraphs.Add(text);

        text.FootNote = new Aspose.Pdf.Note();
        // Create image
        Aspose.Pdf.Image image = new Aspose.Pdf.Image();
        image.File = dataDir + "aspose-logo.jpg";
        image.FixHeight = 20;
        text.FootNote.Paragraphs.Add(image);

        var footNote = new Aspose.Pdf.Text.TextFragment("footnote text");
        footNote.TextState.FontSize = 20;
        footNote.IsInLineParagraph = true;
        text.FootNote.Paragraphs.Add(footNote);

        var table = new Aspose.Pdf.Table();
        table.Rows.Add().Cells.Add().Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Row 1 Cell 1"));
        text.FootNote.Paragraphs.Add(table);

        // Save PDF document
        document.Save(dataDir + "AddImageAndTable_out.pdf");
    }
}
```

## エンドノートの作成方法

エンドノートは、読者を論文の最後の特定の場所に参照させる情報源の引用であり、そこで情報や引用された言葉の出所を見つけることができます。エンドノートを使用する場合、引用または要約された文の後に上付き数字が続きます。

次の例は、PDFページにエンドノートを追加する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateEndNotes()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create TextFragment instance
        var text = new Aspose.Pdf.Text.TextFragment("Hello World");
        // Set FootNote value for TextFragment
        text.EndNote = new Aspose.Pdf.Note("sample End note");
        // Specify custom label for FootNote
        text.EndNote.Text = " Aspose(2015)";
        // Add TextFragment to paragraphs collection of first page of document
        page.Paragraphs.Add(text);

        // Save PDF document
        document.Save(dataDir + "CreateEndNotes_out.pdf");
    }
}
```

## テキストと画像をインライン段落として

PDFファイルのデフォルトのレイアウトはフローレイアウト（左上から右下）です。したがって、PDFファイルに追加される新しい要素は、右下のフローに追加されます。ただし、画像とテキストなどのさまざまなページ要素を同じレベル（互いに続けて）で表示する必要がある場合があります。一つのアプローチは、Tableインスタンスを作成し、両方の要素を個別のセルオブジェクトに追加することです。しかし、別のアプローチはインライン段落です。画像とテキストのIsInLineParagraphプロパティをtrueに設定することで、これらの段落は他のページ要素にインラインで表示されます。

次のコードスニペットは、PDFファイルにテキストと画像をインライン段落として追加する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void TextAndImageAsParagraph()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page to pages collection of Document instance
        var page = document.Pages.Add();
        // Create TextFragmnet
        var text = new Aspose.Pdf.Text.TextFragment("Hello World.. ");
        // Add text fragment to paragraphs collection of Page object
        page.Paragraphs.Add(text);
        // Create an image instance
        var image = new Aspose.Pdf.Image();
        // Set image as inline paragraph so that it appears right after
        // The previous paragraph object (TextFragment)
        image.IsInLineParagraph = true;
        // Specify image file path
        image.File = dataDir + "aspose-logo.jpg";
        // Set image Height (optional)
        image.FixHeight = 30;
        // Set Image Width (optional)
        image.FixWidth = 100;
        // Add image to paragraphs collection of page object
        page.Paragraphs.Add(image);
        // Re-initialize TextFragment object with different contents
        text = new Aspose.Pdf.Text.TextFragment(" Hello Again..");
        // Set TextFragment as inline paragraph
        text.IsInLineParagraph = true;
        // Add newly created TextFragment to paragraphs collection of page
        page.Paragraphs.Add(text);

        // Save PDF document
        document.Save(dataDir + "TextAndImageAsParagraph_out.pdf");
    }
}
```

## テキストを追加する際の文字間隔の指定

テキストはTextFragmentインスタンスを使用してPDFファイルの段落コレクション内に追加することができ、TextParagraphオブジェクトを使用したり、TextStampクラスを使用してPDF内にテキストをスタンプすることもできます。テキストを追加する際に、テキストオブジェクトの文字間隔を指定する必要がある場合があります。この要件を達成するために、CharacterSpacingという新しいプロパティが導入されました。以下のアプローチを参照して、この要件を満たす方法を確認してください。

次のアプローチは、PDFドキュメントにテキストを追加する際に文字間隔を指定する手順を示しています。

### TextBuilderとTextFragmentを使用

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CharacterSpacingUsingTextBuilderAndFragment()
{            
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page to pages collection of Document
        document.Pages.Add();
        // Create TextBuilder instance
        var builder = new Aspose.Pdf.Text.TextBuilder(document.Pages[1]);
        // Create text fragment instance with sample contents
        var wideFragment = new Aspose.Pdf.Text.TextFragment("Text with increased character spacing");
        wideFragment.TextState.ApplyChangesFrom(new Aspose.Pdf.Text.TextState("Arial", 12));
        // Specify character spacing for TextFragment
        wideFragment.TextState.CharacterSpacing = 2.0f;
        // Specify the position of TextFragment
        wideFragment.Position = new Aspose.Pdf.Text.Position(100, 650);
        // Append TextFragment to TextBuilder instance
        builder.AppendText(wideFragment);

        // Save PDF document
        document.Save(dataDir + "CharacterSpacingUsingTextBuilderAndFragment_out.pdf");
    }
}
```

### TextParagraphを使用

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CharacterSpacingUsingTextBuilderAndParagraph()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page to pages collection of Document
        var page = document.Pages.Add();
        // Create TextBuilder instance
        var builder = new Aspose.Pdf.Text.TextBuilder(page);
        // Instantiate TextParagraph instance
        var paragraph = new Aspose.Pdf.Text.TextParagraph();
        // Create TextState instance to specify font name and size
        var state = new Aspose.Pdf.Text.TextState("Arial", 12);
        // Specify the character spacing
        state.CharacterSpacing = 1.5f;
        // Append text to TextParagraph object
        paragraph.AppendLine("This is paragraph with character spacing", state);
        // Specify the position for TextParagraph
        paragraph.Position = new Aspose.Pdf.Text.Position(100, 550);
        // Append TextParagraph to TextBuilder instance
        builder.AppendParagraph(paragraph);

        // Save PDF document
        document.Save(dataDir + "CharacterSpacingUsingTextBuilderAndParagraph_out.pdf");
    }
}
```

### TextStampを使用

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CharacterSpacingUsingTextStamp()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page to pages collection of Document
        var page = document.Pages.Add();
        // Instantiate TextStamp instance with sample text
        var stamp = new Aspose.Pdf.TextStamp("This is text stamp with character spacing");
        // Specify font name for Stamp object
        stamp.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        // Specify Font size for TextStamp
        stamp.TextState.FontSize = 12;
        // Specify character specing as 1f
        stamp.TextState.CharacterSpacing = 1f;
        // Set the XIndent for Stamp
        stamp.XIndent = 100;
        // Set the YIndent for Stamp
        stamp.YIndent = 500;
        // Add textual stamp to page instance
        stamp.Put(page);

        // Save PDF document
        document.Save(dataDir + "CharacterSpacingUsingTextStamp_out.pdf");
    }
}
```

## マルチカラムPDFドキュメントの作成

雑誌や新聞では、ニュースが通常、ページの左から右にかけて印刷される本とは異なり、単一のページに複数のカラムで表示されることがよくあります。Microsoft WordやAdobe Acrobat Writerなどの多くの文書処理アプリケーションでは、ユーザーが単一のページに複数のカラムを作成し、それにデータを追加することができます。

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/)もPDFドキュメントのページ内に複数のカラムを作成する機能を提供しています。マルチカラムPDFファイルを作成するには、Aspose.Pdf.FloatingBoxクラスを使用できます。これは、FloatingBox内のカラム数を指定するColumnInfo.ColumnCountプロパティを提供し、ColumnInfo.ColumnSpacingおよびColumnInfo.ColumnWidthsプロパティを使用してカラム間の間隔とカラムの幅を指定できます。FloatingBoxはドキュメントオブジェクトモデル内の要素であり、相対位置付け（テキスト、グラフ、画像など）と比較して古い位置付けを持つことに注意してください。

カラム間隔はカラム間のスペースを意味し、カラム間のデフォルトの間隔は1.25cmです。カラム幅が指定されていない場合、[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/)はページサイズとカラム間隔に応じて各カラムの幅を自動的に計算します。

以下の例は、グラフオブジェクト（ライン）を持つ2つのカラムを作成し、それらをFloatingBoxの段落コレクションに追加し、その後ページインスタンスの段落コレクションに追加する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateMultiColumnPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Specify the left margin info for the PDF file
        document.PageInfo.Margin.Left = 40;
        // Specify the Right margin info for the PDF file
        document.PageInfo.Margin.Right = 40;
        var page = document.Pages.Add();

        var graph1 = new Aspose.Pdf.Drawing.Graph(500, 2);
        // Add the line to paraphraphs collection of section object
        page.Paragraphs.Add(graph1);

        // Specify the coordinates for the line
        float[] posArr = new float[] { 1, 2, 500, 2 };
        var line1 = new Aspose.Pdf.Drawing.Line(posArr);
        graph1.Shapes.Add(line1);
        // Create string variables with text containing html tags
        string s = "<font face=\"Times New Roman\" size=4>" +

        "<strong> How to Steer Clear of money scams</<strong> "
        + "</font>";
        // Create text paragraphs containing HTML text
        var heading_text = new Aspose.Pdf.HtmlFragment(s);
        page.Paragraphs.Add(heading_text);

        var box = new Aspose.Pdf.FloatingBox();
        // Add four columns in the section
        box.ColumnInfo.ColumnCount = 2;
        // Set the spacing between the columns
        box.ColumnInfo.ColumnSpacing = "5";

        box.ColumnInfo.ColumnWidths = "105 105";
        var text1 = new Aspose.Pdf.Text.TextFragment("By A Googler (The Official Google Blog)");
        text1.TextState.FontSize = 8;
        text1.TextState.LineSpacing = 2;
        box.Paragraphs.Add(text1);
        text1.TextState.FontSize = 10;

        text1.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Italic;
        // Create a graphs object to draw a line
        var graph2 = new Aspose.Pdf.Drawing.Graph(50, 10);
        // Specify the coordinates for the line
        float[] posArr2 = new float[] { 1, 10, 100, 10 };
        var line2 = new Aspose.Pdf.Drawing.Line(posArr2);
        graph2.Shapes.Add(line2);

        // Add the line to paragraphs collection of section object
        box.Paragraphs.Add(graph2);

        var text2 = new Aspose.Pdf.Text.TextFragment(@"Sed augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue. Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et,nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.");
        box.Paragraphs.Add(text2);

        page.Paragraphs.Add(box);

        // Save PDF document
        document.Save(dataDir + "CreateMultiColumnPdf_out.pdf");
    }
}
```

## カスタムタブストップの操作

タブストップは、タブを押すための停止ポイントです。ワードプロセッシングでは、各行には定期的な間隔で配置されたタブストップの数があります（たとえば、毎インチ半）。ただし、ほとんどのワードプロセッサでは、タブストップを任意の場所に設定できるため、変更できます。タブキーを押すと、カーソルまたは挿入ポイントは次のタブストップにジャンプしますが、タブストップ自体は見えません。タブストップはテキストファイルには存在しませんが、ワードプロセッサはそれらを追跡して、タブキーに正しく反応できるようにします。

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/)は、PDFドキュメントでカスタムタブストップを使用することを許可します。Aspose.Pdf.Text.TabStopクラスは、[TextFragment](https://reference.aspose.com/pdf/ja/net/aspose.pdf.text/textfragment)クラスでカスタムタブストップを設定するために使用されます。

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/)は、TabLeaderTypeという列挙型としていくつかの事前定義されたタブリーダータイプも提供しており、その事前定義された値と説明は以下の通りです：

|**タブリーダータイプ**|**説明**|
| :- | :- |
|なし|タブリーダーなし|
|ソリッド|ソリッドタブリーダー|
|ダッシュ|ダッシュタブリーダー|
|ドット|ドットタブリーダー|

以下は、カスタムタブストップを設定する方法の例です。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CustomTabStops()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        var tabStops = new Aspose.Pdf.Text.TabStops();
        var tabStop1 = tabStops.Add(100);
        tabStop1.AlignmentType = Aspose.Pdf.Text.TabAlignmentType.Right;
        tabStop1.LeaderType = Aspose.Pdf.Text.TabLeaderType.Solid;

        var tabStop2 = tabStops.Add(200);
        tabStop2.AlignmentType = Aspose.Pdf.Text.TabAlignmentType.Center;
        tabStop2.LeaderType = Aspose.Pdf.Text.TabLeaderType.Dash;

        var tabStop3 = tabStops.Add(300);
        tabStop3.AlignmentType = Aspose.Pdf.Text.TabAlignmentType.Left;
        tabStop3.LeaderType = Aspose.Pdf.Text.TabLeaderType.Dot;

        var header = new Aspose.Pdf.Text.TextFragment("This is a example of forming table with TAB stops", tabStops);
        var text0 = new Aspose.Pdf.Text.TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", tabStops);
        var text1 = new Aspose.Pdf.Text.TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", tabStops);
        var text2 = new Aspose.Pdf.Text.TextFragment("#$TABdata21 ", tabStops);
        text2.Segments.Add(new Aspose.Pdf.Text.TextSegment("#$TAB"));
        text2.Segments.Add(new Aspose.Pdf.Text.TextSegment("data22 "));
        text2.Segments.Add(new Aspose.Pdf.Text.TextSegment("#$TAB"));
        text2.Segments.Add(new Aspose.Pdf.Text.TextSegment("data23"));

        // Add text fragments to page
        page.Paragraphs.Add(header);
        page.Paragraphs.Add(text0);
        page.Paragraphs.Add(text1);
        page.Paragraphs.Add(text2);

        // Save PDF document
        document.Save(dataDir + "CustomTabStops_out.pdf");
    }
}
```

## PDFに透明なテキストを追加する方法

PDFファイルには、画像、テキスト、グラフ、添付ファイル、注釈オブジェクトが含まれており、TextFragmentを作成する際に前景、背景色情報、およびテキストフォーマットを設定できます。Aspose.PDF for .NETは、アルファカラーチャンネルを使用してテキストを追加する機能をサポートしています。次のコードスニペットは、透明な色でテキストを追加する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTransparentText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Create page to pages collection of PDF file
        var page = document.Pages.Add();

        // Create Graph object
        var canvas = new Aspose.Pdf.Drawing.Graph(100, 400);
        // Create rectangle instance with certain dimensions
        var rect = new Aspose.Pdf.Drawing.Rectangle(100, 100, 400, 400);
        // Create color object from Alpha color channel
        rect.GraphInfo.FillColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.FromArgb(128, System.Drawing.Color.FromArgb(12957183)));
        // Add rectanlge to shapes collection of Graph object
        canvas.Shapes.Add(rect);
        // Add graph object to paragraphs collection of page object
        page.Paragraphs.Add(canvas);
        // Set value to not change position for graph object
        canvas.IsChangePosition = false;

        // Create TextFragment instance with sample value
        var text = new Aspose.Pdf.Text.TextFragment("transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text ");
        // Create color object from Alpha channel
        Aspose.Pdf.Color color = Aspose.Pdf.Color.FromArgb(30, 0, 255, 0);
        // Set color information for text instance
        text.TextState.ForegroundColor = color;
        // Add text to paragraphs collection of page instance
        page.Paragraphs.Add(text);

        // Save PDF document
        document.Save(dataDir + "AddTransparentText_out.pdf");
    }
}
```

## フォントの行間隔を指定する

すべてのフォントには、同じサイズのタイプの行間の意図された距離の高さを持つ抽象的な正方形があります。この正方形はem正方形と呼ばれ、グリフのアウトラインが定義されるデザイングリッドです。入力フォントの多くの文字には、フォントのem正方形の境界を超えて配置されたポイントがあります。そのため、フォントを正しく表示するには、特別な設定の使用が必要です。TextFragmentオブジェクトには、TextState.FormattingOptionsプロパティを介してアクセスできる一連のテキストフォーマットオプションがあります。このパスの最後のプロパティは、Aspose.Pdf.Text.TextFormattingOptions型のプロパティです。このクラスには、特定のフォント（例：入力フォント"HPSimplified.ttf"）用に設計された列挙型[LineSpacingMode](https://reference.aspose.com/pdf/ja/net/aspose.pdf.text.textformattingoptions/linespacingmode)があります。また、[Aspose.Pdf.Text.TextFormattingOptions](https://reference.aspose.com/pdf/ja/net/aspose.pdf.text/textformattingoptions)クラスには、LineSpacingMode型の[LineSpacing](https://reference.aspose.com/pdf/ja/net/aspose.pdf.text/textformattingoptions/properties/linespacing)プロパティがあります。LineSpacingをLineSpacingMode.FullSizeに設定するだけです。フォントを正しく表示するためのコードスニペットは次のようになります：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SpecifyLineSpacing()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    string fontFile = dataDir + "HPSimplified.TTF";

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        //Create TextFormattingOptions with LineSpacingMode.FullSize
        var formattingOptions = new Aspose.Pdf.Text.TextFormattingOptions();
        formattingOptions.LineSpacing = Aspose.Pdf.Text.TextFormattingOptions.LineSpacingMode.FullSize;

        // Create text builder object for first page of document
        //TextBuilder textBuilder = new TextBuilder(document.Pages[1]);
        // Create text fragment with sample string
        var textFragment = new Aspose.Pdf.Text.TextFragment("Hello world");

        if (fontFile != "")
        {
            // Load the TrueType font into stream object
            using (FileStream fontStream = File.OpenRead(fontFile))
            {
                // Set the font name for text string
                textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.OpenFont(fontStream, Aspose.Pdf.Text.FontTypes.TTF);
                // Specify the position for Text Fragment
                textFragment.Position = new Aspose.Pdf.Text.Position(100, 600);
                //Set TextFormattingOptions of current fragment to predefined(which points to LineSpacingMode.FullSize)
                textFragment.TextState.FormattingOptions = formattingOptions;
                // Add the text to TextBuilder so that it can be placed over the PDF file
                //textBuilder.AppendText(textFragment);
                var page = document.Pages.Add();
                page.Paragraphs.Add(textFragment);
            }

            // Save PDF document
            document.Save(dataDir + "SpecifyLineSpacing_out.pdf");
        }
    }
}
```

## テキスト幅を動的に取得する

時には、テキスト幅を動的に取得する必要があります。Aspose.PDF for .NETには、文字列の幅を測定するための2つのメソッドが含まれています。Aspose.Pdf.Text.FontまたはAspose.Pdf.Text.TextStateクラスの[MeasureString](https://reference.aspose.com/pdf/ja/net/aspose.pdf.text/font/methods/measurestring)メソッドを呼び出すことができます（または両方）。以下のコードスニペットは、この機能を使用する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetTextWidthDynamically()
{            
    var font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
    var textState = new Aspose.Pdf.Text.TextState();
    textState.Font = font;
    textState.FontSize = 14;

    if (Math.Abs(font.MeasureString("A", 14) - 9.337) > 0.001)
    {
        Console.WriteLine("Unexpected font string measure!");
    }

    if (Math.Abs(textState.MeasureString("z") - 7.0) > 0.001)
    {
        Console.WriteLine("Unexpected font string measure!");
    }

    for (char c = 'A'; c <= 'z'; c++)
    {
        double fontMeasure = font.MeasureString(c.ToString(), 14);
        double textStateMeasure = textState.MeasureString(c.ToString());

        if (Math.Abs(fontMeasure - textStateMeasure) > 0.001)
        {
            Console.WriteLine("Font and state string measuring doesn't match!");
        }
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