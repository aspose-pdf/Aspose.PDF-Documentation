---
title: العمل مع AcroForms
linktitle: AcroForms
type: docs
weight: 10
url: /net/acroforms/
description: من خلال Aspose.PDF لـ .NET يمكنك إنشاء نموذج من البداية، ملء حقل النموذج في مستند PDF، استخراج البيانات من النموذج، وغير ذلك.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "العمل مع AcroForms",
    "alternativeHeadline": "خيارات العمل مع AcroForms في PDF",
    "author": {
        "@type": "Person",
        "name":"أناستاسيا هولوب",
        "givenName": "أناستاسيا",
        "familyName": "هولوب",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء مستند PDF",
    "keywords": "pdf, c#, acroforms في pdf",
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
    "url": "/net/acroforms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/acroforms/"
    },
    "dateModified": "2022-02-04",
    "description": "من خلال Aspose.PDF لـ .NET يمكنك إنشاء نموذج من البداية، ملء حقل النموذج في مستند PDF، استخراج البيانات من النموذج، وغير ذلك."
}
</script>

## أساسيات AcroForms

**AcroForms** هي تقنية النماذج الأصلية لملفات PDF. AcroForms هي نموذج موجه بالصفحات. تم تقديمها لأول مرة في عام 1998. تقبل الإدخال في صيغة بيانات النماذج أو FDF وصيغة بيانات النماذج XML أو xFDF. تدعم الشركات الطرف الثالث AcroForms. عندما قدمت Adobe AcroForms، أشارت إليها بأنها "نموذج PDF تم إنشاؤه باستخدام Adobe Acrobat Pro/Standard وليس نوعًا خاصًا من نموذج XFA الثابت أو الديناميكي. Acroforms محمولة وتعمل على جميع المنصات.

يمكنك استخدام AcroForms لإضافة صفحات إضافية إلى مستند نموذج PDF. بفضل مفهوم القوالب، يمكنك استخدام AcroForms لدعم ملء النموذج بعدة سجلات قواعد بيانات.

يدعم PDF 1.7 طريقتين مختلفتين لدمج البيانات ونماذج PDF.

*AcroForms (المعروفة أيضًا باسم نماذج Acrobat)*، تم تقديمها وتضمينها في مواصفات تنسيق PDF 1.2.

*نماذج Adobe XML Forms Architecture (XFA)*، تم تقديمها في مواصفات تنسيق PDF 1.5 كميزة اختيارية (لا يتم تضمين مواصفات XFA في مواصفات PDF، فهي مشار إليها فقط).
*نماذج أرشيف XML لـ Adobe (XFA)*، تم تقديمها في مواصفات تنسيق PDF 1.5 كميزة اختيارية (لا تتضمن مواصفات XFA في مواصفات PDF، بل يتم الإشارة إليها فقط.

لفهم **Acroforms** مقابل نماذج **XFA**، نحتاج إلى فهم الأساسيات أولاً. كنقطة بداية، كلاهما نماذج PDF التي يمكنك استخدامها. Acroforms هو الأقدم، تم إنشاؤه في عام 1998، ولا يزال يُشار إليه باعتباره النموذج الكلاسيكي لـ PDF. نماذج XFA هي صفحات ويب يمكنك حفظها كملف PDF، وظهرت في عام 2003. استغرق الأمر بعض الوقت قبل أن يبدأ PDF في قبول نماذج XFA.

لدى AcroForms قدرات لا توجد في XFA وبالعكس، XFA لديه بعض القدرات التي لا توجد في AcroForms. على سبيل المثال:

- يدعم AcroForms مفهوم "القوالب"، مما يسمح بإضافة صفحات إضافية إلى مستند نموذج PDF لدعم تعبئة النموذج بسجلات قواعد بيانات متعددة.
- يدعم XFA مفهوم إعادة تدفق الوثيقة مما يسمح للحقل بتغيير حجمه إذا لزم الأمر لاستيعاب البيانات.

لمزيد من التعلم المفصل لقدرات مكتبة Java، راجع المقالات التالية:
للحصول على دراسة أكثر تفصيلاً لقدرات مكتبة Java، راجع المقالات التالية:

- [إنشاء AcroForm](/pdf/net/create-form) - إنشاء نموذج من البداية باستخدام C#.
- [ملء AcroForm](/pdf/net/fill-form) - ملء حقل النموذج في مستند PDF الخاص بك.
- [استخراج AcroForm](/pdf/net/extract-form) - الحصول على قيمة من جميع الحقول أو حقل فردي من مستند PDF.
- [تعديل AcroForm](/pdf/net/modifing-form) - الحصول أو تعيين FieldLimit، تعيين خط حقل النموذج وغيرها.
- [نشر بيانات AcroForm](/pdf/net/posting-acroform-data/) - استيراد وتصدير بيانات النموذج إلى ملف XML ومنه.
- [استيراد وتصدير البيانات](/pdf/net/import-and-export-data/) - استيراد وتصدير البيانات باستخدام فئة النموذج.

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

