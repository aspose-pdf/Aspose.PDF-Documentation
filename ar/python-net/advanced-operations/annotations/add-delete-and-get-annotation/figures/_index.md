---
title: إضافة تعليقات توضيحية على الأشكال باستخدام بايثون
linktitle: تعليقات توضيحية على الأشكال
type: docs
weight: 30
url: ar/python-net/figures-annotation/
description: يصف هذا المقال كيفية إضافة، الحصول على، وحذف التعليقات التوضيحية للأشكال من مستند PDF الخاص بك باستخدام Aspose.PDF للبايثون عبر .NET
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "إضافة تعليقات توضيحية على الأشكال باستخدام بايثون",
    "alternativeHeadline": "كيفية إضافة تعليقات توضيحية على الأشكال في PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستندات PDF",
    "keywords": "pdf, python, تعليقات توضيحية على الأشكال, تعليق متعدد الأضلاع, تعليق خطي, تعليق مربع, تعليق دائري",
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
    "url": "/python-net/figures-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/figures-annotation/"
    },
    "dateModified": "2023-02-04",
    "description": "يصف هذا المقال كيفية إضافة، الحصول على، وحذف التعليقات التوضيحية للأشكال من مستند PDF الخاص بك باستخدام Aspose.PDF للبايثون"
}
</script>


## إضافة تعليقات توضيحية للمربع والدائرة

في مستندات PDF، تشير التعليقات التوضيحية للمربع إلى نوع معين من التعليقات التوضيحية التي يتم تمثيلها بشكل مربع. تُستخدم التعليقات التوضيحية للمربع لتسليط الضوء أو جذب الانتباه إلى منطقة أو قسم محدد داخل المستند.

يجب أن تعرض التعليقات التوضيحية [المربع](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation/) و[الدائرة](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/circleannotation/) على التوالي، مستطيلًا أو قطع ناقص على الصفحة.

خطوات إنشاء تعليقات توضيحية للمربع أو الدائرة:

1. تحميل ملف PDF - [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) جديد.
2. إنشاء [تعليق توضيحي للمربع](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation) جديد وتعيين المعلمات (مستطيل جديد، عنوان، لون، لون داخلي، شفافية).
3. بعد ذلك، نحتاج إلى إضافة تعليق توضيحي للمربع إلى الصفحة.

يظهر مقتطف الشفرة التالي كيفية إضافة تعليقات توضيحية للمربع في صفحة PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    squareAnnotation = ap.annotations.SquareAnnotation(document.pages[1], ap.Rectangle(60, 600, 250, 450, True))
    squareAnnotation.title = "جون سميث"
    squareAnnotation.color = ap.Color.blue
    squareAnnotation.interior_color = ap.Color.blue_violet
    squareAnnotation.opacity = 0.25

    document.pages[1].annotations.append(squareAnnotation)

    document.save(output_file)
```

يظهر لك جزء الشيفرة التالي كيفية إضافة تعليقات دائرية في صفحة PDF.

```python

    import aspose.pdf as ap

    # افتح المستند
    document = ap.Document(input_file)

    circleAnnotation = ap.annotations.CircleAnnotation(
        document.pages[1], ap.Rectangle(270, 160, 483, 383, True)
    )
    circleAnnotation.title = "جون سميث"
    circleAnnotation.color = ap.Color.red
    circleAnnotation.interior_color = ap.Color.misty_rose
    circleAnnotation.opacity = 0.5
    circleAnnotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1], ap.Rectangle(842, 316, 1021, 459, True)
    )

    document.pages[1].annotations.append(circleAnnotation)
    document.save(output_file)
```


كمثال، سنرى النتيجة التالية لإضافة توضيحات المربع والدائرة إلى مستند PDF:

![عرض توضيح الدائرة والمربع](circle_demo.png)

### الحصول على توضيح الدائرة

يرجى محاولة استخدام مقطع الكود التالي للحصول على توضيح الدائرة من مستند PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    circleAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CIRCLE)
    ]

    for ca in circleAnnotations:
        print(ca.rect)
```

### الحصول على توضيح المربع

يرجى محاولة استخدام مقطع الكود التالي للحصول على توضيح المربع من مستند PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squareAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUARE)
    ]

    for pa in squareAnnotations:
        print(pa.rect)
```



### حذف توضيح الدائرة

يوضح مقطع الشيفرة التالي كيفية حذف التعليق التوضيحي الدائري من ملف PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    circleAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CIRCLE)
    ]

    for ca in circleAnnotations:
        document.pages[1].annotations.delete(ca)

    document.save(output_file)
```

### حذف التعليق التوضيحي المربع

يوضح مقطع الشيفرة التالي كيفية حذف التعليق التوضيحي المربع من ملف PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squareAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUARE)
    ]

    for pa in squareAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```

## إضافة تعليقات توضيحية متعددة الأضلاع ومتعددة الخطوط

تتيح لك أداة متعددة الخطوط إنشاء أشكال ومحيطات بعدد تعسفي من الجوانب على المستند.

[التعليقات التوضيحية متعددة الأضلاع](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polygonannotation/) تمثل المضلعات على الصفحة. يمكن أن تحتوي على أي عدد من الرؤوس المتصلة بخطوط مستقيمة.

[التعليقات التوضيحية متعددة الخطوط](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polylineannotation/) تشبه أيضًا المضلعات، والفرق الوحيد هو أن الرؤوس الأولى والأخيرة غير متصلة ضمناً.

الخطوات التي ننشئ بها التعليقات التوضيحية متعددة الأضلاع:

1. تحميل ملف PDF - [وثيقة جديدة](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
2. إنشاء [تعليق توضيحي متعدد الأضلاع](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polygonannotation) جديد وتعيين معلمات المضلع (مستطيل جديد، نقاط جديدة، عنوان، لون، لون داخلي وشفافية).
3. بعد ذلك يمكننا إضافة التعليقات التوضيحية إلى الصفحة.

يوضح snippet الكود التالي كيفية إضافة التعليقات التوضيحية متعددة الأضلاع إلى ملف PDF:

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    polygonAnnotation = ap.annotations.PolygonAnnotation(
        document.pages[1],
        ap.Rectangle(200, 300, 400, 400, True),
        [
            ap.Point(200, 300),
            ap.Point(220, 300),
            ap.Point(250, 330),
            ap.Point(300, 304),
            ap.Point(300, 400),
        ],
    )
    polygonAnnotation.title = "John Smith"
    polygonAnnotation.color = ap.Color.blue
    polygonAnnotation.interior_color = ap.Color.blue_violet
    polygonAnnotation.opacity = 0.25

    document.pages[1].annotations.append(polygonAnnotation)
    document.save(output_file)
```


The following code snippet shows how to add Polyline Annotations to a PDF file:

1. تحميل ملف PDF - [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) جديد.
1. إنشاء [Polyline Annotations](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polylineannotation/) جديد وتعيين معلمات المضلع (مستطيل جديد، نقاط جديدة، عنوان، لون، لون داخلي وعتامة).
1. بعد ذلك يمكننا إضافة التعليقات التوضيحية إلى الصفحة.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    polylineAnnotation = ap.annotations.PolylineAnnotation(
        document.pages[1],
        ap.Rectangle(270, 193, 571, 383, True),
        [
            ap.Point(545, 150),
            ap.Point(545, 190),
            ap.Point(667, 190),
            ap.Point(667, 110),
            ap.Point(626, 111),
        ],
    )
    polylineAnnotation.title = "John Smith"
    polylineAnnotation.color = ap.Color.red
    polylineAnnotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1], ap.Rectangle(842, 196, 1021, 338, True)
    )

    document.pages[1].annotations.append(polylineAnnotation)
    document.save(output_file)
```


### الحصول على التعليقات التوضيحية متعددة الأضلاع والخطوط المتعددة

يرجى تجربة استخدام جزء الكود التالي للحصول على التعليقات التوضيحية متعددة الأضلاع في مستند PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    polygonAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLYGON)
    ]

    for pa in polygonAnnotations:
        print(pa.rect)
```

يرجى تجربة استخدام جزء الكود التالي للحصول على التعليقات التوضيحية للخطوط المتعددة في مستند PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    polylineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLY_LINE)
    ]

    for pa in polylineAnnotations:
        print(pa.rect)
```

### حذف التعليقات التوضيحية متعددة الأضلاع والخطوط المتعددة

يوضح جزء الكود التالي كيفية حذف التعليقات التوضيحية متعددة الأضلاع من ملف PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    polygonAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLYGON)
    ]

    for pa in polygonAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```


يعرض مقتطف الشيفرة التالي كيفية حذف تعليقات الخط متعدد الأضلاع من ملف PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    polylineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLY_LINE)
    ]

    for pa in polylineAnnotations:
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