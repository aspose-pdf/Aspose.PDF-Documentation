---
title: PDF를 PowerPoint로 변환하기 (.NET)
linktitle: PDF를 PowerPoint로 변환하기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ko/net/convert-pdf-to-powerpoint/
lastmod: "2021-11-01"
description: Aspose.PDF를 사용하면 .NET을 통해 PDF를 PPT(파워포인트) 형식으로 변환할 수 있습니다. PDF를 PPTX로 변환할 수 있는 방법 중 하나는 이미지를 슬라이드로 변환하는 것입니다.
lastmod: "2021-10-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to PowerPoint in .NET",
    "alternativeHeadline": "Convert PDF Documents to PowerPoint Presentations Efficiently in C#",
    "abstract": "Aspose.PDF for .NET는 PDF 문서를 PowerPoint (PPTX) 형식으로 원활하게 변환할 수 있는 강력한 기능을 소개하며, 각 PDF 페이지가 별도의 슬라이드로 변환됩니다. 텍스트를 선택 가능하거나 이미지로 렌더링할 수 있는 옵션을 통해 사용자는 변환 진행 상황을 효율적으로 추적하면서 프레젠테이션을 쉽게 사용자 정의할 수 있습니다. 이 혁신적인 기능을 활용하여 문서 작업 흐름을 최적화하고 생산성을 향상시키세요.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1174",
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
    "url": "/net/convert-pdf-to-powerpoint/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-powerpoint/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

## 개요

이 문서에서는 **C#을 사용하여 PDF를 PowerPoint로 변환하는 방법**을 설명합니다. 다음 주제를 다룹니다.

_형식_: **PPTX**
- [C# PDF를 PPTX로 변환하기](#csharp-pdf-to-pptx)
- [C# PDF를 PPTX로 변환하기](#csharp-pdf-to-pptx)
- [C# PDF 파일을 PPTX로 변환하는 방법](#csharp-pdf-to-pptx)

_형식_: **PowerPoint**
- [C# PDF를 PowerPoint로 변환하기](#csharp-pdf-to-powerpoint)
- [C# PDF를 PowerPoint로 변환하기](#csharp-pdf-to-powerpoint)
- [C# PDF 파일을 PowerPoint로 변환하는 방법](#csharp-pdf-to-powerpoint)

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

## C# PDF를 PowerPoint 및 PPTX로 변환하기

**Aspose.PDF for .NET**는 PDF를 PPTX로 변환하는 진행 상황을 추적할 수 있게 해줍니다.

우리는 PPT/PPTX 프레젠테이션을 생성하고 조작할 수 있는 기능을 제공하는 Aspose.Slides라는 API를 가지고 있습니다. 이 API는 PPT/PPTX 파일을 PDF 형식으로 변환하는 기능도 제공합니다. 최근에 많은 고객으로부터 PDF를 PPTX 형식으로 변환하는 기능을 지원해 달라는 요청을 받았습니다. Aspose.PDF for .NET 10.3.0 버전부터 PDF 문서를 PPTX 형식으로 변환하는 기능을 도입했습니다. 이 변환 과정에서 PDF 파일의 개별 페이지가 PPTX 파일의 별도 슬라이드로 변환됩니다.

PDF를 <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>로 변환하는 동안 텍스트는 선택 및 업데이트할 수 있는 텍스트로 렌더링됩니다. PDF 파일을 PPTX 형식으로 변환하기 위해 Aspose.PDF는 [`PptxSaveOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions)라는 클래스를 제공합니다. PptxSaveOptions 클래스의 객체는 [`Document.Save(..) method`](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 메서드의 두 번째 인수로 전달됩니다. 다음 코드 스니펫은 PDF 파일을 PPTX 형식으로 변환하는 과정을 보여줍니다.

## C# 및 Aspose.PDF .NET을 사용한 PDF를 PowerPoint로 간단히 변환하기

PDF를 PPTX로 변환하기 위해 Aspose.PDF for .NET는 다음 코드 단계를 사용할 것을 권장합니다.

<a name="csharp-pdf-to-powerpoint"><strong>단계: C#에서 PDF를 PowerPoint로 변환하기</strong></a> | <a name="csharp-pdf-to-pptx"><strong>단계: C#에서 PDF를 PPTX로 변환하기</strong></a>

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스의 인스턴스를 생성합니다.
2. [PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) 클래스의 인스턴스를 생성합니다.
3. **Document** 객체의 **Save** 메서드를 사용하여 PDF를 PPTX로 저장합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToPPTX()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate PptxSaveOptions object
        var saveOptions = new Aspose.Pdf.PptxSaveOptions();

        // Save the file in PPTX format
        document.Save(dataDir + "PDFToPPT_out.pptx", saveOptions);
    }
}
```

## 슬라이드를 이미지로 변환하여 PDF를 PPTX로 변환하기

{{% alert color="success" %}}
**온라인에서 PDF를 PowerPoint로 변환해 보세요**

Aspose.PDF for .NET는 ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx)라는 온라인 무료 애플리케이션을 제공하여 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF PDF를 PPTX로 변환하는 무료 앱](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

검색 가능한 PDF를 선택 가능한 텍스트 대신 이미지로 PPTX로 변환해야 하는 경우, Aspose.PDF는 [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) 클래스를 통해 이러한 기능을 제공합니다. 이를 달성하기 위해 [PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) 클래스의 [SlidesAsImages](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions/properties/slidesasimages) 속성을 'true'로 설정합니다. 다음 코드 샘플에서 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToPPTWithSlidesAsImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate PptxSaveOptions object
        var saveOptions = new Aspose.Pdf.PptxSaveOptions
        {
            SlidesAsImages = true
        };

        // Save the file in PPTX format with slides as images
        document.Save(dataDir + "PDFToPPT_out.pptx", saveOptions);
    }
}
```

## PPTX 변환 진행 세부정보

Aspose.PDF for .NET는 PDF를 PPTX로 변환하는 진행 상황을 추적할 수 있게 해줍니다. [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) 클래스는 변환 진행 상황을 추적하기 위해 사용자 정의 메서드에 지정할 수 있는 [CustomProgressHandler](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions/properties/customprogresshandler) 속성을 제공합니다. 다음 코드 샘플에서 보여줍니다.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToPPTWithCustomProgressHandler()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {

        // Instantiate PptxSaveOptions object
        var saveOptions = new Aspose.Pdf.PptxSaveOptions();

        // Specify custom progress handler
        saveOptions.CustomProgressHandler = ShowProgressOnConsole;

        // Save the file in PPTX format with progress tracking
        document.Save(dataDir + "PDFToPPTWithProgressTracking_out.pptx", saveOptions);
    }
}

 // Define the method to handle progress events and display them on the console
private static void ShowProgressOnConsole(Aspose.Pdf.UnifiedSaveOptions.ProgressEventHandlerInfo eventInfo)
{
    switch (eventInfo.EventType)
    {
        case Aspose.Pdf.ProgressEventType.TotalProgress:
            // Display overall progress of the conversion
            Console.WriteLine($"{DateTime.Now.TimeOfDay}  - Conversion progress: {eventInfo.Value}%.");
            break;

        case Aspose.Pdf.ProgressEventType.ResultPageCreated:
            // Display progress of the page layout creation
            Console.WriteLine($"{DateTime.Now.TimeOfDay}  - Result page {eventInfo.Value} of {eventInfo.MaxValue} layout created.");
            break;

        case Aspose.Pdf.ProgressEventType.ResultPageSaved:
            // Display progress of the page being exported
            Console.WriteLine($"{DateTime.Now.TimeOfDay}  - Result page {eventInfo.Value} of {eventInfo.MaxValue} exported.");
            break;

        case Aspose.Pdf.ProgressEventType.SourcePageAnalysed:
            // Display progress of the source page analysis
            Console.WriteLine($"{DateTime.Now.TimeOfDay}  - Source page {eventInfo.Value} of {eventInfo.MaxValue} analyzed.");
            break;

        default:
            break;
    }
}
```

## 참조 

이 문서에서는 다음 주제도 다룹니다. 코드 내용은 위와 동일합니다.

_형식_: **PowerPoint**
- [C# PDF를 PowerPoint 코드](#csharp-pdf-to-powerpoint)
- [C# PDF를 PowerPoint API](#csharp-pdf-to-powerpoint)
- [C# PDF를 PowerPoint로 프로그래밍 방식으로 변환하기](#csharp-pdf-to-powerpoint)
- [C# PDF를 PowerPoint 라이브러리](#csharp-pdf-to-powerpoint)
- [C# PDF를 PowerPoint로 저장하기](#csharp-pdf-to-powerpoint)
- [C# PDF에서 PowerPoint 생성하기](#csharp-pdf-to-powerpoint)
- [C# PDF에서 PowerPoint 만들기](#csharp-pdf-to-powerpoint)
- [C# PDF를 PowerPoint 변환기](#csharp-pdf-to-powerpoint)

_형식_: **PPTX**
- [C# PDF를 PPTX 코드](#csharp-pdf-to-pptx)
- [C# PDF를 PPTX API](#csharp-pdf-to-pptx)
- [C# PDF를 PPTX로 프로그래밍 방식으로 변환하기](#csharp-pdf-to-pptx)
- [C# PDF를 PPTX 라이브러리](#csharp-pdf-to-pptx)
- [C# PDF를 PPTX로 저장하기](#csharp-pdf-to-pptx)
- [C# PDF에서 PPTX 생성하기](#csharp-pdf-to-pptx)
- [C# PDF에서 PPTX 만들기](#csharp-pdf-to-pptx)
- [C# PDF를 PPTX 변환기](#csharp-pdf-to-pptx)