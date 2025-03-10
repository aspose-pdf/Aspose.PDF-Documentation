---
title: ページプロパティの取得と設定
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
url: /ja/net/get-and-set-page-properties/
description: Aspose.PDF for .NETを使用してPDFドキュメントのページプロパティを取得および設定する方法を学び、カスタマイズされたドキュメントフォーマットを実現します。
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get and Set Page Properties",
    "alternativeHeadline": "Manage PDF Page Properties with Ease",
    "abstract": "Aspose.PDF for .NETのページプロパティの取得と設定機能により、開発者はPDFページ属性に簡単にアクセスし、操作できます。この機能を使用すると、ページ数や色の種類、メディアボックス、トリムボックスなどの特定のプロパティなど、重要な情報を数行のコードで取得できます。今日、.NETアプリケーションでの効率的なPDF操作のために、この強力な機能を活用してPDFドキュメント管理機能を向上させましょう。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1117",
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
    "url": "/net/get-and-set-page-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-and-set-page-properties/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

Aspose.PDF for .NETを使用すると、.NETアプリケーション内のPDFファイルのページのプロパティを読み取り、設定できます。このセクションでは、PDFファイル内のページ数を取得し、色などのPDFページプロパティに関する情報を取得し、ページプロパティを設定する方法を示します。示されている例はC#ですが、VB.NETなどの他の.NET言語を使用して同じことを達成できます。

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも機能します。

## PDFファイルのページ数を取得

ドキュメントを扱う際、通常はそれに含まれるページ数を知りたいと思います。Aspose.PDFを使用すると、これには2行のコードもかかりません。

PDFファイルのページ数を取得するには：

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)クラスを使用してPDFファイルを開きます。
1. 次に、[PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection)コレクションのCountプロパティ（Documentオブジェクトから）を使用して、ドキュメント内のページの総数を取得します。

次のコードスニペットは、PDFファイルのページ数を取得する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetNumberOfPagesInAPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetNumberofPages.pdf"))
    {
        // Get page count
        System.Console.WriteLine("Page Count : {0}", document.Pages.Count);
    }
}
```

### ドキュメントを保存せずにページ数を取得

時には、PDFファイルを動的に生成し、PDFファイルの作成中に、ファイルをシステムやストリームに保存せずにページ数を取得する必要が生じることがあります（目次の作成など）。この要件に対応するために、Documentクラスに[ProcessParagraphs](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/processparagraphs)メソッドが導入されました。以下のコードスニペットを参照して、ドキュメントを保存せずにページ数を取得する手順を示します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetPageCountWithoutSavingTheDocument()
{
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create loop instance
        for (var i = 0; i < 300; i++)
        {
            // Add TextFragment to paragraphs collection of page object
            page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Pages count test"));
        }
        // Process the paragraphs in PDF file to get accurate page count
        document.ProcessParagraphs();
        // Print number of pages in document
        Console.WriteLine("Number of pages in document = " + document.Pages.Count);
    }
}
```

## ページプロパティの取得

PDFファイルの各ページには、幅、高さ、ブリードボックス、クロップボックス、トリムボックスなどの多くのプロパティがあります。Aspose.PDFを使用すると、これらのプロパティにアクセスできます。

### **ページプロパティの理解：Artbox、BleedBox、CropBox、MediaBox、TrimBox、Rectプロパティの違い**

- **メディアボックス**：メディアボックスは最も大きなページボックスです。これは、ドキュメントがPostScriptまたはPDFに印刷されたときに選択されたページサイズ（例：A4、A5、USレターなど）に対応します。言い換えれば、メディアボックスはPDFドキュメントが表示または印刷されるメディアの物理的なサイズを決定します。
- **ブリードボックス**：ドキュメントにブリードがある場合、PDFにもブリードボックスがあります。ブリードは、ページの端を超えて延びる色（またはアートワーク）の量です。これは、ドキュメントが印刷され、サイズにカット（「トリム」）されるときに、インクがページの端まで届くことを保証するために使用されます。たとえページがトリムマークからわずかにずれてカットされても、ページに白いエッジは現れません。
- **トリムボックス**：トリムボックスは、印刷およびトリミング後のドキュメントの最終サイズを示します。
- **アートボックス**：アートボックスは、ドキュメント内のページの実際の内容の周りに描かれたボックスです。このページボックスは、他のアプリケーションにPDFドキュメントをインポートする際に使用されます。
- **クロップボックス**：クロップボックスは、Adobe AcrobatでPDFドキュメントが表示される「ページ」サイズです。通常の表示では、Adobe Acrobatではクロップボックスの内容のみが表示されます。
  これらのプロパティの詳細な説明については、Adobe.Pdf仕様、特に10.10.1ページ境界を参照してください。
- **Page.Rect**：メディアボックスとドロップボックスの交差点（一般的に表示される長方形）です。以下の図は、これらのプロパティを示しています。

詳細については、[このページ](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html)をご覧ください。

### **ページプロパティへのアクセス**

[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)クラスは、特定のPDFページに関連するすべてのプロパティを提供します。PDFファイルのすべてのページは、[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)オブジェクトの[PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection)コレクションに含まれています。

そこから、インデックスを使用して個々のPageオブジェクトにアクセスするか、foreachループを使用してコレクションをループし、すべてのページを取得できます。個々のページにアクセスすると、そのプロパティを取得できます。次のコードスニペットは、ページプロパティを取得する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AccessingPageProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetProperties.pdf"))
    {
        // Get page collection
        var pageCollection = document.Pages;
        // Get particular page
        var pdfPage = pageCollection[1];
        // Get page properties
        System.Console.WriteLine("ArtBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.ArtBox.Height, pdfPage.ArtBox.Width, pdfPage.ArtBox.LLX,
            pdfPage.ArtBox.LLY, pdfPage.ArtBox.URX, pdfPage.ArtBox.URY);
        System.Console.WriteLine("BleedBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.BleedBox.Height, pdfPage.BleedBox.Width, pdfPage.BleedBox.LLX,
            pdfPage.BleedBox.LLY, pdfPage.BleedBox.URX, pdfPage.BleedBox.URY);
        System.Console.WriteLine("CropBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.CropBox.Height, pdfPage.CropBox.Width, pdfPage.CropBox.LLX,
            pdfPage.CropBox.LLY, pdfPage.CropBox.URX, pdfPage.CropBox.URY);
        System.Console.WriteLine("MediaBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.MediaBox.Height, pdfPage.MediaBox.Width, pdfPage.MediaBox.LLX,
            pdfPage.MediaBox.LLY, pdfPage.MediaBox.URX, pdfPage.MediaBox.URY);
        System.Console.WriteLine("TrimBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.TrimBox.Height, pdfPage.TrimBox.Width, pdfPage.TrimBox.LLX,
            pdfPage.TrimBox.LLY, pdfPage.TrimBox.URX, pdfPage.TrimBox.URY);
        System.Console.WriteLine("Rect : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.Rect.Height, pdfPage.Rect.Width, pdfPage.Rect.LLX, pdfPage.Rect.LLY,
            pdfPage.Rect.URX, pdfPage.Rect.URY);
        System.Console.WriteLine("Page Number : {0}", pdfPage.Number);
        System.Console.WriteLine("Rotate : {0}", pdfPage.Rotate);
    }
}
```

## PDFファイルの特定のページを取得

Aspose.PDFを使用すると、[PDFを個々のページに分割](/pdf/net/split-pdf-document/)し、それらをPDFファイルとして保存できます。PDFファイル内の指定されたページを取得し、新しいPDFとして保存することは非常に似た操作です：ソースドキュメントを開き、ページにアクセスし、新しいドキュメントを作成し、そのページを追加します。

[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)オブジェクトの[PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection)は、PDFファイル内のページを保持します。このコレクションから特定のページを取得するには：

1. Pagesプロパティを使用してページインデックスを指定します。
1. 新しい[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)オブジェクトを作成します。
1. 新しい[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)オブジェクトに[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)オブジェクトを追加します。
1. [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4)メソッドを使用して出力を保存します。

次のコードスニペットは、PDFファイルから特定のページを取得し、新しいファイルとして保存する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetAParticularPageOfThePdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get particular page
        var pdfPage = document.Pages[2];
        // Save the page as PDF file
        using (var newDocument = new Aspose.Pdf.Document())
        {
            newDocument.Pages.Add(pdfPage);
            // Save PDF document
            newDocument.Save(dataDir + "GetParticularPage_out.pdf");
        }
    }
}
```

## ページの色を決定

[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)クラスは、PDFドキュメント内の特定のページに関連するプロパティを提供し、ページが使用する色のタイプ（RGB、白黒、グレースケール、または未定義）を含みます。

PDFファイルのすべてのページは、[PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection)コレクションに含まれています。ColorTypeプロパティは、ページ上の要素の色を指定します。特定のPDFページの色情報を取得または決定するには、[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)オブジェクトの[ColorType](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/colortype)プロパティを使用します。

次のコードスニペットは、PDFファイルの個々のページをループして色情報を取得する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeterminePageColor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Iterate through all the page of PDF file
        for (var pageCount = 1; pageCount <= document.Pages.Count; pageCount++)
        {
            // Get the color type information for particular PDF page
            Aspose.Pdf.ColorType pageColorType = document.Pages[pageCount].ColorType;
            switch (pageColorType)
            {
                case Aspose.Pdf.ColorType.BlackAndWhite:
                    Console.WriteLine("Page # -" + pageCount + " is Black and white..");
                    break;
                case Aspose.Pdf.ColorType.Grayscale:
                    Console.WriteLine("Page # -" + pageCount + " is Gray Scale...");
                    break;
                case Aspose.Pdf.ColorType.Rgb:
                    Console.WriteLine("Page # -" + pageCount + " is RGB..", pageCount);
                    break;
                case Aspose.Pdf.ColorType.Undefined:
                    Console.WriteLine("Page # -" + pageCount + " Color is undefined..");
                    break;
            }
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