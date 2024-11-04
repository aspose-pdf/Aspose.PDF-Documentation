---
title: إضافة ختم صفحات PDF في PDF باستخدام C#
linktitle: ختم الصفحات في ملف PDF
type: docs
weight: 30
url: /net/page-stamps-in-the-pdf-file/
description: أضف ختم صفحة إلى مستند PDF باستخدام فئة PdfPageStamp مع مكتبة Aspose.PDF لـ .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "إضافة ختم صفحات PDF في PDF باستخدام C#",
    "alternativeHeadline": "إضافة ختم صفحات PDF في PDF باستخدام C#",
    "author": {
        "@type": "Person",
        "name":"أندري أندروخوفسكي",
        "givenName": "أندري",
        "familyName": "أندروخوفسكي",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "توليد مستندات PDF",
    "keywords": "pdf, c#, توليد المستندات",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق مستندات Aspose.PDF",
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
    "url": "/net/page-stamps-in-the-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/page-stamps-in-the-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "أضف ختم صفحة إلى مستند PDF باستخدام فئة PdfPageStamp مع مكتبة Aspose.PDF لـ .NET."
}
</script>
## إضافة ختم الصفحة مع C\#

يمكن استخدام [PdfPageStamp](https://reference.aspose.com/pdf/net/aspose.pdf/PdfPageStamp) عندما تحتاج إلى تطبيق ختم مركب يحتوي على رسومات، نصوص، جداول. يوضح المثال التالي كيفية استخدام الختم لإنشاء أوراق مكتبية مثل استخدام Adobe InDesign، Illustrator، Microsoft Word. لنفترض أن لدينا بعض المستندات الأولية ونريد تطبيق نوعين من الحدود باللون الأزرق واللون البرقوق.

يعمل الجزء التالي من الكود أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
public static void AddPageStamp()
{
    var inputFileName = "sample-4pages.pdf";
    var outputFileName = "AddPageStamp_out.pdf";
    var pageStampFileName = "PageStamp.pdf";
    var document = new Document(_dataDir + inputFileName);

    var bluePageStamp = new PdfPageStamp(_dataDir + pageStampFileName, 1)
    {
        Height = 800,
        Background = true
    };

    var plumPageStamp = new PdfPageStamp(_dataDir + pageStampFileName, 2)
    {
        Height = 800,
        Background = true
    };

    for (int i = 1; i < 5; i++)
    {
        if (i % 2 == 0)
            document.Pages[i].AddStamp(bluePageStamp);
        else
            document.Pages[i].AddStamp(plumPageStamp);
    }

    document.Save(_dataDir + outputFileName);
}
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
                "areaServed": "الولايات المتحدة",
                "availableLanguage": "الإنجليزية"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "مبيعات",
                "areaServed": "المملكة المتحدة",
                "availableLanguage": "الإنجليزية"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "مبيعات",
                "areaServed": "أستراليا",
                "availableLanguage": "الإنجليزية"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "دولار أمريكي"
    },
    "applicationCategory": "مكتبة التلاعب بملفات PDF لـ .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "ويندوز، ماك أو إس، لينوكس",
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

