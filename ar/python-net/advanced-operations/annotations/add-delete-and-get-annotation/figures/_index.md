---
title: إضافة تعليقات توضيحية للأشكال باستخدام Python
linktitle: تعليقات توضيحية للأشكال
type: docs
weight: 30
url: /ar/python-net/figures-annotation/
description: تصف هذه المقالة كيفية إضافة واسترجاع وحذف تعليقات توضيحية للأشكال من مستند PDF الخاص بك باستخدام Aspose.PDF for Python عبر .NET
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: دليل حول كيفية التعامل مع تعليقات توضيحية للأشكال في PDF
Abstract: توفر هذه المقالة دليلًا شاملًا حول إضافة واسترجاع وحذف تعليقات توضيحية من نوع المربع، الدائرة، المضلع، والخط المتعدد في مستندات PDF باستخدام Aspose.PDF for Python. تُبرز تعليقات المربع والدائرة بصريًا مناطق محددة على صفحة PDF بأشكال مستطيلة وبيضوية على التوالي. تتضمن المقالة تعليمات خطوة بخطوة ومقاطع كود Python لإنشاء هذه التعليقات عن طريق تحميل ملف PDF، وتكوين خصائص التعليق مثل العنوان واللون والشفافية، وإلحاقها بصفحات PDF. بالإضافة إلى ذلك، توضح المقالة طرقًا لاسترجاع التعليقات حسب النوع، وطباعة أبعادها المستطيلة، وحذفها من مستند PDF. كما يتم تغطية تعليقات المضلع والخط المتعدد، حيث يُعرف المضلع بسلسلة من الرؤوس المتصلة التي تشكل شكلًا مغلقًا، بينما يربط الخط المتعدد الرؤوس بطريقة مفتوحة. يوفر المستند أمثلة على الكود لتوضيح عمليات إضافة هذه التعليقات إلى PDF، فضلاً عن طرق الوصول إليها وإزالتها.

---

## إضافة تعليقات توضيحية للمربع والدائرة

في مستندات PDF، تشير تعليقة المربع إلى نوع معين من التعليقات يتم تمثيلها بشكل مربع. تُستخدم تعليقات المربع لتسليط الضوء أو لجذب الانتباه إلى منطقة أو قسم معين داخل المستند.

[المربع](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation/) و [الدائرة](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/circleannotation/) يجب أن تعرض، على التوالي، مستطيلًا أو إهليلجًا في الصفحة.

خطوات إنشاء تعليقات المربع أو الدائرة:

1. تحميل ملف PDF - جديد [المستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. إنشاء [تعليق المربع](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation) جديد وتعيين المعلمات (مستطيل جديد، العنوان، اللون، اللون الداخلي، الشفافية).
1. بعد ذلك نحتاج إلى إضافة تعليقة المربع إلى الصفحة.

المقتطف البرمجي التالي يوضح لك كيفية إضافة تعليقات المربع في صفحة PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    squareAnnotation = ap.annotations.SquareAnnotation(document.pages[1], ap.Rectangle(60, 600, 250, 450, True))
    squareAnnotation.title = "John Smith"
    squareAnnotation.color = ap.Color.blue
    squareAnnotation.interior_color = ap.Color.blue_violet
    squareAnnotation.opacity = 0.25

    document.pages[1].annotations.append(squareAnnotation)

    document.save(output_file)
```

المقتطف البرمجي التالي يوضح لك كيفية إضافة تعليقات الدائرة في صفحة PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_file)

    circleAnnotation = ap.annotations.CircleAnnotation(
        document.pages[1], ap.Rectangle(270, 160, 483, 383, True)
    )
    circleAnnotation.title = "John Smith"
    circleAnnotation.color = ap.Color.red
    circleAnnotation.interior_color = ap.Color.misty_rose
    circleAnnotation.opacity = 0.5
    circleAnnotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1], ap.Rectangle(842, 316, 1021, 459, True)
    )

    document.pages[1].annotations.append(circleAnnotation)
    document.save(output_file)
```

كمثال، سنرى النتيجة التالية لإضافة تعليقات المربع والدائرة إلى مستند PDF:

![عرض توضيحي لتعليقات الدائرة والمربع](circle_demo.png)

### الحصول على تعليقة الدائرة

يرجى تجربة المقتطف البرمجي التالي للحصول على تعليقة الدائرة من مستند PDF.

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

### الحصول على تعليقة المربع

يرجى تجربة المقتطف البرمجي التالي للحصول على تعليقة المربع من مستند PDF.

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


### حذف تعليقة الدائرة

المقتطف البرمجي التالي يوضح كيفية حذف تعليقة الدائرة من ملف PDF.

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

### حذف تعليقة المربع

المقتطف البرمجي التالي يوضح كيفية حذف تعليقة المربع من ملف PDF.

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

## إضافة تعليقات المضلع والخط المتعدد

تتيح لك أداة الخط المتعدد إنشاء أشكال وتخطيطات بعدد تعسفي من الجوانب على المستند.

[تعليقات المضلع](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polygonannotation/) تمثل مضلعات على الصفحة. يمكن أن تحتوي على أي عدد من الرؤوس المرتبطة بخطوط مستقيمة.

[تعليقات الخط المتعدد](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polylineannotation/) مشابهة أيضًا للمضلعات، الفرق الوحيد هو أن الرأسين الأول والأخير لا يربطان بشكل ضمني.

خطوات إنشاء تعليقات المضلع:

1. تحميل ملف PDF - جديد [المستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. إنشاء [تعليق مضلع](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polygonannotation) جديد وتعيين معلمات المضلع (مستطيل جديد، نقاط جديدة، العنوان، اللون، اللون الداخلي والشفافية).
1. بعد ذلك يمكننا إضافة التعليقات إلى الصفحة.

المقتطف البرمجي التالي يوضح كيفية إضافة تعليقات المضلع إلى ملف PDF:

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

المقتطف البرمجي التالي يوضح كيفية إضافة تعليقات الخط المتعدد إلى ملف PDF:

1. تحميل ملف PDF - جديد [المستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. إنشاء [تعليقات الخط المتعدد](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polylineannotation/) جديد وتعيين معلمات المضلع (مستطيل جديد، نقاط جديدة، العنوان، اللون، اللون الداخلي والشفافية).
1. بعد ذلك يمكننا إضافة التعليقات إلى الصفحة.

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

### الحصول على تعليقات المضلع والخط المتعدد

يرجى تجربة المقتطف البرمجي التالي للحصول على تعليقات المضلع في مستند PDF.

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

يرجى تجربة المقتطف البرمجي التالي للحصول على تعليقات الخط المتعدد في مستند PDF.

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

### حذف تعليقات المضلع والخط المتعدد

المقتطف البرمجي التالي يوضح كيفية حذف تعليقات المضلع من ملف PDF.

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

المقتطف البرمجي التالي يوضح كيفية حذف تعليقات Polyline من ملف PDF.

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


