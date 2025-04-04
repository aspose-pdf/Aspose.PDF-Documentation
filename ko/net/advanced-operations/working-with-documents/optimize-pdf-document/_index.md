---
title: C#에서 PDF 크기 최적화, 압축 또는 축소
linktitle: PDF 최적화
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ko/net/optimize-pdf/
description: C#을 사용하여 PDF 파일을 최적화하고, 모든 이미지를 축소하고, PDF 크기를 줄이고, 글꼴을 언임베드하고, 사용하지 않는 객체를 제거합니다.
lastmod: "2022-02-17"
sitemap:
changefreq: "monthly"
priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Optimize, Compress or Reduce PDF Size in C#",
    "alternativeHeadline": "Optimize PDF Files Efficiently with C#",
    "abstract": "C#의 새로운 PDF 최적화 기능은 개발자가 이미지를 압축하고, 글꼴을 언임베드하고, 사용하지 않는 객체를 제거하는 등 여러 전략을 사용하여 PDF 파일 크기를 크게 줄일 수 있도록 합니다. 이 개선은 웹 게시, 이메일 공유 및 저장을 위한 효율성을 향상시켜 대형 PDF 문서를 관리하는 효과적인 솔루션을 제공합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "optimize pdf, compress pdf size, reduce pdf size, optimize pdf c#, unembed fonts, remove unused objects, shrink images, optimization methods, pdf document generation, Aspose.PDF",
    "wordcount": "2523",
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
    "url": "/net/optimize-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/optimize-pdf/"
    },
    "dateModified": "2025-04-01",
    "description": "C#을 사용하여 PDF 파일을 최적화하고, 모든 이미지를 축소하고, PDF 크기를 줄이고, 글꼴을 언임베드하고, 사용하지 않는 객체를 제거합니다."
}
</script>

PDF 문서에는 때때로 추가 데이터가 포함될 수 있습니다. PDF 파일의 크기를 줄이면 네트워크 전송 및 저장을 최적화하는 데 도움이 됩니다. 이는 웹 페이지에 게시하거나, 소셜 네트워크에서 공유하거나, 이메일로 전송하거나, 저장소에 보관할 때 특히 유용합니다. PDF를 최적화하기 위해 여러 기술을 사용할 수 있습니다:

- 온라인 브라우징을 위한 페이지 콘텐츠 최적화.
- 모든 이미지 축소 또는 압축.
- 페이지 콘텐츠 재사용 활성화.
- 중복 스트림 병합.
- 글꼴 언임베드.
- 사용하지 않는 객체 제거.
- 평면화된 양식 필드 제거.
- 주석 제거 또는 평면화.

{{% alert color="primary" %}}

최적화 방법에 대한 자세한 설명은 최적화 방법 개요 페이지에서 확인할 수 있습니다.

{{% /alert %}}

## 웹을 위한 PDF 문서 최적화

웹을 위한 최적화 또는 선형화는 PDF 파일을 웹 브라우저에서 온라인 브라우징에 적합하게 만드는 과정을 의미합니다. 웹 표시를 위해 파일을 최적화하려면:

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체에서 입력 문서를 엽니다.
1. [Optimize](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/optimize) 메서드를 사용합니다.
1. [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 메서드를 사용하여 최적화된 문서를 저장합니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

다음 코드 스니펫은 웹을 위해 PDF 문서를 최적화하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizeDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Optimize for web
        document.Optimize();

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

## PDF 크기 축소

[OptimizeResources()](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/optimizeresources) 메서드는 불필요한 정보를 제거하여 문서 크기를 줄일 수 있습니다. 기본적으로 이 메서드는 다음과 같이 작동합니다:

- 문서 페이지에서 사용되지 않는 리소스가 제거됩니다.
- 동일한 리소스가 하나의 객체로 결합됩니다.
- 사용하지 않는 객체가 삭제됩니다.

아래 스니펫은 예시입니다. 그러나 이 메서드는 문서 축소를 보장할 수 없습니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ShrinkDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ShrinkDocument.pdf"))
    {
        // Optimize PDF document. Note, though, that this method cannot guarantee document shrinking
        document.OptimizeResources();

        // Save PDF document
        document.Save(dataDir + "ShrinkDocument_out.pdf");
    }
}
```

## 최적화 전략 관리

최적화 전략을 사용자 정의할 수도 있습니다. 현재 [OptimizeResources()](https://reference.aspose.com/pdf/net/aspose.pdf.document/optimizeresources/methods/1) 메서드는 5가지 기술을 사용합니다. 이러한 기술은 [OptimizationOptions](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/optimizationoptions) 매개변수를 사용하여 OptimizeResources() 메서드에 적용할 수 있습니다.

### 모든 이미지 축소 또는 압축

이미지와 작업하는 두 가지 방법이 있습니다: 이미지 품질을 줄이거나 해상도를 변경하는 것입니다. 어떤 경우든 [ImageCompressionOptions](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions)를 적용해야 합니다. 다음 예제에서는 [ImageQuality](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions/properties/imagequality)를 50으로 줄여 이미지를 축소합니다.

`ImageQuality`는 JPEG 품질과 유사하게 작동하며, 값 0은 가장 낮고 값 100은 가장 높습니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ShrinkImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Shrinkimage.pdf"))
    {
        // Initialize OptimizationOptions
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions();

        // Set CompressImages option
        // If this flag is set to true images will be compressed in the document
        optimizeOptions.ImageCompressionOptions.CompressImages = true;

        // Set ImageQuality option
        // Specifies level of image compression when CompressImages flag is used
        optimizeOptions.ImageCompressionOptions.ImageQuality = 50;

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "Shrinkimage_out.pdf");
    }
}
```

또 다른 방법은 해상도를 낮춰 이미지를 크기 조정하는 것입니다. 이 경우, ResizeImages를 true로 설정하고 MaxResolution을 적절한 값으로 설정해야 합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ResizeImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ResizeImage.pdf"))
    {
        // Initialize OptimizationOptions
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions();

        // Set CompressImages option
        // If this flag is set to true images will be compressed in the document
        optimizeOptions.ImageCompressionOptions.CompressImages = true;

        // Set ImageQuality option
        // Specifies level of image compression when CompressImages flag is used
        optimizeOptions.ImageCompressionOptions.ImageQuality = 75;

        // Set ResizeImage option
        // If this flag set to true and CompressImages is true images will be resized if image resolution is greater then specified MaxResolution parameter
        optimizeOptions.ImageCompressionOptions.ResizeImages = true;

        // Set MaxResolution option
        // Specifies maximum resolution of images. If image has higher resolition it will be scaled
        optimizeOptions.ImageCompressionOptions.MaxResolution = 300;

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "ResizeImages_out.pdf");
    }
}
```

또한 실행 시간도 중요한 문제입니다. 그러나 다시 말하지만, 이 설정도 관리할 수 있습니다. 현재 두 가지 알고리즘 - 표준 및 빠른 알고리즘을 사용할 수 있습니다. 실행 시간을 제어하려면 [Version](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions/properties/version) 속성을 설정해야 합니다. 다음 스니펫은 빠른 알고리즘을 보여줍니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FastShrinkImages()
{
    // Initialize Time
    var time = DateTime.Now.Ticks;

    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Shrinkimage.pdf"))
    {
        // Initialize OptimizationOptions
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions();

        // Set CompressImages option
        // If this flag is set to true images will be compressed in the document
        optimizeOptions.ImageCompressionOptions.CompressImages = true;

        // Set ImageQuality option
        // Specifies level of image compression when CompressImages flag is used
        optimizeOptions.ImageCompressionOptions.ImageQuality = 75;

        // Set Image Compression Version to fast
        // Version of compression algorithm. Possible values are:
        // 1. standard compression
        // 2. fast (improved compression which is faster then standard but may be applicable not for all images)
        // 3. mixed (standard compression is applied to images which can not be compressed by faster algorithm, 
        // this may give best compression but more slow then "fast" algorithm. Version "Fast" is not applicable for 
        // resizing images (standard method will be used). Default is "Standard"
        optimizeOptions.ImageCompressionOptions.Version = Aspose.Pdf.Optimization.ImageCompressionVersion.Fast;

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "FastShrinkImages_out.pdf");
    }

    // Output the time taken for the operation
    Console.WriteLine("Ticks: {0}", DateTime.Now.Ticks - time);
}
```

### 사용하지 않는 객체 제거

PDF 문서에는 때때로 문서의 다른 객체에서 참조되지 않는 PDF 객체가 포함될 수 있습니다. 예를 들어, 페이지가 문서 페이지 트리에서 제거되었지만 페이지 객체 자체는 제거되지 않은 경우에 발생할 수 있습니다. 이러한 객체를 제거하면 문서가 무효화되지 않고 오히려 축소됩니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizeDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set RemoveUsedObject option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            RemoveUnusedObjects = true
        };
        
        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

### 사용하지 않는 스트림 제거

때때로 문서에는 사용하지 않는 리소스 스트림이 포함되어 있습니다. 이러한 스트림은 페이지 리소스 사전에서 참조되기 때문에 "사용하지 않는 객체"가 아닙니다. 따라서 "사용하지 않는 객체 제거" 메서드로 제거되지 않습니다. 그러나 이러한 스트림은 페이지 콘텐츠와 함께 사용되지 않습니다. 이는 이미지가 페이지에서 제거되었지만 페이지 리소스에서는 제거되지 않은 경우에 발생할 수 있습니다. 또한, 페이지가 문서에서 추출되고 문서 페이지가 "공통" 리소스, 즉 동일한 Resources 객체를 가질 때 이러한 상황이 자주 발생합니다. 리소스 스트림이 사용되었는지 여부를 판단하기 위해 페이지 콘텐츠가 분석됩니다. 사용하지 않는 스트림이 제거됩니다. 이는 때때로 문서 크기를 줄입니다. 이 기술의 사용은 이전 단계와 유사합니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizePdfDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set RemoveUsedStreams option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            RemoveUnusedStreams = true
        };

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

### 중복 스트림 연결

일부 문서에는 여러 개의 동일한 리소스 스트림(예: 이미지)이 포함될 수 있습니다. 이는 문서가 자신과 연결될 때 발생할 수 있습니다. 출력 문서에는 동일한 리소스 스트림의 두 개의 독립적인 복사본이 포함됩니다. 우리는 모든 리소스 스트림을 분석하고 비교합니다. 스트림이 중복되면 병합되어 하나의 복사본만 남습니다. 참조는 적절하게 변경되고 객체의 복사본은 제거됩니다. 경우에 따라 이는 문서 크기를 줄이는 데 도움이 됩니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizePdfDocumentWithLinkDuplicateStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set LinkDuplicateStreams option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            LinkDuplicateStreams = true
        };

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

또한 [AllowReusePageContent](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/optimizationoptions/properties/allowreusepagecontent) 설정을 사용할 수 있습니다. 이 속성이 true로 설정되면 동일한 페이지에 대해 문서를 최적화할 때 페이지 콘텐츠가 재사용됩니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizePdfDocumentWithReusePageContent()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set AllowReusePageContent option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            AllowReusePageContent = true
        };

        Console.WriteLine("Start");

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }

    Console.WriteLine("Finished");

    // Calculate and display file sizes
    var fi1 = new FileInfo(dataDir + "OptimizeDocument.pdf");
    var fi2 = new FileInfo(dataDir + "OptimizeDocument_out.pdf");
    Console.WriteLine("Original file size: {0}. Reduced file size: {1}", fi1.Length, fi2.Length);
}
```

### 글꼴 언임베드

문서가 임베드된 글꼴을 사용하는 경우, 이는 모든 글꼴 데이터가 문서에 저장된다는 것을 의미합니다. 장점은 문서가 사용자의 컴퓨터에 글꼴이 설치되어 있든 없든 관계없이 볼 수 있다는 것입니다. 그러나 글꼴을 임베드하면 문서가 커집니다. 글꼴 언임베드 메서드는 모든 임베드된 글꼴을 제거합니다. 따라서 문서 크기가 줄어들지만 올바른 글꼴이 설치되지 않은 경우 문서 자체가 읽을 수 없게 될 수 있습니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizePdfDocumentWithUnembedFonts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set UnembedFonts option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            UnembedFonts = true
        };

        Console.WriteLine("Start");

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");	
    }
	
    Console.WriteLine("Finished");

    // Calculate and display file sizes
    var fi1 = new FileInfo(dataDir + "OptimizeDocument.pdf");
    var fi2 = new FileInfo(dataDir + "OptimizeDocument_out.pdf");
    Console.WriteLine("Original file size: {0}. Reduced file size: {1}", fi1.Length, fi2.Length);
}
```

최적화 리소스는 이러한 방법을 문서에 적용합니다. 이러한 방법 중 하나라도 적용되면 문서 크기가 줄어들 가능성이 높습니다. 이러한 방법이 적용되지 않으면 문서 크기는 변경되지 않으며 이는 분명합니다.

## PDF 문서 크기를 줄이는 추가 방법

### 주석 제거 또는 평면화

주석은 불필요할 경우 삭제할 수 있습니다. 필요하지만 추가 편집이 필요하지 않은 경우 평면화할 수 있습니다. 이 두 가지 기술 모두 파일 크기를 줄입니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FlattenAnnotationsInPdfDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Flatten annotations
        foreach (var page in document.Pages)
        {
            foreach (var annotation in page.Annotations)
            {
                annotation.Flatten();
            }
        }

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

### 양식 필드 제거

PDF 문서에 AcroForms가 포함된 경우, 양식 필드를 평면화하여 파일 크기를 줄이려고 할 수 있습니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FlattenPdfForms()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Load source PDF form
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Flatten Forms
        if (document.Form.Fields.Lenght > 0)
        {
            foreach (var item in document.Form.Fields)
            {
                item.Flatten();
            }
        }

        // Save PDF document
        document.Save(dataDir + "FlattenForms_out.pdf");
    }
}
```

### PDF를 RGB 색상 공간에서 그레이스케일로 변환

PDF 파일은 텍스트, 이미지, 첨부 파일, 주석, 그래프 및 기타 객체로 구성됩니다. PDF를 RGB 색상 공간에서 그레이스케일로 변환해야 할 필요가 있을 수 있습니다. 이렇게 하면 PDF 파일을 인쇄할 때 더 빠르게 처리됩니다. 또한, 파일이 그레이스케일로 변환되면 문서 크기도 줄어들지만 문서 품질이 저하될 수 있습니다. 이 기능은 현재 Adobe Acrobat의 Pre-Flight 기능에서 지원되지만, 오피스 자동화에 대해 이야기할 때 Aspose.PDF는 문서 조작을 위한 궁극적인 솔루션입니다. 이 요구 사항을 충족하기 위해 다음 코드 스니펫을 사용할 수 있습니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertRgbToGrayScale()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Create RGB to DeviceGray conversion strategy
        var strategy = new Aspose.Pdf.RgbToDeviceGrayConversionStrategy();

        // Iterate through each page
        for (int idxPage = 1; idxPage <= document.Pages.Count; idxPage++)
        {
            // Get instance of particular page inside PDF
            var page = document.Pages[idxPage];

            // Convert the RGB colorspace image to GrayScale colorspace
            strategy.Convert(page);
        }

        // Save PDF document
        document.Save(dataDir + "TestGray_out.pdf");
    }
}
```

### FlateDecode 압축

{{% alert color="primary" %}}

이 기능은 버전 18.12 이상에서 지원됩니다.

{{% /alert %}}

Aspose.PDF for .NET는 PDF 최적화 기능을 위한 FlateDecode 압축을 지원합니다. 아래의 코드 스니펫은 **FlateDecode** 압축으로 이미지를 저장하기 위해 최적화에서 옵션을 사용하는 방법을 보여줍니다:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizeDocumentImagesWithFlateCompression()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        // Initialize OptimizationOptions
        var optimizationOptions = new Aspose.Pdf.Optimization.OptimizationOptions();

        // To optimize images using FlateDecode compression, set optimization options to Flate
        optimizationOptions.ImageCompressionOptions.Encoding = Aspose.Pdf.Optimization.ImageEncoding.Flate;

        // Set optimization options
        document.OptimizeResources(optimizationOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocumentImagesWithFlateCompression_out.pdf");
    }
}
```

### XImageCollection에 이미지 저장

Aspose.PDF for .NET는 FlateDecode 압축으로 **XImageCollection**에 새 이미지를 저장할 수 있는 기능을 제공합니다. 이 옵션을 활성화하려면 **ImageFilterType.Flate** 플래그를 사용할 수 있습니다. 다음 코드 스니펫은 이 기능을 사용하는 방법을 보여줍니다:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageToPdfWithFlateCompression()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Open the image file stream
        using (var imageStream = new FileStream(dataDir + "aspose-logo.jpg", FileMode.Open))
        {
            // Add the image to the page resources with Flate compression
            page.Resources.Images.Add(imageStream, Aspose.Pdf.ImageFilterType.Flate);
        }

        // Get the added image
        var ximage = page.Resources.Images[page.Resources.Images.Count];

        // Save the current graphics state
        page.Contents.Add(new Aspose.Pdf.Operators.GSave());

        // Set coordinates for the image placement
        int lowerLeftX = 0;
        int lowerLeftY = 0;
        int upperRightX = 600;
        int upperRightY = 600;

        var rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        var matrix = new Aspose.Pdf.Matrix(new double[]
        {
            rectangle.URX - rectangle.LLX, 0, 0, rectangle.URY - rectangle.LLY, rectangle.LLX, rectangle.LLY
        });

        // Use ConcatenateMatrix operator to define how the image must be placed
        page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));
        page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));

        // Restore the graphics state
        page.Contents.Add(new Aspose.Pdf.Operators.GRestore());

        // Save the document
        document.Save(dataDir + "AddImageToPdfWithFlateCompression_out.pdf");
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