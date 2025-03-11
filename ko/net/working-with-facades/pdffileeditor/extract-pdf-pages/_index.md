---
title: PDF 페이지 추출
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ko/net/extract-pdf-pages/
description: 이 섹션에서는 PdfFileEditor 클래스를 사용하여 Aspose.PDF Facades로 PDF 페이지를 추출하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract PDF pages",
    "alternativeHeadline": "Effortlessly Extract Selected Pages from PDF Files",
    "abstract": "Aspose.PDF for .NET Facades의 PDF 페이지 추출 기능은 사용자가 PDF 문서에서 페이지를 선택적으로 추출할 수 있는 향상된 기능을 제공합니다. PdfFileEditor 클래스를 활용하여 사용자는 파일 경로 또는 스트림을 통해 지정된 범위 또는 페이지 집합을 효율적으로 추출할 수 있어 문서 조작이 더 간편하고 유연해집니다. 이 기능은 원본 파일을 변경하지 않고 PDF 콘텐츠를 사용자 정의하려는 사용자에게 특히 유용합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "660",
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
    "url": "/net/extract-pdf-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-pdf-pages/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

## 두 숫자 사이의 PDF 페이지 추출 (파일 경로 사용)

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 클래스의 [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) 메서드는 PDF 파일에서 지정된 페이지 범위를 추출할 수 있습니다. 이 오버로드는 디스크에서 PDF 파일을 조작하면서 페이지를 추출할 수 있게 해줍니다. 이 오버로드는 다음 매개변수를 요구합니다: 입력 파일 경로, 시작 페이지, 종료 페이지 및 출력 파일 경로. 시작 페이지에서 종료 페이지까지의 페이지가 추출되며 출력은 디스크에 저장됩니다. 다음 코드 스니펫은 파일 경로를 사용하여 두 숫자 사이의 PDF 페이지를 추출하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Extract_PDFPages_FilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();

    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();

    // Extract pages
    pdfEditor.Extract(dataDir + "MultiplePages.pdf", 1, 3, dataDir + "ExtractPagesBetweenNumbers_out.pdf");
}
```

## 파일 경로를 사용한 PDF 페이지 배열 추출

페이지 범위를 추출하는 대신 특정 페이지 집합을 추출하려는 경우, [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) 메서드를 사용하여 그렇게 할 수 있습니다. 먼저 추출해야 할 모든 페이지 번호로 구성된 정수 배열을 생성해야 합니다. 이 [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) 메서드의 오버로드는 다음 매개변수를 요구합니다: 입력 PDF 파일, 추출할 페이지의 정수 배열 및 출력 PDF 파일. 다음 코드 스니펫은 파일 경로를 사용하여 PDF 페이지를 추출하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Extract_PDFPages_Streams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();

    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();

    // Create streams
    using (FileStream inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (FileStream outputStream = new FileStream(dataDir + "ExtractPagesBetweenTwoNumbers_out.pdf", FileMode.Create))
        {
            // Extract pages
            pdfEditor.Extract(inputStream, 1, 3, outputStream);
        }
    }
}
```

## 두 숫자 사이의 PDF 페이지 추출 (스트림 사용)

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 클래스의 [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) 메서드는 스트림을 사용하여 페이지 범위를 추출할 수 있습니다. 이 오버로드에 다음 매개변수를 전달해야 합니다: 입력 스트림, 시작 페이지, 종료 페이지 및 출력 스트림. 시작 페이지와 종료 페이지 사이의 범위로 지정된 페이지가 입력 스트림에서 추출되어 출력 스트림에 저장됩니다. 다음 코드 스니펫은 스트림을 사용하여 두 숫자 사이의 PDF 페이지를 추출하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Extract_ArrayPDFPages_FilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();

    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();
    int[] pagesToExtract = new int[] { 1, 2 };
    // Extract pages
    pdfEditor.Extract(dataDir + "Extract.pdf", pagesToExtract, dataDir + "ExtractArrayOfPages_out.pdf");
}
```

## 스트림을 사용한 PDF 페이지 배열 추출

PDF 스트림에서 페이지 배열을 추출하고 적절한 오버로드의 [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) 메서드를 사용하여 출력 스트림에 저장할 수 있습니다. 페이지 범위를 추출하는 대신 특정 페이지 집합을 추출하려는 경우, [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) 메서드를 사용하여 그렇게 할 수 있습니다. 먼저 추출해야 할 모든 페이지 번호로 구성된 정수 배열을 생성해야 합니다. 이 [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) 메서드의 오버로드는 다음 매개변수를 요구합니다: 입력 스트림, 추출할 페이지의 정수 배열 및 출력 스트림. 다음 코드 스니펫은 스트림을 사용하여 PDF 페이지를 추출하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Extract_ArrayPDFPages_Streams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    
    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();
    // Create streams
    using (FileStream inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (FileStream outputStream = new FileStream(dataDir + "ExtractArrayOfPagesUsingStreams_out.pdf", FileMode.Create))
        {
            int[] pagesToExtract = new int[] { 1, 2 };
            // Extract pages
            pdfEditor.Extract(inputStream, pagesToExtract, outputStream);
        }
    }
}
```