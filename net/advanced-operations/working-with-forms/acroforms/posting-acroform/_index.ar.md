---
title: نشر بيانات AcroForm
linktitle: نشر AcroForm
type: docs
weight: 50
url: /net/posting-acroform-data/
description: يمكنك استيراد وتصدير بيانات النموذج إلى ملف XML باستخدام فضاء الأسماء Aspose.Pdf.Facades في Aspose.PDF لـ .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "نشر بيانات AcroForm",
    "alternativeHeadline": "استيراد وتصدير بيانات النموذج إلى ملف XML",
    "author": {
        "@type": "Person",
        "name":"أناستاسيا هولوب",
        "givenName": "أناستاسيا",
        "familyName": "هولوب",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد وثيقة PDF",
    "keywords": "pdf, c#, نشر بيانات acroform",
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
    "url": "/net/posting-acroform-data/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/posting-acroform-data/"
    },
    "dateModified": "2022-02-04",
    "description": "يمكنك استيراد وتصدير بيانات النموذج إلى ملف XML باستخدام فضاء الأسماء Aspose.Pdf.Facades في Aspose.PDF لـ .NET."
}
</script>

{{% alert color="primary" %}}

AcroForm هو نوع مهم من مستند PDF. يمكنك ليس فقط إنشاء وتعديل AcroForm باستخدام [Aspose.Pdf.Facades namespace](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace)، ولكن أيضًا استيراد وتصدير بيانات النموذج إلى ملف XML وملف. يسمح مساحة الاسم Aspose.Pdf.Facades في Aspose.PDF لـ .NET بتنفيذ ميزة أخرى من AcroForm، والتي تساعدك على نشر بيانات AcroForm إلى صفحة ويب خارجية. تقرأ هذه الصفحة الويب بعد ذلك متغيرات النشر وتستخدم هذه البيانات لمزيد من المعالجة. هذه الميزة مفيدة في الحالات التي لا تريد فقط الاحتفاظ بالبيانات في ملف PDF، بل تريد إرسالها إلى خادمك ثم حفظها في قاعدة بيانات إلخ.

{{% /alert %}}

## تفاصيل التنفيذ

يعمل الجزء التالي من الشفرة أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

في هذه المقالة، حاولنا إنشاء AcroForm باستخدام [Aspose.Pdf.Facades namespace](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace).
في هذا المقال، حاولنا إنشاء نموذج أكرو باستخدام [فضاء أسماء Aspose.Pdf.Facades](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace).

```csharp
// إنشاء مثال على فئة FormEditor وربط ملفات pdf الإدخال والإخراج
Aspose.Pdf.Facades.FormEditor editor = new Aspose.Pdf.Facades.FormEditor("input.pdf","output.pdf");

// إنشاء حقول نموذج أكرو - لقد أنشأت فقط حقلين للبساطة
editor.AddField(Aspose.PDF.Facades.FieldType.Text, "firstname", 1, 100, 600, 200, 625);
editor.AddField(Aspose.PDF.Facades.FieldType.Text, "lastname", 1, 100, 550, 200, 575);

// إضافة زر إرسال وتعيين عنوان URL المستهدف
editor.AddSubmitBtn("submitbutton", 1, "Submit", "http://localhost/csharptesting/show.aspx", 100, 450, 150, 475);

// حفظ ملف pdf الناتج
editor.Save();
```

{{% alert color="primary" %}}

يوضح الجزء التالي من الشفرة كيفية استلام القيم المنشورة على صفحة الويب المستهدفة.
يعرض الجزء التالي من الكود كيفية استقبال القيم المنشورة على صفحة الويب المستهدفة.

```csharp
// Show the posted values on the target web page
Response.Write("Hello " + Request.Form.Get("firstname") + " " + Request.Form.Get("lastname"));
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
    "applicationCategory": "مكتبة التلاعب بملفات PDF لـ .NET",
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


