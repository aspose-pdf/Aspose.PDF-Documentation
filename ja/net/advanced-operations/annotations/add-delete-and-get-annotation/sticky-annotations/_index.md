---
title: PDF スティッキー注釈を使用した C#
linktitle: スティッキー注釈
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ja/net/sticky-annotations/
description: Aspose.PDF を使用して .NET で PDF にノートやハイライトなどのスティッキー注釈を作成する方法を学びます。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF sticky Annotations using C#",
    "alternativeHeadline": "Add Sticky Watermark Annotations to PDF with C#",
    "abstract": "C# における新しい PDF スティッキー注釈機能を紹介します。これにより、ユーザーは PDF ドキュメント内で透かし注釈を直接作成およびカスタマイズできます。この機能は、特定のテキスト位置の設定、透明度の制御、画像の効率的な再利用をサポートし、全体的なドキュメントのプレゼンテーションを向上させ、ファイルサイズを最適化します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF sticky annotations, C# sticky annotations, Watermark Annotation, Aspose.PDF.Drawing, PDF document generation, opacity property, XImageCollection, optimize PDF size",
    "wordcount": "453",
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
    "url": "/net/sticky-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/sticky-annotations/"
    },
    "dateModified": "2024-11-25",
    "description": "このトピックはスティッキー注釈に関するもので、例としてテキスト内の透かし注釈を示します。"
}
</script>

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/) ライブラリでも動作します。

## 透かし注釈を追加する

透かし注釈は、印刷ページの寸法に関係なく、ページ上の固定サイズと位置で印刷されるグラフィックスを表すために使用されます。

特定の PDF ページの位置に [WatermarkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/watermarkannotation) を使用して透かしテキストを追加できます。透かしの透明度は、透明度プロパティを使用して制御することもできます。

透かし注釈を追加するための次のコードスニペットを確認してください。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddWatermarkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "source.pdf"))
    {
        // Load Page object to add Annotation
        var page = document.Pages[1];

        // Create Watermark Annotation
        var wa = new Aspose.Pdf.Annotations.WatermarkAnnotation(page, new Aspose.Pdf.Rectangle(100, 500, 400, 600));

        // Add annotation into Annotation collection of Page
        page.Annotations.Add(wa);

        // Create TextState for Font settings
        var ts = new Aspose.Pdf.Text.TextState();
        ts.ForegroundColor = Aspose.Pdf.Color.Blue;
        ts.Font = Aspose.Pdf.Text.FontRepository.FindFont("Times New Roman");
        ts.FontSize = 32;

        // Set opacity level of Annotation Text
        wa.Opacity = 0.5;

        // Add Text in Annotation
        wa.SetTextAndState(new string[] { "HELLO", "Line 1", "Line 2" }, ts);

        // Save PDF document
        document.Save(dataDir + "AddWatermarkAnnotation_out.pdf");
    }
}
```

## PDF ドキュメント内で単一の画像を複数回参照する

時には、PDF ドキュメント内で同じ画像を複数回使用する必要があります。新しいインスタンスを追加すると、結果として得られる PDF ドキュメントが増加します。Aspose.PDF for .NET 17.1.0 では、新しいメソッド XImageCollection.Add(XImage) を追加しました。このメソッドは、PDF ドキュメントのサイズを最適化するために、元の画像と同じ PDF オブジェクトへの参照を追加することを可能にします。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddWatermarkAnnotationWithImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Define the rectangle for the image
    var imageRectangle = new Aspose.Pdf.Rectangle(0, 0, 30, 15);

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Open the image stream
        using (var imageStream = File.Open(dataDir + "icon.png", FileMode.Open))
        {
            XImage image = null;

            // Iterate through each page in the document
            foreach (Page page in document.Pages)
            {
                // Create a Watermark Annotation
                var annotation = new Aspose.Pdf.Annotations.WatermarkAnnotation(page, page.Rect);
                XForm form = annotation.Appearance["N"];
                form.BBox = page.Rect;

                string name;

                // Add the image to the form resources if it hasn't been added yet
                if (image == null)
                {
                    name = form.Resources.Images.Add(imageStream);
                    image = form.Resources.Images[name];
                }
                else
                {
                    name = form.Resources.Images.Add(image);
                }

                // Add operators to the form contents to place the image
                form.Contents.Add(new Aspose.Pdf.Operators.GSave());
                form.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(new Aspose.Pdf.Matrix(imageRectangle.Width, 0, 0, imageRectangle.Height, 0, 0)));
                form.Contents.Add(new Aspose.Pdf.Operators.Do(name));
                form.Contents.Add(new Aspose.Pdf.Operators.GRestore());

                // Add the annotation to the page
                page.Annotations.Add(annotation, false);

                // Adjust the image rectangle size for the next iteration
                imageRectangle = new Aspose.Pdf.Rectangle(0, 0, imageRectangle.Width * 1.01, imageRectangle.Height * 1.01);
            }
        }

        // Save PDF document
        document.Save(dataDir + "AddWatermarkAnnotationWithImage_out.pdf");
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