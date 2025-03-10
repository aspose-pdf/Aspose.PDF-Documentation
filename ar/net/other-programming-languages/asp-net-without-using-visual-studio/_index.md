---
title: ASP.NET بدون استخدام Visual Studio
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /ar/net/asp-net-without-using-visual-studio/
description: تعلم كيفية استخدام Aspose.PDF for .NET في مشاريع ASP.NET دون الاعتماد على Visual Studio. اتبع هذا الدليل العملي.
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "ASP.NET without using Visual Studio",
    "alternativeHeadline": "Create ASP.NET Applications Without Visual Studio",
    "abstract": "اكتشف كيفية إنشاء تطبيقات ASP.NET دون الاعتماد على Visual Studio باستخدام Aspose.PDF for .NET. تتيح هذه الطريقة المبتكرة للمطورين كتابة HTML و C# أو VB.NET في ملف .aspx واحد، مما يسهل عملية إنشاء مستندات PDF مباشرة داخل صفحات ASP.NET. قم بزيادة كفاءة تطويرك مع هذا التكامل السلس",
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
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

{{% alert color="primary" %}}

[Aspose.PDF for .NET](/pdf/ar/net/) يمكن استخدامه لتطوير صفحات أو تطبيقات ASP.NET دون استخدام Visual Studio. في هذا المثال، سنكتب HTML وكود C# أو VB.NET في ملف .aspx واحد؛ وهذا ما يعرف عادةً بـ Instant ASP.NET.

{{% /alert %}}

## تفاصيل التنفيذ

{{% alert color="primary" %}}

قم بإنشاء تطبيق ويب عينة وانسخ Aspose.PDF.dll إلى دليل يسمى "Bin" في دليل موقعك ( *إذا لم يكن هناك مجلد bin، قم بإنشائه* ). ثم قم بإنشاء صفحة .aspx الخاصة بك وانسخ الكود التالي إليها.
يوضح هذا المثال كيفية استخدام [Aspose.PDF for .NET](/pdf/ar/net/) مع كود مضمن في صفحة ASP.NET من أجل إنشاء مستند PDF بسيط يحتوي على بعض النصوص النموذجية بداخله.
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