---
title: إضافة مرفق إلى مستند PDF
linktitle: إضافة مرفق إلى مستند PDF
type: docs
weight: 10
url: /ar/net/add-attachment-to-pdf-document/
description: تصف هذه الصفحة كيفية إضافة مرفق إلى ملف PDF باستخدام مكتبة Aspose.PDF لـ .NET
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/adding-to-a-pdf-document/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "إضافة مرفق إلى مستند PDF",
    "alternativeHeadline": "كيفية إضافة مرفقات إلى PDF",
    "author": {
        "@type": "Person",
        "name":"أناستاسيا هولوب",
        "givenName": "أناستاسيا",
        "familyName": "هولوب",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستند PDF",
    "keywords": "pdf, c#, مرفقات في pdf",
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
    "url": "/net/add-attachment-to-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-attachment-to-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "تصف هذه الصفحة كيفية إضافة مرفق إلى ملف PDF باستخدام مكتبة Aspose.PDF لـ .NET"
}
</script>
```
يمكن أن تحتوي المرفقات على مجموعة واسعة من المعلومات ويمكن أن تكون من أنواع ملفات متعددة. يشرح هذا المقال كيفية إضافة مرفق إلى ملف PDF.

الشفرة البرمجية التالية تعمل أيضًا مع واجهة [Aspose.Drawing](/pdf/ar/net/drawing/) الرسومية الجديدة.

1. إنشاء مشروع جديد بلغة C#.
1. إضافة مرجع إلى مكتبة Aspose.PDF DLL.
1. إنشاء كائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. إنشاء كائن [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification) مع الملف الذي تقوم بإضافته، ووصف الملف.
1. إضافة كائن [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification) إلى مجموعة [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) في كائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) باستخدام طريقة الإضافة في المجموعة.

مجموعة [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) تحتوي على جميع المرفقات في ملف PDF.
مجموعة [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) تحتوي على جميع المرفقات في ملف PDF.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

// فتح المستند
Document pdfDocument = new Document(dataDir + "AddAttachment.pdf");

// إعداد ملف جديد ليتم إضافته كمرفق
FileSpecification fileSpecification = new FileSpecification(dataDir + "test.txt", "ملف نصي نموذجي");

// إضافة المرفق إلى مجموعة مرفقات المستند
pdfDocument.EmbeddedFiles.Add(fileSpecification);

// حفظ المستند المحدث
pdfDocument.Save(dataDir + "AddllAnnotations_out.pdf");
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


