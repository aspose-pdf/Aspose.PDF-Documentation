---
title: ASP - VBScript via COM Interop
type: docs
weight: 30
url: /net/asp-vbscript-via-com-interop/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "ASP - VBScript via COM Interop",
    "alternativeHeadline": "Create PDFs in ASP with VBScript via COM Interop",
    "abstract": "The new ASP - VBScript via COM Interop feature allows developers to seamlessly create and manipulate PDF documents directly from classic ASP applications using VBScript. By leveraging Aspose.PDF for .NET, users can easily generate PDF files with custom text and extract content from existing PDFs, enhancing the functionality and versatility of their web applications",
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
                "telephone": "\u002B1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "\u002B44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "\u002B61 2 8006 6987",
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
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Prerequisites

{{% alert color="primary" %}}

    Please check the article named Use Aspose.pdf for .NET via COM Interop.

{{% /alert %}}

## Hello World! Example on VB Script

{{% alert color="primary" %}}

This is a simple ASP application that shows you how to create a PDF file with sample text using [Aspose.PDF for .NET](/pdf/net/) and VBScript via COM Interop.

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
'set license
Dim lic
Set lic = CreateObject("Aspose.Pdf.License")
lic.SetLicense("D:\ASPOSE\Licences\Aspose.Total licenses\Aspose.Total.lic")

'Instantiate Pdf instance by calling its empty constructor
Dim pdf
Set pdf = CreateObject("Aspose.Pdf.Generator.Pdf")

'Create a new section in the Pdf object
Dim pdfsection
Set pdfsection = CreateObject("Aspose.Pdf.Generator.Section")

'Add section to Pdf object
pdf.Sections.Add(pdfsection)

' Create Text object
Dim SampleText
Set SampleText = CreateObject("Aspose.Pdf.Generator.Text")

'Add Text Segment to text object
Dim seg1
Set seg1 = CreateObject("Aspose.Pdf.Generator.Segment")

'Assign some content to the segment
seg1.Content = "HelloWorld using ASP and VBScript"

'Add segment (with red text color) to the paragraph
SampleText.Segments.Add(seg1)

' Add Text paragraph to paragraphs collection of a section
pdfsection.Paragraphs.Add(SampleText)

' Save the PDF document
pdf.Save("d:\pdftest\HelloWorldinASP.pdf")
%>

    </body>
</html>
```

## Extracting Text using VBScript

{{% alert color="primary" %}}
    This VBScript sample extracts text from an existing PDF document via COM Interop.
    Error rendering macro 'code' : Invalid value specified for parameter lang
{{% /alert %}}
