---
title: Fill AcroForm - Fill PDF Form using C#
linktitle: Fill AcroForm
type: docs
weight: 20
url: /net/fill-form/
keywords: Fill PDF Form C#
description: يمكنك تعبئة النماذج في مستند PDF الخاص بك باستخدام مكتبة Aspose.PDF لـ .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Fill AcroForm",
    "alternativeHeadline": "كيفية تعبئة AcroForm في PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستند PDF",
    "keywords": "pdf, c#, fill acroform",
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
    "url": "/net/fill-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/fill-form/"
    },
    "dateModified": "2022-02-04",
    "description": "يمكنك تعبئة النماذج في مستند PDF الخاص بك باستخدام مكتبة Aspose.PDF لـ .NET."
}
</script>
يعمل هذا المقتطف من الكود أيضاً مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

## ملء حقل النموذج في مستند PDF

لملء حقل النموذج، احصل على الحقل من مجموعة النموذج الخاصة بكائن المستند. ثم قم بتعيين قيمة الحقل باستخدام خاصية القيمة الخاصة بالحقل.

هذا المثال يختار TextBoxField ويعين قيمته باستخدام خاصية القيمة.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// فتح المستند
Document pdfDocument = new Document(dataDir + "FillFormField.pdf");

// الحصول على حقل
TextBoxField textBoxField = pdfDocument.Form["textbox1"] as TextBoxField;

// تعديل قيمة الحقل
textBoxField.Value = "القيمة المراد ملؤها في الحقل";
dataDir = dataDir + "FillFormField_out.pdf";
// حفظ المستند المحدث
pdfDocument.Save(dataDir);
```

