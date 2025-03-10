---
title: ASP.NET без использования Visual Studio
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /ru/net/asp-net-without-using-visual-studio/
description: Узнайте, как использовать Aspose.PDF for .NET в проектах ASP.NET, не полагаясь на Visual Studio. Следуйте этому практическому руководству.
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "ASP.NET without using Visual Studio",
    "alternativeHeadline": "Create ASP.NET Applications Without Visual Studio",
    "abstract": "Узнайте, как создавать приложения ASP.NET без использования Visual Studio с помощью Aspose.PDF для .NET. Этот инновационный подход позволяет разработчикам писать код HTML, C# или VB.NET в одном файле .aspx, упрощая процесс создания PDF-документов непосредственно на страницах ASP.NET. Повысьте эффективность своей разработки с помощью этой бесшовной интеграции",
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
    "description": "Aspose.PDF может выполнять не только простые и лёгкие задачи, но и справляться с более сложными целями. Ознакомьтесь со следующим разделом для опытных пользователей и разработчиков."
}
</script>

{{% alert цвет="основной" %}}

[Aspose.PDF for .NET](/pdf/net/) можно использовать для разработки страниц или приложений ASP.NET без использования Visual Studio. В этом примере мы будем писать HTML и код C# или VB.NET в одном файле .aspx; это широко известно как Instant ASP.NET.

{{% /alert %}}

## Детали реализации

{{% alert цвет="основной" %}}

Создайте образец веб-приложения и скопируйте Aspose.PDF.dll в каталог с именем «Bin» в каталоге вашего веб-сайта (если папка bin не существует, создайте её). Затем создайте свою страницу .aspx и скопируйте в неё следующий код.
Этот пример показывает, как использовать [Aspose.PDF for .NET](/pdf/net/) со встроенным кодом на странице ASP.NET для создания простого PDF-документа с некоторым образцом текста внутри.
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