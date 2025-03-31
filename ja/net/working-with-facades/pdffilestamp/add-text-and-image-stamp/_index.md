---
title: テキストおよび画像スタンプの追加
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ja/net/add-text-and-image-stamp/
description: このセクションでは、PdfFileStampクラスを使用してAspose.PDF Facadesでテキストおよび画像スタンプを追加する方法を説明します。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Text and Image Stamp",
    "alternativeHeadline": "Add Custom Text and Image Stamps in PDFs",
    "abstract": "Aspose.PDF for .NETのテキストおよび画像スタンプの機能により、ユーザーはPDFドキュメントのすべてまたは特定のページにカスタマイズされたテキストおよび画像スタンプをシームレスに適用できます。この機能はドキュメントのパーソナライズを強化し、位置、回転、品質などのスタンプ属性に対する詳細な制御を可能にし、最終的にはPDFファイルのプレゼンテーションとブランディングを向上させます。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1435",
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
    "url": "/net/add-text-and-image-stamp/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-text-and-image-stamp/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## PDFファイルのすべてのページにテキストスタンプを追加

[PdfFileStamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilestamp)クラスを使用すると、PDFファイルのすべてのページにテキストスタンプを追加できます。テキストスタンプを追加するには、まず[PdfFileStamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilestamp)および[Stamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf/stamp)クラスのオブジェクトを作成する必要があります。また、[Stamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf/stamp)クラスの[BindLogo](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/stamp/methods/bindlogo)メソッドを使用してテキストスタンプを作成する必要があります。他の属性（原点、回転、背景など）も[Stamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf/stamp)オブジェクトを使用して設定できます。その後、[PdfFileStamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilestamp)クラスの[AddStamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilestamp/methods/addstamp)メソッドを使用してPDFファイルにスタンプを追加できます。最後に、[PdfFileStamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilestamp)クラスの[Close](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/facade/methods/close)メソッドを使用して出力PDFファイルを保存します。以下のコードスニペットは、PDFファイルのすべてのページにテキストスタンプを追加する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextStampOnAllPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindLogo(new Aspose.Pdf.Facades.FormattedText("Hello World!",
            System.Drawing.Color.Blue,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.Helvetica,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            true,
            14));

        stamp.SetOrigin(10, 400);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddTextStampOnAllPages_out.pdf");
    }
}
```

## PDFファイルの特定のページにテキストスタンプを追加

[PdfFileStamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilestamp)クラスを使用すると、PDFファイルの特定のページにテキストスタンプを追加できます。テキストスタンプを追加するには、まず[PdfFileStamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilestamp)および[Stamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf/stamp)クラスのオブジェクトを作成する必要があります。また、[Stamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf/stamp)クラスの[BindLogo](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/stamp/methods/bindlogo)メソッドを使用してテキストスタンプを作成する必要があります。他の属性（原点、回転、背景など）も[Stamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf/stamp)オブジェクトを使用して設定できます。PDFファイルの特定のページにテキストスタンプを追加するためには、[Stamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf/stamp)クラスの[Pages](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/stamp/properties/pages)プロパティも設定する必要があります。このプロパティには、スタンプを追加したいページの番号を含む整数配列が必要です。その後、[PdfFileStamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilestamp)クラスの[AddStamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilestamp/methods/addstamp)メソッドを使用してPDFファイルにスタンプを追加できます。最後に、[PdfFileStamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilestamp)クラスの[Close](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/facade/methods/close)メソッドを使用して出力PDFファイルを保存します。以下のコードスニペットは、PDFファイルの特定のページにテキストスタンプを追加する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextStampOnParticularPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindLogo(new Aspose.Pdf.Facades.FormattedText("Hello World!",
            System.Drawing.Color.Blue,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.Helvetica,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            true,
            14));
        stamp.SetOrigin(10, 400);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Set particular pages (page 2)
        stamp.Pages = new[] { 2 };

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddTextStampOnParticularPages_out.pdf");
    }
}
```

## PDFファイルのすべてのページに画像スタンプを追加

[PdfFileStamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilestamp)クラスを使用すると、PDFファイルのすべてのページに画像スタンプを追加できます。画像スタンプを追加するには、まず[PdfFileStamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilestamp)および[Stamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf/stamp)クラスのオブジェクトを作成する必要があります。また、[Stamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf/stamp)クラスの[BindImage](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/stamp/methods/bindimage/index)メソッドを使用して画像スタンプを作成する必要があります。他の属性（原点、回転、背景など）も[Stamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf/stamp)オブジェクトを使用して設定できます。その後、[PdfFileStamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilestamp)クラスの[AddStamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf/page/methods/addstamp)メソッドを使用してPDFファイルにスタンプを追加できます。最後に、[PdfFileStamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilestamp)クラスの[Close](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/facade/methods/close)メソッドを使用して出力PDFファイルを保存します。以下のコードスニペットは、PDFファイルのすべてのページに画像スタンプを追加する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageStampOnAllPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindImage(dataDir + "StampImage.png");
        stamp.SetOrigin(10, 200);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Set particular pages (page 2)
        stamp.Pages = new[] { 2 };

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddImageStampOnAllPages_out.pdf");
    }
}
```

### スタンプとして追加する際の画像品質の制御

画像をスタンプオブジェクトとして追加する際に、画像の品質を制御することもできます。この要件を満たすために、[Stamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf/stamp)クラスにQualityプロパティが追加されました。これは、画像の品質をパーセントで示します（有効な値は0..100です）。

## PDFファイルの特定のページに画像スタンプを追加

[PdfFileStamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilestamp)クラスを使用すると、PDFファイルの特定のページに画像スタンプを追加できます。画像スタンプを追加するには、まず[PdfFileStamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilestamp)および[Stamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf/stamp)クラスのオブジェクトを作成する必要があります。また、[Stamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf/stamp)クラスの[BindImage](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/stamp/methods/bindimage/index)メソッドを使用して画像スタンプを作成する必要があります。他の属性（原点、回転、背景など）も[Stamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf/stamp)オブジェクトを使用して設定できます。PDFファイルの特定のページに画像スタンプを追加するためには、[Stamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf/stamp)クラスの[Pages](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/stamp/properties/pages)プロパティも設定する必要があります。このプロパティには、スタンプを追加したいページの番号を含む整数配列が必要です。その後、[PdfFileStamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilestamp)クラスの[AddStamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf/page/methods/addstamp)メソッドを使用してPDFファイルにスタンプを追加できます。最後に、[PdfFileStamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilestamp)クラスの[Close](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/facade/methods/close)メソッドを使用して出力PDFファイルを保存します。以下のコードスニペットは、PDFファイルの特定のページに画像スタンプを追加する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageStampOnParticularPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindImage(dataDir + "StampImage.png");
        stamp.SetOrigin(10, 200);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddImageStampOnParticularPages_out.pdf");
    }
}
```