---
title: PDF에 헤더 및 푸터 추가
linktitle: PDF에 헤더 및 푸터 추가
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /ko/net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for .NET은 TextStamp 클래스를 사용하여 PDF 파일에 헤더와 푸터를 추가할 수 있게 해줍니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/manage-header-and-footer-of-pdf-file/
    - /net/manage-header-and-footer/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Header and Footer to PDF",
    "alternativeHeadline": "Add Custom Headers and Footers to PDF Files",
    "abstract": "Aspose.PDF for .NET은 사용자가 사용자 정의 가능한 헤더와 푸터를 추가하여 PDF 문서를 풍부하게 할 수 있는 강력한 기능을 소개합니다. TextStamp 및 ImageStamp 클래스를 사용하여 개발자는 텍스트와 이미지를 쉽게 통합하고, 다양한 문서 형식과 스타일에 맞게 배치 및 모양을 조정할 수 있습니다. 이는 문서의 전문성과 가독성을 향상시켜 보고서, 송장 및 기타 공식 커뮤니케이션에 이상적입니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1549",
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
    "url": "/net/add-headers-and-footers-of-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-headers-and-footers-of-pdf-file/"
    },
    "dateModified": "2024-11-26",
    "description": "Aspose.PDF for .NET은 TextStamp 클래스를 사용하여 PDF 파일에 헤더와 푸터를 추가할 수 있게 해줍니다."
}
</script>

**Aspose.PDF for .NET**은 기존 PDF 파일에 헤더와 푸터를 추가할 수 있게 해줍니다. PDF 문서에 이미지나 텍스트를 추가할 수 있습니다. 또한 C#을 사용하여 하나의 PDF 파일에 서로 다른 헤더를 추가해 보십시오.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

## PDF 파일의 헤더에 텍스트 추가

PDF 파일의 헤더에 텍스트를 추가하려면 [TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/textstamp) 클래스를 사용할 수 있습니다. TextStamp 클래스는 글꼴 크기, 글꼴 스타일 및 글꼴 색상 등과 같은 텍스트 기반 스탬프를 생성하는 데 필요한 속성을 제공합니다. 헤더에 텍스트를 추가하려면 필요한 속성을 사용하여 Document 객체와 TextStamp 객체를 생성해야 합니다. 그 후, PDF의 헤더에 텍스트를 추가하기 위해 Page의 AddStamp 메서드를 호출할 수 있습니다.

헤더 영역의 텍스트를 조정할 수 있도록 TopMargin 속성을 설정해야 합니다. 또한 HorizontalAlignment를 Center로, VerticalAlignment를 Top으로 설정해야 합니다.

다음 코드 스니펫은 C#을 사용하여 PDF 파일의 헤더에 텍스트를 추가하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHeaderText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextinHeader.pdf"))
    {
        // Create header as a TextStamp
        var textStamp = new Aspose.Pdf.TextStamp("Header Text")
        {
            TopMargin = 10,
            HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center,
            VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top
        };

        // Add header on all pages
        foreach (var page in document.Pages)
        {
            page.AddStamp(textStamp);
        }

        // Save PDF document
        document.Save(dataDir + "TextinHeader_out.pdf");
    }
}
```

## PDF 파일의 푸터에 텍스트 추가

PDF 파일의 푸터에 텍스트를 추가하려면 TextStamp 클래스를 사용할 수 있습니다. TextStamp 클래스는 글꼴 크기, 글꼴 스타일 및 글꼴 색상 등과 같은 텍스트 기반 스탬프를 생성하는 데 필요한 속성을 제공합니다. 푸터에 텍스트를 추가하려면 필요한 속성을 사용하여 Document 객체와 TextStamp 객체를 생성해야 합니다. 그 후, PDF의 푸터에 텍스트를 추가하기 위해 Page의 AddStamp 메서드를 호출할 수 있습니다.

{{% alert color="primary" %}}

푸터 영역의 텍스트를 조정할 수 있도록 Bottom Margin 속성을 설정해야 합니다. 또한 HorizontalAlignment를 Center로, VerticalAlignment를 Bottom으로 설정해야 합니다.

{{% /alert %}}

다음 코드 스니펫은 C#을 사용하여 PDF 파일의 푸터에 텍스트를 추가하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFooterText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextinFooter.pdf"))
    {
        // Create footer as a TextStamp
        var textStamp = new Aspose.Pdf.TextStamp("Footer Text")
        {
            BottomMargin = 10,
            HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center,
            VerticalAlignment = Aspose.Pdf.VerticalAlignment.Bottom
        };

        // Add footer on all pages
        foreach (var page in document.Pages)
        {
            page.AddStamp(textStamp);
        }

        // Save PDF document
        document.Save(dataDir + "TextinFooter_out.pdf");
    }
}
```

## PDF 파일의 헤더에 이미지 추가

PDF 파일의 헤더에 이미지를 추가하려면 [ImageStamp](https://reference.aspose.com/pdf/net/aspose.pdf/ImageStamp) 클래스를 사용할 수 있습니다. Image Stamp 클래스는 글꼴 크기, 글꼴 스타일 및 글꼴 색상 등과 같은 이미지 기반 스탬프를 생성하는 데 필요한 속성을 제공합니다. 헤더에 이미지를 추가하려면 필요한 속성을 사용하여 Document 객체와 Image Stamp 객체를 생성해야 합니다. 그 후, PDF의 헤더에 이미지를 추가하기 위해 Page의 [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) 메서드를 호출할 수 있습니다.

{{% alert color="primary" %}}

헤더 영역의 이미지를 조정할 수 있도록 TopMargin 속성을 설정해야 합니다. 또한 HorizontalAlignment를 Center로, VerticalAlignment를 Top으로 설정해야 합니다.

{{% /alert %}}

다음 코드 스니펫은 C#을 사용하여 PDF 파일의 헤더에 이미지를 추가하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageHeader()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImageinHeader.pdf"))
    {
        // Create header as an ImageStamp
        var imageStamp = new Aspose.Pdf.ImageStamp(dataDir + "aspose-logo.jpg")
        {
            TopMargin = 10,
            HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center,
            VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top
        };

        // Add image header on all pages
        foreach (var page in document.Pages)
        {
            page.AddStamp(imageStamp);
        }

        // Save PDF document
        document.Save(dataDir + "ImageinHeader_out.pdf");
    }
}
```

## PDF 파일의 푸터에 이미지 추가

PDF 파일의 푸터에 이미지를 추가하려면 Image Stamp 클래스를 사용할 수 있습니다. Image Stamp 클래스는 글꼴 크기, 글꼴 스타일 및 글꼴 색상 등과 같은 이미지 기반 스탬프를 생성하는 데 필요한 속성을 제공합니다. 푸터에 이미지를 추가하려면 필요한 속성을 사용하여 Document 객체와 Image Stamp 객체를 생성해야 합니다. 그 후, PDF의 푸터에 이미지를 추가하기 위해 Page의 AddStamp 메서드를 호출할 수 있습니다.

{{% alert color="primary" %}}

PDF의 푸터 영역의 이미지를 조정할 수 있도록 [BottomMargin](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/bottommargin) 속성을 설정해야 합니다. 또한 [HorizontalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/horizontalalignment)를 `Center`로, [VerticalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/verticalalignment)를 `Bottom`으로 설정해야 합니다.

{{% /alert %}}

다음 코드 스니펫은 C#을 사용하여 PDF 파일의 푸터에 이미지를 추가하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageFooter()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImageInFooter.pdf"))
    {
        // Create footer as an ImageStamp
        var imageStamp = new Aspose.Pdf.ImageStamp(dataDir + "aspose-logo.jpg")
        {
            BottomMargin = 10,
            HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center,
            VerticalAlignment = Aspose.Pdf.VerticalAlignment.Bottom
        };

        // Add image footer on all pages
        foreach (var page in document.Pages)
        {
            page.AddStamp(imageStamp);
        }

        // Save PDF document
        document.Save(dataDir + "ImageInFooter_out.pdf");
    }
}
```

## 하나의 PDF 파일에 서로 다른 헤더 추가

우리는 TopMargin 또는 Bottom Margin 속성을 사용하여 문서의 헤더/푸터 섹션에 TextStamp를 추가할 수 있다는 것을 알고 있지만, 때때로 하나의 PDF 문서에 여러 개의 헤더/푸터를 추가해야 할 필요가 있을 수 있습니다. **Aspose.PDF for .NET**은 이를 수행하는 방법을 설명합니다.

이 요구 사항을 달성하기 위해 개별 TextStamp 객체를 생성하고 (객체 수는 필요한 헤더/푸터 수에 따라 다름) PDF 문서에 추가할 것입니다. 또한 개별 스탬프 객체에 대해 서로 다른 형식 정보를 지정할 수 있습니다. 다음 예제에서는 Document 객체와 세 개의 TextStamp 객체를 생성한 후, PDF의 헤더 섹션에 텍스트를 추가하기 위해 Page의 [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) 메서드를 사용했습니다. 다음 코드 스니펫은 Aspose.PDF for .NET을 사용하여 PDF 파일의 푸터에 이미지를 추가하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddDifferentHeaders()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddingDifferentHeaders.pdf"))
    {
        // Create three stamps
        var stamp1 = new Aspose.Pdf.TextStamp("Header 1");
        var stamp2 = new Aspose.Pdf.TextStamp("Header 2");
        var stamp3 = new Aspose.Pdf.TextStamp("Header 3");

        // Set stamp1 properties (Header 1)
        stamp1.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
        stamp1.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        stamp1.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;
        stamp1.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
        stamp1.TextState.FontSize = 14;

        // Set stamp2 properties (Header 2)
        stamp2.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
        stamp2.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        stamp2.Zoom = 10;

        // Set stamp3 properties (Header 3)
        stamp3.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
        stamp3.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        stamp3.RotateAngle = 35;
        stamp3.TextState.BackgroundColor = Aspose.Pdf.Color.Pink;
        stamp3.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Verdana");

        // Add the stamps to specific pages
        document.Pages[1].AddStamp(stamp1);
        document.Pages[2].AddStamp(stamp2);
        document.Pages[3].AddStamp(stamp3);

        // Save PDF document
        document.Save(dataDir + "MultiHeader_out.pdf");
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