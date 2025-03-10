---
title: PDFファイルの変換
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ja/net/convert-pdf-file/
description: Aspose.PDFを使用して、.NETでPDFファイルをさまざまな形式に変換する方法を学び、柔軟な文書処理を実現します。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF File",
    "alternativeHeadline": "Convert PDF Pages to Image Formats Efficiently",
    "abstract": "PdfConverterクラスを使用して、PDFページをJPEG、GIF、PNGなどの多様な画像形式に簡単に変換するAspose.PDF for .NET Facadesの力を解き放ちます。この機能により、解像度、座標タイプ、ページ範囲などのパラメータを指定して、カスタマイズされた出力を得るための詳細な制御が可能になります。アプリケーションにシームレスなPDFから画像への変換を統合することで、文書処理能力を向上させましょう。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "561",
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
    "url": "/net/convert-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## PDFページを異なる画像形式に変換する (Facades)

PDFページを異なる画像形式に変換するには、[PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter)オブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3)メソッドを使用してPDFファイルを開く必要があります。その後、[DoConvert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/doconvert)メソッドを呼び出して初期化タスクを実行します。次に、[HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/hasnextimage)および[GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfconverter/getnextimage/methods/6)メソッドを使用してすべてのページをループ処理できます。[GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfconverter/getnextimage/methods/6)メソッドを使用すると、特定のページの画像を作成できます。このメソッドには、JPEG、GIF、PNGなどの特定のタイプの画像を作成するためにImageFormatを渡す必要があります。最後に、[PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter)クラスの[Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/close)メソッドを呼び出します。以下のコードスニペットは、PDFページを画像に変換する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPdfPagesToImages01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfConverter object
    using (var converter = new Aspose.Pdf.Facades.PdfConverter())
    {
        // Bind PDF document
        converter.BindPdf(dataDir + "ConvertPdfPagesToImages.pdf");

        // Initialize the converting process
        converter.DoConvert();

        // Check if pages exist and then convert to image one by one
        while (converter.HasNextImage())
        {
            // Generate output file name with '_out' suffix
            var outputFileName = dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg";
            // Convert the page to image and save it
            converter.GetNextImage(outputFileName, System.Drawing.Imaging.ImageFormat.Jpeg);
        }
    }
}
```

次のコードスニペットでは、いくつかのパラメータを変更する方法を示します。[CoordinateType](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/coordinatetype)を使用して、フレーム「CropBox」を設定します。また、[Resolution](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/resolution)を変更して、インチあたりのドット数を指定できます。次は[FormPresentationMode](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/formpresentationmode) - フォームプレゼンテーションモードです。次に、変換の開始ページ番号を設定する[StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/startpage)を指定します。範囲を設定することで、最後のページも指定できます。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPdfPagesToImages02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfConverter object
    using (var converter = new Aspose.Pdf.Facades.PdfConverter())
    {
        // Bind PDF document
        converter.BindPdf(dataDir + "ConvertPdfPagesToImages.pdf");

        // Initialize the converting process
        converter.DoConvert();

        // Set additional conversion settings
        converter.CoordinateType = Aspose.Pdf.PageCoordinateType.CropBox;
        converter.Resolution = new Aspose.Pdf.Devices.Resolution(600);
        converter.FormPresentationMode = Aspose.Pdf.Devices.FormPresentationMode.Production;
        converter.StartPage = 2;

        // Check if pages exist and then convert to image one by one
        while (converter.HasNextImage())
        {
            // Generate output file name
            var outputFileName = dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg";
            // Convert the page to image and save it
            converter.GetNextImage(outputFileName, System.Drawing.Imaging.ImageFormat.Jpeg);
        }
    }
}
```

## 参照

Aspose.PDF for .NETは、PDF文書をさまざまな形式に変換することができ、他の形式からPDFへの変換も行えます。また、Aspose.PDF変換の品質を確認し、Aspose.PDFコンバーターアプリで結果をオンラインで表示できます。タスクを解決するための[変換](/pdf/ja/net/converting/)セクションを学びましょう。