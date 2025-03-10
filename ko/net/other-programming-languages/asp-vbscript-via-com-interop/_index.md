---
title: ASP - VBScript를 통한 COM 상호 운용
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ko/net/asp-vbscript-via-com-interop/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "ASP - VBScript via COM Interop",
    "alternativeHeadline": "Create PDFs in ASP with VBScript via COM Interop",
    "abstract": "새로운 ASP - VBScript via COM Interop 기능은 개발자가 VBScript를 사용하여 클래식 ASP 애플리케이션에서 PDF 문서를 원활하게 생성하고 조작할 수 있도록 합니다. Aspose.PDF for .NET을 활용하여 사용자는 사용자 정의 텍스트로 PDF 파일을 쉽게 생성하고 기존 PDF에서 콘텐츠를 추출할 수 있어 웹 애플리케이션의 기능과 다재다능성을 향상시킵니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "286",
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
    "url": "/net/asp-vbscript-via-com-interop/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/asp-vbscript-via-com-interop/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

## 필수 조건

{{% alert color="primary" %}}

    COM Interop을 통해 .NET용 Aspose.pdf 사용이라는 제목의 기사를 확인하세요.

{{% /alert %}}

## VB 스크립트의 Hello World! 예제

{{% alert color="primary" %}}

이것은 [Aspose.PDF for .NET](/pdf/ko/net/) 및 COM Interop을 통해 VBScript를 사용하여 샘플 텍스트로 PDF 파일을 생성하는 방법을 보여주는 간단한 ASP 애플리케이션입니다.

{{% /alert %}}

```vb
<%@ LANGUAGE = VBScript %>
<% Option Explicit %>
<html>
    <head>
        <title> using Aspose.PDF for .NET in classical ASP sample</title>
    </head>
<body>

<h3>creation of sample PDF document while using Aspose.PDF for .NET with classical ASP and VBScript</h3>

<%
'Set license
Dim lic
Set lic = CreateObject("Aspose.Pdf.License")
lic.SetLicense("Aspose.Total.lic")

'Instantiate Pdf instance by calling its empty constructor
Dim document
Set document = CreateObject("Aspose.Pdf.Document")

'Create a new section in the Pdf object
Dim pdfsection
Set pdfsection = CreateObject("Aspose.Pdf.Generator.Section")

'Add section to Pdf object
document.Sections.Add(pdfsection)

'Create Text object
Dim SampleText
Set SampleText = CreateObject("Aspose.Pdf.Generator.Text")

'Add Text Segment to text object
Dim seg1
Set seg1 = CreateObject("Aspose.Pdf.Generator.Segment")

'Assign some content to the segment
seg1.Content = "HelloWorld using ASP and VBScript"

'Add segment (with red text color) to the paragraph
SampleText.Segments.Add(seg1)

'Add Text paragraph to paragraphs collection of a section
pdfsection.Paragraphs.Add(SampleText)

'Save PDF document
document.Save("HelloWorldinASP_out.pdf")
%>

    </body>
</html>
```

## VBScript를 사용한 텍스트 추출

{{% alert color="primary" %}}
    이 VBScript 샘플은 COM Interop을 통해 기존 PDF 문서에서 텍스트를 추출합니다.
    Error rendering macro 'code' : Invalid value specified for parameter lang
{{% /alert %}}