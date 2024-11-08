---
title: PythonでプログラムによるPDFページのトリミング
linktitle: ページをトリミング
type: docs
weight: 70
url: /ja/python-net/crop-pages/
description: Aspose.PDF for Python via .NETを使用して、幅、高さ、裁ち落とし、トリムボックスなどのページプロパティを取得できます。
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PythonでプログラムによるPDFページのトリミング",
    "alternativeHeadline": "PythonでPDFページをトリミングする方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, pdfページのトリミング",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "url": "/python-net/crop-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/crop-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for Python via .NETを使用して、幅、高さ、裁ち落とし、トリムボックスなどのページプロパティを取得できます。"
}
</script>


## ページプロパティを取得する

PDFファイルの各ページには、幅、高さ、塗り足し、裁ち落とし、トリムボックスなどの多くのプロパティがあります。Aspose.PDF for Pythonを使用すると、これらのプロパティにアクセスできます。

- **media_box**: メディアボックスは、最大のページボックスです。これは、PostScriptやPDFに印刷されたときに選択されたページサイズ（例えばA4、A5、USレターなど）に対応します。言い換えれば、メディアボックスはPDFドキュメントが表示または印刷されるメディアの物理的サイズを決定します。
- **bleed_box**: ドキュメントに塗り足しがある場合、PDFには塗り足しボックスも含まれます。塗り足しは、ページの端を超えて広がる色（またはアートワーク）の量です。これは、ドキュメントが印刷されてサイズに合わせて裁断される（「トリム」される）ときに、インクがページの端まで完全に達するようにするために使用されます。ページが誤って裁断されて - トリムマークからわずかにずれて切られた場合でも - ページに白い端が現れることはありません。
- **trim_box**: トリムボックスは、印刷とトリミングの後のドキュメントの最終サイズを示します。
- **art_box**: アートボックスは、ドキュメント内のページの実際の内容の周りに描かれたボックスです。
 このページボックスは、他のアプリケーションでPDFドキュメントをインポートする際に使用されます。
- **crop_box**: crop boxは、Adobe AcrobatでPDFドキュメントが表示される「ページ」のサイズです。通常のビューでは、Adobe Acrobatにcrop boxの内容のみが表示されます。これらのプロパティの詳細な説明については、Adobe.Pdfの仕様、特に10.10.1ページ境界を参照してください。

以下のスニペットは、ページをクロップする方法を示しています:

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)

    # 新しいボックス矩形を作成
    new_box = ap.Rectangle(200, 220, 2170, 1520, True)
    document.pages[1].crop_box = new_box
    document.pages[1].trim_box = new_box
    document.pages[1].art_box = new_box
    document.pages[1].bleed_box = new_box

    document.save(output_pdf)
```

この例では、サンプルファイルを[こちら](crop_page.pdf)で使用しました。最初は、図1に示されているようにページが表示されます。
![Figure 1. Cropped Page](crop_page.png)

変更後、ページは図2のように表示されます。
![Figure 2. Cropped Page](crop_page2.png)

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "applicationCategory": "Python用PDF操作ライブラリ",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>