---
title: مثال على Hello World باستخدام لغة C#
linktitle: مثال Hello World
type: docs
weight: 40
url: /ar/net/hello-world-example/
description: هذا المثال يوضح كيفية إنشاء مستند PDF بسيط يحتوي على نص Hello World باستخدام Aspose.PDF
lastmod: "2022-02-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "مثال على Hello World باستخدام لغة C#",
    "alternativeHeadline": "مثال Aspose.PDF بلغة C#",
    "author": {
        "@type": "Person",
        "givenName": "أندري",
        "familyName": "أندروخوفسكي",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "إنشاء مستندات PDF",
    "keywords": "pdf, c#, إنشاء مستندات",
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
    "url": "http://docs.aspose.com/pdf/net/hello-world-example/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "http://docs.aspose.com/pdf/net/hello-world-example/"
    },
    "dateModified": "2022-02-04",
    "description": "هذا المثال يوضح كيفية إنشاء مستند PDF بسيط يحتوي على نص Hello World باستخدام Aspose.PDF",
    "articleBody": "يُستخدم مثال \"Hello World\" تقليديًا لتقديم ميزات لغة برمجة أو برنامج مع حالة استخدام بسيطة.\nAspose.PDF لـ .NET هو API غني بالميزات لـ PDF يسمح للمطورين بتضمين إمكانيات إنشاء، تManipulation وتحويل مستندات PDF في تطبيقات .NET الخاصة بهم. يدعم العمل مع العديد من صيغ الملفات الشهيرة بما في ذلك PDF، XFA، TXT، HTML، PCL، XML، XPS، EPUB، TEX وصيغ ملفات الصور. في هذه المقالة، نحن نقوم بإنشاء مستند PDF يحتوي على نص \"Hello World!\". بعد تثبيت Aspose.PDF لـ .NET في بيئتك، يمكنك تنفيذ عينة الكود أدناه لرؤية كيفية عمل API Aspose.PDF.\nيتبع جزء الكود أدناه هذه الخطوات:\n1. إنشاء كائن Document\n2. إضافة صفحة إلى كائن المستند\n3. إنشاء TextFragment\n4. إضافة TextFragment إلى مجموعة الفقرات في الصفحة\n5. حفظ المستند PDF الناتج\nجزء الكود التالي هو برنامج Hello World لعرض عمل API Aspose.PDF لـ .NET."
}
</script>
مثال "Hello World" يستخدم تقليدياً لتقديم ميزات لغة برمجة أو برنامج بحالة استخدام بسيطة.

Aspose.PDF لـ .NET هو API غني بالميزات يسمح للمطورين بتضمين إنشاء ومعالجة وتحويل مستندات PDF في تطبيقات .NET الخاصة بهم. يدعم العمل مع العديد من صيغ الملفات الشهيرة بما في ذلك PDF، XFA، TXT، HTML، PCL، XML، XPS، EPUB، TEX وصيغ ملفات الصور. في هذه المقالة، نحن نقوم بإنشاء مستند PDF يحتوي على نص "Hello World!". بعد تثبيت Aspose.PDF لـ .NET في بيئتك، يمكنك تنفيذ عينة الكود أدناه لرؤية كيفية عمل API Aspose.PDF.

الشفرة التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

تتبع شفرة البرنامج أدناه هذه الخطوات:

1. استدعاء كائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)
1. إضافة [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) إلى كائن المستند
1.
1.
1. أضف TextFragment إلى مجموعة [Paragraph](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) الخاصة بالصفحة
1. [احفظ](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) المستند PDF الناتج

الشفرة التالية هي برنامج مثالي لعرض كيفية عمل واجهة برمجة تطبيقات Aspose.PDF لـ .NET.

```csharp
namespace Aspose.Pdf.Examples
{
    public static class ExampleGetStarted
    {
        private static readonly string _dataDir = "..\\..\\..\\Samples";
        public static void HelloWorld()
        {
            // Initialize document object
            Document document = new Document();
            // Add page
            Page page = document.Pages.Add();
            // Add text to new page
            page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
            // Save updated PDF
            var outputFileName = System.IO.Path.Combine(_dataDir, "HelloWorld_out.pdf");
            document.Save( outputFileName );
        }
    }
}
```
