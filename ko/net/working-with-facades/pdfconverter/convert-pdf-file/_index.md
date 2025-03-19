---
title: PDF 파일 변환
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ko/net/convert-pdf-file/
description: Aspose.PDF를 사용하여 .NET에서 PDF 파일을 다양한 형식으로 변환하는 방법을 배우십시오.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF File",
    "alternativeHeadline": "Convert PDF Pages to Image Formats Efficiently",
    "abstract": "PdfConverter 클래스를 사용하여 PDF 페이지를 JPEG, GIF 및 PNG와 같은 다양한 이미지 형식으로 손쉽게 변환할 수 있는 Aspose.PDF for .NET Facades의 힘을 활용하십시오. 이 기능은 변환 프로세스에 대한 세부적인 제어를 가능하게 하여 해상도, 좌표 유형 및 페이지 범위와 같은 매개변수를 지정하여 맞춤형 출력을 생성할 수 있습니다. 애플리케이션에 원활한 PDF에서 이미지로의 변환을 통합하여 문서 처리 기능을 향상시키십시오.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "561",
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
    "url": "/net/convert-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

## PDF 페이지를 다양한 이미지 형식으로 변환하기 (Facades)

PDF 페이지를 다양한 이미지 형식으로 변환하려면 [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter) 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 메서드를 사용하여 PDF 파일을 열어야 합니다. 그 후, 초기화 작업을 위해 [DoConvert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/doconvert) 메서드를 호출해야 합니다. 그런 다음 [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/hasnextimage) 및 [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfconverter/getnextimage/methods/6) 메서드를 사용하여 모든 페이지를 반복할 수 있습니다. [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfconverter/getnextimage/methods/6) 메서드는 특정 페이지의 이미지를 생성할 수 있게 해줍니다. 또한 이 메서드에 ImageFormat을 전달하여 특정 유형의 이미지(JPEG, GIF 또는 PNG 등)를 생성해야 합니다. 마지막으로 [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter) 클래스의 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/close) 메서드를 호출합니다. 다음 코드 스니펫은 PDF 페이지를 이미지로 변환하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPdfPagesToImages01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfConverter object
    using (var converter = new Aspose.Pdf.Facades.PdfConverter())
    {
        // Bind PDF document
        converter.BindPdf(dataDir + "ConvertPdfPagesToImages.pdf");

        // Initialize the converting process
        converter.DoConvert();

        // Check if pages exist and then convert to image one by one
        while (converter.HasNextImage())
        {
            // Generate output file name with '_out' suffix
            var outputFileName = dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg";
            // Convert the page to image and save it
            converter.GetNextImage(outputFileName, System.Drawing.Imaging.ImageFormat.Jpeg);
        }
    }
}
```

다음 코드 스니펫에서는 일부 매개변수를 변경하는 방법을 보여줍니다. [CoordinateType](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/coordinatetype)로 'CropBox' 프레임을 설정합니다. 또한 [Resolution](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/resolution)을 지정하여 인치당 점 수를 설정할 수 있습니다. 다음은 [FormPresentationMode](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/formpresentationmode) - 양식 프레젠테이션 모드입니다. 그런 다음 변환 시작 페이지 번호를 설정하는 [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/startpage)를 지정합니다. 범위를 설정하여 마지막 페이지를 지정할 수도 있습니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPdfPagesToImages02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfConverter object
    using (var converter = new Aspose.Pdf.Facades.PdfConverter())
    {
        // Bind PDF document
        converter.BindPdf(dataDir + "ConvertPdfPagesToImages.pdf");

        // Initialize the converting process
        converter.DoConvert();

        // Set additional conversion settings
        converter.CoordinateType = Aspose.Pdf.PageCoordinateType.CropBox;
        converter.Resolution = new Aspose.Pdf.Devices.Resolution(600);
        converter.FormPresentationMode = Aspose.Pdf.Devices.FormPresentationMode.Production;
        converter.StartPage = 2;

        // Check if pages exist and then convert to image one by one
        while (converter.HasNextImage())
        {
            // Generate output file name
            var outputFileName = dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg";
            // Convert the page to image and save it
            converter.GetNextImage(outputFileName, System.Drawing.Imaging.ImageFormat.Jpeg);
        }
    }
}
```

## 사용자 정의 글꼴 대체를 사용하여 PDF 페이지를 이미지 형식으로 변환

다음 코드 스니펫에서는 PDF에서 이미지로 변환하는 과정에서 사용자 정의 글꼴 대체를 적용하는 방법을 보여줍니다. FontRepository.Substitutions 컬렉션을 사용하여 사용자 정의 대체 규칙을 등록합니다. 이 예제에서는 "Helvetica" 글꼴이 발견되면 "Arial"로 대체됩니다.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertWithCustomFontSubstitution()
{
    // Add custom font substitution
    Aspose.Pdf.Text.FontRepository.Substitutions.Add(new CustomPdfFontSubstitution());

    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    
    using (var converter = new Aspose.Pdf.Facades.PdfConverter())
    {
        // Bind PDF document
        converter.BindPdf(dataDir + "ConvertWithSubstitution.pdf");

        // Initialize the converting process
        converter.DoConvert();

        // Check if pages exist and then convert to image one by one
        while (converter.HasNextImage())
        {
            // Generate output file name with '_out' suffix
            var outputFileName = dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg";
            // Convert the page to image and save it
            converter.GetNextImage(outputFileName, System.Drawing.Imaging.ImageFormat.Jpeg);
        }
    }
}

private class CustomPdfFontSubstitution : Aspose.Pdf.Text.CustomFontSubstitutionBase
{
    public override bool TrySubstitute(
        Aspose.Pdf.Text.CustomFontSubstitutionBase.OriginalFontSpecification originalFontSpecification,
        out Aspose.Pdf.Text.Font substitutionFont)
    {
        if (originalFontSpecification.OriginalFontName == "Helvetica")
        {
            substitutionFont = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
            return true;
        }
        // Default substitution logic
        return base.TrySubstitute(originalFontSpecification, out substitutionFont);
    }
}
```
{{< /tab >}}
{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertWithCustomFontSubstitution()
{
    // Add custom font substitution
    Aspose.Pdf.Text.FontRepository.Substitutions.Add(new CustomPdfFontSubstitution());

    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    
    using var converter = new Aspose.Pdf.Facades.PdfConverter();

    // Bind PDF document
    converter.BindPdf(dataDir + "ConvertWithSubstitution.pdf");

    // Initialize the converting process
    converter.DoConvert();

    // Check if pages exist and then convert to image one by one
    while (converter.HasNextImage())
    {
        // Generate output file name with '_out' suffix
        var outputFileName = dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg";
        // Convert the page to image and save it
        converter.GetNextImage(outputFileName, System.Drawing.Imaging.ImageFormat.Jpeg);
    }
}

private class CustomPdfFontSubstitution : Aspose.Pdf.Text.CustomFontSubstitutionBase
{
    public override bool TrySubstitute(
        Aspose.Pdf.Text.CustomFontSubstitutionBase.OriginalFontSpecification originalFontSpecification,
        out Aspose.Pdf.Text.Font substitutionFont)
    {
        if (originalFontSpecification.OriginalFontName == "Helvetica")
        {
            substitutionFont = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
            return true;
        }
        // Default substitution logic
        return base.TrySubstitute(originalFontSpecification, out substitutionFont);
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## 참조

Aspose.PDF for .NET은 PDF 문서를 다양한 형식으로 변환할 수 있으며, 다른 형식에서 PDF로 변환할 수도 있습니다. 또한 Aspose.PDF 변환의 품질을 확인하고 Aspose.PDF 변환기 앱을 통해 결과를 온라인으로 볼 수 있습니다. 작업을 해결하기 위해 [변환하기](/pdf/ko/net/converting/) 섹션을 배우십시오.