---
title: إضافة كائن خط إلى ملف PDF
linktitle: إضافة خط
type: docs
weight: 40
url: /ar/net/add-line/
description: يشرح هذا المقال كيفية إنشاء كائن خط في ملف PDF الخاص بك باستخدام Aspose.PDF لـ .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "إضافة كائن خط إلى ملف PDF",
    "alternativeHeadline": "كيفية إنشاء كائن خط في ملف PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستند PDF",
    "keywords": "pdf, c#, خط في pdf",
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
    "url": "/net/add-line/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-line/"
    },
    "dateModified": "2022-02-04",
    "description": "يشرح هذا المقال كيفية إنشاء كائن خط في ملف PDF الخاص بك باستخدام Aspose.PDF لـ .NET."
}
</script>
يعمل الكود التالي أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

## إضافة كائن خط

يدعم Aspose.PDF لـ .NET إمكانية إضافة كائنات الرسوم البيانية (على سبيل المثال، الرسم البياني، الخط، المستطيل، إلخ) إلى مستندات PDF. كما أنك تحصل على القدرة لإضافة كائن [الخط](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/line) حيث يمكنك أيضًا تحديد نمط الشرطة، اللون وتنسيقات أخرى لعنصر الخط.

اتبع الخطوات أدناه:

1. قم بإنشاء [مستند](https://reference.aspose.com/pdf/net/aspose.pdf/document) PDF جديد

1. إضافة [صفحة](https://reference.aspose.com/pdf/net/aspose.pdf/page) إلى مجموعة صفحات ملف PDF

1. إنشاء نموذج [رسم بياني](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph).

1. إضافة كائن الرسم البياني إلى مجموعة فقرات صفحة.

1. إنشاء نموذج [مستطيل](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle).

1. تحديد عرض الخط.

changefreq: "monthly"
type: docs
1. احفظ ملف PDF الخاص بك.

الكود التالي يوضح كيفية إضافة كائن [مستطيل](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) مملوء باللون.

```csharp
        public static void AddLineObjectToPDF()
        {
            // إنشاء مثال للوثيقة
            var document = new Document();

            // إضافة صفحة إلى مجموعة الصفحات في ملف PDF
            var page = document.Pages.Add();

            // إنشاء مثال للرسم البياني
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);

            // إضافة كائن الرسم البياني إلى مجموعة الفقرات لمثال الصفحة
            page.Paragraphs.Add(graph);

            // إنشاء مثال للمستطيل
            var line = new Line(new float[] { 100, 100, 200, 100 });

            // تحديد لون التعبئة لكائن الرسم البياني
            line.GraphInfo.DashArray = new int[] { 0, 1, 0 };
            line.GraphInfo.DashPhase = 1;

            // إضافة كائن المستطيل إلى مجموعة الأشكال لكائن الرسم البياني
            graph.Shapes.Add(line);

            // حفظ ملف PDF
            document.Save(_dataDir + "AddLineObject_out.pdf");
        }
```
![Add Line](add_line.png)

## كيفية إضافة خط متقطع بالنقاط إلى مستند PDF الخاص بك

```csharp
        public static void DashLengthInBlackAndDashLengthInWhite()
        {
            // إنشاء مثيل للوثيقة
            var document = new Document();

            // إضافة صفحة إلى مجموعة الصفحات في ملف PDF
            var page = document.Pages.Add();

            // إنشاء كائن الرسم بأبعاد محددة
            var canvas = new Aspose.Pdf.Drawing.Graph(100, 400);
            // إضافة كائن الرسم إلى مجموعة الفقرات لمثيل الصفحة
            page.Paragraphs.Add(canvas);

            // إنشاء كائن الخط
            var line = new Line(new float[] { 100, 100, 200, 100 });
            // تعيين لون لكائن الخط
            line.GraphInfo.Color = Color.Red;
            // تحديد مصفوفة الشطب لكائن الخط
            line.GraphInfo.DashArray = new int[] { 0, 1, 0 };
            // تعيين مرحلة الشطب لكائن الخط
            line.GraphInfo.DashPhase = 1;
            // إضافة الخط إلى مجموعة الأشكال لكائن الرسم
            canvas.Shapes.Add(line);
            // حفظ ملف PDF
            document.Save(_dataDir + "DashLengthInBlackAndDashLengthInWhite_out.pdf");
        }
```
![خط متقطع](dash_line.png)

## رسم خط عبر الصفحة

يمكننا أيضًا استخدام كائن الخط لرسم خط متقاطع يبدأ من الزاوية السفلية اليسرى إلى الزاوية العلوية اليمنى ومن الزاوية العلوية اليسرى إلى الزاوية السفلية اليمنى.

يرجى الاطلاع على الشفرة التالية لتحقيق هذا المطلب.

```csharp
   public static void ExampleLineAcrossPage()
        {

            // إنشاء مثال للمستند
            var document = new Document();

            // إضافة صفحة إلى مجموعة الصفحات في ملف PDF
            var page = document.Pages.Add();
            // تعيين هامش الصفحة على جميع الجوانب كـ 0

            page.PageInfo.Margin.Left = 0;
            page.PageInfo.Margin.Right = 0;
            page.PageInfo.Margin.Bottom = 0;
            page.PageInfo.Margin.Top = 0;

            // إنشاء كائن الرسم بعرض وارتفاع مساويين لأبعاد الصفحة
            var graph = new Aspose.Pdf.Drawing.Graph(
                (float)page.PageInfo.Width,
                (float)page.PageInfo.Height);

            // إنشاء كائن الخط الأول الذي يبدأ من الزاوية السفلية اليسرى إلى الزاوية العلوية اليمنى للصفحة
            var line = new Line(
                    new float[]{
                        (float)page.Rect.LLX, 0,
                        (float)page.PageInfo.Width,
                        (float)page.Rect.URY });

            // إضافة الخط إلى مجموعة الأشكال في كائن الرسم
            graph.Shapes.Add(line);
            // رسم خط من الزاوية العلوية اليسرى للصفحة إلى الزاوية السفلية اليمنى للصفحة
            var line2 = new Line(
                new float[]{ 0,
                    (float) page.Rect.URY,
                    (float) page.PageInfo.Width,
                    (float) page.Rect.LLX });

            // إضافة الخط إلى مجموعة الأشكال في كائن الرسم
            graph.Shapes.Add(line2);

            // إضافة كائن الرسم إلى مجموعة الفقرات في الصفحة
            page.Paragraphs.Add(graph);

            // حفظ ملف PDF
            document.Save(_dataDir + "ExampleLineAcrossPage_out.pdf");
        }
```
![رسم خط](draw_line.png)

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


