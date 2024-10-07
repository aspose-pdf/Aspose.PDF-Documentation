---
title: تعديل AcroForm
linktitle: تعديل AcroForm
type: docs
weight: 40
url: /net/modifing-form/
description: تعديل النموذج في ملف PDF الخاص بك باستخدام مكتبة Aspose.PDF لـ .NET. يمكنك إضافة أو إزالة الحقول في النموذج الحالي، والحصول وتعيين حد الحقل وغيرها.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "تعديل AcroForm",
    "alternativeHeadline": "كيفية تعديل AcroForm",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد وثيقة PDF",
    "keywords": "pdf, c#, تعديل acroform",
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
    "url": "/net/modifing-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/modifing-form/"
    },
    "dateModified": "2022-02-04",
    "description": "تعديل النموذج في ملف PDF الخاص بك باستخدام مكتبة Aspose.PDF لـ .NET. يمكنك إضافة أو إزالة الحقول في النموذج الحالي، والحصول وتعيين حد الحقل وغيرها."
}
</script>
الشفرة التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

## الحصول على حد الحقل أو تعيينه

تتيح لك طريقة SetFieldLimit(field, limit) في فئة FormEditor تعيين حد للحقل، وهو العدد الأقصى للأحرف التي يمكن إدخالها في حقل.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// إضافة حقل بحد
FormEditor form = new FormEditor();

form.BindPdf( dataDir + "input.pdf");
form.SetFieldLimit("textbox1", 15);
dataDir = dataDir + "SetFieldLimit_out.pdf";
form.Save(dataDir);
```

بالمثل، لدى Aspose.PDF طريقة تحصل على حد الحقل باستخدام نهج DOM. توضح الشفرة التالية الخطوات.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
// الحصول على الحد الأقصى لحد الحقل باستخدام DOM
Document doc = new Document(dataDir + "FieldLimit.pdf");
Console.WriteLine("الحد: " + (doc.Form["textbox1"] as TextBoxField).MaxLen);
```
يمكنك أيضاً الحصول على نفس القيمة باستخدام نطاق *Aspose.PDF.Facades* باستخدام مقتطف الكود التالي.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
// الحصول على الحد الأقصى للحقل باستخدام Facades
Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
form.BindPdf(dataDir + "FieldLimit.pdf");
Console.WriteLine("Limit: " + form.GetFieldLimit("textbox1"));
```

## تعيين الخط المخصص لحقل النموذج

يمكن تكوين حقول النماذج في ملفات PDF الخاصة بـ Adobe لاستخدام الخطوط الافتراضية المحددة.
يمكن تكوين حقول النماذج في ملفات Adobe PDF لاستخدام خطوط افتراضية محددة.

يوضح الجزء التالي من الكود كيفية تعيين الخط الافتراضي لحقول نموذج PDF.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى مجلد الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// فتح المستند
Document pdfDocument = new Document(dataDir + "FormFieldFont14.pdf");

// الحصول على حقل نموذج معين من المستند
Aspose.Pdf.Forms.Field field = pdfDocument.Form["textbox1"] as Aspose.Pdf.Forms.Field;

// إنشاء كائن الخط
Aspose.Pdf.Text.Font font = FontRepository.FindFont("ComicSansMS");

// تعيين معلومات الخط لحقل النموذج
// Field.DefaultAppearance = new Aspose.Pdf.Forms.in.DefaultAppearance(font, 10, System.Drawing.Color.Black);

dataDir = dataDir + "FormFieldFont14_out.pdf";
// حفظ المستند المحدث
pdfDocument.Save(dataDir);
```

## إضافة/إزالة حقول في نموذج موجود

جميع حقول النموذج موجودة في مجموعة Form لكائن المستند.
جميع حقول النموذج موجودة في مجموعة النموذج الخاصة بكائن المستند.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// فتح المستند
Document pdfDocument = new Document(dataDir + "DeleteFormField.pdf");

// حذف حقل معين بالاسم
pdfDocument.Form.Delete("textbox1");
dataDir = dataDir + "DeleteFormField_out.pdf";
// حفظ المستند المعدل
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


