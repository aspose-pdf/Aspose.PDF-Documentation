---
title: كيفية دمج ملفات PDF باستخدام C#
linktitle: دمج ملفات PDF
type: docs
weight: 50
url: /ar/net/merge-pdf-documents/
keywords: "merge multiple pdf into single pdf c#, combine multiple pdf into one c#, merge multiple pdf into one c#"
description: هذه الصفحة تشرح كيفية دمج مستندات PDF في ملف PDF واحد باستخدام C# أو VB.NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "كيفية دمج ملفات PDF باستخدام C#",
    "alternativeHeadline": "دمج مستندات PDF",
    "author": {
        "@type": "Person",
        "name": "أناستازيا هولوب",
        "givenName": "أناستازيا",
        "familyName": "هولوب",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "تلاعب بمستندات PDF",
    "keywords": "pdf, c#, merge pdf, concatenate, combine pdf",
    "wordcount": "212",
    "proficiencyLevel": "مبتدئ",
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
                "contactType": "مبيعات",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "مبيعات",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "مبيعات",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "https://docs.aspose.com/pdf/net/merge-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://docs.aspose.com/pdf/net/merge-pdf-documents/"
    },
    "dateModified": "2022-02-04",
    "description": "هذه الصفحة تشرح كيفية دمج مستندات PDF في ملف PDF واحد باستخدام C# أو VB.NET."
}
</script>
## دمج أو توحيد عدة ملفات PDF في ملف PDF واحد باستخدام C#

دمج ملفات PDF في C# ليس مهمة سهلة بدون استخدام مكتبة خارجية.
يوضح هذا المقال كيفية دمج عدة ملفات PDF في مستند PDF واحد باستخدام Aspose.PDF لـ .NET. الأمثلة مكتوبة بلغة C# ولكن يمكن استخدام الواجهة البرمجية في لغات برمجة .NET الأخرى مثل VB.NET. يتم دمج ملفات PDF بحيث يتم ربط الأول بنهاية المستند الآخر.

يعمل الكود التالي أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

## دمج ملفات PDF باستخدام C# و DOM

لربط ملفي PDF:

1. إنشاء عنصرين [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)، كل واحد يحتوي على أحد ملفات PDF الإدخال.
1. ثم استدعاء طريقة Add لمجموعة [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) للعنصر Document الذي تريد إضافة ملف PDF الآخر إليه.
1.
1.
1. أخيراً، احفظ ملف PDF الناتج باستخدام طريقة [الحفظ](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

الشيفرة التالية توضح كيفية دمج ملفات PDF.

```csharp
// مسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// فتح المستند الأول
Document pdfDocument1 = new Document(dataDir + "Concat1.pdf");
// فتح المستند الثاني
Document pdfDocument2 = new Document(dataDir + "Concat2.pdf");

// إضافة صفحات المستند الثاني إلى الأول
pdfDocument1.Pages.Add(pdfDocument2.Pages);

dataDir = dataDir + "ConcatenatePdfFiles_out.pdf";
// حفظ الملف الناتج المدمج
pdfDocument1.Save(dataDir);
```

## مثال مباشر

[دمج Aspose.PDF](https://products.aspose.app/pdf/merger) هو تطبيق ويب مجاني عبر الإنترنت يتيح لك استكشاف كيفية عمل وظيفة دمج العروض التقديمية.

[![دمج Aspose.PDF](merger.png)](https://products.aspose.app/pdf/merger)

## انظر أيضا

- [تقسيم PDF باستخدام DOM](https://docs.aspose.com/pdf/net/split-pdf-document/)
- [تقسيم ملف PDF باستخدام DOM](https://docs.aspose.com/pdf/net/split-pdf-document/)
- [دمج مستندات PDF باستخدام Facades](https://docs.aspose.com/pdf/net/concatenate-pdf-documents/)
- [تقسيم ملف PDF باستخدام Facades](https://docs.aspose.com/pdf/net/split-pdf-pages/)

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>


