---
title: PDF에서 제목 작업하기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
url: /ko/net/working-with-headings/
weight: 70
description: C#로 PDF 문서의 제목에 번호 매기기를 생성합니다. Aspose.PDF for .NET는 다양한 번호 매기기 스타일을 제공합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Headings in PDF",
    "alternativeHeadline": "Enhance PDF Headings with Custom Numbering Styles",
    "abstract": "Aspose.PDF for .NET를 사용하여 사용자 정의 가능한 제목 번호 매기기로 PDF 문서를 향상시키세요. 이 새로운 기능은 로마 숫자 및 알파벳 목록과 같은 다양한 미리 정의된 번호 매기기 스타일을 적용하여 제목을 효과적으로 구성하고 문서의 가독성과 구조를 개선할 수 있게 해줍니다. 이 다재다능한 기능을 C# 애플리케이션에 통합하여 PDF 생성 프로세스를 간소화하세요.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF, C#, headings in PDF, numbering style, Aspose.PDF for .NET, pre-defined numbering styles, NumberingStyle enumeration, document generation, Heading class, pdf document manipulation",
    "wordcount": "453",
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
    "url": "/net/working-with-headings/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-headings/"
    },
    "dateModified": "2024-11-25",
    "description": "C#로 PDF 문서의 제목에 번호 매기기를 생성합니다. Aspose.PDF for .NET는 다양한 번호 매기기 스타일을 제공합니다."
}
</script>

## 제목에 번호 매기기 스타일 적용

제목은 모든 문서의 중요한 부분입니다. 작가는 항상 제목을 독자에게 더 두드러지고 의미 있게 만들려고 합니다. 문서에 제목이 여러 개 있는 경우, 작가는 이러한 제목을 구성할 수 있는 여러 가지 옵션이 있습니다. 제목을 구성하는 가장 일반적인 방법 중 하나는 번호 매기기 스타일로 제목을 작성하는 것입니다.

[Aspose.PDF for .NET](/pdf/net/)는 많은 미리 정의된 번호 매기기 스타일을 제공합니다. 이러한 미리 정의된 번호 매기기 스타일은 열거형인 NumberingStyle에 저장됩니다. NumberingStyle 열거형의 미리 정의된 값과 그 설명은 아래와 같습니다:

|**제목 유형**|**설명**|
| :- | :- |
|NumeralsArabic|아랍식, 예: 1,1.1,...|
|NumeralsRomanUppercase|로마 대문자, 예: I,I.II,...|
|NumeralsRomanLowercase|로마 소문자, 예: i,i.ii,...|
|LettersUppercase|영어 대문자, 예: A,A.B,...|
|LettersLowercase|영어 소문자, 예: a,a.b,...|
**Aspose.Pdf.Heading** 클래스의 **Style** 속성은 제목의 번호 매기기 스타일을 설정하는 데 사용됩니다.

|**그림: 미리 정의된 번호 매기기 스타일**|
| :- |
위 그림에 표시된 출력을 얻기 위한 소스 코드는 아래 예제에 제공됩니다.

다음 코드 조각은 [Aspose.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ApplyNumberStyleToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        document.PageInfo.Width = 612.0;
        document.PageInfo.Height = 792.0;
        document.PageInfo.Margin = new Aspose.Pdf.MarginInfo();
        document.PageInfo.Margin.Left = 72;
        document.PageInfo.Margin.Right = 72;
        document.PageInfo.Margin.Top = 72;
        document.PageInfo.Margin.Bottom = 72;

        // Add page
        var pdfPage = document.Pages.Add();
        pdfPage.PageInfo.Width = 612.0;
        pdfPage.PageInfo.Height = 792.0;
        pdfPage.PageInfo.Margin = new Aspose.Pdf.MarginInfo();
        pdfPage.PageInfo.Margin.Left = 72;
        pdfPage.PageInfo.Margin.Right = 72;
        pdfPage.PageInfo.Margin.Top = 72;
        pdfPage.PageInfo.Margin.Bottom = 72;

        // Create a floating box with the same margin as the page
        var floatBox = new Aspose.Pdf.FloatingBox();
        floatBox.Margin = pdfPage.PageInfo.Margin;

        // Add the floating box to the page
        pdfPage.Paragraphs.Add(floatBox);

        // Add headings with numbering styles
        var heading = new Aspose.Pdf.Heading(1);
        heading.IsInList = true;
        heading.StartNumber = 1;
        heading.Text = "List 1";
        heading.Style = Aspose.Pdf.NumberingStyle.NumeralsRomanLowercase;
        heading.IsAutoSequence = true;
        floatBox.Paragraphs.Add(heading);

        var heading2 = new Aspose.Pdf.Heading(1);
        heading2.IsInList = true;
        heading2.StartNumber = 13;
        heading2.Text = "List 2";
        heading2.Style = Aspose.Pdf.NumberingStyle.NumeralsRomanLowercase;
        heading2.IsAutoSequence = true;
        floatBox.Paragraphs.Add(heading2);

        var heading3 = new Aspose.Pdf.Heading(2);
        heading3.IsInList = true;
        heading3.StartNumber = 1;
        heading3.Text = "the value, as of the effective date of the plan, of property to be distributed under the plan on account of each allowed";
        heading3.Style = Aspose.Pdf.NumberingStyle.LettersLowercase;
        heading3.IsAutoSequence = true;
        floatBox.Paragraphs.Add(heading3);

        // Save PDF document
        document.Save(dataDir + "ApplyNumberStyle_out.pdf");
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