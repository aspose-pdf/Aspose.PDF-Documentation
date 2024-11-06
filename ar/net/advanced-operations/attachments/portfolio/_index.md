---
title: العمل مع المحفظة في ملف PDF
linktitle: المحفظة
type: docs
weight: 40
url: ar/net/portfolio/
description: كيفية إنشاء محفظة PDF باستخدام C#. يجب استخدام ملف Microsoft Excel ومستند Word وملف صورة لإنشاء محفظة PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "العمل مع المحفظة في ملف PDF",
    "alternativeHeadline": "إنشاء محفظة في مستند PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستند PDF في PDF",
    "keywords": "pdf, c#, المحفظة",
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
    "url": "/net/portfolio/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/portfolio/"
    },
    "dateModified": "2022-02-04",
    "description": "كيفية إنشاء محفظة PDF باستخدام C#. يجب استخدام ملف Microsoft Excel ومستند Word وملف صورة لإنشاء محفظة PDF."
}
</script>

## كيفية إنشاء محفظة PDF

يتيح Aspose.PDF إنشاء مستندات محفظة PDF باستخدام فئة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). أضف ملفًا إلى كائن Document.Collection بعد الحصول عليه باستخدام فئة [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification). عندما يتم إضافة الملفات، استخدم طريقة Save الخاصة بفئة Document لحفظ مستند المحفظة.

المثال التالي يستخدم ملف Microsoft Excel، ومستند Word وملف صورة لإنشاء محفظة PDF.

الكود أدناه يؤدي إلى المحفظة التالية.

الشفرة البرمجية التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

### محفظة PDF التي تم إنشاؤها بواسطة Aspose.PDF

![محفظة PDF التي تم إنشاؤها بواسطة Aspose.PDF لـ .NET](working-with-pdf-portfolio_1.jpg)

```csharp
// مسار دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_TechnicalArticles();

// إنشاء كائن Document
Document doc = new Document();

// إنشاء كائن مجموعة المستندات
doc.Collection = new Collection();

// الحصول على الملفات لإضافتها إلى المحفظة
FileSpecification excel = new FileSpecification( dataDir + "HelloWorld.xlsx");
FileSpecification word = new FileSpecification( dataDir + "HelloWorld.docx");
FileSpecification image = new FileSpecification(dataDir + "aspose-logo.jpg");

// توفير وصف الملفات
excel.Description = "ملف Excel";
word.Description = "ملف Word";
image.Description = "ملف صورة";

// إضافة الملفات إلى مجموعة المستندات
doc.Collection.Add(excel);
doc.Collection.Add(word);
doc.Collection.Add(image);

// حفظ مستند المحفظة
doc.Save(dataDir + "CreatePDFPortfolio_out.pdf");
```
## استخراج الملفات من محفظة PDF

تتيح لك محافظ PDF دمج المحتوى من مصادر متنوعة (على سبيل المثال، ملفات PDF، Word، Excel، JPEG) في حاوية موحدة. تحتفظ الملفات الأصلية بهوياتها الفردية لكن يتم تجميعها في ملف محفظة PDF. يمكن للمستخدمين فتح، قراءة، تعديل، وتنسيق كل ملف مكون بشكل مستقل عن الملفات الأخرى.

يتيح Aspose.PDF إنشاء مستندات محفظة PDF باستخدام فئة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). كما يوفر القدرة على استخراج الملفات من محفظة PDF.

يعرض شريط الكود التالي الخطوات لاستخراج الملفات من محفظة PDF.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_TechnicalArticles();

// تحميل محفظة PDF المصدر
Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "PDFPortfolio.pdf");
// الحصول على مجموعة الملفات المضمنة
EmbeddedFileCollection embeddedFiles = pdfDocument.EmbeddedFiles;
// التكرار خلال كل ملف من محفظة
foreach (FileSpecification fileSpecification in embeddedFiles)
{
    // الحصول على المرفق والكتابة إلى ملف أو تيار
    byte[] fileContent = new byte[fileSpecification.Contents.Length];
    fileSpecification.Contents.Read(fileContent, 0, fileContent.Length);
    string filename = Path.GetFileName(fileSpecification.Name);
    // حفظ الملف المستخرج في موقع ما
    FileStream fileStream = new FileStream(dataDir + "_out" + filename, FileMode.Create);
    fileStream.Write(fileContent, 0, fileContent.Length);
    // إغلاق كائن التيار
    fileStream.Close();
}
```
![استخراج الملفات من محفظة PDF](working-with-pdf-portfolio_2.jpg)

## إزالة الملفات من محفظة PDF

لحذف / إزالة الملفات من محفظة PDF، جرب استخدام الأسطر البرمجية التالية.

```csharp
// لأمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_TechnicalArticles();

// تحميل محفظة PDF الأصلية
Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "PDFPortfolio.pdf");
pdfDocument.Collection.Delete();
pdfDocument.Save(dataDir + "No_PortFolio_out.pdf");
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
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


