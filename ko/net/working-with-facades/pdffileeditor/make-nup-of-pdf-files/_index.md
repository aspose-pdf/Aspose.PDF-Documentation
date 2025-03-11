---
title: PDF 파일의 NUp 만들기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 90
url: /ko/net/make-nup-of-pdf-files/
description: 이 문서에서는 PdfFileEditor 클래스를 사용하여 Aspose.PDF Facades로 PDF 파일의 NUp을 만드는 방법을 보여줍니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Make NUp of PDF files",
    "alternativeHeadline": "Create NUp PDFs with Flexible Input Methods",
    "abstract": "Aspose.PDF for .NET의 NUp 기능은 사용자가 여러 PDF 파일을 효율적으로 결합하여 단일 출력 문서로 만들 수 있도록 하며, 페이지 크기 및 레이아웃 구성을 사용자 정의할 수 있습니다. 이 기능은 파일 경로와 스트림을 모두 지원하여 다양한 워크플로우에 유연하게 통합할 수 있으며 문서 프레젠테이션을 향상시킵니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "895",
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
    "url": "/net/make-nup-of-pdf-files/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/make-nup-of-pdf-files/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

## 파일 경로를 사용하여 PDF의 NUp 만들기

[MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) 메서드는 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 클래스의 메서드로, 입력 PDF 파일의 NUp을 만들고 출력 PDF 파일로 저장할 수 있습니다. 이 오버로드는 파일 경로를 사용하여 NUp을 만들 수 있습니다. 다음 코드 스니펫은 파일 경로를 사용하여 NUP을 만드는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make NUp
    pdfEditor.MakeNUp(dataDir + "MakeNupInput.pdf", dataDir + "MakeNupInput2.pdf", "MakeNUpUsingPaths_out.pdf");
}
```

## 페이지 크기 및 파일 경로를 사용하여 NUp 만들기

[MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) 메서드는 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 클래스의 메서드로, 입력 PDF 파일의 NUp을 만들고 출력 PDF 파일로 저장할 수 있습니다. 이 오버로드는 파일 경로를 사용하여 NUp을 만들 수 있습니다. 이 오버로드를 사용하여 출력 PDF 파일의 페이지 크기도 설정할 수 있습니다. 다음 코드 스니펫은 페이지 크기와 파일 경로를 사용하여 NUp을 만드는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupUsingPageSizeAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make NUp
    pdfEditor.MakeNUp(dataDir + "MakeNupMultiplePagesInput.pdf", dataDir + "MakeNUpUsingPageSizeAndPaths_out.pdf", 2, 3, PageSize.A5);
}
```

## 페이지 크기, 수평 및 수직 값, 파일 경로를 사용하여 PDF의 NUp 만들기

[MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) 메서드는 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 클래스의 메서드로, 입력 PDF 파일의 NUp을 만들고 출력 PDF 파일로 저장할 수 있습니다. 이 오버로드는 파일 경로를 사용하여 NUp을 만들 수 있습니다. 이 오버로드를 사용하여 출력 PDF 파일의 페이지 크기와 각 출력 페이지의 수평 및 수직 페이지 수를 설정할 수 있습니다. 다음 코드 스니펫은 페이지 크기, 수평 및 수직 값을 사용하여 NUp을 만드는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingPageSizeHorizontalAndVerticalValuesAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make NUp
    pdfEditor.MakeNUp(dataDir + "MakeNupInput.pdf", "MakeNUpUsingPageSizeHorizontalAndVerticalValues_out.pdf", 2, 3);
}
```

## PDF 파일 배열 및 파일 경로를 사용하여 NUp 만들기

[MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) 메서드는 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 클래스의 메서드로, 입력 PDF 파일 배열의 NUp을 만들고 이를 단일 출력 PDF 파일로 저장할 수 있습니다. 이 오버로드는 파일 경로를 사용하여 NUp을 만들 수 있습니다. 다음 코드 스니펫은 PDF 파일 배열과 파일 경로를 사용하여 NUp을 만드는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingArrayOfPdfFilesAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create array of files
    string[] filesArray = new string[2];
    filesArray[0] = dataDir + "MakeNupInput.pdf";
    filesArray[1] = dataDir + "MakeNupInput2.pdf";
    // Make NUp
    pdfEditor.MakeNUp(filesArray, dataDir + "MakeNupUsingArrayOfFilesAndPaths_out.pdf", true);
}
```

## 스트림을 사용하여 PDF의 NUp 만들기

[MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) 메서드는 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 클래스의 메서드로, 입력 PDF 스트림의 NUp을 만들고 이를 출력 PDF 스트림으로 저장할 수 있습니다. 이 오버로드는 파일 경로 대신 스트림을 사용하여 NUp을 만들 수 있습니다. 다음 코드 스니펫은 스트림을 사용하여 NUp을 만드는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream1 = new FileStream(dataDir + "MakeNupInput.pdf", FileMode.Open))
    {
        using (var inputStream2 = new FileStream(dataDir + "MakeNupInput2.pdf", FileMode.Open))
        {
            using (var outputStream = new FileStream(dataDir + "MakeNUpUsingStreams_out.pdf", FileMode.Create))
            {
                // Make NUp
                pdfEditor.MakeNUp(inputStream1, inputStream2, outputStream);
            }
        }
    }
}
```

## 페이지 크기 및 스트림을 사용하여 NUp 만들기

[MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) 메서드는 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 클래스의 메서드로, 입력 PDF 스트림의 NUp을 만들고 이를 출력 PDF 스트림으로 저장할 수 있습니다. 이 오버로드는 파일 경로 대신 스트림을 사용하여 NUp을 만들 수 있습니다. 이 오버로드를 사용하여 출력 PDF 스트림의 페이지 크기도 설정할 수 있습니다. 다음 코드 스니펫은 페이지 크기와 스트림을 사용하여 NUp을 만드는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingPageSizeAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeNupInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeNUpUsingPageSizeAndStreams_out.pdf", FileMode.Create))
        {
            // Make NUp
            pdfEditor.MakeNUp(inputStream, outputStream, 2, 3, PageSize.A5);    
        }    
    }
}
```

## 페이지 크기, 수평 및 수직 값, 스트림을 사용하여 PDF의 NUp 만들기

[MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) 메서드는 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 클래스의 메서드로, 입력 PDF 스트림의 NUp을 만들고 이를 출력 PDF 스트림으로 저장할 수 있습니다. 이 오버로드는 파일 경로 대신 스트림을 사용하여 NUp을 만들 수 있습니다. 이 오버로드를 사용하여 출력 PDF 스트림의 페이지 크기와 각 출력 페이지의 수평 및 수직 페이지 수를 설정할 수 있습니다. 다음 코드 스니펫은 페이지 크기, 수평 및 수직 값을 사용하여 NUp을 만드는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingPageSizeHorizontalAndVerticalValuesAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeNupInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeNUpUsingPageSizeHorizontalVerticalValuesAndStreams_out.pdf", FileMode.Create))
        {
            // Make NUp
            pdfEditor.MakeNUp(inputStream, outputStream, 2, 3); 
        }
    }
}
```

## PDF 파일 배열 및 스트림을 사용하여 NUp 만들기

[MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) 메서드는 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 클래스의 메서드로, 입력 PDF 스트림 배열의 NUp을 만들고 이를 단일 출력 PDF 스트림으로 저장할 수 있습니다. 이 오버로드는 파일 경로 대신 스트림을 사용하여 NUp을 만들 수 있습니다. 다음 코드 스니펫은 스트림을 사용하여 PDF 파일 배열로 NUp을 만드는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingArrayOfPdfFilesAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var stream1 = new FileStream(dataDir + "MakeNupInput.pdf", FileMode.Open))
    {
        using (var stream2 = new FileStream(dataDir + "MakeNupInput2.pdf", FileMode.Open))
        {
            using (var outputStream = new FileStream(dataDir + "MakeNUpUsingArrayOfFilesAndStreams_out.pdf", FileMode.Create))
            {
                var fileStreams = new Stream[2];
                fileStreams[0] = stream1;
                fileStreams[1] = stream2;
                // Make NUp
                pdfEditor.MakeNUp(fileStreams, outputStream, true);
            }
        }
    }
}
```