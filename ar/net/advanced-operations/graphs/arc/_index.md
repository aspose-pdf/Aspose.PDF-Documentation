---
title: إضافة كائن قوس إلى ملف PDF
linktitle: إضافة قوس
type: docs
weight: 10
url: /ar/net/add-arc/
description: هذا المقال يشرح كيفية إنشاء كائن قوس في ملف PDF باستخدام Aspose.PDF لـ .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "إضافة كائن قوس إلى ملف PDF",
    "alternativeHeadline": "كيفية إنشاء قوس في ملف PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء مستند PDF",
    "keywords": "pdf, c#, قوس في pdf",
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
    "url": "/net/add-arc/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-arc/"
    },
    "dateModified": "2022-02-04",
    "description": "هذا المقال يشرح كيفية إنشاء كائن قوس في ملف PDF باستخدام Aspose.PDF لـ .NET."
}
</script>
الشفرة التالية تعمل أيضاً مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

## إضافة كائن قوس

Aspose.PDF لـ .NET يدعم إضافة كائنات الرسوم (مثل الرسم البياني، الخط، المستطيل وغيرها) إلى مستندات PDF. كما يقدم الميزة لملء كائن القوس بلون معين.

اتبع الخطوات التالية:

1. إنشاء نموذج [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)

1. إنشاء [كائن الرسم](https://reference.aspose.com/pdf/net/aspose.pdf.drawing) بأبعاد معينة

1. تعيين [الحدود](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border) لكائن الرسم

1. إضافة كائن [الرسم البياني](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) إلى مجموعة الفقرات للصفحة

1. حفظ ملف PDF الخاص بنا

الشفرة التالية تظهر كيفية إضافة كائن [قوس](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/arc).

```csharp
 public static void Arc()
        {
            // إنشاء نموذج Document
            var document = new Document();

            // إضافة صفحة إلى مجموعة الصفحات لملف PDF
            var page = document.Pages.Add();

            // إنشاء كائن الرسم بأبعاد معينة
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // تعيين الحدود لكائن الرسم
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var arc1 = new Arc(100, 100, 95, 0, 90);
            arc1.GraphInfo.Color = Color.GreenYellow;
            graph.Shapes.Add(arc1);

            var arc2 = new Arc(100, 100, 90, 70, 180);
            arc2.GraphInfo.Color = Color.DarkBlue;
            graph.Shapes.Add(arc2);

            var arc3 = new Arc(100, 100, 85, 120, 210);
            arc3.GraphInfo.Color = Color.Red;
            graph.Shapes.Add(arc3);

            // إضافة كائن الرسم البياني إلى مجموعة الفقرات للصفحة
            page.Paragraphs.Add(graph);

            // حفظ ملف PDF
            document.Save(_dataDir + "DrawingArc_out.pdf");

        }
```
## إنشاء كائن قوس مملوء

المثال التالي يُظهر كيفية إضافة كائن قوس مملوء باللون وبأبعاد معينة.

```csharp
        public static void ArcFilled()
        {
            // إنشاء نموذج للمستند
            var document = new Document();

            // إضافة صفحة إلى مجموعة الصفحات في ملف PDF
            var page = document.Pages.Add();

            // إنشاء كائن رسم بأبعاد معينة
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // تعيين حدود لكائن الرسم
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var arc = new Arc(100, 100, 95, 0, 90);
            arc.GraphInfo.FillColor = Color.GreenYellow;
            graph.Shapes.Add(arc);

            var line = new Line(new float[] { 195, 100, 100, 100, 100, 195 });
            line.GraphInfo.FillColor = Color.GreenYellow;
            graph.Shapes.Add(line);

            // إضافة كائن الرسم إلى مجموعة الفقرات في الصفحة
            page.Paragraphs.Add(graph);

            // حفظ ملف PDF
            document.Save(_dataDir + "ExampleFilledArc_out.pdf");

        }
```
لنرى نتيجة إضافة قوس مملوء:

![Filled Arc](filled_arc.png)

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
                "availableLanguage": "الإنجليزية"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "مبيعات",
                "areaServed": "GB",
                "availableLanguage": "الإنجليزية"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "مبيعات",
                "areaServed": "AU",
                "availableLanguage": "الإنجليزية"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "مكتبة تحرير PDF لـ .NET",
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


