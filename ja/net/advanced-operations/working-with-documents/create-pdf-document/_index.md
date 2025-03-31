---
title: C#を使用してPDFを作成する方法
linktitle: PDFドキュメントを作成する
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ja/net/create-pdf-document/
description: Aspose.PDF for .NETを使用してPDFドキュメントを作成およびフォーマットします。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "How to Create PDF using C#",
    "alternativeHeadline": "Create and Format PDFs Effortlessly with C#",
    "abstract": "Aspose.PDF for .NETの新機能により、開発者はC#を使用してPDFドキュメントを簡単に作成およびフォーマットできます。この直感的なAPIを使用すると、ユーザーは検索可能なPDFを生成し、アクセシビリティのためにタグ付きコンテンツを操作し、さまざまな.NETアプリケーションにPDF生成をシームレスに統合して、生産性を向上させ、ワークフローを合理化できます。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF creation, C# PDF generation, Aspose.PDF for .NET, searchable PDF, accessible PDF, Document class, TextFragment, PDF document manipulation, .NET applications, BDC operations",
    "wordcount": "871",
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
    "url": "/net/create-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-pdf-document/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF for .NETを使用してPDFドキュメントを作成およびフォーマットします。"
}
</script>

私たちは常に、C#プロジェクトでPDFドキュメントを生成し、それを正確かつ効果的に扱う方法を探しています。ライブラリからの使いやすい関数を持つことで、作業の多くを追跡し、PDFを生成するための時間のかかる詳細にあまり時間をかけずに済みます。

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

## C#言語を使用してPDFドキュメントを作成（または生成）する

Aspose.PDF for .NET APIを使用すると、C#およびVB.NETを使用してPDFファイルを作成および読み取ることができます。このAPIは、WinForms、ASP.NETなど、さまざまな.NETアプリケーションで使用できます。この記事では、Aspose.PDF for .NET APIを使用して、.NETアプリケーションでPDFファイルを簡単に生成および読み取る方法を示します。

### シンプルなPDFファイルを作成する方法

C#を使用してPDFファイルを作成するには、以下の手順を使用できます。

1. [Document](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document)クラスのオブジェクトを作成します。
1. Documentオブジェクトの[Pages](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document/properties/pages)コレクションに[Page](https://reference.aspose.com/pdf/ja/net/aspose.pdf/page)オブジェクトを追加します。
1. ページの[Paragraphs](https://reference.aspose.com/pdf/ja/net/aspose.pdf/page/properties/paragraphs)コレクションに[TextFragment](https://reference.aspose.com/pdf/ja/net/aspose.pdf.text/textfragment)を追加します。
1. 結果のPDFドキュメントを保存します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateHelloWorldDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Add text to new page
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
        // Save PDF document
        document.Save(dataDir + "HelloWorld_out.pdf");
    }
}
```

### 検索可能なPDFドキュメントを作成する方法

Aspose.PDF for .NETは、既存のPDFドキュメントを作成および操作する機能を提供します。PDFファイル内にテキスト要素を追加すると、結果のPDFは検索可能になります。ただし、テキストを含む画像をPDFファイルに変換する場合、PDF内の内容は検索可能ではありません。ただし、回避策として、結果のファイルにOCRを使用することで、検索可能にすることができます。

以下に示すロジックは、PDF画像のテキストを認識します。認識には、外部OCRがHOCR標準をサポートしていることを使用できます。テスト目的で、無料のGoogle Tesseract OCRを使用しました。したがって、最初にシステムにTesseract-OCRをインストールし、tesseractコンソールアプリケーションを持っている必要があります。

この要件を達成するための完全なコードは以下の通りです：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateSearchableDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchableDocument.pdf"))
    {
        document.Convert(CallBackGetHocr);

        // Save PDF document
        document.Save(dataDir + "SearchableDocument_out.pdf");
    }
}

private static string CallBackGetHocr(System.Drawing.Image img)
{
    var tmpFile = Path.GetTempFileName();
    try
    {
        using (var bmp = new System.Drawing.Bitmap(img))
        {
            bmp.Save(tmpFile, System.Drawing.Imaging.ImageFormat.Bmp);
        }

        var inputFile = string.Concat('"', tmpFile, '"');
        var outputFile = string.Concat('"', tmpFile, '"');
        var arguments = string.Concat(inputFile, " ", outputFile, " -l eng hocr");
        var tesseractProcessName = RunExamples.GetTesseractExePath();

        var psi = new System.Diagnostics.ProcessStartInfo(tesseractProcessName, arguments)
        {
            UseShellExecute = true,
            CreateNoWindow = true,
            WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden,
            WorkingDirectory = Path.GetDirectoryName(tesseractProcessName)
        };

        var p = new System.Diagnostics.Process
        {
            StartInfo = psi
        };
        p.Start();
        p.WaitForExit();

        using (var streamReader = new StreamReader(tmpFile + ".hocr"))
        {
            string text = streamReader.ReadToEnd();
            return text;
        }
    }
    finally
    {
        if (File.Exists(tmpFile))
        {
            File.Delete(tmpFile);
        }
        if (File.Exists(tmpFile + ".hocr"))
        {
            File.Delete(tmpFile + ".hocr");
        }
    }
}
```

### 低レベルの関数を使用してアクセシブルなPDFを作成する方法

このコードスニペットは、PDFドキュメントとそのタグ付きコンテンツを操作し、Aspose.PDFライブラリを使用して処理します。

この例では、PDFの最初のページのタグ付きコンテンツに新しいspan要素を作成し、すべてのBDC要素を見つけてそれらをspanに関連付けます。変更されたドキュメントは、その後保存されます。

BDCPropertiesオブジェクトを使用して、mcid、lang、および展開テキストを指定するBDCステートメントを作成できます：

```cs
var bdc = new Aspose.Pdf.Operators.BDC("P", new Aspose.Pdf.Facades.BDCProperties(1, "de", "Hallo, welt!"));
```

構造ツリーを作成した後、要素オブジェクトのメソッドTagを使用してBDCオペレーターを指定された構造の要素にバインドすることができます：

```cs
Aspose.Pdf.LogicalStructure.SpanElement span = content.CreateSpanElement();
span.Tag(bdc);
```

アクセシブルなPDFを作成する手順：

1. PDFドキュメントをロードします。
1. タグ付きコンテンツにアクセスします。
1. Span要素を作成します。
1. Spanをルート要素に追加します。
1. ページの内容を反復処理します。
1. BDC要素をチェックしてタグ付けします。
1. 修正されたドキュメントを保存します。

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateAnAccessibleDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "tourguidev2_gb_tags.pdf"))
    {
        // Access tagged content
        Aspose.Pdf.Tagged.ITaggedContent content = document.TaggedContent;
        // Create a span element
        Aspose.Pdf.LogicalStructure.SpanElement span = content.CreateSpanElement();
        // Append span to root element
        content.RootElement.AppendChild(span);
        // Iterate over page contents
        foreach (var op in document.Pages[1].Contents)
        {
            var bdc = op as Aspose.Pdf.Operators.BDC;
            if (bdc != null)
            {
                span.Tag(bdc);
            }
        }
        // Save PDF document
        document.Save(dataDir + "AccessibleDocument_out.pdf");
    }
}
```

このコードは、ドキュメントのタグ付きコンテンツ内にspan要素を作成し、最初のページから特定のコンテンツ（BDC操作）をこのspanでタグ付けすることによってPDFを修正します。変更されたPDFは、新しいファイルに保存されます。

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