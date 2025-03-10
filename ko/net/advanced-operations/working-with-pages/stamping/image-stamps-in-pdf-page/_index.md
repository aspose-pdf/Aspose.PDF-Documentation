---
title: PDF에 이미지 스탬프 추가하기 C#
linktitle: PDF 파일의 이미지 스탬프
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ko/net/image-stamps-in-pdf-page/
description: Aspose.PDF 라이브러리의 ImageStamp 클래스를 사용하여 PDF 문서에 이미지 스탬프를 추가합니다.
lastmod: "2024-09-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Image stamps in PDF using C#",
    "alternativeHeadline": "Add Custom Image Stamps to PDF Documents",
    "abstract": "Aspose.PDF 라이브러리의 새로운 기능을 통해 사용자는 C#을 사용하여 PDF 문서에 이미지 스탬프를 원활하게 추가할 수 있습니다. ImageStamp 클래스를 사용하면 개발자는 크기, 불투명도 및 품질과 같은 속성을 사용자 정의할 수 있어 문서의 프레젠테이션과 접근성을 크게 향상시킬 수 있습니다. 이 기능은 대체 텍스트를 추가할 수 있는 기능도 포함되어 있어 스크린 리더의 사용성을 개선합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "646",
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
    "url": "/net/image-stamps-in-pdf-page/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/image-stamps-in-pdf-page/"
    },
    "dateModified": "2024-11-26",
    "description": "Aspose.PDF 라이브러리의 ImageStamp 클래스를 사용하여 PDF 문서에 이미지 스탬프를 추가합니다."
}
</script>

## PDF 파일에 이미지 스탬프 추가하기

ImageStamp 클래스를 사용하여 PDF 파일에 이미지 스탬프를 추가할 수 있습니다. ImageStamp 클래스는 높이, 너비, 불투명도 등 이미지 기반 스탬프를 생성하는 데 필요한 속성을 제공합니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

이미지 스탬프를 추가하려면:

1. 필요한 속성을 사용하여 Document 객체와 ImageStamp 객체를 생성합니다.
1. Page 클래스의 AddStamp 메서드를 호출하여 PDF에 스탬프를 추가합니다.

다음 코드 스니펫은 PDF 파일에 이미지 스탬프를 추가하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageStampInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImageStampInput.pdf"))
    {
        // Create image stamp
        var imageStamp = new Aspose.Pdf.ImageStamp(dataDir + "aspose-logo.jpg");
        imageStamp.Background = true;
        imageStamp.XIndent = 100;
        imageStamp.YIndent = 100;
        imageStamp.Height = 300;
        imageStamp.Width = 300;
        imageStamp.Rotate = Rotation.on270;
        imageStamp.Opacity = 0.5;
        // Add stamp to particular page
        document.Pages[1].AddStamp(imageStamp);
        // Save PDF document
        document.Save(dataDir + "AddImageStamp_out.pdf");
    }
}
```

## 스탬프 추가 시 이미지 품질 제어하기

스탬프 객체로 이미지를 추가할 때 이미지의 품질을 제어할 수 있습니다. ImageStamp 클래스의 Quality 속성이 이 목적에 사용됩니다. 이는 이미지 품질을 백분율로 나타내며(유효 값은 0..100)입니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ControlImageQualityWhenAddingStamp()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImageStampInput.pdf"))
    {
        // Create image stamp
        var imageStamp = new Aspose.Pdf.ImageStamp(dataDir + "aspose-logo.jpg");
        imageStamp.Quality = 10;
        document.Pages[1].AddStamp(imageStamp);
        // Save PDF document
        document.Save(dataDir + "ControlImageQuality_out.pdf");
    }
}
```

## 플로팅 박스의 배경으로 이미지 스탬프 추가하기

Aspose.PDF API를 사용하면 플로팅 박스의 배경으로 이미지 스탬프를 추가할 수 있습니다. FloatingBox 클래스의 BackgroundImage 속성을 사용하여 플로팅 박스의 배경 이미지 스탬프를 설정할 수 있습니다. 다음 코드 샘플을 참조하십시오.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImageStampAsBackgroundInFloatingBox()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page to PDF document
        Page page = document.Pages.Add();
        // Create FloatingBox object
        var aBox = new Aspose.Pdf.FloatingBox(200, 100);
        // Set left position for FloatingBox
        aBox.Left = 40;
        // Set Top position for FloatingBox
        aBox.Top = 80;
        // Set the Horizontal alignment for FloatingBox
        aBox.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        // Add text fragment to paragraphs collection of FloatingBox
        aBox.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("main text"));
        // Set border for FloatingBox
        aBox.Border = new Aspose.Pdf.BorderInfo(BorderSide.All, Aspose.Pdf.Color.Red);
        // Add background image
        aBox.BackgroundImage = new Aspose.Pdf.Image
        {
            File = dataDir + "aspose-logo.jpg"
        };
        // Set background color for FloatingBox
        aBox.BackgroundColor = Aspose.Pdf.Color.Yellow;
        // Add FloatingBox to paragraphs collection of page object
        page.Paragraphs.Add(aBox);
        // Save PDF document
        document.Save(dataDir + "AddImageStampAsBackgroundInFloatingBox_out.pdf");
    }
}
```

## 이미지 스탬프에 대체 텍스트 추가하기

버전 24.6부터 이미지 스탬프에 대체 텍스트를 추가할 수 있습니다.

이 코드는 PDF 파일을 열고 특정 위치에 이미지를 스탬프로 추가하며 접근성을 위해 대체 텍스트를 포함합니다. 업데이트된 PDF는 새 파일 이름으로 저장됩니다.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAlternativeTextToTheImageStamp()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImageStampInput.pdf"))
    {
        // Create image stamp
        var imageStamp = new Aspose.Pdf.ImageStamp(dataDir + "aspose-logo.jpg")
        {
            XIndent = 100,
            YIndent = 700,
            Quality = 100,
            AlternativeText = "Your alt text"  // This property added.
        };
        // Add stamp
        document.Pages[1].AddStamp(imageStamp);
        // Save PDF document
        document.Save(dataDir + "DocWithImageStamp_out.pdf");
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