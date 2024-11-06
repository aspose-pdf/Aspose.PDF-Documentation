---
title: إضافة كائن دائري إلى ملف PDF
linktitle: إضافة دائرة
type: docs
weight: 20
url: ar/net/add-circle/
description: يشرح هذا المقال كيفية إنشاء كائن دائري في ملف PDF الخاص بك باستخدام Aspose.PDF لـ .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "إضافة كائن دائري إلى ملف PDF",
    "alternativeHeadline": "كيفية إنشاء كائن دائري في ملف PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء مستند PDF",
    "keywords": "pdf, c#, دائرة في pdf",
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
                "contactType": "المبيعات",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "المبيعات",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "المبيعات",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/add-circle/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-circle/"
    },
    "dateModified": "2022-02-04",
    "description": "يشرح هذا المقال كيفية إنشاء كائن دائري في ملف PDF الخاص بك باستخدام Aspose.PDF لـ .NET."
}
</script>

الشفرة التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

## إضافة كائن دائرة

مثل الرسوم البيانية الشريطية، يمكن استخدام الرسوم البيانية الدائرية لعرض البيانات في عدد من الفئات المنفصلة. على عكس الرسوم البيانية الشريطية، ومع ذلك، يمكن استخدام الرسوم البيانية الدائرية فقط عندما يكون لديك بيانات لجميع الفئات التي تشكل الكل. لذلك دعونا نلقي نظرة على إضافة كائن [دائرة](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/circle) مع Aspose.PDF لـ .NET.

اتبع الخطوات أدناه:

1. إنشاء نموذج [وثيقة](https://reference.aspose.com/pdf/net/aspose.pdf/document)

1. إنشاء [كائن رسم](https://reference.aspose.com/pdf/net/aspose.pdf.drawing) بأبعاد معينة

1. تعيين [حد](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border) لكائن الرسم

1. إضافة كائن [رسم](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) إلى مجموعة الفقرات للصفحة

1. حفظ ملف PDF الخاص بنا

```csharp
        public static void Circle()
        {
            // إنشاء نموذج وثيقة
            var document = new Document();

            // إضافة صفحة إلى مجموعة الصفحات لملف PDF
            var page = document.Pages.Add();

            // إنشاء كائن رسم بأبعاد معينة
            var graph = new Aspose.Pdf.Drawing.Graph(400, 200);
            // تعيين حد لكائن الرسم
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var circle = new Circle(100, 100, 40);

            circle.GraphInfo.Color = Color.GreenYellow;
            graph.Shapes.Add(circle);

            // إضافة كائن الرسم إلى مجموعة الفقرات للصفحة
            page.Paragraphs.Add(graph);

            // حفظ ملف PDF
            document.Save(_dataDir + "DrawingCircle1_out.pdf");
        }
```
سيبدو الدائرة المرسومة لدينا كما يلي:

![رسم دائرة](drawing_circle.png)

## إنشاء كائن دائرة مملوء

هذا المثال يوضح كيفية إضافة كائن دائرة مملوء باللون.

```csharp
        public static void CircleFilled()
        {
            // إنشاء نموذج للمستند
            var document = new Document();

            // إضافة صفحة إلى مجموعة الصفحات في ملف PDF
            var page = document.Pages.Add();

            // إنشاء كائن رسم بأبعاد معينة
            var graph = new Aspose.Pdf.Drawing.Graph(400, 200);

            // تعيين حدود لكائن الرسم
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var circle = new Circle(100, 100, 40);
            circle.GraphInfo.Color = Color.GreenYellow;
            circle.GraphInfo.FillColor = Color.Green;
            circle.Text = new TextFragment("Circle");

            graph.Shapes.Add(circle);

            // إضافة كائن الرسم إلى مجموعة الفقرات في الصفحة
            page.Paragraphs.Add(graph);

            // حفظ ملف PDF
            document.Save(_dataDir + "DrawingCircle2_out.pdf");
        }
```
لنرى نتيجة إضافة دائرة ممتلئة:

![دائرة ممتلئة](filled_circle.png)

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

