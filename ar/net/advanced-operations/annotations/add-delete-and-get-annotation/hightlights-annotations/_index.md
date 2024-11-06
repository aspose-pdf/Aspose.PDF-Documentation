---
title: تعليقات التمييز بالألوان باستخدام C#
linktitle: تعليق التمييز
type: docs
weight: 20
url: ar/net/highlights-annotation/
description: تُقدم تعليقات التوضيح في النص على شكل تمييزات، تحت خطوط، خطوط مشطوبة، أو خطوط متعرجة في نص الوثيقة.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "تعليقات التمييز بالألوان باستخدام C#",
    "alternativeHeadline": "كيفية إضافة تعليق التمييز في PDF",
    "author": {
        "@type": "Person",
        "name":"أناستاسيا هولوب",
        "givenName": "أناستاسيا",
        "familyName": "هولوب",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد وثيقة PDF",
    "keywords": "pdf, c#, تعليقات التمييز, تعليقات توضيح النص",
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
    "url": "/net/highlights-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/highlights-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "تُقدم تعليقات التوضيح في النص على شكل تمييزات، تحت خطوط، خطوط مشطوبة، أو خطوط متعرجة في نص الوثيقة."
}
</script>

تظهر تعليقات توضيح تنسيق النص كتمييزات، خطوط تحتية، خطوط مشطوبة، أو خطوط تحتية متعرجة في نص المستند. عند فتحها، يجب أن تعرض نافذة منبثقة تحتوي على نص الملاحظة المرتبطة.

يمكن تعديل خصائص تعليقات توضيح تنسيق النص في مستند PDF باستخدام نافذة الخصائص المتوفرة في عنصر تحكم عارض PDF. يمكن تعديل لون، شفافية، مؤلف، وموضوع تعليق توضيح النص.

من الممكن الحصول على أو تعيين إعدادات تعليقات التمييز باستخدام خاصية highlightSettings. تستخدم خاصية highlightSettings لتعيين اللون، الشفافية، المؤلف، الموضوع، تاريخ التعديل وخصائص isLocked لتعليقات التمييز.

من الممكن أيضًا الحصول على أو تعيين إعدادات تعليقات الخط المشطوب باستخدام خاصية strikethroughSettings. تستخدم خاصية strikethroughSettings لتعيين اللون، الشفافية، المؤلف، الموضوع، تاريخ التعديل، وخصائص isLocked لتعليقات الخط المشطوب.

الميزة التالية هي القدرة على الحصول على أو تعيين إعدادات تعليقات الخط السفلي باستخدام خاصية underlineSettings.
الميزة التالية هي القدرة على الحصول على إعدادات أو تعيين إعدادات التسطير باستخدام خاصية underlineSettings.

يعمل مقتطف الكود التالي أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

## إضافة توضيح نصي للعلامات

لإضافة توضيح نصي للعلامات إلى مستند PDF، نحتاج إلى أداء الإجراءات التالية:

1. تحميل ملف PDF - كائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) جديد.
1. إنشاء التعليقات التوضيحية:
    - [HighlightAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/highlightannotation) وتعيين المعايير (العنوان، اللون).
    - [StrikeOutAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/strikeoutannotation) وتعيين المعايير (العنوان، اللون).
    - [SquigglyAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/squigglyannotation) وتعيين المعايير (العنوان، اللون).
    - [UnderlineAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/underlineannotation) وتعيين المعايير (العنوان، اللون).
- [تحت خط](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/underlineannotation) وقم بتعيين الخصائص (العنوان، اللون).
1. بعد ذلك يجب إضافة جميع التعليقات التوضيحية إلى الصفحة.

```csharp
using Aspose.Pdf.Annotations;
using Aspose.Pdf.Text;
using System;
using System.Linq;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleTextMarkupAnnotation
    {
        // المسار إلى مجلد الوثائق.
        private const string _dataDir = "..\\..\\..\\..\\Samples";

        public static void AddTextMarkupAnnotation()
        {
            try
            {
                // تحميل ملف PDF
                Document document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
                var tfa = new Aspose.Pdf.Text.TextFragmentAbsorber("PDF");
                tfa.Visit(document.Pages[1]);

                // إنشاء التعليقات التوضيحية
                HighlightAnnotation highlightAnnotation = new HighlightAnnotation(document.Pages[1],
                   tfa.TextFragments[1].Rectangle )
                {
                    Title = "مستخدم Aspose",
                    Color = Color.LightGreen
                };

                StrikeOutAnnotation strikeOutAnnotation = new StrikeOutAnnotation(
                   document.Pages[1],
                   tfa.TextFragments[2].Rectangle)
                {
                    Title = "مستخدم Aspose",
                    Color = Color.Blue
                };
                SquigglyAnnotation squigglyAnnotation = new SquigglyAnnotation(document.Pages[1],
                    tfa.TextFragments[3].Rectangle)
                {
                    Title = "مستخدم Aspose",
                    Color = Color.Red
                };
                UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(document.Pages[1],
                    tfa.TextFragments[4].Rectangle)
                {
                    Title = "مستخدم Aspose",
                    Color = Color.Violet
                };
                // إضافة التعليق التوضيحي إلى الصفحة
                document.Pages[1].Annotations.Add(highlightAnnotation);
                document.Pages[1].Annotations.Add(squigglyAnnotation);
                document.Pages[1].Annotations.Add(strikeOutAnnotation);
                document.Pages[1].Annotations.Add(underlineAnnotation);
                document.Save(System.IO.Path.Combine(_dataDir, "sample_mod.pdf"));
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
```
إذا كنت ترغب في تسليط الضوء على جزء متعدد الأسطر يجب عليك استخدام المثال المتقدم:

```csharp
        /// <summary>
        /// مثال متقدم إذا كنت ترغب في تسليط الضوء على جزء متعدد الأسطر
        /// </summary>
        public static void AddHighlightAnnotationAdvanced()
        {
            var document = new Document(System.IO.Path.Combine(_dataDir, "sample_mod.pdf"));
            var page = document.Pages[1];
            var tfa = new TextFragmentAbsorber(@"Adobe\W+Acrobat\W+Reader", new TextSearchOptions(true));
            tfa.Visit(page);
            foreach (var textFragment in tfa.TextFragments)
            {
                var highlightAnnotation = HighLightTextFragment(page, textFragment, Color.Yellow);
                page.Annotations.Add(highlightAnnotation);
            }
            document.Save(System.IO.Path.Combine(_dataDir, "sample_mod.pdf"));
        }
        private static HighlightAnnotation HighLightTextFragment(Aspose.Pdf.Page page,
            TextFragment textFragment, Color color)
        {
            if (textFragment.Segments.Count == 1)
                return new HighlightAnnotation(page, textFragment.Segments[1].Rectangle)
                {
                    Title = "مستخدم Aspose",
                    Color = color,
                    Modified = DateTime.Now,
                    QuadPoints = new Point[]
                    {
                        new Point(textFragment.Segments[1].Rectangle.LLX, textFragment.Segments[1].Rectangle.URY),
                        new Point(textFragment.Segments[1].Rectangle.URX, textFragment.Segments[1].Rectangle.URY),
                        new Point(textFragment.Segments[1].Rectangle.LLX, textFragment.Segments[1].Rectangle.LLY),
                        new Point(textFragment.Segments[1].Rectangle.URX, textFragment.Segments[1].Rectangle.LLY)
                    }
                };

            var offset = 0;
            var quadPoints = new Point[textFragment.Segments.Count * 4];
            foreach (var segment in textFragment.Segments)
            {
                quadPoints[offset + 0] = new Point(segment.Rectangle.LLX, segment.Rectangle.URY);
                quadPoints[offset + 1] = new Point(segment.Rectangle.URX, segment.Rectangle.URY);
                quadPoints[offset + 2] = new Point(segment.Rectangle.LLX, segment.Rectangle.LLY);
                quadPoints[offset + 3] = new Point(segment.Rectangle.URX, segment.Rectangle.LLY);
                offset += 4;
            }

            var llx = quadPoints.Min(pt => pt.X);
            var lly = quadPoints.Min(pt => pt.Y);
            var urx = quadPoints.Max(pt => pt.X);
            var ury = quadPoints.Max(pt => pt.Y);
            return new HighlightAnnotation(page, new Rectangle(llx, lly, urx, ury))
            {
                Title = "مستخدم Aspose",
                Color = color,
                Modified = DateTime.Now,
                QuadPoints = quadPoints
            };
        }

        /// <summary>
        /// كيفية الحصول على نص مميز
        /// </summary>
        public static void GetHighlightedText()
        {
            // تحميل ملف PDF
            Document document = new Document(System.IO.Path.Combine(_dataDir, "sample_mod.pdf"));
            var highlightAnnotations = document.Pages[1].Annotations
                .Where(a => a.AnnotationType == AnnotationType.Highlight)
                .Cast<HighlightAnnotation>();
            foreach (var ta in highlightAnnotations)
            {
                Console.WriteLine($"[{ta.GetMarkedText()}]");
            }
        }
```
## الحصول على تعليق توضيحي لترميز النص

يرجى محاولة استخدام قطعة الكود التالية للحصول على تعليق توضيحي لترميز النص من مستند PDF.

```csharp
    public static void GetTextMarkupAnnotation()
    {
        // تحميل ملف PDF
        Document document = new Document(System.IO.Path.Combine(_dataDir, "sample_mod.pdf"));
        var textMarkupAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == AnnotationType.Highlight
            || a.AnnotationType == AnnotationType.Squiggly)
            .Cast<TextMarkupAnnotation>();
            foreach (var ta in textMarkupAnnotations)
            {
                Console.WriteLine($"[{ta.AnnotationType} {ta.Rect}]");
            }
    }
```

## حذف تعليق توضيحي لترميز النص

يوضح قطعة الكود التالية كيفية حذف تعليق توضيحي لترميز النص من ملف PDF.

```csharp
    public static void DeleteTextMarkupAnnotation()
    {
        // تحميل ملف PDF
        Document document = new Document(System.IO.Path.Combine(_dataDir, "sample_mod.pdf"));
        var textMarkupAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == AnnotationType.Highlight
            ||a.AnnotationType == AnnotationType.Squiggly)
            .Cast<TextMarkupAnnotation>();
            foreach (var ta in textMarkupAnnotations)
            {
            document.Pages[1].Annotations.Delete(ta);
            }
            document.Save(System.IO.Path.Combine(_dataDir, "sample_del.pdf"));
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
```

