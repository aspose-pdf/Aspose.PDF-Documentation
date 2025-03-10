---
title: 중심점을 기준으로 스탬프 회전
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ko/net/rotating-stamp-about-the-center-point/
description: 이 섹션에서는 Stamp 클래스를 사용하여 중심점을 기준으로 스탬프를 회전하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Rotating stamp about the center point",
    "alternativeHeadline": "Rotate Stamps Precisely Around Their Center Point",
    "abstract": "Aspose.PDF for .NET의 기능은 사용자가 PDF 파일 내에서 스탬프를 중심점을 기준으로 정확하게 회전할 수 있도록 합니다. Stamp 클래스를 활용하여 개발자는 0도에서 360도까지의 회전 값을 쉽게 설정할 수 있으며, 문서 내 워터마크 배치의 유연성과 사용자 정의를 향상시킵니다. 이 기능은 개인화된 스탬프 방향으로 시각적으로 역동적인 PDF를 만드는 데 이상적입니다.",
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
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

{{% alert color="primary" %}}

[Aspose.Pdf.Facades 네임스페이스](https://reference.aspose.com/pdf/net/aspose.pdf.facades)는 [Aspose.PDF for .NET](/pdf/net/)에서 기존 PDF 파일에 스탬프를 추가할 수 있게 해줍니다. 때때로 사용자는 스탬프를 회전해야 할 필요가 있습니다. 이 기사에서는 스탬프를 중심점을 기준으로 회전하는 방법을 살펴보겠습니다.

{{% /alert %}}

## 구현 세부사항

[Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 클래스는 PDF 파일에 워터마크를 추가할 수 있게 해줍니다. [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.stamp/bindimage/methods/1) 메서드를 사용하여 스탬프로 추가할 이미지를 지정할 수 있습니다. [SetOrigin](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/setorigin) 메서드는 추가된 스탬프의 원점을 설정할 수 있게 해주며, 이 원점은 스탬프의 왼쪽 아래 좌표입니다. [SetImageSize](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/setimagesize) 메서드를 사용하여 이미지의 크기도 설정할 수 있습니다.

이제 스탬프를 스탬프의 중심을 기준으로 회전하는 방법을 살펴보겠습니다. [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 클래스는 Rotation이라는 속성을 제공합니다. 이 속성은 스탬프 콘텐츠의 회전을 0도에서 360도까지 설정하거나 가져옵니다. 우리는 0도에서 360도까지의 회전 값을 지정할 수 있습니다. 회전 값을 지정함으로써 스탬프를 중심점을 기준으로 회전할 수 있습니다. Stamp가 Stamp 유형의 객체인 경우 회전 값은 aStamp.Rotation = 90으로 지정할 수 있습니다. 이 경우 스탬프는 스탬프 콘텐츠의 중심을 기준으로 90도 회전합니다. 다음 코드 스니펫은 스탬프를 중심점을 기준으로 회전하는 방법을 보여줍니다:


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