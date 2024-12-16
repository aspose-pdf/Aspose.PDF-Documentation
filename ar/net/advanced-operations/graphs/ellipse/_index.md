---
title: إضافة كائن بيضوي إلى ملف PDF
linktitle: إضافة بيضوي
type: docs
weight: 60
url: /ar/net/add-ellipse/
description: يشرح هذا المقال كيفية إنشاء كائن بيضوي في ملف PDF باستخدام Aspose.PDF لـ .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "إضافة كائن بيضوي إلى ملف PDF",
    "alternativeHeadline": "كيفية إنشاء كائن بيضوي في ملف PDF",
    "author": {
        "@type": "Person",
        "name":"أناستازيا هولوب",
        "givenName": "أناستازيا",
        "familyName": "هولوب",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء مستندات PDF",
    "keywords": "pdf, c#, البيضوي في pdf",
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
    "url": "/net/add-ellipse/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-ellipse/"
    },
    "dateModified": "2022-02-04",
    "description": "يشرح هذا المقال كيفية إنشاء كائن بيضوي في ملف PDF باستخدام Aspose.PDF لـ .NET."
}
</script>
الشفرة التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

## إضافة كائن القطع الناقص

Aspose.PDF لـ .NET يدعم إضافة كائنات [القطع الناقص](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/ellipse) إلى مستندات PDF. كما يقدم الميزة لملء كائن القطع الناقص بلون معين.

```csharp
 public static void Ellipse()
        {
            // إنشاء نموذج المستند
            var document = new Document();

            // إضافة صفحة إلى مجموعة الصفحات في ملف PDF
            var page = document.Pages.Add();

            // إنشاء كائن الرسم بأبعاد معينة
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);

            // تعيين حدود لكائن الرسم
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var ellipse1 = new Ellipse(150, 100, 120, 60);
            ellipse1.GraphInfo.Color = Color.GreenYellow;
            ellipse1.Text = new TextFragment("Ellipse");
            graph.Shapes.Add(ellipse1);

            var ellipse2 = new Ellipse(50, 50, 18, 300);
            ellipse2.GraphInfo.Color = Color.DarkRed;

            graph.Shapes.Add(ellipse2);

            // إضافة كائن الرسم إلى مجموعة الفقرات في الصفحة
            page.Paragraphs.Add(graph);

            // حفظ ملف PDF
            document.Save(_dataDir + "DrawingEllipse_out.pdf");

        }
```
![إضافة قطع ناقص](ellipse.png)

## إنشاء كائن قطع ناقص مملوء

الشفرة التالية توضح كيفية إضافة كائن [قطع ناقص](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/ellipse) مملوء باللون.

```csharp
     public static void EllipseFilled()
        {
            // إنشاء نموذج المستند
            var document = new Document();

            // إضافة صفحة إلى مجموعة الصفحات في ملف PDF
            var page = document.Pages.Add();

            // إنشاء كائن الرسم بأبعاد معينة
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);

            // تحديد حدود لكائن الرسم
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var ellipse1 = new Ellipse(100, 100, 120, 180);
            ellipse1.GraphInfo.FillColor = Color.GreenYellow;
            graph.Shapes.Add(ellipse1);

            var ellipse2 = new Ellipse(200, 150, 180, 120);
            ellipse2.GraphInfo.FillColor = Color.DarkRed;
            graph.Shapes.Add(ellipse2);

            // إضافة كائن الرسم إلى مجموعة الفقرات في الصفحة
            page.Paragraphs.Add(graph);

            // حفظ ملف PDF
            document.Save(_dataDir + "DrawingEllipse_out.pdf");
        }
```
![Filled Ellipse](fill_ellipse.png)

## إضافة نص داخل الشكل البيضاوي

يدعم Aspose.PDF لـ .NET إضافة نص داخل كائن الرسم. خاصية النص لكائن الرسم توفر خيار لتعيين نص كائن الرسم. يوضح الجزء التالي من الكود كيفية إضافة نص داخل كائن مستطيل.

```csharp
        public static void EllipseWithText()
        {
            // إنشاء نموذج للمستند
            var document = new Document();

            // إضافة صفحة إلى مجموعة الصفحات في ملف PDF
            var page = document.Pages.Add();

            // إنشاء كائن الرسم بأبعاد معينة
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // تعيين حدود لكائن الرسم
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var textFragment = new TextFragment("Ellipse");
            textFragment.TextState.Font = FontRepository.FindFont("Helvetica");
            textFragment.TextState.FontSize = 24;

            var ellipse1 = new Ellipse(100, 100, 120, 180);
            ellipse1.GraphInfo.FillColor = Color.GreenYellow;
            ellipse1.Text = textFragment;
            graph.Shapes.Add(ellipse1);


            var ellipse2 = new Ellipse(200, 150, 180, 120);
            ellipse2.GraphInfo.FillColor = Color.DarkRed;
            ellipse2.Text = textFragment;
            graph.Shapes.Add(ellipse2);

            // إضافة كائن الرسم إلى مجموعة الفقرات في الصفحة
            page.Paragraphs.Add(graph);

            // حفظ ملف PDF
            document.Save(_dataDir + "DrawingEllipseText_out.pdf");

        }
 ```
![نص داخل القطع الناقص](text_ellipse.png)

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
    "applicationCategory": "مكتبة تعديل PDF لـ .NET",
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

