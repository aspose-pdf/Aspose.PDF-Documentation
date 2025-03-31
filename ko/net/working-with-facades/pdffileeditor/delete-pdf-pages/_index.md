---
title: PDF 페이지 삭제
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /ko/net/delete-pdf-pages/
description: 이 섹션에서는 PdfFileEditor 클래스를 사용하여 Aspose.PDF Facades로 PDF 페이지를 삭제하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Delete PDF pages",
    "alternativeHeadline": "Effortlessly Remove Pages from PDF Files",
    "abstract": "Aspose.PDF for .NET Facades를 사용하여 PDF 문서에서 특정 페이지를 손쉽게 삭제하세요. PdfFileEditor 클래스를 활용하면 파일 경로와 스트림 모두에서 원하지 않는 페이지를 제거하여 최종 출력에 대한 정확한 제어로 PDF 편집 프로세스를 간소화할 수 있습니다. 이 효율적인 페이지 삭제 기능으로 문서 관리 능력을 향상시키세요.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "262",
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
    "url": "/net/delete-pdf-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/delete-pdf-pages/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

디스크에 있는 PDF 파일에서 여러 페이지를 삭제하려면 다음 세 가지 매개변수를 사용하는 [Delete](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/delete/index) 메서드의 오버로드를 사용할 수 있습니다: 입력 파일 경로, 삭제할 페이지 번호 배열, 출력 PDF 파일 경로. 두 번째 매개변수는 삭제해야 할 모든 페이지를 나타내는 정수 배열입니다. 지정된 페이지는 입력 파일에서 제거되며 결과는 출력 파일로 저장됩니다. 다음 코드 스니펫은 파일 경로를 사용하여 PDF 페이지를 삭제하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeletePages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Array of pages to delete
    var pagesToDelete = new int[] { 1, 2 };
    // Delete pages
    pdfEditor.Delete(dataDir + "DeletePagesInput.pdf", pagesToDelete, dataDir + "DeletePagesUsingFilePath_out.pdf");
}
```

## 스트림을 사용한 PDF 페이지 삭제

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 클래스의 [Delete](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/delete/index) 메서드는 입력 PDF 파일에서 페이지를 삭제할 수 있는 오버로드도 제공합니다. 이 오버로드는 입력 및 출력 파일이 모두 스트림에 있을 때 사용됩니다. 이 오버로드는 다음 세 가지 매개변수를 사용합니다: 입력 스트림, 삭제할 PDF 페이지의 정수 배열, 출력 스트림. 다음 코드 스니펫은 스트림을 사용하여 PDF 페이지를 삭제하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeletePagesUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "DeletePagesInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "DeletePagesUsingStream_out.pdf", FileMode.Create))
        {
            // Array of pages to delete
            var pagesToDelete = new int[] { 1, 2 };
            // Delete pages
            pdfEditor.Delete(inputStream, pagesToDelete, outputStream);
        }
    }
}
```