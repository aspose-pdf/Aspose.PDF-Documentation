---
title: إضافة رقم الصفحة إلى ملف PDF باستخدام C#
linktitle: إضافة رقم الصفحة
type: docs
weight: 100
url: /net/add-page-number/
description: يتيح لك Aspose.PDF لـ .NET إضافة ختم رقم الصفحة إلى ملف PDF باستخدام فئة ختم رقم الصفحة.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/get-and-set-page-properties/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "إضافة رقم الصفحة إلى ملف PDF باستخدام C#",
    "alternativeHeadline": "كيفية إضافة ختم رقم الصفحة إلى ملف PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء مستند PDF",
    "keywords": "pdf, c#, ختم رقم الصفحة",
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
    "url": "/net/add-page-number/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-page-number/"
    },
    "dateModified": "2022-02-04",
    "description": "يتيح لك Aspose.PDF لـ .NET إضافة ختم رقم الصفحة إلى ملف PDF باستخدام فئة ختم رقم الصفحة."
}
</script>
كل الوثائق يجب أن تحتوي على أرقام الصفحات فيها. يسهل رقم الصفحة على القارئ تحديد أجزاء مختلفة من الوثيقة.
**Aspose.PDF لـ .NET** يتيح لك إضافة أرقام الصفحات مع PageNumberStamp.

الشفرة التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

يمكنك استخدام فئة [PageNumberStamp](https://reference.aspose.com/pdf/net/aspose.pdf/pagenumberstamp) لإضافة ختم رقم الصفحة في ملف PDF.
يمكنك استخدام فئة [PageNumberStamp](https://reference.aspose.com/pdf/net/aspose.pdf/pagenumberstamp) لإضافة ختم رقم الصفحة في ملف PDF.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// فتح المستند
Document pdfDocument = new Document(dataDir+ "PageNumberStamp.pdf");

// إنشاء ختم رقم الصفحة
PageNumberStamp pageNumberStamp = new PageNumberStamp();
// هل الختم هو خلفية
pageNumberStamp.Background = false;
pageNumberStamp.Format = "Page # of " + pdfDocument.Pages.Count;
pageNumberStamp.BottomMargin = 10;
pageNumberStamp.HorizontalAlignment = HorizontalAlignment.Center;
pageNumberStamp.StartingNumber = 1;
// تعيين خصائص النص
pageNumberStamp.TextState.Font = FontRepository.FindFont("Arial");
pageNumberStamp.TextState.FontSize = 14.0F;
pageNumberStamp.TextState.FontStyle = FontStyles.Bold;
pageNumberStamp.TextState.FontStyle = FontStyles.Italic;
pageNumberStamp.TextState.ForegroundColor = Color.Aqua;

// إضافة الختم إلى صفحة معينة
pdfDocument.Pages[1].AddStamp(pageNumberStamp);

dataDir = dataDir + "PageNumberStamp_out.pdf";
// حفظ المستند الناتج
pdfDocument.Save(dataDir);
```
## مثال حي

[إضافة أرقام صفحات PDF](https://products.aspose.app/pdf/page-number) هو تطبيق ويب مجاني على الإنترنت يتيح لك استكشاف كيفية عمل إضافة أرقام الصفحات.

[![كيفية إضافة رقم صفحة في ملف PDF باستخدام C#](page_number.png)](https://products.aspose.app/pdf/page-number)

## إضافة/إزالة ترقيم بيتس

**ترقيم بيتس** (المعروف أيضًا باسم ختم بيتس) يستخدم في المجالات القانونية، والطبية، والتجارية لوضع أرقام تعريفية و/أو علامات التاريخ/الوقت على الصور والمستندات أثناء مسحها ضوئيًا أو معالجتها، على سبيل المثال، خلال مرحلة الاكتشاف استعدادًا للمحاكمة أو تحديد إيصالات الأعمال. يوفر هذا العملية التعريف، الحماية، والترقيم المتتابع التلقائي للصور أو المستندات.

Aspose.PDF لديه دعم محدود لترقيم بيتس الآن. سيتم تحديث هذه الوظيفة وفقًا لطلبات العملاء.

### كيفية إزالة ترقيم بيتس

```csharp
static void Demo03()
{
    Document doc = new Document(@"C:\Samples\Sample-Document03.pdf");
    foreach (var page in doc.Pages)
    {
        var batesNum = page.Artifacts.First(ar => ar.CustomSubtype == "BatesN");
        page.Artifacts.Delete(batesNum);
    }
    doc.Save(@"C:\Samples\Sample-Document04.pdf");
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
                "areaServed": "الولايات المتحدة الأمريكية",
                "availableLanguage": "الإنجليزية"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "مبيعات",
                "areaServed": "المملكة المتحدة",
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
```

