---
title: العمل مع AcroForms باستخدام بايثون
linktitle: AcroForms
type: docs
weight: 10
url: /python-net/acroforms/
description: مع Aspose.PDF لبايثون يمكنك إنشاء نموذج من البداية، ملء حقل النموذج في مستند PDF، استخراج البيانات من النموذج، إلخ.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "العمل مع AcroForms باستخدام بايثون",
    "alternativeHeadline": "خيارات العمل مع AcroForms في PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء مستند PDF",
    "keywords": "pdf, python, acroforms in pdf",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق مستندات Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "url": "/python-net/acroforms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/acroforms/"
    },
    "dateModified": "2023-02-04",
    "description": "مع Aspose.PDF لبايثون يمكنك إنشاء نموذج من البداية، ملء حقل النموذج في مستند PDF، استخراج البيانات من النموذج، إلخ."
}
</script>


## أساسيات AcroForms

**AcroForms** - تكنولوجيا نماذج PDF فريدة من Adobe. AcroForms هو نموذج موجه للصفحات. ظهرت لأول مرة في عام 1998. تقبل المدخلات بصيغة تنسيق البيانات أو FDF وصيغة بيانات نموذج XML أو xFDF. يدعم مزودو الطرف الثالث AcroForms. عندما قدمت Adobe AcroForms، أطلقوا عليها اسم "نموذج PDF، وهو من تأليف Adobe Acrobat Pro/Standard وليس نوعًا خاصًا من نموذج XFA الثابت أو الديناميكي. AcroForms محمولة وتعمل على جميع المنصات.

يمكنك استخدام AcroForms لإضافة صفحات إضافية إلى مستند نموذج PDF. بفضل مفهوم القوالب، يمكنك استخدام AcroForms لدعم تعبئة النموذج بسجلات قاعدة بيانات متعددة.

يدعم PDF 1.7 طريقتين مختلفتين لدمج البيانات ونماذج PDF.

*AcroForms (المعروفة أيضًا بنماذج Acrobat)*، تم تقديمها وتضمينها في مواصفات صيغة PDF 1.2.

لمزيد من التعلم التفصيلي لإمكانيات مكتبة Java، انظر المقالات التالية:

- [إنشاء AcroForm](/pdf/python-net/create-form) - إنشاء نموذج من البداية باستخدام Python.
- [ملء AcroForm](/pdf/python-net/fill-form) - ملء حقل النموذج في مستند PDF الخاص بك.
- [استخراج AcroForm](/pdf/python-net/extract-form) - الحصول على قيمة من جميع الحقول أو حقل فردي من مستند PDF.

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "applicationCategory": "PDF Manipulation Library for Python",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>