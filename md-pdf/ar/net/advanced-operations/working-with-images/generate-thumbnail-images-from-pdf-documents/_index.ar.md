---
title: توليد صور مصغرة من مستندات PDF
linktitle: توليد صور مصغرة
type: docs
weight: 110
url: /net/generate-thumbnail-images-from-pdf-documents/
description: تصف هذا القسم كيفية توليد صور مصغرة من مستندات PDF
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "توليد صور مصغرة من مستندات PDF",
    "alternativeHeadline": "كيفية توليد صور مصغرة من ملف PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستندات PDF",
    "keywords": "pdf, c#, توليد صور مصغرة",
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
    "url": "/net/generate-thumbnail-images-from-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/generate-thumbnail-images-from-pdf-documents/"
    },
    "dateModified": "2022-02-04",
    "description": "تصف هذا القسم كيفية توليد صور مصغرة من مستندات PDF"
}
</script>
{{% alert color="primary" %}}
مجموعة Adobe Acrobat SDK هي مجموعة من الأدوات التي تساعدك على تطوير البرمجيات التي تتفاعل مع تقنية Acrobat. تحتوي المجموعة على ملفات رأسية، مكتبات الأنواع، أدوات بسيطة، شفرة نموذجية، وتوثيق.

باستخدام Acrobat SDK، يمكنك تطوير برمجيات تتكامل مع Acrobat وAdobe Reader بعدة طرق:

- **جافا سكريبت** — كتابة البرامج النصية، سواء في مستند PDF فردي أو خارجياً، لتوسيع وظائف Acrobat أو Adobe Reader.
- **الإضافات** — إنشاء إضافات مرتبطة ديناميكيًا وتوسع وظائف Acrobat أو Adobe Reader.
- **التواصل بين التطبيقات** — كتابة عملية تطبيق منفصلة تستخدم التواصل بين التطبيقات (IAC) للتحكم في وظائف Acrobat. يتم دعم DDE وOLE على Microsoft® Windows®، وأحداث Apple/AppleScript على Mac OS®. IAC غير متاحة على UNIX®.

Aspose.PDF لـ .NET يوفر الكثير من نفس الوظائف، مما يحررك من الاعتماد على أتمتة Adobe Acrobat.
{{% /alert %}}
Aspose.PDF لـ .NET يوفر الكثير من الوظائف نفسها، مما يحررك من الاعتماد على أدوات أدوبي أكروبات أوتوميشن.

## تطوير التطبيق باستخدام واجهة برمجة تطبيقات أكروبات للتواصل بين التطبيقات

فكر في واجهة برمجة تطبيقات أكروبات على أنها تحتوي على طبقتين مميزتين تستخدمان كائنات التواصل بين التطبيقات لأكروبات (IAC):

- طبقة تطبيق أكروبات (AV). تتيح لك طبقة AV التحكم في كيفية عرض المستند. على سبيل المثال، يقع عرض كائن المستند في الطبقة المرتبطة بأكروبات.
- طبقة المستند المحمول (PD). توفر طبقة PD الوصول إلى المعلومات داخل المستند، مثل صفحة. من طبقة PD يمكنك أداء التلاعبات الأساسية بمستندات PDF، مثل حذف الصفحات أو نقلها أو استبدالها، بالإضافة إلى تغيير خصائص التعليق التوضيحي. يمكنك أيضًا طباعة صفحات PDF، وتحديد النص، والوصول إلى النص المعدل، وإنشاء أو حذف الصور المصغرة.

نظرًا لأننا نهدف إلى تحويل صفحات PDF إلى صور مصغرة، فإننا نركز أكثر على IAC.
كما أننا نعتزم تحويل صفحات PDF إلى صور مصغرة، فنحن نركز أكثر على IAC.

### نهج أكروبات

لتوليد الصور المصغرة لكل مستند، استخدمنا Adobe Acrobat SDK 7.0 و Microsoft .NET Framework 2.0.

يجمع [Acrobat SDK](https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/) مع النسخة الكاملة من Adobe Acrobat تعرض مكتبة COM من الكائنات (للأسف، Adobe Reader المجاني لا يعرض واجهات COM) التي يمكن استخدامها للتلاعب والوصول إلى معلومات PDF. باستخدام هذه الكائنات COM عبر COM Interop، قم بتحميل مستند PDF، احصل على الصفحة الأولى وقم بعرض هذه الصفحة إلى الحافظة. ثم، باستخدام .NET Framework، انسخ هذا إلى بتماب، قم بتحجيم ودمج الصورة واحفظ النتيجة كملف GIF أو PNG.

بمجرد تثبيت Adobe Acrobat، استخدم regedit.exe وابحث تحت HKEY_CLASSES_ROOT عن إدخال يسمى AcroExch.PDDoc.

**السجل يظهر إدخال AcroExch.PDDDoc**

![todo:image_alt_text](generate-thumbnail-images-from-pdf-documents_1.png)
![todo:image_alt_text](generate-thumbnail-images-from-pdf-documents_1.png)

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Images-CreateThumbnailImagesUsingAdobe-CreateThumbnailImagesUsingAdobe.cs" >}}

## نهج Aspose.PDF لـ .NET

يوفر Aspose.PDF لـ .NET دعمًا واسعًا للتعامل مع مستندات PDF. كما يدعم القدرة على تحويل صفحات مستندات PDF إلى مجموعة متنوعة من تنسيقات الصور. يمكن تحقيق الوظيفة المذكورة أعلاه بسهولة باستخدام Aspose.PDF لـ .NET.

لدى Aspose.PDF فوائد مميزة:

- لا تحتاج إلى تثبيت Adobe Acrobat على نظامك للعمل مع ملفات PDF.
- استخدام Aspose.PDF لـ .NET بسيط وسهل الفهم مقارنةً بأتمتة Acrobat.

إذا كنا بحاجة لتحويل صفحات PDF إلى صور JPEG، فإن الفضاء الاسمي [Aspose.PDF.Devices](https://reference.aspose.com/pdf/net/aspose.pdf.devices) يوفر فئة تُدعى [JpegDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/jpegdevice) لتقديم صفحات PDF في صور JPEG.
إذا احتجنا إلى تحويل صفحات PDF إلى صور JPEG، فإن الفضاء الاسمي [Aspose.PDF.Devices](https://reference.aspose.com/pdf/net/aspose.pdf.devices) يوفر فئة تُسمى [JpegDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/jpegdevice) لتقديم صفحات PDF على شكل صور JPEG.

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Images-CreateThumbnailImages-CreateThumbnailImages.cs" >}}

{{% alert color="primary" %}}

- شكرًا لـ CodeProject على [إنشاء صورة مصغرة من مستند PDF](https://www.codeproject.com/Articles/5887/Generate-Thumbnail-Images-from-PDF-Documents).
- شكرًا لـ Acrobat على [مرجع SDK الخاص بـ Acrobat](https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/documentation.html).

{{% /alert %}}

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

