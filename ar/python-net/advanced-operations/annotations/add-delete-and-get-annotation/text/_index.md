---
title: استخدام التعليقات النصية لملف PDF عبر بايثون
linktitle: تعليق نصي
type: docs
weight: 10
url: /ar/python-net/text-annotation/
description: يتيح لك Aspose.PDF لـ Python إضافة، الحصول على، وحذف التعليقات النصية من ملف PDF الخاص بك.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: دليل حول كيفية التلاعب بالتعليقات النصية في PDF
Abstract: توفر هذه المقالة دليلًا شاملاً حول كيفية التلاعب بالتعليقات النصية داخل ملفات PDF باستخدام مكتبة Aspose.PDF لبايثون. تغطي الإضافة، الاسترجاع، والحذف لأنواع مختلفة من التعليقات، بما في ذلك النصية، النص الحر، وتعليقات الشطب. التعليقات النصية هي ملاحظات مرفقة بموقع محدد داخل PDF، تُعرض كأيقونات تُظهر النص في نافذة منبثقة عند فتحها. تعليقات النص الحر تعرض النص مباشرة على الصفحة، بينما تعليقات الشطب تُشير إلى النص بخط لتوضيح أنه يجب إزالته أو تجاهله. العملية تتضمن إضافة التعليقات إلى مجموعة Annotations الخاصة بالصفحة باستخدام طريقة `add()`، وتُقدم أمثلة لكل نوع من التعليقات. تُظهر مقتطفات الشيفرة كيفية تنفيذ هذه المهام، بما في ذلك إنشاء التعليقات بخصائص محددة مثل العنوان، الموضوع، اللون، والعلامات، بالإضافة إلى استرجاع وحذف التعليقات من صفحات PDF. يُعد هذا الدليل مصدرًا عمليًا للمطورين الراغبين في تحسين مستندات PDF من خلال التلاعب بالتعليقات باستخدام Aspose.PDF.
---

## كيفية إضافة تعليق نصي إلى ملف PDF موجود

التعليق النصي هو تعليق مرفق بموقع محدد في مستند PDF. عندما يكون مغلقًا، يُعرض التعليق كأيقونة؛ وعند الفتح، يجب أن يظهر نافذة منبثقة تحتوي على نص الملاحظة بالخط والحجم الذي يختاره القارئ.

التعليقات محصورة في مجموعة [التعليقات](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/) لصفحة معينة. تحتوي هذه المجموعة على التعليقات لتلك الصفحة فقط؛ كل صفحة لها مجموعة التعليقات الخاصة بها.

لإضافة تعليق إلى صفحة معينة، أضفه إلى مجموعة التعليقات لتلك الصفحة باستخدام طريقة [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/#methods).

1. أولاً، أنشئ تعليقًا تريد إضافته إلى ملف PDF.
1. ثم افتح ملف PDF المدخل.
1. أضف التعليق إلى مجموعة [التعليقات](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/) لكائن 'page'.

يظهر مقتطف الشيفرة التالي لك كيفية إضافة تعليق في صفحة PDF.

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

## الحصول على التعليق النصي من ملف PDF

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

## حذف التعليق النصي من ملف PDF

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


## كيفية إضافة (أو إنشاء) تعليق نص حر جديد

التعليق النص الحر يعرض النص مباشرة على الصفحة. تسمح لك فئة [FreeTextAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/freetextannotation/) بإنشاء هذا النوع من التعليقات. في المقتطف التالي، نضيف تعليق نص حر فوق أول ظهور للسلسلة.

```python

    import aspose.pdf as ap

    # Load the PDF file
    document = ap.Document(input_file)

    freeTextAnnotation = ap.annotations.FreeTextAnnotation(
        document.pages[1], ap.Rectangle(299, 713, 308, 720, True), ap.annotations.DefaultAppearance()
    )
    freeTextAnnotation.title = "Aspose User"
    freeTextAnnotation.color = ap.Color.light_green

    document.pages[1].annotations.append(freeTextAnnotation)
    document.save(output_file)
```

## الحصول على التعليق النص الحر من ملف PDF

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

## حذف التعليق النص الحر من ملف PDF

```python

    import aspose.pdf as ap

    # Load the PDF file
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

يتيح لك Aspose.PDF لـ Python إضافة، حذف وتحديث التعليقات في مستندات PDF. إحدى الفئات تسمح لك أيضًا بشطب التعليقات. عندما يتم تطبيق StrikeOutAnnotation على PDF، يُرسم خط عبر النص المحدد، للدلالة على أنه يجب إزالته أو تجاهله.

يُظهر مقتطف الشيفرة التالي كيفية إضافة [StrikeOutAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/strikeoutannotation/) إلى PDF.

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

## حذف StrikeOutAnnotation من PDF

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



