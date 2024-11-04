---
title: إزالة الجداول من ملف PDF موجود
linktitle: إزالة الجداول
type: docs
weight: 50
url: /net/remove-tables-from-existing-pdf/
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "إزالة الجداول من ملف PDF موجود",
    "alternativeHeadline": "كيفية حذف الجداول من ملف PDF",
    "author": {
        "@type": "Person",
        "name":"أناستاسيا هولوب",
        "givenName": "أناستاسيا",
        "familyName": "هولوب",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستند PDF",
    "keywords": "pdf, c#, إزالة جدول, حذف جداول",
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
    "url": "/net/remove-tables-from-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/remove-tables-from-existing-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": ""
}
</script>
{{% alert color="primary" %}}

Aspose.PDF لـ NET يوفر القدرات لإدراج/إنشاء جدول داخل مستند PDF أثناء توليده من البداية أو يمكنك أيضًا إضافة كائن الجدول في أي مستند PDF موجود. قد تكون لديك متطلبات لـ [التلاعب بالجداول في مستند PDF موجود](https://docs.aspose.com/pdf/net/manipulate-tables-in-existing-pdf/) حيث يمكنك تحديث المحتويات في خلايا الجدول الموجودة. قد تصادف أيضًا متطلبات لإزالة كائنات الجدول من مستند PDF الموجود.

{{% /alert %}}

لإزالة الجداول، نحتاج إلى استخدام فئة [TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber) للحصول على الجداول في PDF الموجود ثم استدعاء [Remove](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber/methods/remove).

يعمل أيضًا الشفرة التالية مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

## إزالة الجدول من مستند PDF

لقد أضفنا وظيفة جديدة أي.
لقد أضفنا وظيفة جديدة ألا وهي:

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// تحميل مستند PDF موجود
Document pdfDocument = new Document(dataDir + "Table_input.pdf");

// إنشاء كائن TableAbsorber للعثور على الجداول
TableAbsorber absorber = new TableAbsorber();

// زيارة الصفحة الأولى مع الامتصاص
absorber.Visit(pdfDocument.Pages[1]);

// الحصول على الجدول الأول في الصفحة
AbsorbedTable table = absorber.TableList[0];

// إزالة الجدول
absorber.Remove(table);

// حفظ PDF
pdfDocument.Save(dataDir + "Table_out.pdf");
```

## إزالة الجداول المتعددة من مستند PDF

أحيانًا قد يحتوي مستند PDF على أكثر من جدول وقد تحتاج إلى إزالة الجداول المتعددة منه. لإزالة الجداول المتعددة من مستند PDF، يرجى استخدام الشريط التالي:

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// تحميل مستند PDF موجود
Document pdfDocument = new Document(dataDir + "Table_input2.pdf");

// إنشاء كائن TableAbsorber للعثور على الجداول
TableAbsorber absorber = new TableAbsorber();

// زيارة الصفحة الثانية مع الامتصاص
absorber.Visit(pdfDocument.Pages[1]);

// الحصول على نسخة من مجموعة الجداول
AbsorbedTable[] tables = new AbsorbedTable[absorber.TableList.Count];
absorber.TableList.CopyTo(tables, 0);

// التكرار عبر نسخة من المجموعة وإزالة الجداول
foreach (AbsorbedTable table in tables)
    absorber.Remove(table);

// حفظ المستند
pdfDocument.Save(dataDir + "Table2_out.pdf");
```

{{% alert color="primary" %}}
يرجى أخذ في الاعتبار أن إزالة أو استبدال جدول يغير مجموعة TableList. لذلك، في حالة إزالة/استبدال الجداول في حلقة، فإن نسخ مجموعة TableList أمر ضروري.
{{% /alert %}}

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF لمكتبة .NET",
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

