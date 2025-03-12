---
title: ASP - VBScript عبر COM Interop
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ar/net/asp-vbscript-via-com-interop/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "ASP - VBScript via COM Interop",
    "alternativeHeadline": "Create PDFs in ASP with VBScript via COM Interop",
    "abstract": "تتيح ميزة ASP - VBScript عبر COM Interop الجديدة للمطورين إنشاء وتعديل مستندات PDF بسلاسة مباشرة من تطبيقات ASP الكلاسيكية باستخدام VBScript. من خلال الاستفادة من Aspose.PDF for .NET، يمكن للمستخدمين بسهولة إنشاء ملفات PDF بنص مخصص واستخراج المحتوى من ملفات PDF الموجودة، مما يعزز من وظائف ومرونة تطبيقاتهم على الويب.",
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
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## المتطلبات الأساسية

{{% alert color="primary" %}}

    يرجى مراجعة المقالة المسماة استخدام Aspose.pdf لـ .NET عبر COM Interop.

{{% /alert %}}

## مثال مرحبًا بالعالم! على VB Script

{{% alert color="primary" %}}

هذا تطبيق ASP بسيط يوضح لك كيفية إنشاء ملف PDF بنص عينة باستخدام [Aspose.PDF for .NET](/pdf/ar/net/) و VBScript عبر COM Interop.

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

## استخراج النص باستخدام VBScript

{{% alert color="primary" %}}
    هذا المثال من VBScript يستخرج النص من مستند PDF موجود عبر COM Interop.
    Error rendering macro 'code' : Invalid value specified for parameter lang
{{% /alert %}}