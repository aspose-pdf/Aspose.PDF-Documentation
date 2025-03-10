---
title: ASP - VBScript via COM Interop
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /pt/net/asp-vbscript-via-com-interop/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "ASP - VBScript via COM Interop",
    "alternativeHeadline": "Create PDFs in ASP with VBScript via COM Interop",
    "abstract": "O novo recurso ASP - VBScript via COM Interop permite que os desenvolvedores criem e manipulem documentos PDF diretamente de aplicações ASP clássicas usando VBScript. Ao aproveitar Aspose.PDF for .NET, os usuários podem gerar facilmente arquivos PDF com texto personalizado e extrair conteúdo de PDFs existentes, aprimorando a funcionalidade e versatilidade de suas aplicações web.",
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
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Pré-requisitos

{{% alert color="primary" %}}

    Por favor, verifique o artigo intitulado Use Aspose.pdf para .NET via COM Interop.

{{% /alert %}}

## Olá Mundo! Exemplo em VB Script

{{% alert color="primary" %}}

Este é um aplicativo ASP simples que mostra como criar um arquivo PDF com texto de exemplo usando [Aspose.PDF for .NET](/pdf/net/) e VBScript via COM Interop.

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

## Extraindo Texto usando VBScript

{{% alert color="primary" %}}
    Este exemplo de VBScript extrai texto de um documento PDF existente via COM Interop.
    Error rendering macro 'code' : Invalid value specified for parameter lang
{{% /alert %}}