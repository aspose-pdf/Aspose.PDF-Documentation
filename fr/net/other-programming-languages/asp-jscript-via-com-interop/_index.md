---
title: ASP - JScript via COM Interop
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /fr/net/asp-jscript-via-com-interop/
description: Apprenez à utiliser Aspose.PDF for .NET dans les applications ASP et JScript via COM Interop. Activez des capacités PDF avancées.
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "ASP - JScript via COM Interop",
    "alternativeHeadline": "Integrate JScript with ASP for PDF Creation",
    "abstract": "Présentation d'une fonctionnalité puissante qui permet aux développeurs ASP d'utiliser JScript via COM Interop pour la création de documents PDF sans effort. Cette fonctionnalité permet une intégration facile de Aspose.PDF for .NET, permettant aux utilisateurs d'ajouter dynamiquement des chaînes de texte aux fichiers PDF directement dans leurs applications ASP, rationalisant ainsi les flux de travail de génération de documents.",
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
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs et développeurs avancés."
}
</script>

{{% alert color="primary" %}}

Ceci est une application ASP simple qui vous montre comment ajouter une chaîne de texte simple à un fichier PDF en utilisant [Aspose.PDF for .NET](/pdf/net/) et JScript via COM Interop.

{{% /alert %}}

Exemple :

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