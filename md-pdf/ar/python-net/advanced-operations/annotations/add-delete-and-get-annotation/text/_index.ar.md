---
title: استخدام التعليقات النصية لملفات PDF عبر بايثون
linktitle: التعليقات النصية
type: docs
weight: 10
url: /python-net/text-annotation/
description: Aspose.PDF لبايثون يتيح لك إضافة، الحصول على، وحذف التعليقات النصية من وثيقة PDF الخاصة بك.
lastmod: "2023-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "استخدام التعليقات النصية لملفات PDF عبر بايثون",
    "alternativeHeadline": "كيفية إضافة التعليقات النصية في PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء مستندات PDF",
    "keywords": "pdf, python, التعليقات النصية",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق وثائق Aspose.PDF",
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
    "url": "/python-net/text-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/text-annotation/"
    },
    "dateModified": "2023-02-04",
    "description": "Aspose.PDF لبايثون يتيح لك إضافة، الحصول على، وحذف التعليقات النصية من وثيقة PDF الخاصة بك."
}
</script>


## كيفية إضافة تعليق نصي إلى ملف PDF موجود

التعليق النصي هو تعليق مرتبط بموقع محدد في مستند PDF. عند إغلاقه، يظهر التعليق كرمز؛ وعند فتحه، يجب أن يعرض نافذة منبثقة تحتوي على نص الملاحظة بالخط والحجم اللذين يختارهما القارئ.

يحتوي [Annotations](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/) على التعليقات الخاصة بصفحة معينة. تحتوي هذه المجموعة على التعليقات لتلك الصفحة الفردية فقط؛ كل صفحة لديها مجموعة التعليقات الخاصة بها.

لإضافة تعليق إلى صفحة معينة، أضفه إلى مجموعة التعليقات لتلك الصفحة باستخدام [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/#methods).

1. أولاً، قم بإنشاء التعليق الذي ترغب في إضافته إلى ملف PDF.
2. ثم افتح ملف PDF المدخل.

1. أضف التعليق إلى مجموعة [التعليقات](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/) الخاصة بكائن 'page'.

يظهر لك مقطع الشيفرة التالي كيفية إضافة تعليق في صفحة PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    textAnnotation = ap.annotations.TextAnnotation(
        document.pages[1], ap.Rectangle(300, 700.664, 320, 720.769, True)
    )
    textAnnotation.title = "Aspose User"
    textAnnotation.subject = "Inserted text 1"
    textAnnotation.contents = "qwerty"
    textAnnotation.flags = ap.annotations.AnnotationFlags.PRINT
    textAnnotation.color = ap.Color.blue

    document.pages[1].annotations.append(textAnnotation)
    document.save(output_file)
```

## احصل على تعليق النص من ملف PDF

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    textAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.TEXT)
    ]

    for ta in textAnnotations:
        print(ta.rect)
```


## حذف التعليقات النصية من ملف PDF

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    textAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.TEXT)
    ]

    for ta in textAnnotations:
        document.pages[1].annotations.delete(ta)

    document.save(output_file)
```

## كيفية إضافة (أو إنشاء) تعليق نصي جديد مجاني

يظهر التعليق النصي المجاني النص مباشرة على الصفحة. تتيح فئة [FreeTextAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/freetextannotation/) إنشاء هذا النوع من التعليقات. في المقطع التالي، نضيف تعليقًا نصيًا مجانيًا فوق أول ظهور للسلسلة.

```python

    import aspose.pdf as ap

    # تحميل ملف PDF
    document = ap.Document(input_file)

    freeTextAnnotation = ap.annotations.FreeTextAnnotation(
        document.pages[1], ap.Rectangle(299, 713, 308, 720, True), ap.annotations.DefaultAppearance()
    )
    freeTextAnnotation.title = "Aspose User"
    freeTextAnnotation.color = ap.Color.light_green

    document.pages[1].annotations.append(freeTextAnnotation)
    document.save(output_file)
```


## احصل على تعليق نصي مجاني من ملف PDF

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    freeTextAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.FREE_TEXT)
    ]

    for fa in freeTextAnnotations:
        print(fa.rect)
```

## حذف تعليق نصي مجاني من ملف PDF

```python

    import aspose.pdf as ap

    # تحميل ملف PDF
    document = ap.Document(input_file)
    freeTextAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.FREE_TEXT)
    ]

    for fa in freeTextAnnotations:
        document.pages[1].annotations.delete(fa)

    document.save(output_file)
```

### شطب الكلمات باستخدام StrikeOutAnnotation

Aspose.PDF لـ Python يتيح لك إضافة وحذف وتحديث التعليقات التوضيحية في مستندات PDF.
 إحدى الفئات تسمح لك بشطب التعليقات التوضيحية أيضًا. عندما يتم تطبيق تعليق توضيحي مشطوب على ملف PDF، يتم رسم خط عبر النص المحدد، مما يشير إلى أنه يجب إزالته أو تجاهله.

يظهر مقتطف الشيفرة التالي كيفية إضافة [StrikeOutAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/strikeoutannotation/) إلى PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    strikeoutAnnotation = ap.annotations.StrikeOutAnnotation(
        document.pages[1], ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
    )
    strikeoutAnnotation.title = "Aspose User"
    strikeoutAnnotation.subject = "Inserted text 1"
    strikeoutAnnotation.flags = ap.annotations.AnnotationFlags.PRINT
    strikeoutAnnotation.color = ap.Color.blue

    document.pages[1].annotations.append(strikeoutAnnotation)
    document.save(output_file)
```

## الحصول على StrikeOutAnnotation من PDF

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    StrikeoutAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT)
    ]

    for pa in StrikeoutAnnotations:
        print(pa.rect)
```

## حذف تعليق StrikeOutAnnotation من ملف PDF

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    StrikeoutAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT)
    ]

    for pa in StrikeoutAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
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