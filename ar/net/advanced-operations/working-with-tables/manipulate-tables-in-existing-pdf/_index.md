---
title: التلاعب بالجداول في ملف PDF موجود
linktitle: التلاعب بالجداول
type: docs
weight: 40
url: /ar/net/manipulate-tables-in-existing-pdf/
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "التلاعب بالجداول في ملف PDF موجود",
    "alternativeHeadline": "كيفية تحديث محتوى الجداول في ملف PDF موجود",
    "author": {
        "@type": "Person",
        "name":"أناستاسيا هولوب",
        "givenName": "أناستاسيا",
        "familyName": "هولوب",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستند PDF",
    "keywords": "pdf, c#, التلاعب بالجداول",
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
    "url": "/net/manipulate-tables-in-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manipulate-tables-in-existing-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": ""
}
</script>
## التعامل مع الجداول في ملفات PDF الموجودة

أحد أقدم الميزات التي يدعمها Aspose.PDF لـ .NET هي قدراته في التعامل مع الجداول ويوفر دعمًا كبيرًا لإضافة جداول في ملفات PDF التي يتم إنشاؤها من الصفر أو أي ملفات PDF موجودة. تحصل أيضًا على القدرة على دمج الجدول مع قاعدة البيانات (DOM) لإنشاء جداول ديناميكية بناءً على محتويات قاعدة البيانات. في هذا الإصدار الجديد، قمنا بتنفيذ ميزة جديدة للبحث وتحليل الجداول البسيطة الموجودة بالفعل على صفحة من مستند PDF. توفر فئة جديدة تُدعى **Aspose.PDF.Text.TableAbsorber** هذه القدرات. استخدام TableAbsorber مشابه جدًا لفئة TextFragmentAbsorber الموجودة. يوضح الجزء التالي من الشفرة الخطوات لتحديث المحتويات في خلية جدول محددة.

يعمل الجزء التالي من الشفرة أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// تحميل ملف PDF الموجود
Document pdfDocument = new Document(dataDir + "input.pdf");
// إنشاء كائن TableAbsorber للعثور على الجداول
TableAbsorber absorber = new TableAbsorber();

// زيارة الصفحة الأولى بواسطة الجهاز
absorber.Visit(pdfDocument.Pages[1]);

// الحصول على الوصول إلى الجدول الأول على الصفحة، خليتهم الأولى والأجزاء النصية فيها
TextFragment fragment = absorber.TableList[0].RowList[0].CellList[0].TextFragments[1];

// تغيير نص الجزء النصي الأول في الخلية
fragment.Text = "مرحبا بالعالم";
dataDir = dataDir + "ManipulateTable_out.pdf";
pdfDocument.Save(dataDir);
```
## استبدال جدول قديم بجدول جديد في مستند PDF

في حالة الحاجة للعثور على جدول معين واستبداله بالجدول المطلوب، يمكنك استخدام الطريقة Replace() للفئة [TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber) للقيام بذلك. يوضح المثال التالي الوظيفة لاستبدال الجدول داخل مستند PDF:

```csharp
// للحصول على الأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// تحميل مستند PDF الحالي
Document pdfDocument = new Document(dataDir + @"Table_input2.pdf");

// إنشاء كائن TableAbsorber للعثور على الجداول
TableAbsorber absorber = new TableAbsorber();

// زيارة الصفحة الأولى بواسطة absorber
absorber.Visit(pdfDocument.Pages[1]);

// الحصول على أول جدول في الصفحة
AbsorbedTable table = absorber.TableList[0];

// إنشاء جدول جديد
Table newTable = new Table();
newTable.ColumnWidths = "100 100 100";
newTable.DefaultCellBorder = new BorderInfo(BorderSide.All, 1F);

Row row = newTable.Rows.Add();
row.Cells.Add("العمود 1");
row.Cells.Add("العمود 2");
row.Cells.Add("العمود 3");

// استبدال الجدول بجدول جديد
absorber.Replace(pdfDocument.Pages[1], table, newTable);

// حفظ المستند
pdfDocument.Save(dataDir + "TableReplaced_out.pdf");
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

