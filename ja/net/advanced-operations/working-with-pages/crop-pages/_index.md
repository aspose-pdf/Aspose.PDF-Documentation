```
---
title: Crop PDF Pages programmatically C#
linktitle: Crop Pages
type: docs
weight: 80
url: ja/net/crop-pages/
description: Aspose.PDF for .NET を使用して、幅、高さ、ブリードボックス、クロップボックス、トリムボックスなどのページプロパティを取得できます。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Crop PDF Pages programmatically C#",
    "alternativeHeadline": "How to crop PDF Pages in .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, crop pdf pages",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/crop-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/crop-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NET を使用して、幅、高さ、ブリードボックス、クロップボックス、トリムボックスなどのページプロパティを取得できます。"
}
</script>
```
## ページのプロパティを取得する

PDFファイルの各ページには、幅、高さ、ブリード、クロップ、トリムボックスなど、多くのプロパティがあります。Aspose.PDFを使用すると、これらのプロパティにアクセスできます。

- **メディアボックス**: メディアボックスは最大のページボックスです。これは、ドキュメントがPostScriptまたはPDFに印刷されたときに選択されたページサイズ（例えばA4、A5、USレターなど）に対応します。言い換えれば、メディアボックスはPDFドキュメントが表示または印刷されるメディアの物理的なサイズを決定します。
- **ブリードボックス**: ドキュメントにブリードがある場合、PDFにもブリードボックスがあります。ブリードは、ページの端を超えて伸びる色（またはアートワーク）の量です。これは、ドキュメントが印刷されてサイズにカット（「トリミング」）されたときに、インクがページの端まで行くことを確実にするために使用されます。ページがトリムマークからわずかに外れてカットされた場合でも - ミストリムされた場合でも - ページに白い端が表示されることはありません。
- **トリムボックス**: トリムボックスは、印刷およびトリミング後のドキュメントの最終サイズを示します。
- **アートボックス**: アートボックスは、ドキュメントのページの実際の内容を囲むボックスです。
- **アートボックス**: アートボックスは、ドキュメントのページの実際の内容を囲むボックスです。
- **クロップボックス**: クロップボックスは、PDFドキュメントがAdobe Acrobatで表示される「ページ」のサイズです。通常のビューでは、Adobe Acrobatでクロップボックスの内容のみが表示されます。これらのプロパティの詳細な説明については、Adobe.Pdfの仕様、特に10.10.1 ページ境界を参照してください。
- **Page.Rect**: MediaBoxとDropBoxの交差点（一般的には可視矩形）。以下の画像はこれらのプロパティを示しています。
詳細については、[このページ](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html)をご覧ください。

以下のコードスニペットも [Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリで動作します。

以下のスニペットは、ページをクロップする方法を示しています：

```csharp
public static void CropPagesPDF()
{
    var pdfDocument1 = new Aspose.Pdf.Document("crop_page.pdf");
    Console.WriteLine(pdfDocument1.Pages[1].CropBox);
    Console.WriteLine(pdfDocument1.Pages[1].TrimBox);
    Console.WriteLine(pdfDocument1.Pages[1].ArtBox);
    Console.WriteLine(pdfDocument1.Pages[1].BleedBox);
    Console.WriteLine(pdfDocument1.Pages[1].MediaBox);

    // 新しいボックス矩形を作成
    var newBox = new Rectangle(200, 220, 2170, 1520);
    pdfDocument1.Pages[1].CropBox = newBox;
    pdfDocument1.Pages[1].TrimBox = newBox;
    pdfDocument1.Pages[1].ArtBox = newBox;
    pdfDocument1.Pages[1].BleedBox = newBox;
   
    pdfDocument1.Save("crop_page_modified.pdf");           
}
```
この例では、[こちら](crop_page.pdf)のサンプルファイルを使用しました。最初にページは図1に示されています。
![図1. クロップされたページ](crop_page.png)

変更後、ページは図2のようになります。
![図2. クロップされたページ](crop_page2.png)

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

