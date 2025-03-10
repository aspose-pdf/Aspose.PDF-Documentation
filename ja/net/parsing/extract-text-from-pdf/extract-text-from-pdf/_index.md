---
title: PDFからテキストを抽出する C#
linktitle: PDFからテキストを抽出する
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ja/net/extract-text-from-all-pdf/
description: この記事では、C#でAspose.PDFを使用してPDF文書からテキストを抽出するさまざまな方法について説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Text from PDF C#",
    "alternativeHeadline": "Effortlessly Extract Text from PDFs in C#",
    "abstract": "開発者がPDF文書からテキストを簡単に抽出できる強力な新機能を発見してください。この機能は、すべてのページまたは特定の領域からの抽出をサポートし、マルチカラムレイアウトに対応し、わずか数行のコードでハイライトされたテキストの取得を可能にします。この多用途なツールを使用して、文書処理能力を向上させ、コンテンツ抽出を効率化します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "2005",
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
    "url": "/net/extract-text-from-all-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-text-from-all-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## PDF文書のすべてのページからテキストを抽出する

PDF文書からテキストを抽出することは一般的な要件です。この例では、Aspose.PDF for .NETがPDF文書のすべてのページからテキストを抽出する方法を示します。**TextAbsorber**クラスのオブジェクトを作成する必要があります。その後、**Document**クラスを使用してPDFを開き、**Pages**コレクションの**Accept**メソッドを呼び出します。**TextAbsorber**クラスは文書からテキストを吸収し、**Text**プロパティで返します。以下のコードスニペットは、PDF文書のすべてのページからテキストを抽出する方法を示しています。

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextFromDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextAll.pdf"))
    {
        // Create TextAbsorber object to extract text
        var textAbsorber = new Aspose.Pdf.Text.TextAbsorber();

        // Accept the absorber for all the pages
        document.Pages.Accept(textAbsorber);

        // Get the extracted text
        string extractedText = textAbsorber.Text;

        // Create a writer and open the file
        using (TextWriter tw = new StreamWriter(dataDir + "extracted-text.txt"))
        {
            // Write a line of text to the file
            tw.WriteLine(extractedText);
        }
    }
}
```

Documentオブジェクトの特定のページで**Accept**メソッドを呼び出します。インデックスは、テキストを抽出する必要がある特定のページ番号です。

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextFromPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {

        // Create TextAbsorber object to extract text
        var textAbsorber = new Aspose.Pdf.Text.TextAbsorber();

        // Accept the absorber for a particular page
        document.Pages[1].Accept(textAbsorber);

        // Get the extracted text
        string extractedText = textAbsorber.Text;

        // Create a writer and open the file
        using (TextWriter tw = new StreamWriter(dataDir + "extracted-text_out.txt"))
        {
            // Write a line of text to the file
            tw.WriteLine(extractedText);
        }
    }
}
```

## テキストデバイスを使用してページからテキストを抽出する

**TextDevice**クラスを使用してPDFファイルからテキストを抽出できます。TextDeviceはその実装でTextAbsorberを使用しているため、実際には同じことを行いますが、TextDeviceはページから何かを抽出するための「デバイス」アプローチを統一するために実装されています。TextAbsorberはページ、全PDF、またはXFormからテキストを抽出できますが、このTextAbsorberはより汎用的です。

### すべてのページからテキストを抽出する

以下の手順とコードスニペットは、テキストデバイスを使用してPDFからテキストを抽出する方法を示しています。

1. 入力PDFファイルを指定してDocumentクラスのオブジェクトを作成します。
1. TextDeviceクラスのオブジェクトを作成します。
1. TextExtractOptionsクラスのオブジェクトを使用して抽出オプションを指定します。
1. TextDeviceクラスのProcessメソッドを使用して内容をテキストに変換します。
1. テキストを出力ファイルに保存します。

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextFromPagesWithTextDevice()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    var builder = new System.Text.StringBuilder();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {
        // String to hold extracted text
        string extractedText = "";

        foreach (var page in document.Pages)
        {
            using (MemoryStream textStream = new MemoryStream())
            {
                // Create text device
                var textDevice = new Aspose.Pdf.Devices.TextDevice();

                // Set text extraction options - set text extraction mode (Raw or Pure)
                var textExtOptions = new Aspose.Pdf.Text.TextExtractionOptions(Aspose.Pdf.Text.TextExtractionOptions.TextFormattingMode.Pure);
                textDevice.ExtractionOptions = textExtOptions;

                // Convert a particular page and save text to the stream
                textDevice.Process(page, textStream);
                // Convert a particular page and save text to the stream
                textDevice.Process(document.Pages[1], textStream);

                // Get text from memory stream
                extractedText = System.Text.Encoding.Unicode.GetString(textStream.ToArray());
            }
            builder.Append(extractedText);
        }
    }

    // Save the extracted text in text file
    File.WriteAllText(dataDir + "input_Text_Extracted_out.txt", builder.ToString());
}
```

## 特定のページ領域からテキストを抽出する

**TextAbsorber**クラスは、PDF文書の特定のページまたはすべてのページからテキストを抽出する機能を提供します。このクラスは、抽出されたテキストを**Text**プロパティで返します。ただし、特定のページ領域からテキストを抽出する必要がある場合は、**TextSearchOptions**の**Rectangle**プロパティを使用できます。Rectangleプロパティは、値としてRectangleオブジェクトを受け取り、このプロパティを使用してテキストを抽出する必要があるページの領域を指定できます。

テキストを抽出するためにページの**Accept**メソッドが呼び出されます。**Document**と**TextAbsorber**クラスのオブジェクトを作成します。**Document**オブジェクトの個々のページに対して**Accept**メソッドを呼び出します。**Index**は、テキストを抽出する必要がある特定のページ番号です。**TextAbsorber**クラスの**Text**プロパティからテキストを取得できます。以下のコードスニペットは、個々のページからテキストを抽出する方法を示しています。

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextFromParticularPageRegion()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextAll.pdf"))
    {
        // Create TextAbsorber object to extract text
        var absorber = new Aspose.Pdf.Text.TextAbsorber();
        absorber.TextSearchOptions.LimitToPageBounds = true;
        absorber.TextSearchOptions.Rectangle = new Aspose.Pdf.Rectangle(100, 200, 250, 350);

        // Accept the absorber for first page
        document.Pages[1].Accept(absorber);

        // Get the extracted text
        string extractedText = absorber.Text;

        // Create a writer and open the file
        using (TextWriter tw = new StreamWriter(dataDir + "extracted-text.txt"))
        {
            // Write a line of text to the file
            tw.WriteLine(extractedText);
        }
    }
}
```

## カラムに基づいてテキストを抽出する

PDFファイルは、テキスト、画像、注釈、添付ファイル、グラフなどの要素で構成される場合があり、Aspose.PDF for .NETはこれらの要素を追加および操作する機能を提供します。このAPIは、PDF文書からのテキストの追加と抽出に関して優れており、PDF文書が複数のカラム（マルチカラム）で構成されているシナリオに直面することがあります。この場合、同じレイアウトを尊重しながらページの内容を抽出する必要があります。そのため、Aspose.PDF for .NETはこの要件を達成するための適切な選択です。一つのアプローチは、PDF文書内の内容のフォントサイズを減少させてからテキスト抽出を行うことです。以下のコードスニペットは、テキストサイズを減少させてからPDF文書からテキストを抽出する手順を示しています。

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextBasedOnColumns()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    var extractedText = string.Empty;
    // Open PDF document
    using (var sourceDocument = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {

        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        sourceDocument.Pages.Accept(textFragmentAbsorber);
        Aspose.Pdf.Text.TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
        foreach (Aspose.Pdf.Text.TextFragment textFragment in textFragmentCollection)
        {
            // Need to reduce font size at least for 70%
            textFragment.TextState.FontSize = textFragment.TextState.FontSize * 0.7f;
        }
        using (Stream sourceStream = new MemoryStream())
        {
            sourceDocument.Save(sourceStream);
            using (var destDocument = new Aspose.Pdf.Document(sourceStream))
            {
                var textAbsorber = new Aspose.Pdf.Text.TextAbsorber();
                destDocument.Pages.Accept(textAbsorber);
                extractedText = textAbsorber.Text;
                textAbsorber.Visit(destDocument);
            }
        }

        // Save the extracted text in text file
        File.WriteAllText(dataDir + "ExtractColumnsText_out.txt", extractedText);
    }
}
```

### 第二のアプローチ - ScaleFactorを使用する

この新しいリリースでは、TextAbsorberと内部テキストフォーマットメカニズムにいくつかの改善を導入しました。したがって、'Pure'モードを使用してテキストを抽出する際に、ScaleFactorオプションを指定でき、上記のアプローチに加えてマルチカラムPDF文書からテキストを抽出する別のアプローチとなります。このスケールファクターは、テキスト抽出中に内部テキストフォーマットメカニズムで使用されるグリッドを調整するために設定できます。1と0.1の間（0.1を含む）のScaleFactor値を指定することは、フォントの減少と同じ効果があります。

0.1と-0.1の間のScaleFactor値はゼロ値として扱われますが、テキスト抽出中に必要なスケールファクターを自動的に計算するアルゴリズムを作成します。この計算は、ページ上で最も一般的なフォントの平均グリフ幅に基づいていますが、抽出されたテキストにおいてカラムの文字列が次のカラムの開始に達しないことを保証することはできません。ScaleFactor値が指定されていない場合、デフォルト値の1.0が使用されます。これは、スケーリングが行われないことを意味します。指定されたScaleFactor値が10を超えるか、-0.1未満の場合、デフォルト値の1.0が使用されます。

大量のPDFファイルのテキストコンテンツ抽出を処理する際には、自動スケーリング（ScaleFactor = 0）の使用を提案します。または、グリッド幅の冗長な減少を手動で設定します（約ScaleFactor = 0.5）。ただし、具体的な文書に対してスケーリングが必要かどうかを判断する必要はありません。文書に対して冗長なグリッド幅の減少を設定した場合（それが必要ない場合）、抽出されたテキストコンテンツは完全に適切なままです。以下のコードスニペットを参照してください。

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExctractTextWithScaleFactor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {

        var textAbsorber = new Aspose.Pdf.Text.TextAbsorber();
        textAbsorber.ExtractionOptions = new Aspose.Pdf.Text.TextExtractionOptions(Aspose.Pdf.Text.TextExtractionOptions.TextFormattingMode.Pure);
        // Setting scale factor to 0.5 is enough to split columns in the majority of documents
        // Setting of zero allows to algorithm choose scale factor automatically
        textAbsorber.ExtractionOptions.ScaleFactor = 0.5; /* 0; */
        document.Pages.Accept(textAbsorber);
        var extractedText = textAbsorber.Text;

        // Save the extracted text in text file
        File.WriteAllText(dataDir + "ExtractTextUsingScaleFactor_out.text", extractedText);
    }
}
```

{{% alert color="primary" %}}

新しいScaleFactorと古い手動フォント減少係数との間には直接の対応関係はないことに注意してください。ただし、デフォルトのアルゴリズムは、内部的な理由によりすでに減少したフォントサイズの値を考慮に入れます。たとえば、フォントサイズを10から7に減少させることは、スケールファクターを5/8（= 0.625）に設定するのと同じ効果があります。

{{% /alert %}}

## PDF文書からハイライトされたテキストを抽出する

PDF文書からのテキスト抽出のさまざまなシナリオにおいて、PDF文書からハイライトされたテキストのみを抽出する必要が生じることがあります。この機能を実装するために、APIにTextMarkupAnnotation.GetMarkedText()およびTextMarkupAnnotation.GetMarkedTextFragments()メソッドを追加しました。TextMarkupAnnotationをフィルタリングし、前述のメソッドを使用することで、PDF文書からハイライトされたテキストを抽出できます。以下のコードスニペットは、PDF文書からハイライトされたテキストを抽出する方法を示しています。

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractHighlightedTextFromDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractHighlightedText.pdf"))
    {
        // Loop through all the annotations
        foreach (Aspose.Pdf.Annotations.Annotation annotation in document.Pages[1].Annotations)
        {
            // Filter TextMarkupAnnotation
            if (annotation is Aspose.Pdf.Annotations.TextMarkupAnnotation)
            {
                var highlightedAnnotation = annotation as Aspose.Pdf.Annotations.TextMarkupAnnotation;
                // Retrieve highlighted text fragments
                Aspose.Pdf.Text.TextFragmentCollection collection = highlightedAnnotation.GetMarkedTextFragments();
                foreach (Aspose.Pdf.Text.TextFragment textFragment in collection)
                {
                    // Display highlighted text
                    Console.WriteLine(textFragment.Text);
                }
            }
        }
    }
}
```

## XMLからテキストフラグメントおよびセグメント要素にアクセスする

時には、XMLから生成されたPDF文書を処理する際にTextFragmentまたはTextSegmentアイテムにアクセスする必要があります。Aspose.PDF for .NETは、名前でそのようなアイテムにアクセスする機能を提供します。以下のコードスニペットは、この機能を使用する方法を示しています。

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AccessTextFragmentAndSegmentElementsFromXML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        document.BindXml(dataDir + "40014.xml");

        // Get page
        var page = (Aspose.Pdf.Page)document.GetObjectById("mainSection");

        // Get elements by Id
        var segment = (Aspose.Pdf.Text.TextSegment)document.GetObjectById("boldHtml");
        segment = (Aspose.Pdf.Text.TextSegment)document.GetObjectById("strongHtml");

        // Save PDF document
        document.Save(dataDir + "DocumentFromXML_out.pdf");
    }
}
```