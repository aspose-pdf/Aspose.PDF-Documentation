---
title: DICOM 이미지 지원
linktitle: DICOM 이미지 지원
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 100
url: /ko/net/support-for-dicom-mages/
description: 이 섹션에서는 C# 라이브러리를 사용하여 PDF 파일에서 DICOM 이미지를 지원하는 방법을 설명합니다.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Support for DICOM Images",
    "alternativeHeadline": "Add DICOM images to PDFs using C# library",
    "abstract": "Aspose.PDF for .NET은 DICOM 이미지 지원을 통합하여 의료 이미지를 PDF 문서에 원활하게 삽입할 수 있게 합니다. 이 새로운 기능은 PDF 생성 과정에서 DICOM 이미지 처리를 효율적으로 수행하기 위해 C# 라이브러리를 활용합니다. 이 기능은 PDF 파일에 DICOM 이미지를 포함하는 작업 흐름을 단순화합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "DICOM images, PDF, C#, Aspose.PDF, DICOM to PDF, add DICOM to PDF, .NET library, ImageFileType.Dicom",
    "wordcount": "194",
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
    "url": "/net/support-for-dicom-mages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/support-for-dicom-mages/"
    },
    "dateModified": "2024-11-26",
    "description": "이 섹션에서는 C# 라이브러리를 사용하여 PDF 파일에서 DICOM 이미지를 지원하는 방법을 설명합니다."
}
</script>

DICOM 표준은 미국 전기기계 제조업체 협회(NEMA)에 의해 개발되었습니다. 이 형식은 개별 이미지 프레임, 프레임 시리즈, 환자 정보, 연구, 장비, 기관, 검사를 수행하는 의료 인력 등을 생성, 저장, 전송 및 인쇄하는 기능을 포함합니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

**Aspose.PDF for .NET**은 PDF 문서에 DICOM 이미지를 추가하는 기능을 지원합니다. 다음 코드 스니펫은 이 기능을 사용하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddDicomImageToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create an image instance and set its properties
        var image = new Aspose.Pdf.Image
        {
            FileType = Aspose.Pdf.ImageFileType.Dicom,
            ImageStream = new FileStream(dataDir + "DicomImage.dcm", FileMode.Open, FileAccess.Read)
        };

        // Add image to the first page
        page.Paragraphs.Add(image);

        // Save PDF document
        document.Save(dataDir + "PdfWithDicomImage_out.pdf");
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