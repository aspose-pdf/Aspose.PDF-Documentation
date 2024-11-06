---
title: إضافة كائن مستطيل إلى ملف PDF
linktitle: إضافة مستطيل
type: docs
weight: 50
url: ar/net/add-rectangle/
description: يشرح هذا المقال كيفية إنشاء كائن مستطيل في ملف PDF باستخدام Aspose.PDF لـ .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "إضافة كائن مستطيل إلى ملف PDF",
    "alternativeHeadline": "كيفية إنشاء كائن مستطيل في ملف PDF",
    "author": {
        "@type": "Person",
        "name":"أناستازيا هولوب",
        "givenName": "أناستازيا",
        "familyName": "هولوب",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستند PDF",
    "keywords": "pdf, c#, مستطيل في pdf",
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
    "url": "/net/add-rectangle/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-rectangle/"
    },
    "dateModified": "2022-02-04",
    "description": "يشرح هذا المقال كيفية إنشاء كائن مستطيل في ملف PDF باستخدام Aspose.PDF لـ .NET."
}
</script>
الشفرة التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

## إضافة كائن مستطيل

Aspose.PDF لـ .NET يدعم ميزة إضافة كائنات الرسم البياني (على سبيل المثال، الرسم البياني، الخط، المستطيل، وغيرها) إلى مستندات PDF. كما تحصل على ميزة إضافة كائن [المستطيل](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) حيث يُقدم أيضًا إمكانية ملء كائن المستطيل بلون معين، التحكم في ترتيب Z، إضافة ملء لون متدرج، وغير ذلك.

أولًا، دعونا ننظر في إمكانية إنشاء كائن المستطيل.

اتبع الخطوات أدناه:

1. إنشاء [مستند](https://reference.aspose.com/pdf/net/aspose.pdf/document) PDF جديد

1. إضافة [صفحة](https://reference.aspose.com/pdf/net/aspose.pdf/page) إلى مجموعة الصفحات لملف PDF

1. إضافة [جزء نصي](https://reference.aspose.com/pdf/net/aspose.pdf/texfragment) إلى مجموعة الفقرات لمثيل الصفحة

1. إنشاء مثيل [الرسم البياني](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph)
1. إنشاء نموذج مستطيل
1. إضافة كائن [مستطيل](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) إلى مجموعة الأشكال في كائن الرسم
1. إضافة كائن الرسم إلى مجموعة الفقرات في نموذج الصفحة
1. إضافة [جزء نصي](https://reference.aspose.com/pdf/net/aspose.pdf/texfragment) إلى مجموعة الفقرات في نموذج الصفحة
1. واحفظ ملف PDF الخاص بك

```csharp
 private static void AddRectangle(Page page, float x, float y, float width, float height, Color color, int zindex)
        {
            // إنشاء كائن رسم بنفس الأبعاد المحددة لكائن المستطيل
            Aspose.Pdf.Drawing.Graph graph = new Aspose.Pdf.Drawing.Graph(width, height)
            {
                // هل يمكننا تغيير موقع نموذج الرسم
                IsChangePosition = false,
                // تعيين موقع الإحداثية اليسرى لنموذج الرسم
                Left = x,
                // تعيين موقع الإحداثية العلوية لكائن الرسم
                Top = y
            };
            // إضافة مستطيل داخل "الرسم"
            Rectangle rect = new Rectangle(0, 0, width, height);
            // تعيين لون ملء المستطيل
            rect.GraphInfo.FillColor = color;
            // لون كائن الرسم
            rect.GraphInfo.Color = color;
            // إضافة المستطيل إلى مجموعة الأشكال في نموذج الرسم
            graph.Shapes.Add(rect);
            // تعيين مؤشر زي لكائن المستطيل
            graph.ZIndex = zindex;
            // إضافة الرسم إلى مجموعة الفقرات في نموذج الصفحة
            page.Paragraphs.Add(graph);
        }
```
![إنشاء مستطيل](create_rectangle.png)

## إنشاء كائن مستطيل مملوء

Aspose.PDF لـ .NET يوفر أيضًا ميزة ملء كائن المستطيل بلون معين.

يوضح الجزء التالي من الكود كيفية إضافة كائن [المستطيل](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) المملوء باللون.

```csharp
    {
        private const string _dataDir = "C:\\Samples\\";
        public static void RectangleFilled()
        {
            // إنشاء نموذج Document
            var doc = new Document();

            // إضافة صفحة إلى مجموعة الصفحات في ملف PDF
            var page = doc.Pages.Add();
            // إنشاء نموذج Graph
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);

            // إضافة كائن الرسم البياني إلى مجموعة الفقرات لنموذج الصفحة
            page.Paragraphs.Add(graph);

            // إنشاء نموذج مستطيل
            var rect = new Rectangle(100, 100, 200, 120);

            // تحديد لون التعبئة لكائن الرسم البياني
            rect.GraphInfo.FillColor = Color.Red;

            // إضافة كائن المستطيل إلى مجموعة الأشكال لكائن الرسم البياني
            graph.Shapes.Add(rect);

            // حفظ ملف PDF
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```
انظر إلى نتيجة المستطيل المملوء بلون صلب:

![مستطيل مملوء](fill_rectangle.png)

## إضافة رسم بتعبئة التدرج

يدعم Aspose.PDF لـ .NET ميزة إضافة كائنات الرسم البياني إلى مستندات PDF وأحيانًا يُطلب تعبئة كائنات الرسم البياني بلون التدرج. لتعبئة كائنات الرسم البياني بلون التدرج، نحتاج إلى تعيين setPatterColorSpace بكائن gradientAxialShading كالتالي.

يوضح الشفرة التالية كيفية إضافة كائن [مستطيل](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) مملوء بلون التدرج.

```csharp
 public static void CreateFilledRectangletGradientFill()
        {
            // إنشاء نموذج للمستند
            var doc = new Document();

            // إضافة صفحة إلى مجموعة صفحات ملف PDF
            var page = doc.Pages.Add();
            // إنشاء نموذج للرسم البياني
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // إضافة كائن الرسم البياني إلى مجموعة الفقرات لنموذج الصفحة
            page.Paragraphs.Add(graph);
            // إنشاء نموذج للمستطيل
            var rect = new Rectangle(0, 0, 300, 300);
            // تحديد لون التعبئة لكائن الرسم البياني
            var gradientColor = new Color();
            var gradientSettings = new GradientAxialShading(Color.Red, Color.Blue)
            {
                Start = new Point(0, 0),
                End = new Point(350, 350)
            };
            gradientColor.PatternColorSpace = gradientSettings;
            rect.GraphInfo.FillColor = gradientColor;

            // إضافة كائن المستطيل إلى مجموعة الأشكال لكائن الرسم البياني
            graph.Shapes.Add(rect);

            // حفظ ملف PDF
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```
![مستطيل تدرج](gradient.png)

## إنشاء مستطيل بقناة ألوان ألفا

Aspose.PDF لـ .NET يدعم ملء كائن المستطيل بلون معين. يمكن أيضًا أن يحتوي كائن المستطيل على قناة ألوان ألفا لإعطاء مظهر شفاف. يوضح الجزء التالي من الكود كيفية إضافة كائن [مستطيل](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) مع قناة ألوان ألفا.

يمكن لبيكسلات الصورة تخزين معلومات حول شفافيتها إلى جانب قيمة اللون. يتيح ذلك إنشاء صور بمناطق شفافة أو شبه شفافة.

بدلاً من جعل اللون شفافًا، يخزن كل بيكسل معلومات عن مدى عتامته. يُسمى هذا البيانات العتامة بقناة ألفا وعادةً ما تُخزن بعد قنوات الألوان للبيكسل.

```csharp
     public static void RectangleFilled_AlphaChannel()
        {
            // إنشاء مثيل للوثيقة
            var doc = new Document();

            // إضافة صفحة إلى مجموعة الصفحات في ملف PDF
            var page = doc.Pages.Add();
            // إنشاء مثيل للرسم
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);
            // إضافة كائن الرسم إلى مجموعة الفقرات لمثيل الصفحة
            page.Paragraphs.Add(graph);
            // إنشاء مثيل المستطيل
            var rect = new Rectangle(100, 100, 200, 120);
            // تحديد لون التعبئة لكائن الرسم
            rect.GraphInfo.FillColor = Color.FromArgb(128, 244, 180, 0);

            // إضافة كائن المستطيل إلى مجموعة الأشكال لكائن الرسم
            graph.Shapes.Add(rect);

            // إنشاء كائن مستطيل ثاني
            var rect1 = new Rectangle(200, 150, 200, 100);
            rect1.GraphInfo.FillColor = Color.FromArgb(160, 120, 0, 120);
            graph.Shapes.Add(rect1);

            // إضافة مثيل الرسم إلى مجموعة الفقرات للصفحة
            page.Paragraphs.Add(graph);

            // حفظ ملف PDF
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```
![Rectangle Alpha Channel Color](rectangle_color.png)

## التحكم في ترتيب Z للمستطيل

Aspose.PDF لـ .NET يدعم الخاصية لإضافة كائنات الرسوم (على سبيل المثال الرسم البياني، الخط، المستطيل إلخ.) إلى مستندات PDF. عند إضافة أكثر من نسخة من نفس الكائن داخل ملف PDF، يمكننا التحكم في تقديمها من خلال تحديد ترتيب Z. يُستخدم ترتيب Z أيضًا عندما نحتاج إلى تقديم الكائنات فوق بعضها البعض.

يظهر المقتطف الكودي التالي الخطوات لتقديم كائنات [المستطيل](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) فوق بعضها البعض.

```csharp
 public static void AddRectangleZOrder()
        {
            // إنشاء كائن من فئة الوثيقة
            Document doc1 = new Document();
            /// إضافة صفحة إلى مجموعة صفحات ملف PDF
            Page page1 = doc1.Pages.Add();
            // تعيين حجم صفحة PDF
            page1.SetPageSize(375, 300);
            // تعيين هامش اليسار لكائن الصفحة كـ 0
            page1.PageInfo.Margin.Left = 0;
            // تعيين هامش الأعلى لكائن الصفحة كـ 0
            page1.PageInfo.Margin.Top = 0;
            // إنشاء مستطيل جديد باللون الأحمر، ترتيب Z كـ 0 وأبعاد معينة
            AddRectangle(page1, 50, 40, 60, 40, Color.Red, 2);
            // إنشاء مستطيل جديد باللون الأزرق، ترتيب Z كـ 0 وأبعاد معينة
            AddRectangle(page1, 20, 20, 30, 30, Color.Blue, 1);
            // إنشاء مستطيل جديد باللون الأخضر، ترتيب Z كـ 0 وأبعاد معينة
            AddRectangle(page1, 40, 40, 60, 30, Color.Green, 0);
            // حفظ الملف الناتج من PDF
            doc1.Save(_dataDir + "ControlRectangleZOrder_out.pdf");
        }
```
![التحكم في ترتيب Z](control.png)

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


