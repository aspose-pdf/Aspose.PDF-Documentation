---
title: PDF를 HTML로 변환하기 (.NET)
linktitle: PDF를 HTML 형식으로 변환하기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ko/net/convert-pdf-to-html/
lastmod: "2021-11-01"
description: 이 주제에서는 Aspose.PDF C# 라이브러리를 사용하여 PDF 파일을 HTML 형식으로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to HTML in .NET",
    "alternativeHeadline": "Convert PDF Files to HTML with Simplified Options in C#",
    "abstract": "PDF 문서를 HTML 형식으로 원활하게 변환할 수 있는 강력한 새로운 기능을 소개합니다. 이 기능은 다중 페이지 출력, SVG 이미지 관리 및 투명 텍스트 렌더링 옵션을 지원하여 개발자가 몇 줄의 C# 코드로 PDF를 웹 준비 콘텐츠로 쉽게 변환할 수 있도록 합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1349",
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
    "url": "/net/convert-pdf-to-html/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-html/"
    },
    "dateModified": "2025-04-04",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

## 개요

이 문서에서는 **C#을 사용하여 PDF를 HTML로 변환하는 방법**을 설명합니다. 다음 주제를 다룹니다.

- [PDF를 HTML로 변환하기](#csharp-pdf-to-html)

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

## PDF를 HTML로 변환하기

**Aspose.PDF for .NET**은 다양한 파일 형식을 PDF 문서로 변환하고 PDF 파일을 다양한 출력 형식으로 변환하는 많은 기능을 제공합니다. 이 문서에서는 PDF 파일을 <abbr title="HyperText Markup Language">HTML</abbr>로 변환하는 방법에 대해 설명합니다. Aspose.PDF for .NET은 InLineHtml 접근 방식을 사용하여 HTML 파일을 PDF 형식으로 변환하는 기능을 제공합니다. PDF 파일을 HTML 형식으로 변환하는 기능에 대한 많은 요청이 있었으며 이 기능을 제공했습니다. 이 기능은 XHTML 1.0도 지원합니다.

**Aspose.PDF for .NET**은 PDF 파일을 HTML로 변환하는 기능을 지원합니다. Aspose.PDF 라이브러리로 수행할 수 있는 주요 작업은 다음과 같습니다:

- PDF를 HTML로 변환하기.
- 출력 다중 페이지 HTML로 분할하기.
- SVG 파일 저장을 위한 폴더 지정하기.
- 변환 중 SVG 이미지 압축하기.
- 이미지를 PNG 배경으로 저장하기.
- 이미지 폴더 지정하기.
- 본문 내용만 포함된 후속 파일 생성하기.
- 투명 텍스트 렌더링.
- PDF 문서 레이어 렌더링.

{{% alert color="success" %}}
**온라인에서 PDF를 HTML로 변환해 보세요**

Aspose.PDF for .NET은 ["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html)라는 온라인 무료 애플리케이션을 제공하여 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF PDF를 HTML로 변환하는 무료 앱](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

Aspose.PDF for .NET은 소스 PDF 파일을 HTML로 변환하기 위한 두 줄의 코드를 제공합니다. [`SaveFormat enumeration`](https://reference.aspose.com/pdf/ko/net/aspose.pdf/saveformat)에는 소스 파일을 HTML로 저장할 수 있는 값 Html이 포함되어 있습니다. 다음 코드 스니펫은 PDF 파일을 HTML로 변환하는 과정을 보여줍니다.

<a name="csharp-pdf-to-html" id="cshart-pdf-to-html"><strong>PDF를 HTML로 변환하기</strong></a>

1. 소스 PDF 문서로 [Document](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document/) 객체의 인스턴스를 생성합니다.
2. **Document.Save()** 메서드를 호출하여 **SaveFormat.Html** 형식으로 저장합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoHTML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Save the output HTML
        document.Save(dataDir + "output_out.html", Aspose.Pdf.SaveFormat.Html);
    }
}
```

### 출력 다중 페이지 HTML로 분할하기

여러 페이지가 있는 큰 PDF 파일을 HTML 형식으로 변환할 때 출력은 단일 HTML 페이지로 나타납니다. 이는 매우 길어질 수 있습니다. 페이지 크기를 제어하기 위해 PDF를 HTML로 변환하는 동안 출력을 여러 페이지로 분할할 수 있습니다. 다음 코드 스니펫을 사용해 보십시오.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoMultiPageHTML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Instantiate HTML SaveOptions object
        var htmlOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Specify to split the output into multiple pages
            SplitIntoPages = true
        };

        // Save the output HTML
        document.Save(dataDir + "MultiPageHTML_out.html", htmlOptions);
    }
}
```

### SVG 파일 저장을 위한 폴더 지정하기

PDF를 HTML로 변환하는 동안 SVG 이미지를 저장할 폴더를 지정할 수 있습니다. [`HtmlSaveOption class`](https://reference.aspose.com/pdf/ko/net/aspose.pdf/htmlsaveoptions) [`SpecialFolderForSvgImages property`](https://reference.aspose.com/pdf/ko/net/aspose.pdf/htmlsaveoptions/fields/specialfolderforsvgimages)를 사용하여 특별한 SVG 이미지 디렉토리를 지정합니다. 이 속성은 변환 중에 SVG 이미지를 저장해야 하는 디렉토리의 경로를 가져오거나 설정합니다. 매개변수가 비어 있거나 null인 경우 모든 SVG 파일은 다른 이미지 파일과 함께 저장됩니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SavePDFtoHTMLWithSVG()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Instantiate HTML save options object
        var newOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Specify the folder where SVG images are saved during PDF to HTML conversion
            SpecialFolderForSvgImages = dataDir
        };

        // Save the output HTML
        document.Save(dataDir + "SaveSVGFiles_out.html", newOptions);
    }
}
```

### 변환 중 SVG 이미지 압축하기

PDF를 HTML로 변환하는 동안 SVG 이미지를 압축하려면 다음 코드를 사용해 보십시오:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SavePDFtoCompressedHTMLWithSVG()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Create HtmlSaveOptions with tested feature
        var newOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Compress the SVG images if there are any
            CompressSvgGraphicsIfAny = true
        };

        // Save the output HTML
        document.Save(dataDir + "CompressedSVGHTML_out.html", newOptions);
    }
}
```

### 이미지를 PNG 배경으로 저장하기

이미지를 저장하기 위한 기본 출력 형식은 SVG입니다. 변환 중에 PDF의 일부 이미지는 SVG 벡터 이미지로 변환됩니다. 이는 느릴 수 있습니다. 대신 각 페이지에 대해 하나의 PNG 배경 파일로 이미지를 변환할 수 있습니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PdfToHtmlSaveImagesAsPngBackground()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion_PDFToHTMLFormat();
           
    // Create HtmlSaveOption with tested feature
    var htmlSaveOptions = new HtmlSaveOptions();
           
    // Option to save images in PNG format as background for each page.
    htmlSaveOptions.RasterImagesSavingMode = HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground;

    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
       document.Save(dataDir + "imagesAsPngBackground_out.html", htmlSaveOptions);         
    }
}
```

### 이미지 폴더 지정하기

PDF를 HTML로 변환하는 동안 이미지를 저장할 폴더를 지정할 수도 있습니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SavePDFtoHTMLWithSeparateImageFolder()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Create HtmlSaveOptions with tested feature
        var newOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Specify the separate folder to save images
            SpecialFolderForAllImages = dataDir
        };

        // Save the output HTML
        document.Save(dataDir + "HTMLWithSeparateImageFolder_out.html", newOptions);
    }
}
```

### 본문 내용만 포함된 후속 파일 생성하기

최근에 PDF 파일을 HTML로 변환하고 사용자가 각 페이지의 `<body>` 태그의 내용만 가져올 수 있는 기능을 도입해 달라는 요청을 받았습니다. 이는 CSS, `<html>`, `<head>` 세부 사항이 포함된 하나의 파일과 다른 파일에 `<body>` 내용만 포함된 모든 페이지를 생성합니다.

이 요구 사항을 충족하기 위해 HtmlSaveOptions 클래스에 HtmlMarkupGenerationMode라는 새로운 속성이 도입되었습니다.

다음 간단한 코드 스니펫을 사용하여 출력 HTML을 페이지로 분할할 수 있습니다. 출력 페이지에서 모든 HTML 객체는 현재 위치에 정확히 배치되어야 합니다(글꼴 처리 및 출력, CSS 생성 및 출력, 이미지 생성 및 출력), 단 출력 HTML은 현재 태그 내에 있는 내용을 포함하게 됩니다(현재 "body" 태그는 생략됩니다). 그러나 이 접근 방식을 사용할 때 CSS에 대한 링크는 귀하의 코드의 책임입니다. 왜냐하면 것과 같은 것들은 제거될 것이기 때문입니다. 이를 위해 File.ReadAllText()를 통해 CSS를 읽고 AJAX를 통해 웹 페이지로 전송하여 jQuery로 적용할 수 있습니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToHTMLWithBodyContent()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Initialize HtmlSaveOptions
        var options = new Aspose.Pdf.HtmlSaveOptions
        {
            // Set HtmlMarkupGenerationMode to generate only body content
            HtmlMarkupGenerationMode =
                Aspose.Pdf.HtmlSaveOptions.HtmlMarkupGenerationModes.WriteOnlyBodyContent,

            // Specify to split the output into multiple pages
            SplitIntoPages = true
        };

        // Save the output HTML
        document.Save(dataDir + "CreateSubsequentFiles_out.html", options);
    }
}
```

### 투명 텍스트 렌더링

소스/입력 PDF 파일에 전경 이미지에 의해 그림자가 드리워진 투명 텍스트가 포함된 경우 텍스트 렌더링 문제가 발생할 수 있습니다. 따라서 이러한 시나리오를 처리하기 위해 SaveShadowedTextsAsTransparentTexts 및 SaveTransparentTexts 속성을 사용할 수 있습니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToHTMLWithTransparentTextRendering()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Initialize HtmlSaveOptions
        var htmlOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Enable transparent text rendering
            SaveShadowedTextsAsTransparentTexts = true,
            SaveTransparentTexts = true
        };

        // Save the output HTML
        document.Save(dataDir + "TransparentTextRendering_out.html", htmlOptions);
    }
}
```

### PDF 문서 레이어 렌더링

PDF를 HTML로 변환하는 동안 PDF 문서 레이어를 별도의 레이어 유형 요소로 렌더링할 수 있습니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToHTMLWithLayersRendering()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Instantiate HTML SaveOptions object
        var htmlOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Enable rendering of PDF document layers separately in the output HTML
            ConvertMarkedContentToLayers = true
        };

        // Save the output HTML
        document.Save(dataDir + "LayersRendering_out.html", htmlOptions);
    }
}
```