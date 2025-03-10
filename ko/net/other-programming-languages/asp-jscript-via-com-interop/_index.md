---
title: ASP - JScript를 COM Interop을 통해
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ko/net/asp-jscript-via-com-interop/
description: COM Interop을 통해 ASP 및 JScript 애플리케이션에서 Aspose.PDF for .NET을 사용하는 방법을 배웁니다. 고급 PDF 기능을 활성화합니다.
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "ASP - JScript via COM Interop",
    "alternativeHeadline": "Integrate JScript with ASP for PDF Creation",
    "abstract": "ASP 개발자가 COM Interop을 통해 JScript를 활용하여 원활한 PDF 문서 생성을 가능하게 하는 강력한 기능을 소개합니다. 이 기능은 Aspose.PDF for .NET의 통합을 용이하게 하여 사용자가 ASP 애플리케이션 내에서 PDF 파일에 텍스트 문자열을 동적으로 추가할 수 있도록 하여 문서 생성 워크플로를 간소화합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "182",
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
    "url": "/net/asp-jscript-via-com-interop/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/asp-jscript-via-com-interop/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 단순하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

{{% alert color="primary" %}}

이것은 [Aspose.PDF for .NET](/pdf/net/) 및 COM Interop을 통해 PDF 파일에 간단한 텍스트 문자열을 추가하는 방법을 보여주는 간단한 ASP 애플리케이션입니다.

{{% /alert %}}

예시:

```javascript
<%@ LANGUAGE = JScript %>
<html>
    <head>
        <title> using Aspose.PDF for .NET in classical ASP sample</title>
    </head>
    <body>
        <h3>creation of sample PDF document while using Aspose.PDF for .NET with classical ASP and JScript</h3>
<%
// set license
var lic = Server.CreateObject("Aspose.Pdf.License");
lic.SetLicense("D:\\ASPOSE\\Aspose.Total.lic");

// Instantiate Pdf instance by calling its empty constructor
var pdf = Server.CreateObject("Aspose.Pdf.Document");

// Create a new Page in the PDF object
var pdfpage = pdf.Pages.Add();

// Create Text Fragment object
var sampleText = Server.CreateObject("Aspose.Pdf.Text.TextFragment");

// Assign some content to the Fragment
sampleText.Text =  = "HelloWorld using ASP and JScript";

// Add Text paragraph to paragraphs collection of a section
pdfpage.Paragraphs.Add(SampleText);

// Save PDF document
pdf.Save("d:\\pdftest\\HelloWorldinASP.pdf");

%>
    </body>
</html>
```