---
title: إضافة توقيع رقمي أو توقيع PDF رقميًا في C#
linktitle: توقيع PDF رقميًا
type: docs
weight: 10
url: /net/digitally-sign-pdf-file/
description: توقيع مستندات PDF رقميًا باستخدام C# أو VB.NET. تحقق أو قم بالتحقق من صحة PDFs الموقعة رقميًا باستخدام C# أو VB.NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "كيفية التوقيع على PDF رقميًا",
    "alternativeHeadline": "التعامل مع PDF الموقع رقميًا",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستند PDF",
    "keywords": "pdf, c#, توقيع pdf رقميًا",
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
    "url": "/net/digitally-sign-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/digitally-sign-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "توقيع مستندات PDF رقميًا باستخدام C# أو VB.NET. تحقق أو قم بالتحقق من صحة PDFs الموقعة رقميًا باستخدام C# أو VB.NET."
}
</script>
Aspose.PDF لـ .NET يدعم ميزة التوقيع الرقمي على ملفات PDF باستخدام فئة SignatureField. يمكنك أيضًا تصديق ملف PDF باستخدام شهادة PKCS12. شيء مشابه لـ [إضافة التواقيع والأمان في Adobe Acrobat](https://www.adobepress.com/articles/article.asp?p=1272495&seqNum=6).

عند التوقيع على مستند PDF باستخدام توقيع، فإنك تؤكد بشكل أساسي محتوياته "كما هي". ونتيجة لذلك، فإن أي تغييرات أخرى تتم بعد ذلك تبطل التوقيع وبالتالي، ستعرف إذا تم تغيير المستند. بينما يتيح لك تصديق المستند أولاً تحديد التغييرات التي يمكن للمستخدم إجراؤها على المستند دون إبطال التصديق.

بعبارة أخرى، سيظل المستند معتبرًا بأنه يحتفظ بسلامته ويمكن للمستلم أن يثق في المستند. لمزيد من التفاصيل، يرجى زيارة تصديق وتوقيع PDF. بشكل عام، يمكن مقارنة تصديق المستند بتوقيع الكود على ملف تنفيذي لـ .NET.

يعمل أيضًا الكود التالي مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).
يعمل الجزء التالي من الشيفرة أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

## ميزات التوقيع Aspose.PDF لـ .NET

يمكننا استخدام الفئات والطرق التالية لتوقيع PDF

- الفئة [DocMDPSignature](https://reference.aspose.com/pdf/net/aspose.pdf.forms/docmdpsignature)
- التعداد [DocMDPAccessPermissions](https://reference.aspose.com/pdf/net/aspose.pdf.forms/docmdpaccesspermissions)
- الخاصية [IsCertified](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/properties/iscertified) في فئة [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature)

## توقيع PDF باستخدام التواقيع الرقمية

```csharp
public static void SignDocument()
{
    string inFile = System.IO.Path.Combine(_dataDir,"DigitallySign.pdf");
    string outFile = System.IO.Path.Combine(_dataDir,"DigitallySign_out.pdf");
    using (Document document = new Document(inFile))
    {
        using (PdfFileSignature signature = new PdfFileSignature(document))
        {
            PKCS7 pkcs = new PKCS7(@"C:\Keys\test.pfx", "Pa$$w0rd2020"); // استخدم أشياء PKCS7/PKCS7Detached
            signature.Sign(1, true, new System.Drawing.Rectangle(300, 100, 400, 200),pkcs);
            // حفظ ملف PDF الناتج
            signature.Save(outFile);
        }
    }
}
```
## إضافة الطابع الزمني إلى التوقيع الرقمي

### كيفية التوقيع الرقمي على ملف PDF مع طابع زمني

Aspose.PDF لـ .NET يدعم التوقيع الرقمي على ملف PDF باستخدام خادم الطابع الزمني أو خدمة الويب.

لتحقيق هذا المطلب، تم إضافة فئة [TimestampSettings](https://reference.aspose.com/pdf/net/aspose.pdf/timestampsettings) إلى فضاء الأسماء Aspose.PDF. يرجى الاطلاع على الشفرة التالية التي تحصل على الطابع الزمني وتضيفه إلى مستند PDF:

```csharp
public static void SignWithTimeStampServer()
{
    using (Document document = new Document(System.IO.Path.Combine(_dataDir,"SimpleResume.pdf")))
    {
        using (PdfFileSignature signature = new PdfFileSignature(document))
        {
            PKCS7 pkcs = new PKCS7(@"C:\Keys\test.pfx", "Start2020");
            TimestampSettings timestampSettings = new TimestampSettings("https://freetsa.org/tsr", string.Empty); // يمكن تجاهل اسم المستخدم/كلمة المرور
            pkcs.TimestampSettings = timestampSettings;
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(100, 100, 200, 100);
            // إنشاء أي من أنواع التوقيع الثلاثة
            signature.Sign(1, "سبب التوقيع", "الاتصال", "الموقع", true, rect, pkcs);
            // حفظ ملف PDF الناتج
            signature.Save(System.IO.Path.Combine(_dataDir, "DigitallySignWithTimeStamp_out.pdf"));
        }
    }
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
                "areaServed": "الولايات المتحدة",
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
    "applicationCategory": "مكتبة التلاعب بملفات PDF لـ .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "ويندوز، ماك، لينكس",
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

