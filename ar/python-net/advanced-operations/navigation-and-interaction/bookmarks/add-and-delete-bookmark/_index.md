---
title: إضافة وحذف إشارة مرجعية باستخدام Python
linktitle: إضافة وحذف إشارة مرجعية
type: docs
weight: 10
url: /ar/python-net/add-and-delete-bookmark/
description: يمكنك إضافة إشارة مرجعية إلى مستند PDF باستخدام Python. من الممكن حذف جميع الإشارات المرجعية أو إشارات مرجعية معينة من مستند PDF.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "إضافة وحذف إشارة مرجعية",
    "alternativeHeadline": "كيفية إضافة وحذف إشارة مرجعية من PDF",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "إنشاء مستند PDF",
    "keywords": "pdf، python، حذف إشارة مرجعية، إضافة إشارة مرجعية",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق Aspose.PDF Doc",
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
    "url": "/python-net/add-and-delete-bookmark/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-and-delete-bookmark/"
    },
    "dateModified": "2023-02-04",
    "description": "يمكنك إضافة إشارة مرجعية إلى مستند PDF باستخدام Python. من الممكن حذف جميع الإشارات المرجعية أو إشارات مرجعية معينة من مستند PDF."
}
</script>


## إضافة إشارة مرجعية إلى مستند PDF

تُحتفظ بالإشارات المرجعية في مجموعة [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) للكائن Document، وهي نفسها في مجموعة [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).

لإضافة إشارة مرجعية إلى PDF:

1. افتح مستند PDF باستخدام كائن [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
2. أنشئ إشارة مرجعية وحدد خصائصها.
3. أضف مجموعة [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) إلى مجموعة Outlines.

يظهر لك المقتطف البرمجي التالي كيفية إضافة إشارة مرجعية في مستند PDF.

```python

    import aspose.pdf as ap

    # افتح المستند
    document = ap.Document(input_pdf)

    # أنشئ كائن الإشارة المرجعية
    outline = ap.OutlineItemCollection(document.outlines)
    outline.title = "Test Bookmark"
    outline.italic = True
    outline.bold = True
    # حدد رقم صفحة الوجهة
    outline.action = ap.annotations.GoToAction(document.pages[1])
    # أضف الإشارة المرجعية إلى مجموعة الإشارات المرجعية في المستند.
    document.outlines.append(outline)

    # احفظ الناتج
    document.save(output_pdf)
```


## إضافة إشارة مرجعية فرعية إلى مستند PDF

يمكن أن تكون الإشارات المرجعية متداخلة، مما يشير إلى علاقة هرمية مع الإشارات المرجعية الأصلية والفرعية. يشرح هذا المقال كيفية إضافة إشارة مرجعية فرعية، وهي إشارة مرجعية من المستوى الثاني، إلى ملف PDF.

لإضافة إشارة مرجعية فرعية إلى ملف PDF، قم أولاً بإضافة إشارة مرجعية رئيسية:

1. افتح مستندًا.
2. أضف إشارة مرجعية إلى [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/)، مع تحديد خصائصها.
3. أضف OutlineItemCollection إلى مجموعة كائن [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) الخاصة بالمستند.

يتم إنشاء الإشارة المرجعية الفرعية تمامًا مثل الإشارة المرجعية الرئيسية، كما هو موضح أعلاه، ولكن يتم إضافتها إلى مجموعة الإشارات المرجعية الرئيسية.

توضح مقتطفات الكود التالية كيفية إضافة إشارة مرجعية فرعية إلى مستند PDF.

```python

    import aspose.pdf as ap

    # افتح المستند
    document = ap.Document(input_pdf)

    # إنشاء كائن إشارة مرجعية رئيسية
    outline = ap.OutlineItemCollection(document.outlines)
    outline.title = "Parent Outline"
    outline.italic = True
    outline.bold = True

    # إنشاء كائن إشارة مرجعية فرعية
    childOutline = ap.OutlineItemCollection(document.outlines)
    childOutline.title = "Child Outline"
    childOutline.italic = True
    childOutline.bold = True

    # إضافة إشارة مرجعية فرعية في مجموعة الإشارات المرجعية الرئيسية
    outline.append(childOutline)
    # إضافة إشارة مرجعية رئيسية في مجموعة الإشارات المرجعية للمستند.
    document.outlines.append(outline)

    # حفظ المخرج
    document.save(output_pdf)
```


## حذف جميع الإشارات المرجعية من مستند PDF

جميع الإشارات المرجعية في ملف PDF موجودة في مجموعة [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/). يشرح هذا المقال كيفية حذف جميع الإشارات المرجعية من ملف PDF.

لحذف جميع الإشارات المرجعية من ملف PDF:

1. قم باستدعاء طريقة الحذف لمجموعة [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).
2. احفظ الملف المعدل باستخدام طريقة [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) الخاصة بكائن [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

توضح مقتطفات الشيفرات التالية كيفية حذف جميع الإشارات المرجعية من مستند PDF.

```python

    import aspose.pdf as ap

    # فتح المستند
    document = ap.Document(input_pdf)

    # حذف جميع الإشارات المرجعية
    document.outlines.delete()

    # حفظ الملف المحدث
    document.save(output_pdf)

```

## حذف إشارة مرجعية معينة من مستند PDF

لحذف إشارة مرجعية معينة من ملف PDF:

1. مرر عنوان العلامة المرجعية كمعامل إلى طريقة الحذف في مجموعة [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).
1. ثم احفظ الملف المحدث باستخدام طريقة الحفظ للكائن Document.

توفر فئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) مجموعة [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/). تقوم طريقة [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/#methods) بحذف أي علامة مرجعية بعنوان يمرر إلى الطريقة.

توضح أجزاء الشيفرة التالية كيفية حذف علامة مرجعية معينة من مستند PDF.

```python

    import aspose.pdf as ap

    # افتح المستند
    document = ap.Document(input_pdf)

    # حذف العلامة المرجعية المحددة بالعنوان
    document.outlines.delete("Child Outline")

    # حفظ الملف المحدث
    document.save(output_pdf)