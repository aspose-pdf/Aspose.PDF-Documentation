---
title: Visual Studio 없이 ASP.NET 사용하기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /ko/net/asp-net-without-using-visual-studio/
description: Visual Studio에 의존하지 않고 ASP.NET 프로젝트에서 Aspose.PDF for .NET을 사용하는 방법을 배우십시오. 이 실용적인 가이드를 따르십시오.
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "ASP.NET without using Visual Studio",
    "alternativeHeadline": "Create ASP.NET Applications Without Visual Studio",
    "abstract": "Visual Studio에 의존하지 않고 Aspose.PDF for .NET을 사용하여 ASP.NET 애플리케이션을 만드는 방법을 알아보세요. 이 혁신적인 접근 방식은 개발자가 단일 .aspx 파일에서 HTML 및 C# 또는 VB.NET 코드를 작성할 수 있게 하여 ASP.NET 페이지 내에서 PDF 문서를 직접 생성하는 과정을 간소화합니다. 이 원활한 통합으로 개발 효율성을 극대화하세요.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "263",
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
    "url": "/net/asp-net-without-using-visual-studio/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/asp-net-without-using-visual-studio/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

{{% alert color="primary" %}}

[Aspose.PDF for .NET](/pdf/ko/net/)은 Visual Studio를 사용하지 않고 ASP.NET 페이지 또는 애플리케이션을 개발하는 데 사용할 수 있습니다. 이 예제에서는 HTML과 C# 또는 VB.NET 코드를 단일 .aspx 파일에 작성할 것입니다. 이를 일반적으로 Instant ASP.NET이라고 합니다.

{{% /alert %}}

## 구현 세부사항

{{% alert color="primary" %}}

샘플 웹 애플리케이션을 만들고 Aspose.PDF.dll을 웹사이트 디렉토리의 "Bin"이라는 디렉토리에 복사합니다 ( *bin 폴더가 존재하지 않으면 생성하십시오* ). 그런 다음 .aspx 페이지를 만들고 다음 코드를 복사합니다.
이 예제는 ASP.NET 페이지에서 인라인 코드와 함께 [Aspose.PDF for .NET](/pdf/ko/net/)를 사용하는 방법을 보여주며, 내부에 샘플 텍스트가 포함된 간단한 PDF 문서를 생성합니다.
{{% /alert %}}

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
<%@ Page Language ="C#" %>
<%@ Import Namespace="System" %>
<%@ Import Namespace="System.IO" %>
<%@ Import Namespace="System.Data" %>
<%@ Import Namespace="Aspose.PDF" %>

<html>
    <head>
        <title> using Aspose.PDF for .NET with Inline ASP.NET</title>
    </head>
    <body>
        <h3>creation of simple PDF document while using Aspose.PDF for .NET with Inline ASP.NET</h3>
<%
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    // Set license
    Aspose.Pdf.License lic = new Aspose.Pdf.License();
    lic.SetLicense("Aspose.Total.lic");

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        Aspose.Pdf.Page page = document.Pages.Add();
        // Add text to new page
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
        // Save PDF document
        document.Save(dataDir + "HelloWorld_out.pdf");
    }
%>

    </body>
</html>
```