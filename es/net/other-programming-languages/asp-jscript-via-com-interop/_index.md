---
title: ASP - JScript a través de COM Interop
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /es/net/asp-jscript-via-com-interop/
description: Aprende a usar Aspose.PDF for .NET en aplicaciones ASP y JScript a través de COM Interop. Habilita capacidades avanzadas de PDF.
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "ASP - JScript via COM Interop",
    "alternativeHeadline": "Integrate JScript with ASP for PDF Creation",
    "abstract": "Presentando una poderosa característica que permite a los desarrolladores de ASP utilizar JScript a través de COM Interop para la creación fluida de documentos PDF. Esta funcionalidad permite la integración sin esfuerzo de Aspose.PDF for .NET, permitiendo a los usuarios agregar dinámicamente cadenas de texto a archivos PDF directamente dentro de sus aplicaciones ASP, optimizando los flujos de trabajo de generación de documentos.",
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
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

{{% alert color="primary" %}}

Esta es una aplicación ASP simple que te muestra cómo agregar una cadena de texto simple a un archivo PDF usando [Aspose.PDF for .NET](/pdf/net/) y JScript a través de COM Interop.

{{% /alert %}}

Ejemplo:

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