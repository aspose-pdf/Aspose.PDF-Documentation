---
title: إزالة الجداول من ملف PDF موجود
linktitle: إزالة الجداول
type: docs
weight: 50
url: /python-net/remove-tables-from-existing-pdf/
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "إزالة الجداول من ملف PDF موجود",
    "alternativeHeadline": "كيفية حذف الجداول من PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء مستندات PDF",
    "keywords": "PDF، بايثون، إزالة الجدول، حذف الجداول",
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
    "url": "/python-net/remove-tables-from-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/remove-tables-from-existing-pdf/"
    },
    "dateModified": "2023-02-04",
    "description": ""
}
</script>


{{% alert color="primary" %}}

يوفر Aspose.PDF for Python عبر .NET القدرة على إدراج/إنشاء جدول داخل مستند PDF أثناء إنشائه من الصفر أو يمكنك أيضًا إضافة كائن الجدول في أي مستند PDF موجود. ومع ذلك، قد يكون لديك متطلب [للتعامل مع الجداول في PDF الموجود](https://docs.aspose.com/pdf/python-net/manipulate-tables-in-existing-pdf/) حيث يمكنك تحديث المحتويات في خلايا الجدول الموجودة. ومع ذلك، قد تصادف متطلبًا لإزالة كائنات الجدول من مستند PDF موجود.

{{% /alert %}}

لإزالة الجداول، نحتاج إلى استخدام فئة [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) للحصول على الجداول في PDF الموجود ثم استدعاء [remove()](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods).

## إزالة الجدول من مستند PDF

لقد أضفنا وظيفة جديدة وهي.
 [remove()](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods) إلى [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) الموجودة من أجل إزالة جدول من مستند PDF. بمجرد أن يجد الماص الجداول على الصفحة بنجاح، يصبح قادرًا على إزالتها. يرجى مراجعة مقتطف الشيفرة التالي الذي يوضح كيفية إزالة جدول من مستند PDF:

```python

    import aspose.pdf as ap

    # تحميل مستند PDF موجود
    pdf_document = ap.Document(input_file)
    # إنشاء كائن TableAbsorber للعثور على الجداول
    absorber = ap.text.TableAbsorber()
    # زيارة الصفحة الأولى باستخدام الماص
    absorber.visit(pdf_document.pages[1])
    # الحصول على الجدول الأول في الصفحة
    table = absorber.table_list[0]
    # إزالة الجدول
    absorber.remove(table)
    # حفظ PDF
    pdf_document.save(output_file)
```

## إزالة جداول متعددة من مستند PDF

قد يحتوي مستند PDF في بعض الأحيان على أكثر من جدول وقد تحتاج إلى إزالة جداول متعددة منه. في سبيل إزالة جداول متعددة من مستند PDF، يرجى استخدام مقطع الكود التالي:

```python

    import aspose.pdf as ap

    # تحميل مستند PDF موجود
    pdf_document = ap.Document(input_file)
    # إنشاء كائن TableAbsorber للعثور على الجداول
    absorber = ap.text.TableAbsorber()
    # زيارة الصفحة الثانية مع المستخدم
    absorber.visit(pdf_document.pages[1])
    # الحصول على نسخة من مجموعة الجداول
    tables = absorber.table_list
    #  التحلق عبر نسخة المجموعة وإزالة الجداول
    for table in tables:
        absorber.remove(table)
    # حفظ المستند
    pdf_document.save(output_file)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
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
    "applicationCategory": "PDF Manipulation Library for Python via .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>