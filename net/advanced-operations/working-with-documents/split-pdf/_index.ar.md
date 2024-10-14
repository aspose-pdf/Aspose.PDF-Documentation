---
title: تقسيم ملفات PDF برمجيًا
linktitle: تقسيم ملفات PDF
type: docs
weight: 60
url: /net/split-pdf-document/
keywords: تقسيم pdf إلى ملفات متعددة، تقسيم pdf إلى pdfs منفصلة، تقسيم pdf c#
description: هذا الموضوع يوضح كيفية تقسيم صفحات PDF إلى ملفات PDF فردية في تطبيقات .NET الخاصة بك باستخدام C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/split-document/
    - /net/split-pdf-pages/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "تقسيم ملفات PDF برمجيًا",
    "alternativeHeadline": "كيفية تقسيم PDF مع .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستندات PDF",
    "keywords": "pdf, c#, تقسيم pdf",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق وثائق Aspose.PDF",
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
    "url": "/net/split-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/split-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "هذا الموضوع يوضح كيفية تقسيم صفحات PDF إلى ملفات PDF فردية في تطبيقات .NET الخاصة بك باستخدام C#."
}
</script>
## مثال حي

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) هو تطبيق ويب مجاني يسمح لك بفحص كيفية عمل وظيفة تقسيم العروض التقديمية.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

يوضح هذا الموضوع كيفية تقسيم صفحات PDF إلى ملفات PDF فردية في تطبيقات .NET الخاصة بك. لتقسيم صفحات PDF إلى ملفات PDF ذات صفحة واحدة باستخدام C#، يمكن اتباع الخطوات التالية:

1. تكرار صفحات مستند PDF من خلال مجموعة [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) لكائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)
1. في كل تكرار، قم بإنشاء كائن Document جديد وأضف كائن [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) الفردي إلى المستند الفارغ
1. حفظ PDF الجديد باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4)

يعمل الجزء التالي من الشفرة أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).
يعمل الكود التالي أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

## تقسيم ملف PDF إلى ملفات متعددة أو ملفات PDF منفصلة في C#

يوضح لك الكود التالي بلغة C# كيفية تقسيم صفحات PDF إلى ملفات PDF منفردة.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// فتح المستند
Document pdfDocument = new Document(dataDir + "SplitToPages.pdf");

int pageCount = 1;

// تكرار على جميع الصفحات
foreach (Page pdfPage in pdfDocument.Pages)
{
    Document newDocument = new Document();
    newDocument.Pages.Add(pdfPage);
    newDocument.Save(dataDir + "page_" + pageCount + "_out" + ".pdf");
    pageCount++;
}
```

