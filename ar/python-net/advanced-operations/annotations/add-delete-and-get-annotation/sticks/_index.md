---
title: التعليقات المعلقة في PDF باستخدام بايثون
linktitle: التعليق المُلصق
type: docs
weight: 50
url: /ar/python-net/sticky-annotations/
description: اكتشف كيفية إضافة التعليقات المعلقة في مستندات PDF باستخدام Aspose.PDF في بايثون عبر .NET للتعليقات وردود الفعل.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: دليل حول كيفية تعديل التعليقات المعلقة في PDF
Abstract: توفر هذه المقالة دليلاً مفصلاً حول كيفية إدارة تعليقات العلامة المائية في مستندات PDF باستخدام مكتبة Aspose.PDF للبايثون. يشرح العملية لإضافة واسترجاع وحذف تعليقات العلامة المائية لضمان أصالة الوثيقة والعلامة التجارية. يمكن استخدام تعليق العلامة المائية لتضمين رسومات، مثل الشعارات، بحجم وموقع ثابت على الصفحة. يتضمن الدليل مقتطفات شفرة توضح كيفية إضافة تعليق علامة مائية في موقع محدد مع شفافية قابلة للتعديل، بالإضافة إلى كيفية استرجاع وحذف تعليقات العلامة المائية الموجودة. تُظهر أمثلة الشفرة استخدام مكتبة Aspose.PDF للتعامل مع مستندات PDF برمجياً، مقدماً نهجاً عملياً للمطورين لدمج وظائف العلامة المائية في تطبيقاتهم.
---

## إضافة تعليق العلامة المائية

أكثر التعليقات وضوحًا وسهولة في التصور والنقل هي تعليق العلامة المائية. هذه طريقة مثالية لوضع شعار أو أي علامة أخرى في مستند PDF لتأكيد أصالته.

يُستخدم تعليق العلامة المائية لتمثيل الرسومات التي تُطبع بحجم وموقع ثابت على الصفحة، بغض النظر عن أبعاد الصفحة المطبوعة.

يمكنك إضافة نص العلامة المائية باستخدام [WatermarkAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/watermarkannotation/) في موقع محدد من صفحة PDF. يمكن أيضًا التحكم في شفافية العلامة المائية باستخدام خاصية [opacity](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/watermarkannotation/#properties).

يرجى مراجعة مقتطف التعليمات البرمجية التالي لإضافة WatermarkAnnotation.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    # Create Annotation
    # Load Page object to add Annotation
    page = document.pages[1]

    # Create Annotation
    wa = ap.annotations.WatermarkAnnotation(page, ap.Rectangle(100, 0, 400, 100, True))

    # Add annotaiton into Annotation collection of Page
    page.annotations.append(wa)

    # Create TextState for Font settings
    ts = ap.text.TextState()
    ts.foreground_color = ap.Color.blue
    ts.font_size = 25
    ts.font = ap.text.FontRepository.find_font("Arial");

    # Set opacity level of Annotaiton Text
    wa.opacity = 0.5

    # Add Text in Annotation
    wa.set_text_and_state([ "HELLO", "Line 1", "Line 2" ], ts)

    document.save(output_file)
```

## الحصول على تعليق العلامة المائية

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    watermarkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.WATERMARK)
    ]

    for ta in watermarkAnnotations:
        print(ta.rect)
```

## حذف تعليق العلامة المائية

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    watermarkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.WATERMARK)
    ]

    for ta in watermarkAnnotations:
        document.pages[1].annotations.delete(ta)

    document.save(output_file)
```


