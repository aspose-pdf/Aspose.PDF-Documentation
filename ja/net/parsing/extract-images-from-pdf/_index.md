---
title: PDFから画像を抽出する C#
linktitle: PDFから画像を抽出する
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ja/net/extract-images-from-the-pdf-file/
description: C#を使用してPDFから画像の一部を抽出する方法
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Images from PDF C#",
    "alternativeHeadline": "Effortlessly Extract Images from PDF Files in C#",
    "abstract": "C#でPDFファイルから画像を直接抽出する新機能を使用して、Aspose.PDF for .NETの力を解き放ちます。この機能により、ユーザーは特定のページから画像を簡単に取得して保存でき、.NETアプリケーションでの効率的な画像管理と処理が促進されます。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "240",
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
    "url": "/net/extract-images-from-the-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-images-from-the-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

画像は各ページの[Resources](https://reference.aspose.com/pdf/net/aspose.pdf/resources)コレクションの[Images](https://reference.aspose.com/pdf/net/aspose.pdf/resources/properties/images)コレクションに保持されています。特定のページを抽出するには、特定の画像のインデックスを使用してImagesコレクションから画像を取得します。

画像のインデックスは[XImage](https://reference.aspose.com/pdf/net/aspose.pdf/ximage)オブジェクトを返します。このオブジェクトは、抽出した画像を保存するために使用できるSaveメソッドを提供します。以下のコードスニペットは、PDFファイルから画像を抽出する方法を示しています。

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractImages.pdf"))
    {
        // Extract a particular image
        var xImage = document.Pages[1].Resources.Images[1];

        using (var outputImage = new FileStream(dataDir + "outputImage.jpg", FileMode.Create))
        {
            // Save the output image
            xImage.Save(outputImage, ImageFormat.Jpeg);
        }

        // Save PDF document
        document.Save(dataDir + "ExtractImages_out.pdf");
    }
}
```