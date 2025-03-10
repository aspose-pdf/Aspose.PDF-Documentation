---
title: PDFにヘッダーとフッターを追加
linktitle: PDFにヘッダーとフッターを追加
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /ja/net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for .NETを使用すると、TextStampクラスを使ってPDFファイルにヘッダーとフッターを追加できます。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Header and Footer to PDF",
    "alternativeHeadline": "Add Custom Headers and Footers to PDF Files",
    "abstract": "Aspose.PDF for .NETは、ユーザーがカスタマイズ可能なヘッダーとフッターを追加することでPDF文書を豊かにする強力な機能を紹介します。TextStampおよびImageStampクラスを使用することで、開発者はテキストと画像の両方を簡単に統合し、さまざまな文書形式やスタイルに合わせて配置や外観を調整できます。これにより、文書のプロフェッショナリズムと可読性が向上し、レポート、請求書、その他の正式なコミュニケーションに最適です。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1549",
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
    "url": "/net/add-headers-and-footers-of-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-headers-and-footers-of-pdf-file/"
    },
    "dateModified": "2024-11-26",
    "description": "Aspose.PDF for .NETを使用すると、TextStampクラスを使ってPDFファイルにヘッダーとフッターを追加できます。"
}
</script>

**Aspose.PDF for .NET**を使用すると、既存のPDFファイルにヘッダーとフッターを追加できます。PDF文書に画像やテキストを追加することができます。また、C#を使用して1つのPDFファイルに異なるヘッダーを追加することも試してみてください。

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

## PDFファイルのヘッダーにテキストを追加

[TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/textstamp)クラスを使用して、PDFファイルのヘッダーにテキストを追加できます。TextStampクラスは、フォントサイズ、フォントスタイル、フォントカラーなど、テキストベースのスタンプを作成するために必要なプロパティを提供します。ヘッダーにテキストを追加するには、必要なプロパティを使用してDocumentオブジェクトとTextStampオブジェクトを作成する必要があります。その後、PDFのヘッダーにテキストを追加するために、PageのAddStampメソッドを呼び出すことができます。

ヘッダー領域にテキストを調整するようにTopMarginプロパティを設定する必要があります。また、HorizontalAlignmentをCenter、VerticalAlignmentをTopに設定する必要があります。

次のコードスニペットは、C#を使用してPDFファイルのヘッダーにテキストを追加する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHeaderText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextinHeader.pdf"))
    {
        // Create header as a TextStamp
        var textStamp = new Aspose.Pdf.TextStamp("Header Text")
        {
            TopMargin = 10,
            HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center,
            VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top
        };

        // Add header on all pages
        foreach (var page in document.Pages)
        {
            page.AddStamp(textStamp);
        }

        // Save PDF document
        document.Save(dataDir + "TextinHeader_out.pdf");
    }
}
```

## PDFファイルのフッターにテキストを追加

PDFファイルのフッターにテキストを追加するには、TextStampクラスを使用できます。TextStampクラスは、フォントサイズ、フォントスタイル、フォントカラーなど、テキストベースのスタンプを作成するために必要なプロパティを提供します。フッターにテキストを追加するには、必要なプロパティを使用してDocumentオブジェクトとTextStampオブジェクトを作成する必要があります。その後、PDFのフッターにテキストを追加するために、PageのAddStampメソッドを呼び出すことができます。

{{% alert color="primary" %}}

フッター領域にテキストを調整するようにBottom Marginプロパティを設定する必要があります。また、HorizontalAlignmentをCenter、VerticalAlignmentをBottomに設定する必要があります。

{{% /alert %}}

次のコードスニペットは、C#を使用してPDFファイルのフッターにテキストを追加する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFooterText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextinFooter.pdf"))
    {
        // Create footer as a TextStamp
        var textStamp = new Aspose.Pdf.TextStamp("Footer Text")
        {
            BottomMargin = 10,
            HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center,
            VerticalAlignment = Aspose.Pdf.VerticalAlignment.Bottom
        };

        // Add footer on all pages
        foreach (var page in document.Pages)
        {
            page.AddStamp(textStamp);
        }

        // Save PDF document
        document.Save(dataDir + "TextinFooter_out.pdf");
    }
}
```

## PDFファイルのヘッダーに画像を追加

[ImageStamp](https://reference.aspose.com/pdf/net/aspose.pdf/ImageStamp)クラスを使用して、PDFファイルのヘッダーに画像を追加できます。Image Stampクラスは、フォントサイズ、フォントスタイル、フォントカラーなど、画像ベースのスタンプを作成するために必要なプロパティを提供します。ヘッダーに画像を追加するには、必要なプロパティを使用してDocumentオブジェクトとImage Stampオブジェクトを作成する必要があります。その後、PDFのヘッダーに画像を追加するために、Pageの[AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp)メソッドを呼び出すことができます。

{{% alert color="primary" %}}

ヘッダー領域に画像を調整するようにTopMarginプロパティを設定する必要があります。また、HorizontalAlignmentをCenter、VerticalAlignmentをTopに設定する必要があります。

{{% /alert %}}

次のコードスニペットは、C#を使用してPDFファイルのヘッダーに画像を追加する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageHeader()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImageinHeader.pdf"))
    {
        // Create header as an ImageStamp
        var imageStamp = new Aspose.Pdf.ImageStamp(dataDir + "aspose-logo.jpg")
        {
            TopMargin = 10,
            HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center,
            VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top
        };

        // Add image header on all pages
        foreach (var page in document.Pages)
        {
            page.AddStamp(imageStamp);
        }

        // Save PDF document
        document.Save(dataDir + "ImageinHeader_out.pdf");
    }
}
```

## PDFファイルのフッターに画像を追加

PDFファイルのフッターに画像を追加するには、Image Stampクラスを使用できます。Image Stampクラスは、フォントサイズ、フォントスタイル、フォントカラーなど、画像ベースのスタンプを作成するために必要なプロパティを提供します。フッターに画像を追加するには、必要なプロパティを使用してDocumentオブジェクトとImage Stampオブジェクトを作成する必要があります。その後、PDFのフッターに画像を追加するために、PageのAddStampメソッドを呼び出すことができます。

{{% alert color="primary" %}}

[BottomMargin](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/bottommargin)プロパティを設定して、PDFのフッター領域に画像を調整する必要があります。また、[HorizontalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/horizontalalignment)を`Center`、[VerticalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/verticalalignment)を`Bottom`に設定する必要があります。

{{% /alert %}}

次のコードスニペットは、C#を使用してPDFファイルのフッターに画像を追加する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageFooter()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImageInFooter.pdf"))
    {
        // Create footer as an ImageStamp
        var imageStamp = new Aspose.Pdf.ImageStamp(dataDir + "aspose-logo.jpg")
        {
            BottomMargin = 10,
            HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center,
            VerticalAlignment = Aspose.Pdf.VerticalAlignment.Bottom
        };

        // Add image footer on all pages
        foreach (var page in document.Pages)
        {
            page.AddStamp(imageStamp);
        }

        // Save PDF document
        document.Save(dataDir + "ImageInFooter_out.pdf");
    }
}
```

## 1つのPDFファイルに異なるヘッダーを追加

ヘッダー/フッターセクションにTextStampを追加するためにTopMarginまたはBottom Marginプロパティを使用できることは知っていますが、時には1つのPDF文書に複数のヘッダー/フッターを追加する必要がある場合があります。**Aspose.PDF for .NET**は、これを行う方法を説明します。

この要件を達成するために、個別のTextStampオブジェクトを作成し（オブジェクトの数は必要なヘッダー/フッターの数によります）、それらをPDF文書に追加します。また、個々のスタンプオブジェクトに異なる書式情報を指定することもできます。次の例では、Documentオブジェクトと3つのTextStampオブジェクトを作成し、Pageの[AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp)メソッドを使用してPDFのヘッダーセクションにテキストを追加しました。次のコードスニペットは、Aspose.PDF for .NETを使用してPDFファイルのフッターに画像を追加する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddDifferentHeaders()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddingDifferentHeaders.pdf"))
    {
        // Create three stamps
        var stamp1 = new Aspose.Pdf.TextStamp("Header 1");
        var stamp2 = new Aspose.Pdf.TextStamp("Header 2");
        var stamp3 = new Aspose.Pdf.TextStamp("Header 3");

        // Set stamp1 properties (Header 1)
        stamp1.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
        stamp1.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        stamp1.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;
        stamp1.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
        stamp1.TextState.FontSize = 14;

        // Set stamp2 properties (Header 2)
        stamp2.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
        stamp2.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        stamp2.Zoom = 10;

        // Set stamp3 properties (Header 3)
        stamp3.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
        stamp3.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        stamp3.RotateAngle = 35;
        stamp3.TextState.BackgroundColor = Aspose.Pdf.Color.Pink;
        stamp3.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Verdana");

        // Add the stamps to specific pages
        document.Pages[1].AddStamp(stamp1);
        document.Pages[2].AddStamp(stamp2);
        document.Pages[3].AddStamp(stamp3);

        // Save PDF document
        document.Save(dataDir + "MultiHeader_out.pdf");
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