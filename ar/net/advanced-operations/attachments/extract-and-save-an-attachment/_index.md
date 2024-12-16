---
title: استخراج وحفظ مرفق
linktitle: استخراج وحفظ مرفق
type: docs
weight: 20
url: /ar/net/extract-and-save-an-attachment/
description: يتيح لك Aspose.PDF لـ .NET الحصول على جميع المرفقات من مستند PDF. كما يمكنك الحصول على مرفق فردي من مستندك.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "headline": "استخراج وحفظ مرفق",
    "alternativeHeadline": "كيفية استخراج وحفظ المرفقات",
    "author": {
        "name":"أناستاسيا هولوب",
        "givenName": "أناستاسيا",
        "familyName": "هولوب",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستند PDF",
    "keywords": "pdf, c#, حفظ المرفقات, استخراج المرفقات",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "name": "فريق توثيق Aspose.PDF",
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
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/extract-and-save-an-attachment/",
    "mainEntityOfPage": {
        "@id": "/net/extract-and-save-an-attachment/"
    },
    "dateModified": "2022-02-04",
    "description": "يتيح لك Aspose.PDF لـ .NET الحصول على جميع المرفقات من مستند PDF. كما يمكنك الحصول على مرفق فردي من مستندك."
}
</script>
## الحصول على كل المرفقات

مع Aspose.PDF، من الممكن الحصول على كل المرفقات من مستند PDF. هذا مفيد إما عندما تريد حفظ المستندات بشكل منفصل عن مستند PDF، أو إذا كنت بحاجة إلى إزالة المرفقات من مستند PDF.

للحصول على كل المرفقات من ملف PDF:

1. تصفح مجموعة [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) لكائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). تحتوي مجموعة [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) على كل المرفقات. كل عنصر في هذه المجموعة يمثل كائن [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification). كل تكرار في حلقة foreach عبر مجموعة [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) يعيد كائن [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification).
1.

الشفرات التالية توضح كيفية الحصول على جميع المرفقات من مستند PDF.

الشفرة التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

```csharp
// للأمثلة الكاملة وملفات البيانات، الرجاء زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

// فتح المستند
Document pdfDocument = new Document(dataDir + "GetAlltheAttachments.pdf");

// الحصول على مجموعة الملفات المضمنة
EmbeddedFileCollection embeddedFiles = pdfDocument.EmbeddedFiles;

// الحصول على عدد الملفات المضمنة
Console.WriteLine("إجمالي الملفات : {0}", embeddedFiles.Count);

int count = 1;

// التكرار خلال المجموعة للحصول على جميع المرفقات
foreach (FileSpecification fileSpecification in embeddedFiles)
{
    Console.WriteLine("الاسم: {0}", fileSpecification.Name);
    Console.WriteLine("الوصف: {0}",
    fileSpecification.Description);
    Console.WriteLine("نوع MIME: {0}", fileSpecification.MIMEType);

    // التحقق إذا كان الكائن العامل يحتوي على الأوامر
    if (fileSpecification.Params != null)
    {
        Console.WriteLine("المجموع: {0}",
        fileSpecification.Params.CheckSum);
        Console.WriteLine("تاريخ الإنشاء: {0}",
        fileSpecification.Params.CreationDate);
        Console.WriteLine("تاريخ التعديل: {0}",
        fileSpecification.Params.ModDate);
        Console.WriteLine("الحجم: {0}", fileSpecification.Params.Size);
    }

    // الحصول على المرفق وكتابته إلى ملف أو تيار
    byte[] fileContent = new byte[fileSpecification.Contents.Length];
    fileSpecification.Contents.Read(fileContent, 0,
    fileContent.Length);
    FileStream fileStream = new FileStream(dataDir + count + "_out" + ".txt",
    FileMode.Create);
    fileStream.Write(fileContent, 0, fileContent.Length);
    fileStream.Close();
    count+=1;
}
```
## الحصول على مرفق فردي

للحصول على مرفق فردي، يمكننا تحديد مؤشر المرفق في كائن `EmbeddedFiles` لمثيل المستند. يرجى استخدام قطعة الكود التالية.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى مجلد المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

// فتح المستند
Document pdfDocument = new Document(dataDir + "GetIndividualAttachment.pdf");

// الحصول على الملف المضمن المحدد
FileSpecification fileSpecification = pdfDocument.EmbeddedFiles[1];

// الحصول على خصائص الملف
Console.WriteLine("الاسم: {0}", fileSpecification.Name);
Console.WriteLine("الوصف: {0}", fileSpecification.Description);
Console.WriteLine("نوع MIME: {0}", fileSpecification.MIMEType);

// التحقق إذا كان كائن البارامتر يحتوي على البارامترات
if (fileSpecification.Params != null)
{
    Console.WriteLine("التحقق: {0}",
    fileSpecification.Params.CheckSum);
    Console.WriteLine("تاريخ الإنشاء: {0}",
    fileSpecification.Params.CreationDate);
    Console.WriteLine("تاريخ التعديل: {0}",
    fileSpecification.Params.ModDate);
    Console.WriteLine("الحجم: {0}", fileSpecification.Params.Size);
}

// الحصول على المرفق وكتابته إلى ملف أو تيار
byte[] fileContent = new byte[fileSpecification.Contents.Length];
fileSpecification.Contents.Read(fileContent, 0, fileContent.Length);

FileStream fileStream = new FileStream(dataDir + "test_out" + ".txt", FileMode.Create);
fileStream.Write(fileContent, 0, fileContent.Length);
fileStream.Close();
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "مكتبة التعامل مع ملفات PDF لـ .NET",
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

