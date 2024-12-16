---
title: كيفية إنشاء ملف PDF باستخدام C#
linktitle: إنشاء مستند PDF
type: docs
weight: 10
url: /ar/net/create-pdf-document/
description: إنشاء وتنسيق مستند PDF باستخدام Aspose.PDF لـ .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "كيفية إنشاء ملف PDF باستخدام C#",
    "alternativeHeadline": "إنشاء مستند PDF من البداية",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستندات PDF",
    "keywords": "pdf, dotnet, إنشاء مستند pdf",
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
    "url": "/net/create-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "إنشاء وتنسيق مستند PDF باستخدام Aspose.PDF لـ .NET."
}
</script>
نحن دائمًا نبحث عن طريقة لإنشاء مستندات PDF والعمل معها في مشاريع C# بشكل أكثر دقة وفعالية. وجود وظائف سهلة الاستخدام من مكتبة يتيح لنا تتبع المزيد من العمل، وأقل على التفاصيل التي تستغرق وقتًا طويلاً في محاولة لإنشاء PDFs، سواء في .NET.

الشفرة التالية تعمل أيضا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

## إنشاء (أو توليد) مستند PDF باستخدام لغة C#

تتيح لك واجهة برمجة التطبيقات Aspose.PDF لـ .NET إنشاء وقراءة ملفات PDF باستخدام C# وVB.NET. يمكن استخدام الواجهة في مجموعة متنوعة من تطبيقات .NET بما في ذلك WinForms وASP.NET وعدة تطبيقات أخرى. في هذا المقال، سنوضح كيفية استخدام واجهة برمجة التطبيقات Aspose.PDF لـ .NET لتوليد وقراءة ملفات PDF بسهولة في تطبيقات .NET.

### كيفية إنشاء ملف PDF بسيط

لإنشاء ملف PDF باستخدام C#، يمكن استخدام الخطوات التالية.

1. إنشاء كائن من فئة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)
1.
1. إضافة [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) إلى مجموعة [Paragraphs](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) للصفحة
1. حفظ المستند PDF الناتج

```csharp
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

// تهيئة كائن المستند
Document document = new Document();
// إضافة صفحة
Page page = document.Pages.Add();
// إضافة نص إلى الصفحة الجديدة
page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
// حفظ PDF المحدث
document.Save(dataDir + "HelloWorld_out.pdf");
```

### كيفية إنشاء مستند PDF قابل للبحث

Aspose.PDF لـ .NET يوفر الميزة لإنشاء وكذلك التعديل على مستندات PDF الموجودة.
Aspose.PDF لـ .NET يوفر القدرة على إنشاء وكذلك التعديل على مستندات PDF الموجودة.

المنطق المحدد أدناه يتعرف على النصوص لصور PDF. للتعرف يمكنك استخدام دعم OCR الخارجي الذي يدعم معيار HOCR. لأغراض الاختبار، استخدمنا OCR من Google tesseract المجاني. لذلك، أولاً يجب عليك تثبيت Tesseract-OCR على نظامك، وسوف تحصل على تطبيق وحدة التحكم tesseract.

فيما يلي الكود الكامل لتحقيق هذا المطلب:

```csharp
using System;

namespace Aspose.Pdf.Examples.Advanced.WorkingWithDocuments
{
    class ExampleCreateDocument
    {
        private const string _dataDir = "C:\\Samples";
        public static void CreateSearchableDocuments(string file)
        {
            Aspose.Pdf.Document doc = new Aspose.Pdf.Document(file);
            bool convertResult = false;
            try
            {
                convertResult = doc.Convert(CallBackGetHocr);
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
            doc.Save(file);
            doc.Dispose();
        }

        static string CallBackGetHocr(System.Drawing.Image img)
        {
            string tmpFile = System.IO.Path.GetTempFileName();
            try
            {
                System.Drawing.Bitmap bmp = new System.Drawing.Bitmap(img);

                bmp.Save(tmpFile, System.Drawing.Imaging.ImageFormat.Bmp);
                string inputFile = string.Concat('"', tmpFile, '"');
                string outputFile = string.Concat('"', tmpFile, '"');
                string arguments = string.Concat(inputFile, " ", outputFile, " -l eng hocr");
                string tesseractProcessName = @"C:\Program Files\Tesseract-OCR\Tesseract.exe";

                System.Diagnostics.ProcessStartInfo psi =
                    new System.Diagnostics.ProcessStartInfo(tesseractProcessName, arguments)
                    {
                        UseShellExecute = true,
                        CreateNoWindow = true,
                        WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden,
                        WorkingDirectory = System.IO.Path.GetDirectoryName(tesseractProcessName)
                    };

                System.Diagnostics.Process p = new System.Diagnostics.Process
                {
                    StartInfo = psi
                };
                p.Start();
                p.WaitForExit();

                System.IO.StreamReader streamReader = new System.IO.StreamReader(tmpFile + ".hocr");
                string text = streamReader.ReadToEnd();
                streamReader.Close();

                return text;
            }
            finally
            {
                if (System.IO.File.Exists(tmpFile))
                    System.IO.File.Delete(tmpFile);
                if (System.IO.File.Exists(tmpFile + ".hocr"))
                    System.IO.File.Delete(tmpFile + ".hocr");
            }
        }
    }
}
```

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

