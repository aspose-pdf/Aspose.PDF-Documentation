---
title: تعليقات إضافية باستخدام C#
linktitle: تعليقات إضافية
type: docs
weight: 60
url: /net/extra-annotations/
description: تصف هذه القسم كيفية إضافة والحصول على وحذف أنواع إضافية من التعليقات التوضيحية من وثيقة PDF الخاصة بك.
lastmod: "2023-09-12"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "تعليقات إضافية باستخدام C#",
    "alternativeHeadline": "كيفية إضافة تعليقات إضافية في PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء وثيقة PDF",
    "keywords": "pdf, c#, تعليق توضيحي بالرابط, تعليق توضيحي بالعناية",
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
    "url": "/net/extra-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extra-annotations/"
    },
    "dateModified": "2022-02-04",
    "description": "تصف هذه القسم كيفية إضافة والحصول على وحذف أنواع إضافية من التعليقات التوضيحية من وثيقة PDF الخاصة بك."
}
</script>
## كيفية إضافة تعليق توضيحي لعلامة الإدخال في ملف PDF موجود

علامة الإدخال هي رمز يشير إلى تحرير النص. علامة الإدخال هي أيضًا تعليق توضيحي للتمييز، لذلك تنبع الفئة Caret من الفئة Markup وتوفر أيضًا وظائف للحصول على خصائص علامة الإدخال أو تعيينها وإعادة تعيين تدفق مظهر علامة الإدخال.

يعمل الكود التالي أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

خطوات إنشاء التعليق التوضيحي لعلامة الإدخال:

1. تحميل ملف PDF - جديد [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. إنشاء [Caret Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/caretannotation) جديد وتعيين معايير علامة الإدخال (Rectangle جديد، العنوان، الموضوع، الأعلام، اللون، العرض، أسلوب البداية وأسلوب النهاية). يُستخدم هذا التعليق التوضيحي للإشارة إلى إدخال النص.
1. قم بإنشاء [StrikeOutAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/strikeoutannotation) جديد واضبط الإعدادات (مستطيل جديد، العنوان، اللون، نقاط QuadPoints جديدة ونقاط جديدة، الموضوع، InReplyTo، ReplyType).
1. بعد ذلك يمكننا إضافة التعليقات التوضيحية إلى الصفحة.

يوضح مقتطف الكود التالي كيفية إضافة تعليق توضيحي Caret إلى ملف PDF:
```csharp
using Aspose.Pdf.Annotations;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleCaretAnnotation
    {
        // مسار الدليل الخاص بالمستندات.
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        public static void AddCaretAnnotation()
        {
            // تحميل ملف PDF
            Document document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
            // يُستخدم هذا التعليق التوضيحي للإشارة إلى إدخال النص
            var caretAnnotation1 = new CaretAnnotation(document.Pages[1], new Rectangle(299.988, 713.664, 308.708, 720.769))
            {
                Title = "مستخدم Aspose",
                Subject = "نص مدخل 1",
                Flags = AnnotationFlags.Print,
                Color = Color.Blue
            };
            // يُستخدم هذا التعليق التوضيحي للإشارة إلى استبدال النص
            var caretAnnotation2 = new CaretAnnotation(document.Pages[1], new Rectangle(361.246, 727.908, 370.081, 735.107))
            {
                Flags = AnnotationFlags.Print,
                Subject = "نص مدخل 2",
                Title = "مستخدم Aspose",
                Color = Color.Blue
            };

            var strikeOutAnnotation = new StrikeOutAnnotation(document.Pages[1],
                new Rectangle(318.407, 727.826, 368.916, 740.098))
            {
                Color = Color.Blue,
                QuadPoints = new[] {
                new Point(321.66, 739.416),
                new Point(365.664, 739.416),
                new Point(321.66, 728.508),
                new Point(365.664, 728.508)
            },
                Subject = "شطب",
                InReplyTo = caretAnnotation2,
                ReplyType = ReplyType.Group
            };

            document.Pages[1].Annotations.Add(caretAnnotation1);
            document.Pages[1].Annotations.Add(caretAnnotation2);
            document.Pages[1].Annotations.Add(strikeOutAnnotation);

            document.Save(System.IO.Path.Combine(_dataDir, "sample_caret.pdf"));
        }
```
### الحصول على تعليق التأشير

الرجاء محاولة استخدام مقتطف الكود التالي للحصول على تعليق التأشير في مستند PDF

```csharp
public static void GetCaretAnnotation()
{
    // تحميل ملف PDF
    Document document = new Document(System.IO.Path.Combine(_dataDir, "sample_caret.pdf"));
    var caretAnnotations = document.Pages[1].Annotations
        .Where(a => a.AnnotationType == AnnotationType.Caret)
        .Cast<CaretAnnotation>();
    foreach (var ca in caretAnnotations)
    {
        Console.WriteLine($"{ca.Rect}");
    }
}
```

### حذف تعليق التأشير

يظهر مقتطف الكود التالي كيفية حذف تعليق التأشير من ملف PDF.

```csharp
public static void DeleteCaretAnnotation()
{
    // تحميل ملف PDF
    Document document = new Document(System.IO.Path.Combine(_dataDir, "sample_caret.pdf"));
    var caretAnnotations = document.Pages[1].Annotations
        .Where(a => a.AnnotationType == AnnotationType.Caret)
        .Cast<CaretAnnotation>();

    foreach (var ca in caretAnnotations)
    {
        document.Pages[1].Annotations.Delete(ca);
    }
    document.Save(System.IO.Path.Combine(_dataDir, "sample_caret_del.pdf"));
}
```
## حذف منطقة معينة من الصفحة باستخدام تعليق توضيحي للحذف في Aspose.PDF لـ .NET

Aspose.PDF لـ .NET يدعم ميزة إضافة والتManipulate Annotations في ملف PDF موجود. مؤخراً، نشر بعض عملائنا طلبًا لحذف (إزالة النص، الصورة، إلخ من) منطقة معينة من صفحة وثيقة PDF. لتلبية هذا المطلب، توفر فئة تسمى RedactionAnnotation، والتي يمكن استخدامها لحذف مناطق معينة من الصفحة أو يمكن استخدامها لManipulate Annotations الحذف الموجودة وحذفها (أي تسطيح التعليق التوضيحي وإزالة النص تحته).

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// فتح المستند
Document doc = new Document(dataDir + "input.pdf");

// إنشاء مثيل RedactionAnnotation لمنطقة صفحة معينة
RedactionAnnotation annot = new RedactionAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(200, 500, 300, 600));
annot.FillColor = Aspose.Pdf.Color.Green;
annot.BorderColor = Aspose.Pdf.Color.Yellow;
annot.Color = Aspose.Pdf.Color.Blue;
// النص المطبوع على التعليق التوضيحي للحذف
annot.OverlayText = "REDACTED";
annot.TextAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// تكرار النص التغطي على التعليق التوضيحي للحذف
annot.Repeat = true;
// إضافة التعليق التوضيحي إلى مجموعة التعليقات التوضيحية للصفحة الأولى
doc.Pages[1].Annotations.Add(annot);
// تسطيح التعليق التوضيحي وحذف محتويات الصفحة (أي إزالة النص والصورة
// تحت التعليق التوضيحي المحذوف)
annot.Redact();
dataDir = dataDir + "RedactPage_out.pdf";
doc.Save(dataDir);
```
### نهج الواجهات

مساحة الاسم Aspose.PDF.Facades تحتوي أيضًا على فئة تُسمى [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) التي توفر ميزة التعامل مع التعليقات التوضيحية الموجودة داخل ملف PDF. تحتوي هذه الفئة على طريقة تُسمى [RedactArea(..)](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/redactarea) التي توفر القدرة على إزالة مناطق معينة من الصفحة.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

Aspose.Pdf.Facades.PdfAnnotationEditor editor = new Aspose.Pdf.Facades.PdfAnnotationEditor();
// إخفاء منطقة معينة من الصفحة
editor.RedactArea(1, new Aspose.Pdf.Rectangle(100, 100, 20, 70), System.Drawing.Color.White);
editor.BindPdf(dataDir + "input.pdf");
editor.Save(dataDir + "FacadesApproach_out.pdf");
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
                "contactType": "المبيعات",
                "areaServed": "الولايات المتحدة",
                "availableLanguage": "الإنجليزية"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "المبيعات",
                "areaServed": "بريطانيا العظمى",
                "availableLanguage": "الإنجليزية"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "المبيعات",
                "areaServed": "أستراليا",
                "availableLanguage": "الإنجليزية"
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
```

