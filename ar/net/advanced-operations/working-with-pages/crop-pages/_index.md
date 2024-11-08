---
title: قص صفحات PDF برمجيًا C#
linktitle: قص الصفحات
type: docs
weight: 80
url: /ar/net/crop-pages/
description: يمكنك الحصول على خصائص الصفحة، مثل العرض والطول والهوامش وصندوق القص والتشذيب باستخدام Aspose.PDF لـ .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "قص صفحات PDF برمجيًا C#",
    "alternativeHeadline": "كيفية قص صفحات PDF في .NET",
    "author": {
        "@type": "Person",
        "name":"أناستازيا هولوب",
        "givenName": "أناستازيا",
        "familyName": "هولوب",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء وثيقة PDF",
    "keywords": "pdf, c#, قص صفحات pdf",
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
    "url": "/net/crop-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/crop-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "يمكنك الحصول على خصائص الصفحة، مثل العرض والطول والهوامش وصندوق القص والتشذيب باستخدام Aspose.PDF لـ .NET."
}
</script>
## خصائص الصفحة

كل صفحة في ملف PDF لها عدد من الخصائص، مثل العرض، الارتفاع، وصناديق القص والتشذيب. تسمح لك Aspose.PDF بالوصول إلى هذه الخصائص.

- **صندوق الوسائط**: صندوق الوسائط هو أكبر صندوق صفحة. يتوافق مع حجم الصفحة (على سبيل المثال A4، A5، US Letter، إلخ) المختار عندما تم طباعة المستند إلى PostScript أو PDF. بعبارة أخرى، يحدد صندوق الوسائط الحجم الفعلي للوسائط التي يتم عرض الوثيقة PDF أو طباعتها عليها.
- **صندوق النزيف**: إذا كان المستند يحتوي على نزيف، فسيكون للـ PDF أيضًا صندوق نزيف. النزيف هو مقدار اللون (أو العمل الفني) الذي يمتد إلى ما وراء حافة الصفحة. يُستخدم للتأكد من أنه عندما يتم طباعة المستند وقصه إلى الحجم ("التشذيب")، ستذهب الحبر إلى حافة الصفحة بالكامل. حتى لو تم قص الصفحة بشكل غير دقيق - قص قليلًا عن علامات القص - لن تظهر حواف بيضاء على الصفحة.
- **صندوق التشذيب**: يشير صندوق التشذيب إلى الحجم النهائي للمستند بعد الطباعة والتشذيب.
- **صندوق الفن**: صندوق الفن هو الصندوق المرسوم حول محتويات الصفحات الفعلية في مستنداتك.
- **صندوق الفن**: صندوق الفن هو الصندوق المرسوم حول المحتويات الفعلية للصفحات في مستنداتك.
- **صندوق القص**: صندوق القص هو "حجم الصفحة" الذي يتم عرض مستند PDF الخاص بك في Adobe Acrobat. في العرض العادي، يتم عرض محتويات صندوق القص فقط في Adobe Acrobat. للحصول على وصف تفصيلي لهذه الخصائص، اقرأ مواصفات Adobe.Pdf، وبالأخص القسم 10.10.1 حدود الصفحة.
- **Page.Rect**: تقاطع (المستطيل المرئي المشترك) لـ MediaBox و DropBox. الصورة أدناه توضح هذه الخصائص.
لمزيد من التفاصيل، يرجى زيارة [هذه الصفحة](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

الشفرة التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

الشفرة أدناه توضح كيفية قص الصفحة:

```csharp
public static void CropPagesPDF()
{
    var pdfDocument1 = new Aspose.Pdf.Document("crop_page.pdf");
    Console.WriteLine(pdfDocument1.Pages[1].CropBox);
    Console.WriteLine(pdfDocument1.Pages[1].TrimBox);
    Console.WriteLine(pdfDocument1.Pages[1].ArtBox);
    Console.WriteLine(pdfDocument1.Pages[1].BleedBox);
    Console.WriteLine(pdfDocument1.Pages[1].MediaBox);

    // إنشاء مستطيل صندوق جديد
    var newBox = new Rectangle(200, 220, 2170, 1520);
    pdfDocument1.Pages[1].CropBox = newBox;
    pdfDocument1.Pages[1].TrimBox = newBox;
    pdfDocument1.Pages[1].ArtBox = newBox;
    pdfDocument1.Pages[1].BleedBox = newBox;
   
    pdfDocument1.Save("crop_page_modified.pdf");           
}
```
في هذا المثال استخدمنا ملف نموذجي [هنا](crop_page.pdf). في البداية كانت صفحتنا تبدو كما هو موضح في الشكل 1.
![الشكل 1. صفحة مقصوصة](crop_page.png)

بعد التغيير، ستبدو الصفحة كما في الشكل 2.
![الشكل 2. صفحة مقصوصة](crop_page2.png)

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
    "applicationCategory": "مكتبة تعديل ملفات PDF لـ .NET",
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


