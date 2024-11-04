---
title: نقل صفحات PDF برمجياً باستخدام بايثون
linktitle: نقل صفحات PDF
type: docs
weight: 100
url: /python-net/move-pages/
description: حاول نقل الصفحات إلى الموقع المطلوب أو إلى نهاية ملف PDF باستخدام Aspose.PDF لبايثون عبر .NET.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "نقل صفحات PDF برمجياً باستخدام بايثون",
    "alternativeHeadline": "كيفية نقل صفحات PDF باستخدام بايثون",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء مستندات PDF",
    "keywords": "pdf, python, نقل صفحة pdf",
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
    "url": "/python-net/move-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/move-pages/"
    },
    "dateModified": "2023-04-04",
    "description": "حاول نقل الصفحات إلى الموقع المطلوب أو إلى نهاية ملف PDF باستخدام Aspose.PDF لبايثون عبر .NET."
}
</script>


## نقل صفحة من مستند PDF إلى آخر

توضح هذه الموضوع كيفية نقل صفحة من مستند PDF إلى نهاية مستند آخر باستخدام Python.
لنقل صفحة يجب علينا:

1. إنشاء كائن فئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) مع ملف PDF المصدر.
1. إنشاء كائن فئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) مع ملف PDF الوجهة.
1. الحصول على الصفحة من مجموعة [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) إضافة الصفحة إلى مستند الوجهة.
1. حفظ ملف PDF الناتج باستخدام طريقة [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).
1. [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) حذف الصفحة في المستند المصدر.

1. احفظ ملف PDF المصدر باستخدام طريقة [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

يوضح لك مقتطف الشيفرة التالي كيفية نقل صفحة واحدة.

```python

    import aspose.pdf as ap

    srcDocument = ap.Document(src_file_name)
    dstDocument = ap.Document(dst_File_name)
    page = srcDocument.pages[2]
    dstDocument.pages.add(page)
    # احفظ ملف الإخراج
    dstDocument.save(dst_File_name_new)
    srcDocument.pages.delete(2)
    srcDocument.save(src_file_name_new)
```

## نقل مجموعة من الصفحات من مستند PDF إلى آخر

1. أنشئ كائن فئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) مع ملف PDF المصدر.
1. أنشئ كائن فئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) مع ملف PDF الوجهة.
1. حدد مصفوفة بأرقام الصفحات المراد نقلها.
1. قم بتشغيل حلقة عبر المصفوفة:

1. احصل على الصفحة من [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) المجموعة.
1. [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) الصفحة إلى المستند الوجهة.
1. احفظ ملف PDF الناتج باستخدام طريقة [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).
1. [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) الصفحة في المستند المصدر باستخدام المصفوفة.
1. احفظ ملف PDF المصدر باستخدام طريقة [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

يوضح لك مقطع الشيفرة التالي كيفية إدراج صفحة فارغة في نهاية ملف PDF.

```python

    import aspose.pdf as ap

    srcDocument = ap.Document(input_pdf)
    dstDocument = ap.Document()
    pages = [1, 3]
    for page_index in pages:
        page = srcDocument.pages[page_index]
        dstDocument.pages.add(page)
    # حفظ ملفات الإخراج
    dstDocument.save(output_pdf_1)
    srcDocument.pages.delete(pages)
    srcDocument.save(output_pdf_2)
```


## نقل صفحة إلى موقع جديد في مستند PDF الحالي

1. أنشئ كائن من فئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) مع ملف PDF المصدر.
1. احصل على الصفحة من مجموعة [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. أضف الصفحة إلى الموقع الجديد (على سبيل المثال إلى النهاية) باستخدام [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods).
1. احذف الصفحة في الموقع السابق باستخدام [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods).
1. احفظ ملف PDF الناتج باستخدام طريقة [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    import aspose.pdf as ap

    srcDocument = ap.Document(input_pdf)

    page = srcDocument.pages[2]
    srcDocument.pages.add(page)
    srcDocument.pages.delete(2)

    # حفظ ملف الإخراج
    srcDocument.save(output_pdf)