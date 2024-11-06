---
title: 既存のPDFファイルで画像を置換
linktitle: 画像置換
type: docs
weight: 70
url: ja/net/replace-image-in-existing-pdf-file/
description: このセクションでは、C#ライブラリを使用して既存のPDFファイルで画像を置換する方法について説明します。
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "既存のPDFファイルで画像を置換",
    "alternativeHeadline": "PDFで画像を置換する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF文書生成",
    "keywords": "pdf, dotnet, pdfで画像を置換",
    "wordcount": "302",
    "proficiencyLevel":"初心者",
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
    "url": "/net/replace-image-in-existing-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/replace-image-in-existing-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "このセクションでは、C#ライブラリを使用して既存のPDFファイルで画像を置換する方法について説明します。"
}
</script>
以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリでも動作します。

画像コレクションの [Replace](https://reference.aspose.com/pdf/net/aspose.pdf/ximagecollection/methods/replace/index) メソッドを使用すると、既存のPDFファイルの画像を置換することができます。

画像コレクションは、ページのリソースコレクションで見つけることができます。画像を置換するには：

1. Document オブジェクトを使用してPDFファイルを開きます。
2. 特定の画像を置換し、Document オブジェクトの Save メソッドを使用して更新されたPDFファイルを保存します。

以下のコードスニペットは、PDFファイルで画像を置換する方法を示しています。

```csharp
// ドキュメントを開く
Document pdfDocument = new Document("input.pdf");
// 特定の画像を置換
pdfDocument.Pages[1].Resources.Images.Replace(1, new FileStream("lovely.jpg", FileMode.Open));
// 更新されたPDFファイルを保存
pdfDocument.Save("output.pdf");
```

