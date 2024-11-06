---
title: إضافة خلفية إلى ملف PDF باستخدام C#
linktitle: إضافة خلفيات
type: docs
weight: 110
url: ar/net/add-backgrounds/
description: أضف صورة خلفية إلى ملف PDF الخاص بك باستخدام C#. استخدم كائن BackgroundArtifact.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "إضافة خلفية إلى ملف PDF باستخدام C#",
    "alternativeHeadline": "العمل مع الخلفية في PDF",
    "author": {
        "@type": "Person",
        "name":"أناستازيا هولوب",
        "givenName": "أناستازيا",
        "familyName": "هولوب",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستند PDF",
    "keywords": "pdf, c#, الخلفية في pdf",
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
    "url": "/net/add-backgrounds/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-backgrounds/"
    },
    "dateModified": "2022-02-04",
    "description": "أضف صورة خلفية إلى ملف PDF الخاص بك باستخدام C#. استخدم كائن BackgroundArtifact."
}
</script>
يمكن استخدام الصور الخلفية لإضافة علامة مائية، أو تصميم خفي آخر، إلى المستندات. في Aspose.PDF لـ .NET، يتكون كل مستند PDF من مجموعة صفحات وكل صفحة تحتوي على مجموعة من الأدوات. يمكن استخدام فئة [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact) لإضافة صورة خلفية إلى كائن صفحة.

تعمل الشفرة البرمجية التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

توضح الشفرة البرمجية التالية كيفية إضافة صورة خلفية إلى صفحات PDF باستخدام كائن BackgroundArtifact مع C#.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// إنشاء كائن مستند جديد
Document doc = new Document();

// إضافة صفحة جديدة لكائن المستند
Page page = doc.Pages.Add();

// إنشاء كائن أداة الخلفية
BackgroundArtifact background = new BackgroundArtifact();

// تحديد الصورة لكائن أداة الخلفية
background.BackgroundImage = File.OpenRead(dataDir + "aspose-total-for-net.jpg");

// إضافة أداة الخلفية إلى مجموعة أدوات الصفحة
page.Artifacts.Add(background);

dataDir = dataDir + "ImageAsBackground_out.pdf";
// حفظ المستند
doc.Save(dataDir);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "مكتبة Aspose.PDF لـ .NET",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "مكتبة التلاعب بملفات PDF لـ .NET",
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
```

