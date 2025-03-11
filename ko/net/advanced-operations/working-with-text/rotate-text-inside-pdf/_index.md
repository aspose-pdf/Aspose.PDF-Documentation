---
title: PDF 내 텍스트 회전하기 C#
linktitle: PDF 내 텍스트 회전하기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ko/net/rotate-text-inside-pdf/
description: Aspose.PDF를 사용하여 .NET에서 PDF 파일 내 텍스트 정렬을 조정하고 프레젠테이션을 개선하는 방법을 배웁니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Rotate Text Inside PDF using C#",
    "alternativeHeadline": "Rotate Text to Any Angle in PDF with C#",
    "abstract": "Aspose.PDF for .NET은 사용자가 PDF 문서 내에서 다양한 각도로 텍스트 조각과 전체 단락을 회전할 수 있도록 합니다. 이 기능은 전문적이고 창의적인 응용 프로그램에서 다양한 형식 요구를 충족하기 위해 정확한 텍스트 방향 조정을 가능하게 하여 문서의 유연성을 향상시킵니다. 사용자는 제공된 API를 사용하여 이러한 회전을 쉽게 구현할 수 있으며, 문서 생성 경험을 향상시킵니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "860",
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
    "url": "/net/rotate-text-inside-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/rotate-text-inside-pdf/"
    },
    "dateModified": "2024-11-26",
    "description": "PDF에 텍스트를 회전하는 다양한 방법을 배웁니다. Aspose.PDF를 사용하면 텍스트를 원하는 각도로 회전하고, 텍스트 조각이나 전체 단락을 회전할 수 있습니다."
}
</script>

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

## 회전 속성을 사용하여 PDF 내 텍스트 회전하기

[TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) 클래스의 회전 속성을 사용하여 다양한 각도로 텍스트를 회전할 수 있습니다. 텍스트 회전은 문서 생성의 다양한 시나리오에서 사용할 수 있습니다. 요구 사항에 따라 텍스트를 회전하기 위해 도 단위로 회전 각도를 지정할 수 있습니다. 텍스트 회전을 구현할 수 있는 다양한 시나리오를 확인해 보십시오.

## TextFragment 및 TextBuilder를 사용하여 회전 구현하기

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RotateTextInsidePDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Get particular page
        var page = document.Pages.Add();
        // Create text fragment
        var textFragment1 = new Aspose.Pdf.Text.TextFragment("main text");
        textFragment1.Position = new Aspose.Pdf.Text.Position(100, 600);
        // Set text properties
        textFragment1.TextState.FontSize = 12;
        textFragment1.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
        // Create rotated text fragment
        var textFragment2 = new Aspose.Pdf.Text.TextFragment("rotated text");
        textFragment2.Position = new Aspose.Pdf.Text.Position(200, 600);
        // Set text properties
        textFragment2.TextState.FontSize = 12;
        textFragment2.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
        textFragment2.TextState.Rotation = 45;
        // Create rotated text fragment
        var textFragment3 = new Aspose.Pdf.Text.TextFragment("rotated text");
        textFragment3.Position = new Aspose.Pdf.Text.Position(300, 600);
        // Set text properties
        textFragment3.TextState.FontSize = 12;
        textFragment3.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
        textFragment3.TextState.Rotation = 90;
        // create TextBuilder object
        var textBuilder = new Aspose.Pdf.Text.TextBuilder(page);
        // Append the text fragment to the PDF page
        textBuilder.AppendText(textFragment1);
        textBuilder.AppendText(textFragment2);
        textBuilder.AppendText(textFragment3);
        // Save PDF document
        document.Save(dataDir + "RotateTextInsidePDF_out.pdf");
    }
}
```

## TextParagraph 및 TextBuilder를 사용하여 회전 구현하기 (회전된 조각)

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RotateTextInsidePDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Get particular page
        var page = document.Pages.Add();
        var paragraph = new Aspose.Pdf.Text.TextParagraph();
        paragraph.Position = new Aspose.Pdf.Text.Position(200, 600);
        // Create text fragment
        var textFragment1 = new Aspose.Pdf.Text.TextFragment("rotated text");
        // Set text properties
        textFragment1.TextState.FontSize = 12;
        textFragment1.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
        // Set rotation
        textFragment1.TextState.Rotation = 45;
        // Create text fragment
        var textFragment2 = new Aspose.Pdf.Text.TextFragment("main text");
        // Set text properties
        textFragment2.TextState.FontSize = 12;
        textFragment2.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
        // Create text fragment
        var textFragment3 = new Aspose.Pdf.Text.TextFragment("another rotated text");
        // Set text properties
        textFragment3.TextState.FontSize = 12;
        textFragment3.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
        // Set rotation
        textFragment3.TextState.Rotation = -45;
        // Append the text fragments to the paragraph
        paragraph.AppendLine(textFragment1);
        paragraph.AppendLine(textFragment2);
        paragraph.AppendLine(textFragment3);
        // Create TextBuilder object
        var textBuilder = new Aspose.Pdf.Text.TextBuilder(page);
        // Append the text paragraph to the PDF page
        textBuilder.AppendParagraph(paragraph);
        // Save PDF document
        document.Save(dataDir + "RotateTextInsidePDF_out.pdf");
    }
}
```

## TextFragment 및 Page.Paragraphs를 사용하여 회전 구현하기

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RotateTextInsidePDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Get particular page
        var page = document.Pages.Add();
        // Create text fragment
        var textFragment1 = new Aspose.Pdf.Text.TextFragment("main text");
        // Set text properties
        textFragment1.TextState.FontSize = 12;
        textFragment1.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
        // Create text fragment
        var textFragment2 = new Aspose.Pdf.Text.TextFragment("rotated text");
        // Set text properties
        textFragment2.TextState.FontSize = 12;
        textFragment2.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
        // Set rotation
        textFragment2.TextState.Rotation = 315;
        // Create text fragment
        var textFragment3 = new Aspose.Pdf.Text.TextFragment("rotated text");
        // Set text properties
        textFragment3.TextState.FontSize = 12;
        textFragment3.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
        // Set rotation
        textFragment3.TextState.Rotation = 270;
        page.Paragraphs.Add(textFragment1);
        page.Paragraphs.Add(textFragment2);
        page.Paragraphs.Add(textFragment3);
        // Save PDF document
        document.Save(dataDir + "RotateTextInsidePDF_out.pdf");
    }
}
```

## TextParagraph 및 TextBuilder를 사용하여 회전 구현하기 (전체 단락 회전)

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RotateTextInsidePDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Get particular page
        var page = document.Pages.Add();
        for (int i = 0; i < 4; i++)
        {
            var paragraph = new Aspose.Pdf.Text.TextParagraph();
            paragraph.Position = new Aspose.Pdf.Text.Position(200, 600);
            // Specify rotation
            paragraph.Rotation = i * 90 + 45;
            // Create text fragment
            var textFragment1 = new Aspose.Pdf.Text.TextFragment("Paragraph Text");
            // Create text fragment
            textFragment1.TextState.FontSize = 12;
            textFragment1.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
            textFragment1.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
            textFragment1.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
            // Create text fragment
            var textFragment2 = new Aspose.Pdf.Text.TextFragment("Second line of text");
            // Set text properties
            textFragment2.TextState.FontSize = 12;
            textFragment2.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
            textFragment2.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
            textFragment2.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
            // Create text fragment
            var textFragment3 = new Aspose.Pdf.Text.TextFragment("And some more text...");
            // Set text properties
            textFragment3.TextState.FontSize = 12;
            textFragment3.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
            textFragment3.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
            textFragment3.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
            textFragment3.TextState.Underline = true;
            paragraph.AppendLine(textFragment1);
            paragraph.AppendLine(textFragment2);
            paragraph.AppendLine(textFragment3);
            // Create TextBuilder object
            var textBuilder = new Aspose.Pdf.Text.TextBuilder(page);
            // Append the text fragment to the PDF page
            textBuilder.AppendParagraph(paragraph);
        }
        // Save PDF document
        document.Save(dataDir + "RotateTextInsidePDF_out.pdf");
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