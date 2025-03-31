---
title: PDF 파일 정보 설정
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ko/net/set-pdf-file-information/
description: 이 섹션에서는 Aspose.PDF Facades를 사용하여 PDF 파일 정보를 설정하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Set PDF File Information",
    "alternativeHeadline": "Set Custom Metadata for PDF Files Effortlessly",
    "abstract": "Aspose.PDF for .NET의 새로운 기능을 통해 PDF 파일 관리를 향상시키고, 저자, 제목 및 키워드와 같은 파일 특정 정보를 쉽게 설정하고 업데이트할 수 있습니다. PdfFileInfo 클래스를 활용하여 PDF를 효율적으로 수정하고, 조직화 및 검색 가능성을 향상시키기 위해 귀중한 메타데이터를 추가하세요. SaveNewInfo 메서드를 사용하여 이러한 업데이트를 원활하게 저장하여 작업 흐름을 간소화하세요.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "251",
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
    "url": "/net/set-pdf-file-information/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/set-pdf-file-information/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 단순하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

[PdfFileInfo](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffileinfo) 클래스는 PDF 파일의 파일 특정 정보를 설정할 수 있게 해줍니다. [PdfFileInfo](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffileinfo) 클래스의 객체를 생성한 다음 저자, 제목, 키워드 및 작성자 등의 다양한 파일 특정 속성을 설정해야 합니다. 마지막으로 [PdfFileInfo](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffileinfo) 객체의 [SaveNewInfo](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades.pdffileinfo/savenewinfo/methods/1) 메서드를 사용하여 업데이트된 PDF 파일을 저장합니다.

다음 코드 스니펫은 PDF 파일 정보를 설정하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPdfInfo()
{
    // Define the directory for input and output files
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create PdfFileInfo object to work with PDF metadata
    using (var fileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "sample.pdf"))
    {
        // Set PDF information
        fileInfo.Author = "Aspose";
        fileInfo.Title = "Hello World!";
        fileInfo.Keywords = "Peace and Development";
        fileInfo.Creator = "Aspose";
        
        // Save the PDF with updated information
        fileInfo.SaveNewInfo(dataDir + "SetFileInfo_out.pdf");
    }
}
```

## 메타 정보 설정

[SetMetaInfo](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffileinfo/methods/setmetainfo) 메서드는 정보를 추가할 수 있게 해줍니다. 우리의 예제에서는 필드를 추가했습니다. 다음 코드 스니펫을 확인하세요:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetMetaInfo()
{
    // Define the directory for input and output files
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of the PdfFileInfo object
    using (var fileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "sample.pdf"))
    {
        // Set a new custom attribute as meta info
        fileInfo.SetMetaInfo("Reviewer", "Aspose.PDF user");

        // Save the updated file
        fileInfo.SaveNewInfo(dataDir + "SetMetaInfo_out.pdf");
    }
}
```