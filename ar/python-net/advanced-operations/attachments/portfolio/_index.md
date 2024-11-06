---
title: العمل مع المحفظة في PDF باستخدام Python
linktitle: المحفظة
type: docs
weight: 20
url: ar/python-net/portfolio/
description: كيفية إنشاء محفظة PDF باستخدام Python. يجب عليك استخدام ملف Microsoft Excel، ومستند Word، وملف صورة لإنشاء محفظة PDF.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "العمل مع المحفظة في PDF باستخدام Python",
    "alternativeHeadline": "إنشاء محفظة في وثيقة PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد وثيقة pdf في pdf",
    "keywords": "pdf, python, portfolio",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/python-net/portfolio/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/portfolio/"
    },
    "dateModified": "2023-02-04",
    "description": "كيفية إنشاء محفظة PDF باستخدام Python. يجب عليك استخدام ملف Microsoft Excel، ومستند Word، وملف صورة لإنشاء محفظة PDF."
}
</script>


إنشاء ملف PDF يعزز القدرة على تجميع وأرشفة أنواع مختلفة من الملفات في مستند واحد متسق. يمكن أن يتضمن مثل هذا المستند ملفات نصية، وصور، وجداول بيانات، وعروض تقديمية، ومواد أخرى، ويضمن أن يتم تخزين وتنظيم جميع المواد ذات الصلة في مكان واحد.

سيساعدك ملف PDF على عرض تقديمك بجودة عالية، أينما كنت تستخدمه. بشكل عام، إنشاء ملف PDF هو مهمة حديثة ومعاصرة للغاية.

## كيفية إنشاء ملف PDF 

تسمح مكتبة Aspose.PDF لبايثون عبر .NET بإنشاء مستندات PDF باستخدام فئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). أضف ملفًا إلى كائن document.collection بعد الحصول عليه باستخدام فئة [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/). وعندما يتم إضافة الملفات، استخدم طريقة [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) الخاصة بفئة Document لحفظ مستند ملف PDF.

يستخدم المثال التالي ملف Excel من مايكروسوفت، ومستند وورد وملف صورة لإنشاء ملف PDF.

الكود أدناه ينتج المحفظة التالية.

### محفظة PDF تم إنشاؤها باستخدام Aspose.PDF لـ Python

![محفظة PDF تم إنشاؤها باستخدام Aspose.PDF لـ Python](working-with-pdf-portfolio_1.jpg)

```python

    import aspose.pdf as ap

    # إنشاء كائن المستند
    document = ap.Document()

    # إنشاء كائن مجموعة المستندات
    document.collection = ap.Collection()

    # الحصول على الملفات لإضافتها إلى المحفظة
    excel = ap.FileSpecification(input_excel)
    word = ap.FileSpecification(input_doc)
    image = ap.FileSpecification(input_jpg)

    # توفير وصف للملفات
    excel.description = "ملف Excel"
    word.description = "ملف Word"
    image.description = "ملف صورة"

    # إضافة الملفات إلى مجموعة المستندات
    document.collection.append(excel)
    document.collection.append(word)
    document.collection.append(image)

    # حفظ مستند المحفظة
    document.save(output_pdf)
```

## إزالة الملفات من محفظة PDF

من أجل حذف/إزالة الملفات من محفظة PDF، حاول استخدام الأسطر البرمجية التالية.

```python

    import aspose.pdf as ap

    # فتح المستند
    document = ap.Document(input_pdf)
    document.collection.delete()

    # حفظ الملف المحدث
    document.save(output_pdf)
```

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