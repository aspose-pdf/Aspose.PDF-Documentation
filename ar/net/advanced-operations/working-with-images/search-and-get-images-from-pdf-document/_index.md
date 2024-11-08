---
title: الحصول على الصور والبحث عنها في ملف PDF
linktitle: البحث عن الصور والحصول عليها
type: docs
weight: 60
url: /ar/net/search-and-get-images-from-pdf-document/
description: توضح هذه القسم كيفية البحث عن الصور والحصول عليها من مستند PDF باستخدام مكتبة Aspose.PDF.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "الحصول على الصور والبحث عنها في ملف PDF",
    "alternativeHeadline": "كيفية الحصول على الصور والبحث عنها في ملف PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستند PDF",
    "keywords": "pdf, .net, get image, search image",
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
    "url": "/net/search-and-get-images-from-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/search-and-get-images-from-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "توضح هذه القسم كيفية البحث عن الصور والحصول عليها من مستند PDF باستخدام مكتبة Aspose.PDF."
}
</script>
يسمح لك ImagePlacementAbsorber بالبحث بين الصور في جميع صفحات مستند PDF.

الشفرة التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

للبحث في مستند كامل عن الصور:

1. استدعِ طريقة Accept لمجموعة الصفحات. تأخذ طريقة Accept كائن ImagePlacementAbsorber كمعامل. يُعيد هذا مجموعة من كائنات ImagePlacement.
2. قم بالتكرار خلال كائنات ImagePlacement واحصل على خصائصها (الصورة، الأبعاد، الدقة وهكذا).

تُظهر الشفرة التالية كيفية البحث في المستند عن جميع صوره.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// فتح المستند
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir+ "SearchAndGetImages.pdf");

// إنشاء كائن ImagePlacementAbsorber لأداء بحث موضع الصورة
ImagePlacementAbsorber abs = new ImagePlacementAbsorber();

// قبول الامتصاص لجميع الصفحات
doc.Pages.Accept(abs);

// التكرار خلال جميع ImagePlacements، الحصول على الصورة وخصائص ImagePlacement
foreach (ImagePlacement imagePlacement in abs.ImagePlacements)
{
    // الحصول على الصورة باستخدام كائن ImagePlacement
    XImage image = imagePlacement.Image;

    // عرض خصائص موضع الصورة لجميع المواضع
    Console.Out.WriteLine("عرض الصورة:" + imagePlacement.Rectangle.Width);
    Console.Out.WriteLine("ارتفاع الصورة:" + imagePlacement.Rectangle.Height);
    Console.Out.WriteLine("LLX للصورة:" + imagePlacement.Rectangle.LLX);
    Console.Out.WriteLine("LLY للصورة:" + imagePlacement.Rectangle.LLY);
    Console.Out.WriteLine("دقة الصورة الأفقية:" + imagePlacement.Resolution.X);
    Console.Out.WriteLine("دقة الصورة الرأسية:" + imagePlacement.Resolution.Y);
}
```
للحصول على صورة من صفحة فردية، استخدم الكود التالي:

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
doc.Pages[1].Accept(abs);
```

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
    "applicationCategory": "مكتبة تلاعب PDF لـ .NET",
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

