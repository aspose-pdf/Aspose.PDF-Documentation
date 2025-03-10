---
title: PDF에서 이미지 추출 C#
linktitle: PDF에서 이미지 추출
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ko/net/extract-images-from-the-pdf-file/
description: C#에서 Aspose.PDF for .NET을 사용하여 PDF에서 이미지의 일부를 추출하는 방법
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
    "abstract": "C#에서 PDF 파일에서 이미지를 직접 추출하는 새로운 기능으로 Aspose.PDF for .NET의 힘을 활용하세요. 이 기능은 사용자가 특정 페이지에서 이미지를 쉽게 검색하고 저장할 수 있도록 하여 .NET 애플리케이션에서 효율적인 이미지 관리 및 처리를 촉진합니다.",
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
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

각 페이지의 [Resources](https://reference.aspose.com/pdf/net/aspose.pdf/resources) 컬렉션의 [Images](https://reference.aspose.com/pdf/net/aspose.pdf/resources/properties/images) 컬렉션에 이미지가 저장됩니다. 특정 페이지를 추출하려면 해당 이미지의 특정 인덱스를 사용하여 Images 컬렉션에서 이미지를 가져옵니다.

이미지의 인덱스는 [XImage](https://reference.aspose.com/pdf/net/aspose.pdf/ximage) 객체를 반환합니다. 이 객체는 추출된 이미지를 저장하는 데 사용할 수 있는 Save 메서드를 제공합니다. 다음 코드 스니펫은 PDF 파일에서 이미지를 추출하는 방법을 보여줍니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와도 작동합니다.

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