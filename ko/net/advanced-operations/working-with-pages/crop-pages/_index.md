---
title: Crop PDF Pages programmatically C#
linktitle: Crop Pages
type: docs
weight: 80
url: /ko/net/crop-pages/
description: Aspose.PDF for .NET을 사용하여 너비, 높이, 블리드, 크롭 및 트림박스와 같은 페이지 속성을 얻을 수 있습니다.
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
    "alternativeHeadline": ".NET에서 PDF 페이지를 자르는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, c#, crop pdf pages",
    "wordcount": "302",
    "proficiencyLevel":"초급",
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
    "description": "Aspose.PDF for .NET을 사용하여 너비, 높이, 블리드, 크롭 및 트림박스와 같은 페이지 속성을 얻을 수 있습니다."
}
</script>

## 페이지 속성 가져오기

PDF 파일의 각 페이지에는 너비, 높이, 블리드, 크롭 및 트림박스와 같은 여러 속성이 있습니다. Aspose.PDF를 사용하면 이러한 속성에 접근할 수 있습니다.

- **미디어 박스**: 미디어 박스는 가장 큰 페이지 박스입니다. 문서가 포스트스크립트 또는 PDF로 인쇄될 때 선택된 페이지 크기(예: A4, A5, US Letter 등)에 해당합니다. 즉, 미디어 박스는 PDF 문서가 표시되거나 인쇄되는 미디어의 물리적 크기를 결정합니다.
- **블리드 박스**: 문서에 블리드가 있는 경우, PDF에도 블리드 박스가 있습니다. 블리드는 페이지 가장자리를 넘어 확장되는 색상(또는 아트워크)의 양입니다. 문서가 인쇄되고 크기에 맞게 잘릴 때("트리밍"), 잉크가 페이지 가장자리까지 도달하도록 하기 위해 사용됩니다. 페이지가 트림 표시에서 약간 벗어나 잘릴 경우에도 페이지에 흰색 가장자리가 나타나지 않습니다.
- **트림 박스**: 트림 박스는 인쇄 및 트리밍 후 문서의 최종 크기를 나타냅니다.
- **아트 박스**: 아트 박스는 문서의 페이지에 있는 실제 내용 주변에 그려진 박스입니다.
- **Art box**: 문서 페이지의 실제 내용 주변에 그려진 상자입니다.
- **Crop box**: PDF 문서가 Adobe Acrobat에서 표시되는 "페이지" 크기입니다. 일반 보기에서는 Adobe Acrobat에서 Crop box의 내용만 표시됩니다. 이러한 속성의 자세한 설명은 Adobe.Pdf 사양, 특히 10.10.1 페이지 경계를 참조하십시오.
- **Page.Rect**: MediaBox와 DropBox의 교차점(일반적으로 보이는 직사각형)입니다. 아래 그림은 이러한 속성을 설명합니다.
자세한 내용은 [이 페이지](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html)를 방문하십시오.

다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리에서도 작동합니다.

아래 코드 조각은 페이지를 크롭하는 방법을 보여줍니다:

```csharp
public static void CropPagesPDF()
{
    var pdfDocument1 = new Aspose.Pdf.Document("crop_page.pdf");
    Console.WriteLine(pdfDocument1.Pages[1].CropBox);
    Console.WriteLine(pdfDocument1.Pages[1].TrimBox);
    Console.WriteLine(pdfDocument1.Pages[1].ArtBox);
    Console.WriteLine(pdfDocument1.Pages[1].BleedBox);
    Console.WriteLine(pdfDocument1.Pages[1].MediaBox);

    // 새로운 박스 직사각형 생성
    var newBox = new Rectangle(200, 220, 2170, 1520);
    pdfDocument1.Pages[1].CropBox = newBox;
    pdfDocument1.Pages[1].TrimBox = newBox;
    pdfDocument1.Pages[1].ArtBox = newBox;
    pdfDocument1.Pages[1].BleedBox = newBox;
   
    pdfDocument1.Save("crop_page_modified.pdf");           
}
```
이 예에서 우리는 [여기](crop_page.pdf)에 있는 샘플 파일을 사용했습니다. 처음에 우리 페이지는 그림 1에 나타난 것처럼 보입니다.
![그림 1. 자른 페이지](crop_page.png)

변경 후 페이지는 그림 2처럼 보일 것입니다.
![그림 2. 자른 페이지](crop_page2.png)

