---
title: التعليقات التوضيحية الإضافية باستخدام بايثون
linktitle: تعليقات توضيحية إضافية
type: docs
weight: 60
url: /ar/python-net/extra-annotations/
description: تعلم كيفية إضافة تعليقات توضيحية إضافية مثل التظليل أو الملاحظات إلى ملفات PDF باستخدام بايثون مع Aspose.PDF لتحسين محتوى PDF.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: دليل حول كيفية التعامل مع التعليقات التوضيحية الإ إضافية في PDF
Abstract: المقالة توفر دليلاً شاملاً حول كيفية إضافة واسترجاع وحذف أنواع مختلفة من التعليقات التوضيحية في ملف PDF باستخدام بايثون، وتحديدا مع مكتبة Aspose.PDF. تغطي ثلاثة أنواع من التعليقات التوضيحية - التعليق التوضيحي Caret، الرابط، والحذف الأحمر. توضح المقالة أن تعليقات Caret تُستخدم لاقتراحات تحرير النص. تصف عملية تحميل ملف PDF، وإنشاء تعليق Caret بمعلمات محددة (مثل المستطيل، العنوان، الموضوع، العلامات، واللون)، وإضافته إلى المستند، وحفظ التغييرات. تُقدم مقتطفات الشيفرة لإضافة واسترجاع وحذف تعليقات Caret. تُستخدم تعليقات الرابط لإنشاء مناطق قابلة للنقر تُعيد التوجيه إلى عناوين URL أو إلى مواضع محددة في المستند. يتضمن الدليل تعليمات وشيفرة لإضافة تعليق رابط عن طريق تحديد جزء نصي (مثل رقم هاتف)، وتعيين إجراء، وإدارة هذه التعليقات.
---

## كيفية إضافة تعليق Caret إلى ملف PDF موجود عبر بايثون

تعليق Caret هو رمز يشير إلى تحرير النص. كما أن تعليق Caret هو أيضًا تعليق توصيفي، لذا فإن فئة Caret تُشتق من فئة Markup وتوفر أيضًا وظائف للحصول على خصائص تعليق Caret أو تعيينها وإعادة ضبط تدفق مظهر تعليق Caret.
غالبًا ما تُستخدم تعليقات Caret لاقتراح تغييرات أو إضافات أو تعديلات على النص.

الخطوات التي نستخدمها لإنشاء تعليق Caret:

1. تحميل ملف PDF - جديد [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. إنشاء [CaretAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/caretannotation/) جديد وتعيين معلمات Caret (مستطيل جديد، العنوان، الموضوع، العلامات، اللون). يُستخدم هذا التعليق لتحديد إدخال النص.
1. بمجرد أن نتمكن من إلحاق التعليقات إلى الصفحة.

المقتطف البرمجي التالي يوضح كيفية إضافة تعليق Caret إلى ملف PDF:

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_file)

    caretAnnotation1 = ap.annotations.CaretAnnotation(
        document.pages[1], ap.Rectangle(200, 700.664, 308.708, 740.769, True)
    )
    caretAnnotation1.title = "Aspose User"
    caretAnnotation1.subject = "Inserted text 1"
    caretAnnotation1.flags = ap.annotations.AnnotationFlags.PRINT
    caretAnnotation1.color = ap.Color.blue

    document.pages[1].annotations.append(caretAnnotation1)
    document.save(output_file)
```

### الحصول على تعليق Caret

يرجى تجربة المقتطف البرمجي التالي للحصول على تعليق Caret في مستند PDF

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    caretAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CARET)
    ]

    for ca in caretAnnotations:
        print(ca.rect)
```

### حذف تعليق Caret

المقتطف البرمجي التالي يوضح كيفية حذف تعليق Caret من ملف PDF باستخدام بايثون.

```python

    import aspose.pdf as ap

    # Load the PDF file
    document = ap.Document(input_file)
    caretAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CARET)
    ]

    for ca in caretAnnotations:
        document.pages[1].annotations.delete(ca)

    document.save(output_file)
```

## حذف جزء معين من الصفحة باستخدام تعليق Redaction باستخدام Aspose.PDF للبايثون

يدعم Aspose.PDF للبايثون عبر .NET القدرة على إضافة وتعامل مع التعليقات التوضيحية في ملف PDF موجود. تُستخدم تعليقات Redaction في مستندات PDF لإزالة أو إخفاء المعلومات السرية من المستند بشكل دائم. عملية تحرير المعلومات تشمل تغطية أو تظليل محتوى محدد، مثل النصوص أو الصور أو الرسومات، بطريقة تُقيد رؤيتها ووصول الآخرين إليها. هذا يضمن بقاء المعلومات الحساسة مخفية ومحمية داخل المستند. لتلبية هذا المتطلب، يتم توفير فئة تسمى [RedactionAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/redactionannotation/) يمكن استخدامها لحذف مناطق معينة من الصفحة أو يمكن استخدامها لتعديل تعليقات Redaction الحالية وحذفها (أي تسوية التعليق وإزالة النص تحته).

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    page = document.pages[1]
    redactionAnnotation = ap.annotations.RedactionAnnotation(page, ap.Rectangle(270, 190, 371, 250, True))
    redactionAnnotation.title = "John Smith"
    redactionAnnotation.fill_color = ap.Color.light_gray
    redactionAnnotation.color = ap.Color.red
    redactionAnnotation.redact()

    page.annotations.append(redactionAnnotation)
    document.save(output_file)
```

### الحصول على تعليق Redaction

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    redactionAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.REDACTION)
    ]

    for pa in redactionAnnotations:
        print(pa.rect)
```

### حذف تعليق Redaction

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    redactionAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.REDACTION)
    ]

    for pa in redactionAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```



