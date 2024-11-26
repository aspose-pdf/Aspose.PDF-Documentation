---
title: ASP.NET without using Visual Studio
type: docs
weight: 60
url: /net/asp-net-without-using-visual-studio/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "ASP.NET without using Visual Studio",
    "alternativeHeadline": "Create ASP.NET Applications Without Visual Studio",
    "abstract": "Discover how to create ASP.NET applications without relying on Visual Studio using Aspose.PDF for .NET. This innovative approach allows developers to write HTML and C# or VB.NET code in a single .aspx file, streamlining the process of generating PDF documents directly within ASP.NET pages. Maximize your development efficiency with this seamless integration",
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
    "url": "/net/asp-net-without-using-visual-studio/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/asp-net-without-using-visual-studio/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

{{% alert color="primary" %}}

[Aspose.PDF for .NET](/pdf/net/) can be used to develop ASP.NET pages or applications without using Visual Studio. In this example, we’ll write HTML and the C# or VB.NET code in a single .aspx file; this is commonly known as Instant ASP.NET.

{{% /alert %}}

## Implementation details

{{% alert color="primary" %}}

Create a sample web application and copy Aspose.PDF.dll into a directory named "Bin" in your website directory ( *if bin folder does not exist, create one* ). Then create your .aspx page and copy the following code into it.
This example shows how to use [Aspose.PDF for .NET](/pdf/net/) with inline code in an ASP.NET page in order to create a simple PDF document with some sample text inside it.
{{% /alert %}}

```cs
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
    // set license
    Aspose.Pdf.License lic = new Aspose.Pdf.License();
    lic.SetLicense("D:\\ASPOSE\\Licences\\Aspose.Total licenses\\Aspose.Total.lic");

    // Initialize document object
    Document document = new Document();
    // Add page
    Page page = document.Pages.Add();
    // Add text to new page
    page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
    // Save updated PDF
    var outputFileName = dataDir + "HelloWorld_out.pdf";
    document.Save(outputFileName);
%>

    </body>
</html>
```
