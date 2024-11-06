---
title: تحديد فاصل السطر
linktitle: تحديد فاصل السطر
type: docs
weight: 70
url: ar/python-net/determine-line-break/
description: تعرف على كيفية تحديد فاصل السطر في TextFragment متعدد الأسطر باستخدام Python
lastmod: "2024-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "تحديد فاصل السطر",
    "alternativeHeadline": "كيفية تحديد فاصل السطر في TextFragment",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء مستندات pdf",
    "keywords": "pdf, python, تحديد فاصل السطر",
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
                "contactType": "المبيعات",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "المبيعات",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "المبيعات",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/determine-line-break/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/determine-line-break/"
    },
    "dateModified": "2024-02-04",
    "description": "تعرف على كيفية تحديد فاصل السطر في TextFragment متعدد الأسطر باستخدام Python"
}
</script>


## تتبع انكسار الخط للنص متعدد الأسطر

يُظهر مقطع الشيفرة التالي كيفية تتبع سلوك انكسار الخط لنص متعدد الأسطر داخل مستند PDF.

تم تعريف دالة track_line_breaking() لعرض هذه الوظيفة. يبدأ بتحديد مسارات ملفات الإخراج لكل من مستند PDF الذي تم إنشاؤه وملف نصي مرافق يحتوي على معلومات حول انكسار الخط.

داخل الدالة، يتم إنشاء كائن مستند PDF جديد، ويتم إضافة صفحة جديدة إليه. بعد ذلك، يتم استخدام حلقة لتوليد أربع نسخ من TextFragment تحتوي على نص مع فواصل أسطر ("\r\n") مدرجة داخل السلسلة لمحاكاة النص متعدد الأسطر.

يتم تكوين كل TextFragment بحجم خط يبلغ 20 نقطة قبل إضافته إلى فقرات الصفحة.

بعد إضافة جميع TextFragment، يتم حفظ المستند.

ثم تتابع الدالة لاستخراج الإشعارات حول انكسار الخط من الصفحة الثانية من مستند PDF الذي تم إنشاؤه باستخدام طريقة get_notifications().
 هذه الإشعارات تُكتب إلى ملف نصي محدد مسبقًا.

يوضح هذا المقتطف من الكود كيفية إنشاء وثيقة PDF تحتوي على نص متعدد الأسطر ثم استخراج معلومات بشأن سلوك كسر الأسطر، مما يوفر رؤى حول كيفية تنسيق النص داخل الوثيقة.

```python

    import aspose.pdf as ap

    def track_line_breaking():
        """تتبع كسر الأسطر في TextFragment متعدد الأسطر"""
        output_pdf = DIR_OUTPUT_TEXTS + "track_line_breaking.pdf"
        output_txt = DIR_OUTPUT_TEXTS + "track_line_breaking.txt"

        # إنشاء كائن وثيقة جديد
        document = ap.Document()
        page = document.pages.add()

        for i in range(4):
            text = ap.text.TextFragment(
                "Lorem ipsum \r\ndolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
            )
            text.text_state.font_size = 20
            page.paragraphs.add(text)
        document.save(output_pdf)

        notifications = document.pages[1].get_notifications()
        with open(output_txt, "w") as f:
            f.write(notifications)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF لمكتبة .NET",
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
                "contactType": "مبيعات",
                "areaServed": "الولايات المتحدة",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "مبيعات",
                "areaServed": "المملكة المتحدة",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "مبيعات",
                "areaServed": "أستراليا",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "مكتبة معالجة PDF لـ .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "ويندوز، ماك أو إس، لينكس",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>