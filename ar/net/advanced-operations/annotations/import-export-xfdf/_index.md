---
title: استيراد وتصدير التعليقات التوضيحية إلى XFDF
linktitle: استيراد وتصدير التعليقات التوضيحية إلى XFDF
type: docs
weight: 40
url: ar/net/import-export-xfdf/
description: يمكنك استيراد وتصدير التعليقات التوضيحية بتنسيق XFDF باستخدام C# ومكتبة Aspose.PDF لـ .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "استيراد وتصدير التعليقات التوضيحية إلى XFDF",
    "alternativeHeadline": "طرق لاستيراد وتصدير بيانات التعليقات التوضيحية إلى ملفات XFDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء وثيقة PDF",
    "keywords": "pdf, c#, استيراد تصدير إلى XFDF",
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
    "url": "/net/import-export-xfdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-export-xfdf/"
    },
    "dateModified": "2022-02-04",
    "description": "يمكنك استيراد وتصدير التعليقات التوضيحية بتنسيق XFDF باستخدام C# ومكتبة Aspose.PDF لـ .NET."
}
</script>
{{% alert color="primary" %}}

XFDF تعني تنسيق بيانات النماذج XML. إنها تنسيق ملف يعتمد على XML. يُستخدم هذا التنسيق لتمثيل بيانات النماذج أو التعليقات التوضيحية الموجودة في نموذج PDF. يمكن استخدام XFDF لأغراض متعددة، ولكن في حالتنا، يمكن استخدامه لإما إرسال أو استقبال بيانات النماذج أو التعليقات التوضيحية إلى أجهزة كمبيوتر أو خوادم أخرى، أو يمكن استخدامه لأرشفة بيانات النماذج أو التعليقات التوضيحية. في هذه المقالة، سنرى كيف أخذت Aspose.Pdf.Facades هذا المفهوم بعين الاعتبار وكيف يمكننا استيراد وتصدير بيانات التعليقات التوضيحية إلى ملف XFDF.

{{% /alert %}}

**Aspose.PDF لـ .NET** هو مكون غني بالميزات عندما يتعلق الأمر بتحرير مستندات PDF. كما نعلم أن XFDF هو جانب مهم من تلاعب نماذج PDF، فقد أخذ فضاء الأسماء Aspose.Pdf.Facades في Aspose.PDF لـ .NET هذا بعين الاعتبار جيدًا، وقدم طرقًا لاستيراد وتصدير بيانات التعليقات التوضيحية إلى ملفات XFDF.

فئة [PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) تحتوي على طريقتين للعمل مع استيراد وتصدير التعليقات التوضيحية إلى ملف XFDF.
[PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) تحتوي الفئة على طريقتين للعمل مع استيراد وتصدير التعليقات التوضيحية إلى ملف XFDF.

الشفرة التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

الشفرة التالية توضح لك كيفية تصدير التعليقات التوضيحية إلى ملف XFDF:

```csharp
using Aspose.Pdf.Annotations;
using Aspose.Pdf.Facades;
using System.IO;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleAnnotationImportExport
    {
        // مسار إلى دليل المستندات.
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        /// <summary>
        /// استيراد التعليقات التوضيحية من ملف XFDF
        /// ملف تنسيق بيانات النماذج XML (XFDF) تم إنشاؤه بواسطة Adobe Acrobat، تطبيق إنشاء PDF؛
        /// يخزن وصف عناصر نموذج الصفحة وقيمها، مثل الأسماء والقيم لحقول النص؛ يستخدم لحفظ بيانات النموذج التي يمكن استيرادها إلى مستند PDF.
        /// يمكنك استيراد بيانات التعليق التوضيحي من ملف XFDF إلى PDF باستخدام
        /// طريقة ImportAnnotationsFromXfdf في فئة PdfAnnotationEditor.
        /// </summary>       
   
        public static void ExportAnnotationXFDF()
        {
            // إنشاء كائن PdfAnnotationEditor
            PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();

            // ربط مستند PDF بمحرر التعليق التوضيحي
            AnnotationEditor.BindPdf(Path.Combine(_dataDir, "AnnotationDemo1.pdf"));
           
            // تصدير التعليقات
            var fileStream = File.OpenWrite(Path.Combine(_dataDir, "exportannotations.xfdf"));
            var annotType = new AnnotationType[] { AnnotationType.Line, AnnotationType.Square };
            AnnotationEditor.ExportAnnotationsXfdf(fileStream, 1, 1, annotType);
            fileStream.Flush();
            fileStream.Close();
        }
        //...
    }
}
```
الشريحة التالية توضح كيفية استيراد التعليقات التوضيحية إلى ملف XFDF:

```csharp
public static void ImportAnnotationXFDF()
{
    // إنشاء كائن PdfAnnotationEditor
    PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();
    // إنشاء وثيقة PDF جديدة
    var document = new Document();
    document.Pages.Add();
    AnnotationEditor.BindPdf(document);

    var exportFileName = Path.Combine(_dataDir, "exportannotations.xfdf");
    if (!File.Exists(exportFileName))
        ExportAnnotationXFDF();

    // استيراد التعليقات التوضيحية
    AnnotationEditor.ImportAnnotationsFromXfdf(exportFileName);

    // حفظ PDF الناتج
    document.Save(Path.Combine(_dataDir, "AnnotationDemo2.pdf"));
}
```

## طريقة أخرى لتصدير / استيراد التعليقات التوضيحية دفعة واحدة

في الشفرة أدناه، تسمح طريقة ImportAnnotations باستيراد التعليقات التوضيحية مباشرة من وثيقة PDF أخرى.

```csharp
        /// <summary>
        /// طريقة ImportAnnotations تسمح باستيراد التعليقات التوضيحية مباشرة من وثيقة PDF أخرى
        /// </summary>

        public static void ImportAnnotationFromPDF()
        {
            // إنشاء كائن PdfAnnotationEditor
            PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();
            // إنشاء وثيقة PDF جديدة
            var document = new Document();
            document.Pages.Add();
            AnnotationEditor.BindPdf(document);
            var exportFileName = Path.Combine(_dataDir, "exportannotations.xfdf");
            if (!File.Exists(exportFileName))
                ExportAnnotationXFDF();

            // يسمح محرر التعليقات التوضيحية باستيراد التعليقات من عدة وثائق PDF،
            // لكن في هذا المثال، نستخدم واحدة فقط.
            AnnotationEditor.ImportAnnotations(new[] { Path.Combine(_dataDir, "AnnotationDemo1.pdf") });

            // حفظ PDF الناتج
            document.Save(Path.Combine(_dataDir, "AnnotationDemo3.pdf"));
        }
    }
}
```
changefreq: "monthly"
type: docs

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
                "areaServed": "الولايات المتحدة",
                "availableLanguage": "الإنجليزية"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "مبيعات",
                "areaServed": "بريطانيا",
                "availableLanguage": "الإنجليزية"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "مبيعات",
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
```

