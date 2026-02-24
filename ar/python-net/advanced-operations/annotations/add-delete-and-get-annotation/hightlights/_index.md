---
title: تحديد إضاءات PDF باستخدام بايثون
linktitle: تحديد الإضاءات
type: docs
weight: 20
url: /ar/python-net/highlights-annotation/
description: تعرّف على طريقة إضافة تعليقات إضاءة إلى ملفات PDF باستخدام بايثون ومكتبة Aspose.PDF لتأكيد النص.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: دليل حول كيفية تعديل تعليقات الإضاءات في PDF
Abstract: توفر المقالة دليلًا شاملاً حول كيفية استخدام تعليقات تنسيق النص في مستندات PDF، مع التركيز على الوظائف التي تقدمها مكتبة Aspose.PDF في بايثون. تشرح هدف واستخدام الأنواع المختلفة من التعليقات، بما في ذلك إضاءة النص، تسطير الأسطر، شطب النص، وتعليقات الخط المتعرج، كل منها مصمم لتأكيد أو تعديل النص بطرق مختلفة. يوضح المستند الخطوات اللازمة لإضافة هذه التعليقات إلى ملف PDF، بما في ذلك تحميل المستند، إنشاء التعليقات مع معلمات محددة مثل العنوان واللون، وإلحاقها بالصفحة المطلوبة. بالإضافة إلى ذلك، تتضمن المقالة مقتطفات شفرة لاسترداد التعليقات من PDF، مما يسمح للمستخدمين بفلترة وطباعة تفاصيل التعليقات حسب النوع. أخيرًا، تفصل العملية الخاصة بحذف التعليقات، مع تقديم أمثلة شفرة لإزالة كل نوع من تعليقات تنسيق النص من المستند. يُعتبر هذا الدليل مصدرًا عمليًا للمطورين الذين يهدفون إلى تعديل تعليقات النص في ملفات PDF برمجيًا باستخدام بايثون.
---

تُستخدم تعليقات تنسيق النص في PDF لتسليط الضوء، تسطير، شطب أو إضافة ملاحظات إلى النص في المستند. تهدف هذه التعليقات إلى إبراز أو جذب الانتباه إلى أجزاء محددة من النص. تتيح مثل هذه التعليقات للمستخدمين وضع علامات مرئية أو تعديل محتوى ملف PDF.

تُستخدم تعليقات الإضاءة لتلوين خلفية النص بلون، عادةً الأصفر، للدلالة على أهميته أو صلته.

تُعد تعليقات التسطير خطًا يُوضع تحت النص المحدد للدلالة على أهميته، أو لتأكيده، أو للإشارة إلى تعديلات مقترحة.

تتضمن تعليقات الشطب أو الشطب نصًا معينًا لتوضيح أنه قد تم حذفه أو استبداله أو لم يعد صالحًا.

يُستخدم الخط المتعرج لتسطير النص للدلالة على نوع مختلف من التأكيد، مثل الأخطاء الإملائية، المشكلات المحتملة، أو التغييرات المقترحة.

## إضافة تعليقات تنسيق النص

لإضافة تعليق تنسيق نص إلى مستند PDF، نحتاج إلى تنفيذ الإجراءات التالية:

1. تحميل ملف PDF - كائن [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) جديد.
1. إنشاء التعليقات:
- [HighlightAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/highlightannotation/) وضبط المعلمات (العنوان، اللون).
- [StrikeOutAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/strikeoutannotation/) وضبط المعلمات (العنوان، اللون).
- [SquigglyAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squigglyannotation/) وضبط المعلمات (العنوان، اللون).
- [UnderlineAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/underlineannotation/) وضبط المعلمات (العنوان، اللون).
1. بعد ذلك، يجب إضافة جميع التعليقات إلى الصفحة.

### إضافة تعليق إضاءة

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_file)

    # Create Circle Annotation
    highlightAnnotation = ap.annotations.HighlightAnnotation(
        document.pages[1], ap.Rectangle(300, 750, 320, 770, True)
    )
    document.pages[1].annotations.append(highlightAnnotation)
    document.save(output_file)
```

### إضافة تعليق شطب

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

### إضافة تعليق خط متعرج

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    page = document.pages[1]
    squigglyAnnotation = ap.annotations.SquigglyAnnotation(page, ap.Rectangle(67, 317, 261, 459, True))
    squigglyAnnotation.title = "John Smith"
    squigglyAnnotation.color = ap.Color.blue

    page.annotations.append(squigglyAnnotation)

    document.save(output_file)
```

### إضافة تعليق تسطير

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    underlineAnnotation = ap.annotations.UnderlineAnnotation(
        document.pages[1], ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
    )
    underlineAnnotation.title = "Aspose User"
    underlineAnnotation.subject = "Inserted Underline 1"
    underlineAnnotation.flags = ap.annotations.AnnotationFlags.PRINT
    underlineAnnotation.color = ap.Color.blue

    document.pages[1].annotations.append(underlineAnnotation)
    document.save(output_file)
```

## الحصول على تعليقات تنسيق النص

يرجى تجربة استخدام مقتطف الشفرة التالي للحصول على تعليقات تنسيق النص من مستند PDF.

### الحصول على تعليق إضاءة

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT)
    ]

    for ha in highlightAnnotations:
        print(ha.rect)
```

### الحصول على تعليق شطب

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


### الحصول على تعليق خط متعرج

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squigglyAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUIGGLY)
    ]

    for pa in squigglyAnnotations:
        print(pa.rect)
```

### الحصول على تعليق تسطير

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    UnderlineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.UNDERLINE)
    ]

    for ta in UnderlineAnnotations:
        print(ta.rect)
```

## حذف تعليقات تنسيق النص

يعرض مقتطف الشفرة التالي كيفية حذف تعليقات تنسيق النص من ملف PDF.

### حذف تعليق إضاءة

```python

    import aspose.pdf as ap

    # Load the PDF file
    document = ap.Document(input_file)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT)
    ]

    for hs in highlightAnnotations:
        document.pages[1].annotations.delete(hs)

    document.save(output_file)
```

### حذف تعليق شطب

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

### حذف تعليق خط متعرج

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squigglyAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUIGGLY)
    ]

    for pa in squigglyAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```

### حذف تعليق تسطير

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    underlineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.UNDERLINE)
    ]

    for ta in underlineAnnotations:
        document.pages[1].annotations.delete(ta)

    document.save(output_file)
```



