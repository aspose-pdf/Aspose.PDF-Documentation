---
title: PDF 페이지 삽입
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ko/net/insert-pdf-pages/
description: 이 섹션에서는 PdfFileEditor 클래스를 사용하여 Aspose.PDF Facades로 PDF 페이지를 삽입하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Insert PDF pages",
    "alternativeHeadline": "Insert Specific PDF Pages into Existing Documents",
    "abstract": "Aspose.PDF for .NET PdfFileEditor 클래스를 사용하여 한 PDF에서 다른 PDF로 특정 페이지를 삽입할 수 있는 새로운 기능으로 PDF 관리 최적화. 이 기능은 범위 기반 및 배열 기반 페이지 삽입을 모두 지원하여 파일 경로 또는 스트림을 통해 문서를 원활하게 결합하여 작업 효율성을 향상시킵니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "751",
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
    "url": "/net/insert-pdf-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/insert-pdf-pages/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

## 파일 경로를 사용하여 두 숫자 사이에 PDF 페이지 삽입

특정 페이지 범위를 한 PDF에서 다른 PDF로 삽입할 수 있습니다. [PdfFileEditor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffileeditor) 클래스의 [Insert](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) 메서드를 사용합니다. 이를 위해서는 페이지를 삽입할 입력 PDF 파일, 삽입을 위해 페이지를 가져올 포트 파일, 페이지를 삽입할 위치, 입력 PDF 파일에 삽입해야 할 포트 파일의 페이지 범위가 필요합니다. 이 범위는 시작 페이지 및 종료 페이지 매개변수로 지정됩니다. 마지막으로, 지정된 페이지 범위가 삽입된 출력 PDF 파일이 저장됩니다. 다음 코드 스니펫은 파일 스트림을 사용하여 두 숫자 사이에 PDF 페이지를 삽입하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertPdfPagesBetweenTwoNumbersUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Insert pages
    pdfEditor.Insert(
        dataDir + "MultiplePages.pdf", 1, 
        dataDir + "InsertPages.pdf", 2, 5, 
        dataDir + "InsertPagesBetweenNumbers_out.pdf");
}
```

## 파일 경로를 사용하여 PDF 페이지 배열 삽입

특정 페이지를 다른 PDF 파일에 삽입하려면, 페이지의 정수 배열을 요구하는 [Insert](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) 메서드의 오버로드를 사용할 수 있습니다. 이 배열에서 입력 PDF 파일에 삽입할 특정 페이지를 지정할 수 있습니다. 이를 위해서는 페이지를 삽입할 입력 PDF 파일, 삽입을 위해 페이지를 가져올 포트 파일, 페이지를 삽입할 위치, 입력 PDF 파일에 삽입해야 할 포트 파일의 페이지 정수 배열이 필요합니다. 이 배열에는 입력 PDF 파일에 삽입하고자 하는 특정 페이지 목록이 포함되어 있습니다. 마지막으로, 지정된 페이지 배열이 삽입된 출력 PDF 파일이 저장됩니다. 다음 코드 스니펫은 파일 경로를 사용하여 PDF 페이지 배열을 삽입하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertArrayOfPdfPagesUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    var pagesToInsert = new int[] { 2, 3 };
    // Insert pages
    pdfEditor.Insert(
        dataDir + "MultiplePages.pdf", 1, 
        dataDir + "InsertPages.pdf", pagesToInsert, 
        dataDir + "InsertArrayOfPages_out.pdf");
}
```

## 스트림을 사용하여 두 숫자 사이에 PDF 페이지 삽입

스트림을 사용하여 페이지 범위를 삽입하려면, [PdfFileEditor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffileeditor) 클래스의 [Insert](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) 메서드의 적절한 오버로드를 사용하면 됩니다. 이를 위해서는 페이지를 삽입할 입력 PDF 스트림, 삽입을 위해 페이지를 가져올 포트 스트림, 페이지를 삽입할 위치, 입력 PDF 스트림에 삽입해야 할 포트 스트림의 페이지 범위가 필요합니다. 이 범위는 시작 페이지 및 종료 페이지 매개변수로 지정됩니다. 마지막으로, 지정된 페이지 범위가 삽입된 출력 PDF 스트림이 저장됩니다. 다음 코드 스니펫은 스트림을 사용하여 두 숫자 사이에 PDF 페이지를 삽입하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertPdfPagesBetweenTwoNumbersUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (var portStream = new FileStream(dataDir + "InsertPages.pdf", FileMode.Open))
        {
            using (var outputStream = new FileStream(dataDir + "InsertPagesBetweenNumbersUsingStreams_out.pdf", FileMode.Create))
            {
                // Insert pages
                pdfEditor.Insert(inputStream, 1, portStream, 1, 4, outputStream);
            }
        }
    }
}
```

## 스트림을 사용하여 PDF 페이지 배열 삽입

스트림을 사용하여 페이지 배열을 다른 PDF 파일에 삽입할 수도 있습니다. 페이지의 정수 배열을 요구하는 Insert 메서드의 적절한 오버로드를 사용하면 됩니다. 이 배열에서 입력 PDF 스트림에 삽입할 특정 페이지를 지정할 수 있습니다. 이를 위해서는 페이지를 삽입할 입력 PDF 스트림, 삽입을 위해 페이지를 가져올 포트 스트림, 페이지를 삽입할 위치, 입력 PDF 파일에 삽입해야 할 포트 스트림의 페이지 정수 배열이 필요합니다. 이 배열에는 입력 PDF 스트림에 삽입하고자 하는 특정 페이지 목록이 포함되어 있습니다. 마지막으로, 지정된 페이지 배열이 삽입된 출력 PDF 스트림이 저장됩니다. 다음 코드 스니펫은 스트림을 사용하여 PDF 페이지 배열을 삽입하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertArrayOfPdfPagesUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Pages to insert
    var pagesToInsert = new int[] { 2, 3 };
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (var portStream = new FileStream(dataDir + "InsertPages.pdf", FileMode.Open))
        {
            using (var outputStream = new FileStream(dataDir + "InsertPagesUsingStreams_out.pdf", FileMode.Create))
            {
                // Insert pages
                pdfEditor.Insert(inputStream, 1, portStream, pagesToInsert, outputStream);
            }
        }
    }
}
```