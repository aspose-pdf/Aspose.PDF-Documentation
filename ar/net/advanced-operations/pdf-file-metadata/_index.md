---
title: العمل مع بيانات ملف PDF الوصفية | C#
linktitle: بيانات ملف PDF الوصفية
type: docs
weight: 140
url: ar/net/pdf-file-metadata/
description: يشرح هذا القسم كيفية الحصول على معلومات ملف PDF، وكيفية الحصول على بيانات XMP الوصفية من ملف PDF، وتعيين معلومات ملف PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "العمل مع بيانات ملف PDF الوصفية | C#",
    "alternativeHeadline": "كيفية الحصول على بيانات ملف PDF الوصفية",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء مستندات PDF",
    "keywords": "pdf, c#, بيانات ملف pdf الوصفية",
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
    "url": "/net/pdf-file-metadata/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-file-metadata/"
    },
    "dateModified": "2022-02-04",
    "description": "يشرح هذا القسم كيفية الحصول على معلومات ملف PDF، وكيفية الحصول على بيانات XMP الوصفية من ملف PDF، وتعيين معلومات ملف PDF."
}
</script>
يعمل الكود التالي أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

## الحصول على معلومات ملف PDF

للحصول على معلومات محددة عن ملف PDF، عليك أولاً الحصول على كائن [DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo) باستخدام خاصية [Info](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/info) لكائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). بمجرد استرجاع كائن [DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo)، يمكنك الحصول على قيم الخصائص الفردية. يوضح الكود التالي كيفية الحصول على معلومات ملف PDF.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// فتح المستند
Document pdfDocument = new Document(dataDir + "GetFileInfo.pdf");
// الحصول على معلومات المستند
DocumentInfo docInfo = pdfDocument.Info;
// عرض معلومات المستند
Console.WriteLine("المؤلف: {0}", docInfo.Author);
Console.WriteLine("تاريخ الإنشاء: {0}", docInfo.CreationDate);
Console.WriteLine("الكلمات الدلالية: {0}", docInfo.Keywords);
Console.WriteLine("تاريخ التعديل: {0}", docInfo.ModDate);
Console.WriteLine("الموضوع: {0}", docInfo.Subject);
Console.WriteLine("العنوان: {0}", docInfo.Title);
```
## تعيين معلومات ملف PDF

يتيح لك Aspose.PDF لـ.NET تعيين معلومات محددة لملف PDF، مثل الكاتب، تاريخ الإنشاء، الموضوع، والعنوان. لتعيين هذه المعلومات:

1. قم بإنشاء كائن [DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo).
1. قم بتعيين قيم الخصائص.
1. احفظ المستند المحدث باستخدام طريقة Save الخاصة بفئة الوثيقة.

{{% alert color="primary" %}}

يرجى ملاحظة أنه لا يمكنك تعيين قيم ضد حقول *Application* و *Producer*، لأنه سيتم عرض Aspose Ltd. و Aspose.PDF لـ.NET x.x.x ضد هذه الحقول.

{{% /alert %}}

يوضح الجزء التالي من الشفرة كيفية تعيين معلومات ملف PDF.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// فتح المستند
Document pdfDocument = new Document(dataDir + "SetFileInfo.pdf");

// تحديد معلومات الوثيقة
DocumentInfo docInfo = new DocumentInfo(pdfDocument);

docInfo.Author = "Aspose";
docInfo.CreationDate = DateTime.Now;
docInfo.Keywords = "Aspose.Pdf, DOM, API";
docInfo.ModDate = DateTime.Now;
docInfo.Subject = "معلومات PDF";
docInfo.Title = "تعيين معلومات مستند PDF";

dataDir = dataDir + "SetFileInfo_out.pdf";
// حفظ المستند الناتج
pdfDocument.Save(dataDir);
```
## الحصول على بيانات XMP الوصفية من ملف PDF

يتيح لك Aspose.PDF الوصول إلى بيانات XMP الوصفية لملف PDF. للحصول على بيانات ملف PDF الوصفية:

1. قم بإنشاء كائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) وافتح ملف PDF الذي تريد.
1. احصل على بيانات الوصفية للملف باستخدام خاصية [Metadata](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/metadata).

يوضح الجزء التالي من الكود كيفية الحصول على البيانات الوصفية من ملف PDF.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// فتح المستند
Document pdfDocument = new Document(dataDir + "GetXMPMetadata.pdf");

// الحصول على الخصائص
Console.WriteLine(pdfDocument.Metadata["xmp:CreateDate"]);
Console.WriteLine(pdfDocument.Metadata["xmp:Nickname"]);
Console.WriteLine(pdfDocument.Metadata["xmp:CustomProperty"]);
```

## تعيين بيانات XMP الوصفية في ملف PDF

يتيح لك Aspose.PDF تعيين البيانات الوصفية في ملف PDF.
Aspose.PDF يتيح لك تعيين البيانات الوصفية في ملف PDF.

1. إنشاء كائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. تعيين قيم البيانات الوصفية باستخدام خاصية [Metadata](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/metadata).
1. حفظ المستند المحدث باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) لكائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

يوضح الجزء التالي من الكود كيفية تعيين البيانات الوصفية في ملف PDF.

```csharp
// لأمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// فتح المستند
Document pdfDocument = new Document(dataDir + "SetXMPMetadata.pdf");

// تعيين الخصائص
pdfDocument.Metadata["xmp:CreateDate"] = DateTime.Now;
pdfDocument.Metadata["xmp:Nickname"] = "Nickname";
pdfDocument.Metadata["xmp:CustomProperty"] = "Custom Value";

dataDir = dataDir + "SetXMPMetadata_out.pdf";
// حفظ المستند
pdfDocument.Save(dataDir);
```
## إدراج بيانات الوصف مع بادئة

بعض المطورين يحتاجون إلى إنشاء فضاء أسماء جديد للبيانات الوصفية مع بادئة. يوضح الجزء التالي من الكود كيفية إدراج بيانات وصفية مع بادئة.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// فتح المستند
Document pdfDocument = new Document(dataDir + "SetXMPMetadata.pdf");
pdfDocument.Metadata.RegisterNamespaceUri("xmp", "http:// Ns.adobe.com/xap/1.0/"); // تمت إزالة بادئة Xmlns
pdfDocument.Metadata["xmp:ModifyDate"] = DateTime.Now;

dataDir = dataDir + "SetPrefixMetadata_out.pdf";
// حفظ المستند
pdfDocument.Save(dataDir);
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


