---
title: الحصول على، تحديث وتوسيع إشارة مرجعية باستخدام بايثون
linktitle: الحصول على، تحديث وتوسيع إشارة مرجعية
type: docs
weight: 20
url: ar/python-net/get-update-and-expand-bookmark/
description: تصف هذه المقالة كيفية استخدام الإشارات المرجعية في ملف PDF باستخدام مكتبة Aspose.PDF لبايثون.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "الحصول على، تحديث وتوسيع إشارة مرجعية باستخدام بايثون",
    "alternativeHeadline": "كيفية الحصول على إشارات مرجعية من ملف PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستندات PDF",
    "keywords": "pdf, python, الحصول على إشارات مرجعية",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق توثيق Aspose.PDF",
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
    "url": "/python-net/get-update-and-expand-bookmark/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/get-update-and-expand-bookmark/"
    },
    "dateModified": "2023-02-04",
    "description": "تصف هذه المقالة كيفية استخدام الإشارات المرجعية في ملف PDF باستخدام مكتبة Aspose.PDF لبايثون."
}
</script>


## الحصول على الإشارات المرجعية

تحتوي مجموعة [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) الخاصة بكائن [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) على جميع الإشارات المرجعية لملف PDF. يوضح هذا المقال كيفية الحصول على الإشارات المرجعية من ملف PDF، وكيفية معرفة الصفحة التي توجد بها إشارة مرجعية معينة.

للحصول على الإشارات المرجعية، قم بالتكرار خلال مجموعة [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) واحصل على كل إشارة مرجعية في OutlineItemCollection. يوفر [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) الوصول إلى جميع سمات الإشارة المرجعية. يُظهر لك مقطع الشيفرة التالي كيفية الحصول على الإشارات المرجعية من ملف PDF.

```python

    import aspose.pdf as ap

    # افتح المستند
    document = ap.Document(input_pdf)

    # قم بالتكرار خلال جميع الإشارات المرجعية
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
```


## الحصول على رقم الصفحة للإشارة المرجعية

بمجرد إضافة إشارة مرجعية، يمكنك معرفة الصفحة التي توجد عليها من خلال الحصول على رقم الصفحة المرتبط بكائن الإشارة المرجعية.

```python

    import aspose.pdf as ap

    # إنشاء محرر الإشارات المرجعية
    bookmarkEditor = ap.facades.PdfBookmarkEditor()
    # فتح ملف PDF
    bookmarkEditor.bind_pdf(input_pdf)
    # استخراج الإشارات المرجعية
    bookmarks = bookmarkEditor.extract_bookmarks()
    for bookmark in bookmarks:
        str_level_seprator = ""
        for i in range(bookmark.level):
            str_level_seprator += "----"

        print(str_level_seprator, "العنوان:", bookmark.title)
        print(str_level_seprator, "رقم الصفحة:", bookmark.page_number)
        print(str_level_seprator, "إجراء الصفحة:", bookmark.action)
```

## الحصول على الإشارات المرجعية الفرعية من مستند PDF

يمكن تنظيم الإشارات المرجعية في هيكل هرمي، مع الآباء والأطفال.
  للحصول على جميع العلامات المرجعية، قم بالتكرار من خلال مجموعات الكائن Document الخاصة بعناصر Outlines. ومع ذلك، للحصول على العلامات المرجعية الفرعية أيضًا، قم بالتكرار من خلال جميع العلامات المرجعية في كل كائن [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) يتم الحصول عليه في الحلقة الأولى. تعرض مقتطفات الشيفرة التالية كيفية الحصول على العلامات المرجعية الفرعية من مستند PDF.

```python

    import aspose.pdf as ap

    # افتح المستند
    document = ap.Document(input_pdf)

    # كرر عبر جميع العلامات المرجعية
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
        count = len(outline_item)
        if count > 0:
            print("العلامات المرجعية الفرعية")
            # هناك علامات مرجعية فرعية، ثم كرر من خلالها أيضًا
            for j in range(len(outline_item)):
                child_outline_item = outline_item[i + 1]
                print(child_outline_item.title)
                print(child_outline_item.italic)
                print(child_outline_item.bold)
                print(child_outline_item.color)
```

## تحديث الإشارات المرجعية في مستند PDF

لتحديث إشارة مرجعية في ملف PDF، أولاً، احصل على الإشارة المرجعية المحددة من مجموعة OutlineColletion لكائن المستند عن طريق تحديد فهرس الإشارة المرجعية. بمجرد استرجاع الإشارة المرجعية إلى كائن [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/)، يمكنك تحديث خصائصها ثم حفظ ملف PDF المحدث باستخدام طريقة Save. توضح مقتطفات الشيفرة التالية كيفية تحديث الإشارات المرجعية في مستند PDF.

```python

    import aspose.pdf as ap

    # افتح المستند
    document = ap.Document(input_pdf)

    # احصل على كائن الإشارة المرجعية
    outline = document.outlines[1]

    # احصل على كائن الإشارة المرجعية الفرعية
    child_outline = outline[1]
    child_outline.title = "Updated Outline"
    child_outline.italic = True
    child_outline.bold = True

    # احفظ النتيجة
    document.save(output_pdf)
```

## الإشارات المرجعية الموسعة عند عرض المستند

تُحتفظ الإشارات المرجعية في مجموعة [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) لكائن المستند، وهي نفسها في مجموعة [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).
 ومع ذلك، قد يكون لدينا متطلب بأن تكون جميع العلامات المرجعية موسعة عند عرض ملف PDF.

من أجل تحقيق هذا المتطلب، يمكننا تعيين حالة الفتح لكل عنصر مخطط/علامة مرجعية كما هو مفتوح. يوضح لك مقتطف الكود التالي كيفية تعيين حالة الفتح لكل علامة مرجعية كموسع في مستند PDF.

```python

    import aspose.pdf as ap

    # افتح المستند
    document = ap.Document(input_pdf)

    # تعيين وضع عرض الصفحة، أي إظهار الصور المصغرة، ملء الشاشة، إظهار لوحة المرفقات
    document.page_mode = ap.PageMode.USE_OUTLINES
    # الانتقال عبر كل عنصر مخطط في مجموعة المخططات في ملف PDF
    for i in range(len(document.outlines)):
        item = document.outlines[i + 1]
        # تعيين حالة الفتح لعنصر المخطط
        item.open = True

    # حفظ الإخراج
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