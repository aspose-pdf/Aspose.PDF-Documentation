---
title: إضافة كائن منحنى إلى ملف PDF
linktitle: إضافة منحنى
type: docs
weight: 30
url: /net/add-curve/
description: يشرح هذا المقال كيفية إنشاء كائن منحنى لملف PDF الخاص بك باستخدام Aspose.PDF لـ .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "إضافة كائن منحنى إلى ملف PDF",
    "alternativeHeadline": "كيفية إنشاء كائن منحنى في ملف PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء مستند PDF",
    "keywords": "pdf, .net, منحنى في pdf",
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
    "url": "/net/add-curve/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-curve/"
    },
    "dateModified": "2022-02-04",
    "description": "يشرح هذا المقال كيفية إنشاء كائن منحنى لملف PDF الخاص بك باستخدام Aspose.PDF لـ .NET."
}
</script>

الرمز التالي يعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

## إضافة كائن منحنى

يُعد الرسم البياني [Curve](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/curve) اتحادًا متصلاً لخطوط المشروع، حيث يلتقي كل خط بثلاثة خطوط أخرى في نقاط مزدوجة عادية.

يوضح Aspose.PDF لـ .NET كيفية استخدام منحنيات بيزييه في رسوماتك.
تُستخدم منحنيات بيزييه على نطاق واسع في الرسوميات الحاسوبية لنمذجة المنحنيات الناعمة. يكون المنحنى محتوىً بالكامل داخل الغلاف المحدب لنقاط التحكم الخاصة به، يمكن عرض النقاط بصريًا واستخدامها للتلاعب بالمنحنى بشكل حدسي.
يحتوي المنحنى بأكمله داخل المربع الذي تكون زواياه الأربع نقاط المعطاة (غلافها المحدب).

في هذه المقالة، سنستكشف ببساطة منحنيات الرسوم البيانية، والمنحنيات المملوءة، التي يمكنك إنشاؤها في مستند PDF الخاص بك.

اتبع الخطوات أدناه:

1. إنشاء نموذج [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 

1.
1. ضبط [الحدود](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border) لكائن الرسم

1. إضافة كائن [الرسم البياني](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) إلى مجموعة فقرات الصفحة

1. حفظ ملف PDF لدينا

```csharp
 public static void ExampleCurve()
        {
            // إنشاء نموذج المستند
            var document = new Document();

            // إضافة صفحة إلى مجموعة الصفحات في ملف PDF
            var page = document.Pages.Add();

            // إنشاء كائن الرسم بأبعاد محددة
            var graph = new Aspose.Pdf.Drawing.Graph(400, 200);

            // ضبط الحدود لكائن الرسم
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120 });
            curve1.GraphInfo.Color = Color.GreenYellow;
            graph.Shapes.Add(curve1);

            // إضافة كائن الرسم البياني إلى مجموعة الفقرات في الصفحة
            page.Paragraphs.Add(graph);

            // حفظ ملف PDF
            document.Save(_dataDir + "DrawingCurve1_out.pdf");
        }
```
الصورة التالية تظهر النتيجة بعد تنفيذها باستخدام شفرة البرنامج لدينا:

![رسم منحنى](drawing_curve.png)

## إنشاء كائن منحنى مملوء

هذا المثال يوضح كيفية إضافة كائن منحنى مملوء باللون.

```csharp
      public static void CurveFilled()
        {
            // إنشاء نموذج وثيقة
            var document = new Document();

            // إضافة صفحة إلى مجموعة الصفحات في ملف PDF
            var page = document.Pages.Add();

            // إنشاء كائن رسم بأبعاد محددة
            var graph = new Aspose.Pdf.Drawing.Graph(400, 200);

            // تحديد الحدود لكائن الرسم
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120 });
            curve1.GraphInfo.FillColor = Color.GreenYellow;
            graph.Shapes.Add(curve1);

            // إضافة كائن الرسم إلى مجموعة الفقرات في الصفحة
            page.Paragraphs.Add(graph);

            // حفظ ملف PDF
            document.Save(_dataDir + "DrawingCurve2_out.pdf");
        }
```
انظر إلى نتيجة إضافة منحنى مملوء:

![منحنى مملوء](filled_curve.png)

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

