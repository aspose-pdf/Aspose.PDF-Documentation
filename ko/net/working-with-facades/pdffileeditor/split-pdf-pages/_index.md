---
title: PDF 페이지 나누기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /ko/net/split-pdf-pages/
description: 이 섹션에서는 PdfFileEditor 클래스를 사용하여 Aspose.PDF Facades로 PDF 페이지를 나누는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Split PDF pages",
    "alternativeHeadline": "Effortlessly Split PDF Pages via File Paths and Streams",
    "abstract": "Aspose.PDF for .NET의 새로운 PDF 페이지 나누기 기능은 사용자가 PdfFileEditor 클래스를 사용하여 PDF 문서를 효율적으로 다양한 세그먼트로 나눌 수 있도록 합니다. 이 기능은 첫 페이지에서 지정된 페이지까지 나누기, 대량 세트로 나누기, 개별 페이지를 분리하는 것을 지원하며, 모두 파일 경로 또는 스트림을 통해 PDF 조작을 위한 다양한 옵션을 제공합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1017",
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
    "url": "/net/split-pdf-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/split-pdf-pages/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

## 파일 경로를 사용하여 첫 페이지에서 PDF 페이지 나누기

[SplitFromFirst](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/splitfromfirst/methods/1) 메서드는 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 클래스의 메서드로, 지정된 페이지 번호에서 끝나는 첫 페이지부터 PDF 파일을 나눌 수 있습니다. 디스크에서 PDF 파일을 조작하려면 입력 및 출력 PDF 파일의 파일 경로를 이 메서드에 전달할 수 있습니다. 다음 코드 스니펫은 파일 경로를 사용하여 첫 페이지에서 PDF 페이지를 나누는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesFromFirstUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Split pages
    pdfEditor.SplitFromFirst(dataDir + "MultiplePages.pdf", 3, dataDir + "SplitPagesUsingPaths_out.pdf");
}
```

## 파일 스트림을 사용하여 첫 페이지에서 PDF 페이지 나누기

[SplitFromFirst](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/splitfromfirst/methods/1) 메서드는 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 클래스의 메서드로, 지정된 페이지 번호에서 끝나는 첫 페이지부터 PDF 파일을 나눌 수 있습니다. 스트림에서 PDF 파일을 조작하려면 입력 및 출력 PDF 스트림을 이 메서드에 전달할 수 있습니다. 다음 코드 스니펫은 파일 스트림을 사용하여 첫 페이지에서 PDF 페이지를 나누는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesFromFirstUsingFileStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "SplitPagesUsingStreams_out.pdf", FileMode.Create))
        {
            // Split pages
            pdfEditor.SplitFromFirst(inputStream, 3, outputStream);
        }
    }
}
```

## 파일 경로를 사용하여 대량으로 PDF 페이지 나누기

[SplitToBulks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittobulks/index) 메서드는 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 클래스의 메서드로, PDF 파일을 여러 페이지 세트로 나눌 수 있습니다. 이 예제에서는 두 세트의 페이지(1, 2) 및 (5, 6)가 필요합니다. 디스크에서 PDF 파일에 접근하려면 입력 PDF를 파일 경로로 전달해야 합니다. 이 메서드는 MemoryStream 배열을 반환합니다. 이 배열을 반복하여 개별 페이지 세트를 별도의 파일로 저장할 수 있습니다. 다음 코드 스니펫은 파일 경로를 사용하여 대량으로 PDF 페이지를 나누는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesToBulkUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    var fileNumber = 1;
    // Create array of pages to split
    var numberOfPages = new int[][] { new int[] { 1, 2 }, new int[] { 3, 4 } };
    // Split to bulk
    var outBuffer = pdfEditor.SplitToBulks(dataDir + "MultiplePages.pdf", numberOfPages);
    // Save individual files
    foreach (var outStream in outBuffer)
    {
        using (var outFileStream = new FileStream(dataDir + "File_" + fileNumber.ToString() + "_out.pdf", FileMode.Create))
        {
            outStream.WriteTo(outFileStream);
            fileNumber++;
        }
    }
}
```

## 스트림을 사용하여 대량으로 PDF 페이지 나누기

[SplitToBulks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittobulks/index) 메서드는 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 클래스의 메서드로, PDF 파일을 여러 페이지 세트로 나눌 수 있습니다. 이 예제에서는 두 세트의 페이지(1, 2) 및 (5, 6)가 필요합니다. 디스크에서 파일에 접근하는 대신 이 메서드에 스트림을 전달할 수 있습니다. 이 메서드는 MemoryStream 배열을 반환합니다. 이 배열을 반복하여 개별 페이지 세트를 별도의 파일로 저장할 수 있습니다. 다음 코드 스니펫은 스트림을 사용하여 대량으로 PDF 페이지를 나누는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesToBulkUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create input stream
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        var fileNumber = 1;
        // Create array of pages to split
        var numberOfPages = new int[][] { new int[] { 1, 2 }, new int[] { 3, 4 } };
        // Split to bulk
        var outBuffer = pdfEditor.SplitToBulks(inputStream, numberOfPages);
        // Save individual files
        foreach (var outStream in outBuffer)
        {
            using (var outFileStream = new FileStream(dataDir + "File_" + fileNumber.ToString() + "_out.pdf", FileMode.Create))
            {
                outStream.WriteTo(outFileStream);
                fileNumber++;
            }
        }
    }
}
```

## 파일 경로를 사용하여 끝에서 PDF 페이지 나누기

[SplitToEnd](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittoend/index) 메서드는 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 클래스의 메서드로, 지정된 페이지 번호에서 PDF 파일의 끝까지 나누고 새 PDF로 저장할 수 있습니다. 이를 위해 파일 경로를 사용하여 입력 및 출력 파일 경로와 나누기를 시작할 페이지 번호를 전달해야 합니다. 출력 PDF는 디스크에 저장됩니다. 다음 코드 스니펫은 파일 경로를 사용하여 끝에서 PDF 페이지를 나누는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesToEndUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Split pages
    pdfEditor.SplitToEnd(dataDir + "MultiplePages.pdf", 3, dataDir + "SplitPagesToEndUsingPaths_out.pdf");
}
```

## 스트림을 사용하여 끝에서 PDF 페이지 나누기

[SplitToEnd](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittoend/index) 메서드는 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 클래스의 메서드로, 지정된 페이지 번호에서 PDF 파일의 끝까지 나누고 새 PDF로 저장할 수 있습니다. 이를 위해 스트림을 사용하여 입력 및 출력 스트림과 나누기를 시작할 페이지 번호를 전달해야 합니다. 출력 PDF는 출력 스트림에 저장됩니다. 다음 코드 스니펫은 스트림을 사용하여 끝에서 PDF 페이지를 나누는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesToEndUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "SplitPagesToEndUsingStreams_out.pdf", FileMode.Create))
        {
            // Split pages
            pdfEditor.SplitToEnd(inputStream, 3, outputStream);   
        }
    }
}
```

## 파일 경로를 사용하여 PDF를 개별 페이지로 나누기

{{% alert color="primary" %}}

PDF 문서를 나누고 결과를 온라인에서 확인하려면 이 링크를 사용하세요:

[products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter) {{% /alert %}}

PDF 파일을 개별 페이지로 나누려면 [SplitToPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittopages/index) 메서드에 PDF를 파일 경로로 전달해야 합니다. 이 메서드는 PDF 파일의 개별 페이지를 포함하는 MemoryStream 배열을 반환합니다. 이 MemoryStream 배열을 반복하여 개별 페이지를 디스크에 개별 PDF 파일로 저장할 수 있습니다. 다음 코드 스니펫은 파일 경로를 사용하여 PDF를 개별 페이지로 나누는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfToIndividualPagesUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    var fileNumber = 1;
    // Split to pages
    var outBuffer = pdfEditor.SplitToPages(dataDir + "splitPdfToIndividualPagesInput.pdf");
    // Save individual files
    foreach (var outStream in outBuffer)
    {
        using (var outFileStream = new FileStream(dataDir + "File_" + fileNumber.ToString() + "_out.pdf", FileMode.Create))
        {
            outStream.WriteTo(outFileStream);
            fileNumber++;
        }
    }
}
```

## 스트림을 사용하여 PDF를 개별 페이지로 나누기

PDF 파일을 개별 페이지로 나누려면 [SplitToPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittopages/index) 메서드에 PDF를 스트림으로 전달해야 합니다. 이 메서드는 PDF 파일의 개별 페이지를 포함하는 MemoryStream 배열을 반환합니다. 이 MemoryStream 배열을 반복하여 개별 페이지를 디스크에 개별 PDF 파일로 저장하거나, 나중에 애플리케이션에서 사용할 수 있도록 이 개별 페이지를 메모리 스트림에 유지할 수 있습니다. 다음 코드 스니펫은 스트림을 사용하여 PDF를 개별 페이지로 나누는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfToIndividualPagesUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create input stream
    using (var inputStream = new FileStream(dataDir + "splitPdfToIndividualPagesInput.pdf", FileMode.Open))
    {
        var fileNumber = 1;
        // Split to pages
        var outBuffer = pdfEditor.SplitToPages(inputStream);
        // Save individual files
        foreach (var outStream in outBuffer)
        {
            using (var outFileStream = new FileStream(dataDir + "File_" + fileNumber.ToString() + "_out.pdf", FileMode.Create))
            {
                outStream.WriteTo(outFileStream);
                fileNumber++;
            }
        }
    }
}
```