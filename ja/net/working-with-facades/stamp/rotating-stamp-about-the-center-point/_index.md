---
title: 中心点を中心にしたスタンプの回転
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ja/net/rotating-stamp-about-the-center-point/
description: このセクションでは、Stampクラスを使用してスタンプを中心点の周りで回転させる方法を説明します。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Rotating stamp about the center point",
    "alternativeHeadline": "Rotate Stamps Precisely Around Their Center Point",
    "abstract": "Aspose.PDF for .NETの機能により、ユーザーはPDFファイル内のスタンプを中心点の周りで正確に回転させることができます。Stampクラスを利用することで、開発者は0度から360度までの回転値を簡単に設定でき、文書内の透かしの配置の柔軟性とカスタマイズ性を向上させます。この機能は、個別のスタンプの向きを持つ視覚的に動的なPDFを作成するのに最適です。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "339",
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
    "url": "/net/rotating-stamp-about-the-center-point/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/rotating-stamp-about-the-center-point/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

{{% alert color="primary" %}}

[Aspose.Pdf.Facades名前空間](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades)は、[Aspose.PDF for .NET](/pdf/ja/net/)で既存のPDFファイルにスタンプを追加することを可能にします。時には、ユーザーがスタンプを回転させる必要があります。この記事では、スタンプを中心点の周りで回転させる方法を見ていきます。

{{% /alert %}}

## 実装の詳細

[Stamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf/stamp)クラスは、PDFファイルに透かしを追加することを可能にします。 [BindImage](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades.stamp/bindimage/methods/1)メソッドを使用して、スタンプとして追加する画像を指定できます。[SetOrigin](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/stamp/methods/setorigin)メソッドを使用すると、追加されたスタンプの原点を設定できます。この原点は、スタンプの左下の座標です。また、[SetImageSize](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/stamp/methods/setimagesize)メソッドを使用して画像のサイズを設定することもできます。

次に、スタンプをスタンプの中心の周りで回転させる方法を見ていきます。[Stamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf/stamp)クラスは、Rotationという名前のプロパティを提供します。このプロパティは、スタンプコンテンツの回転を0から360の範囲で設定または取得します。0から360の任意の回転値を指定できます。回転値を指定することで、スタンプを中心点の周りで回転させることができます。StampがStamp型のオブジェクトである場合、回転値はaStamp.Rotation = 90として指定できます。この場合、スタンプはスタンプコンテンツの中心で90度回転します。以下のコードスニペットは、スタンプを中心点の周りで回転させる方法を示しています：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddRotatingStampToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();  

    // Create PdfFileInfo object to get height and width of the pages
    using (var fileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "RotatingStamp.pdf"))
    {
        // Create Stamp object
        var aStamp = new Aspose.Pdf.Facades.Stamp();

        // Bind image file with the Stamp object
        aStamp.BindImage(dataDir + "RotatingStamp.jpg");

        // Specify whether the stamp will be added as a background or not
        aStamp.IsBackground = false;

        // Specifies at which pages to add the watermark
        aStamp.Pages = new int[] { 1 };

        // Specifies the watermark rotation - rotate at 90 degrees
        aStamp.Rotation = 90;

        // Specifies the position of stamp - lower left corner of the stamp
        aStamp.SetOrigin(fileInfo.GetPageWidth(1) / 2, fileInfo.GetPageHeight(1) / 2);

        // Set the size of the watermark
        aStamp.SetImageSize(100, 100);

        // Open PDF document
        using (var document = new Aspose.Pdf.Document(dataDir + "RotatingStamp_out.pdf"))
        {
            // Create PdfFileStamp class to bind input and output files
            using (var stamper = new Aspose.Pdf.Facades.PdfFileStamp(document))
            {
                // Add the stamp in the PDF file
                stamper.AddStamp(aStamp);
            }
        }
    }
}
```