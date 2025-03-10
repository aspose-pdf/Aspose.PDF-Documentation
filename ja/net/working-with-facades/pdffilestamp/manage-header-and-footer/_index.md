---
title: ヘッダーとフッターの管理
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ja/net/manage-header-and-footer/
description: Aspose.PDFを使用して.NETでPDFファイルのヘッダーとフッターを操作する方法を探り、文書の構造を改善します。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manage Header and Footer",
    "alternativeHeadline": "Enhance PDFs with Custom Headers and Footers",
    "abstract": "Aspose.PDF for .NETのヘッダーとフッターの管理機能により、ユーザーはPdfFileStampクラスを使用してPDF文書にヘッダーとフッターを簡単に追加、カスタマイズ、フォーマットできます。この機能は、テキストや画像の挿入をサポートし、文書のプレゼンテーションに柔軟性を提供しながら、プロフェッショナルなフォーマットを確保します。ユーザーは、この機能をアプリケーションにシームレスに統合して、PDFファイルの視覚的な魅力と整理を向上させることができます。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1007",
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
    "url": "/net/manage-header-and-footer/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manage-header-and-footer/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## PDFファイルにヘッダーを追加

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main)クラスを使用すると、PDFファイルにヘッダーを追加できます。ヘッダーを追加するには、まず[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main)クラスのオブジェクトを作成する必要があります。ヘッダーのテキストは、[FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext)クラスを使用してフォーマットできます。ファイルにヘッダーを追加する準備ができたら、[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main)クラスの[AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4)メソッドを呼び出す必要があります。また、[AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4)メソッドでは、少なくとも上部のマージンを指定する必要があります。最後に、[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main)クラスの[Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close)メソッドを使用して出力PDFファイルを保存します。以下のコードスニペットは、PDFファイルにヘッダーを追加する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHeader()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create formatted text for the header
        var formattedText = new Aspose.Pdf.Facades.FormattedText(
            "Aspose - Your File Format Experts!",
            System.Drawing.Color.Yellow,
            System.Drawing.Color.Black,
            Aspose.Pdf.Facades.FontStyle.Courier,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            false,
            14);

        // Add header
        fileStamp.AddHeader(formattedText, 10);

        // Save PDF document
        fileStamp.Save(dataDir + "AddHeader_out.pdf");
    }
}
```

## PDFファイルにフッターを追加

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main)クラスを使用すると、PDFファイルにフッターを追加できます。フッターを追加するには、まず[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main)クラスのオブジェクトを作成する必要があります。フッターのテキストは、[FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext)クラスを使用してフォーマットできます。ファイルにフッターを追加する準備ができたら、[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main)クラスの[AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index)メソッドを呼び出す必要があります。また、[AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index)メソッドでは、少なくとも下部のマージンを指定する必要があります。最後に、[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main)クラスの[Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close)メソッドを使用して出力PDFファイルを保存します。以下のコードスニペットは、PDFファイルにフッターを追加する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFooter()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create formatted text for the footer
        var formattedText = new Aspose.Pdf.Facades.FormattedText(
            "Aspose - Your File Format Experts!",
            System.Drawing.Color.Blue,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.Courier,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            false,
            14);

        // Add footer
        fileStamp.AddFooter(formattedText, 10);

        // Save PDF document
        fileStamp.Save(dataDir + "AddFooter_out.pdf");
    }
}
```

## 既存のPDFファイルのヘッダーに画像を追加

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main)クラスを使用すると、PDFファイルのヘッダーに画像を追加できます。ヘッダーに画像を追加するには、まず[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main)クラスのオブジェクトを作成する必要があります。その後、[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main)クラスの[AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4)メソッドを呼び出す必要があります。画像を[AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/addheader/methods/4)メソッドに渡すことができます。最後に、[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main)クラスの[Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close)メソッドを使用して出力PDFファイルを保存します。以下のコードスニペットは、PDFファイルのヘッダーに画像を追加する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageHeader()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Add Header
        using (var fs = new FileStream(dataDir + "ImageHeader.png", FileMode.Open))
        {
            fileStamp.AddHeader(fs, 10);  // Add image header with position offset

            // Save PDF document
            fileStamp.Save(dataDir + "AddImageHeader_out.pdf");
        }
    }
}
```

## 既存のPDFファイルのフッターに画像を追加

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main)クラスを使用すると、PDFファイルのフッターに画像を追加できます。フッターに画像を追加するには、まず[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main)クラスのオブジェクトを作成する必要があります。その後、[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main)クラスの[AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index)メソッドを呼び出す必要があります。画像を[AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index)メソッドに渡すことができます。最後に、[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main)クラスの[Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close)メソッドを使用して出力PDFファイルを保存します。以下のコードスニペットは、PDFファイルのフッターに画像を追加する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageFooter()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Add footer
        using (var fs = new FileStream(dataDir + "ImageFooter.png", FileMode.Open))
        {
            fileStamp.AddFooter(fs, 10);  // Add image footer with position offset

            // Save PDF document
            fileStamp.Save(dataDir + "AddImageFooter_out.pdf");
        }
    }
}
```