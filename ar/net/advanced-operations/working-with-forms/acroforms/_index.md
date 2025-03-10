---
title: العمل مع AcroForms
linktitle: أكرو فورمز
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ar/net/acroforms/
description: مع Aspose.PDF for .NET يمكنك إنشاء نموذج من الصفر، ملء حقول النموذج في مستند PDF، استخراج البيانات من النموذج، وما إلى ذلك.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with AcroForms",
    "alternativeHeadline": "Enhance PDF forms with flexible AcroForms functionality",
    "abstract": "Aspose.PDF for .NET يقدم قدرات محسنة للعمل مع AcroForms، مما يمكّن المستخدمين من إنشاء نماذج بكفاءة من الصفر، ملء حقول PDF، واستخراج البيانات بسلاسة. تدعم هذه الميزة القوية دمج سجلات قاعدة بيانات متعددة، مما يسمح بإدارة نماذج ديناميكية وتجربة مستخدم سلسة",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "AcroForms, PDF forms technology, create a form, fill form fields, extract data, database records, Templates, modify AcroForms, posting AcroForm data, import and export data",
    "wordcount": "484",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
    "url": "/net/acroforms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/acroforms/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF يمكن أن يؤدي مهام بسيطة وسهلة ولكن أيضًا يمكنه التعامل مع أهداف أكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## أساسيات AcroForms

**AcroForms** هي تقنية نماذج PDF الأصلية. AcroForms هي نموذج موجه نحو الصفحة. تم تقديمها لأول مرة في عام 1998. تقبل المدخلات بتنسيق بيانات النماذج أو FDF وتنسيق بيانات النماذج XML أو xFDF. تدعم الشركات الخارجية AcroForms. عندما قدمت Adobe AcroForms، أشاروا إليها على أنها "نموذج PDF تم تأليفه باستخدام Adobe Acrobat Pro/Standard وليس نوعًا خاصًا من نموذج XFA الثابت أو الديناميكي. AcroForms قابلة للنقل وتعمل على جميع الأنظمة الأساسية.

يمكنك استخدام AcroForms لإضافة صفحات إضافية إلى مستند نموذج PDF. بفضل مفهوم القوالب، يمكنك استخدام AcroForms لدعم ملء النموذج بسجلات قاعدة بيانات متعددة.

يدعم PDF 1.7 طريقتين مختلفتين لدمج البيانات ونماذج PDF.

*AcroForms (المعروفة أيضًا باسم نماذج Acrobat)*، تم تقديمها وتضمينها في مواصفة تنسيق PDF 1.2.

*نماذج Adobe XML Forms Architecture (XFA)*، تم تقديمها في مواصفة تنسيق PDF 1.5 كميزة اختيارية (لم يتم تضمين مواصفة XFA في مواصفة PDF، بل تم الإشارة إليها فقط).

لفهم **Acroforms** مقابل **XFA**، نحتاج إلى فهم الأساسيات أولاً. للبدء، كلاهما نماذج PDF يمكنك استخدامها. Acroforms هي الأقدم، تم إنشاؤها في عام 1998، ولا تزال تُعتبر نموذج PDF الكلاسيكي. نماذج XFA هي صفحات ويب يمكنك حفظها كملف PDF، وظهرت في عام 2003. استغرق الأمر بعض الوقت قبل أن يبدأ PDF في قبول نماذج XFA.

تتمتع AcroForms بقدرات غير موجودة في XFA، وعلى العكس من ذلك، فإن XFA لديها بعض القدرات غير الموجودة في AcroForms. على سبيل المثال:

- تدعم AcroForms مفهوم "القوالب"، مما يسمح بإضافة صفحات إضافية إلى مستند نموذج PDF لدعم ملء النموذج بسجلات قاعدة بيانات متعددة.
- تدعم XFA مفهوم إعادة تدفق المستند مما يسمح لحقل بتغيير حجمه إذا لزم الأمر لاستيعاب البيانات.

للتعلم بشكل أكثر تفصيلًا عن قدرات مكتبة Java، راجع المقالات التالية:

- [إنشاء AcroForm](/pdf/ar/net/create-form) - إنشاء نموذج من الصفر باستخدام C#.
- [ملء AcroForm](/pdf/ar/net/fill-form) - ملء حقل النموذج في مستند PDF الخاص بك.
- [استخراج AcroForm](/pdf/ar/net/extract-form) - الحصول على قيمة من جميع الحقول أو حقل فردي من مستند PDF.
- [تعديل AcroForm](/pdf/ar/net/modifing-form) - الحصول على أو تعيين FieldLimit، تعيين خط حقل النموذج وما إلى ذلك.
- [نشر بيانات AcroForm](/pdf/ar/net/posting-acroform-data/) - استيراد وتصدير بيانات النموذج إلى ملف XML.
- [استيراد وتصدير البيانات](/pdf/ar/net/import-and-export-data/) - استيراد وتصدير البيانات باستخدام فئة النموذج.
- [إزالة النماذج من PDF](/pdf/ar/net/remove-form/) - إزالة النص بناءً على النوع الفرعي/النموذج، حذف جميع النماذج.
- [استيراد وتصدير البيانات بتنسيق JSON](/pdf/ar/net/import-export-json/) - استيراد وتصدير البيانات باستخدام JSON

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