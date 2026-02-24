---
title: استخراج الروابط من ملف PDF باستخدام بايثون
linktitle: استخراج الروابط
type: docs
weight: 30
url: /ar/python-net/extract-links/
description: اكتشف كيفية استخراج الروابط التشعبية من مستندات PDF باستخدام بايثون و Aspose.PDF لإدارة المحتوى وتحليل الروابط.
lastmod: "2025-07-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية استخراج الروابط من PDF
Abstract: يوضح دليل Aspose.PDF للبايثون عبر .NET حول استخراج الروابط كيفية استرجاع تعليقات الروابط التشعبية من مستندات PDF برمجياً باستخدام بايثون. يتضمن الوثيقة أمثلة عملية على الشيفرة ويسلط الضوء على كيفية استخدام هذه الوظيفة لمهام مثل تدقيق الروابط، تحليل التنقل، أو بناء ميزات تفاعلية للمستند. سواءً كنت تعمل مع ملفات PDF صفحة واحدة أو تعالج دفعات كبيرة، يقدم هذا الدليل نهجًا واضحًا وفعالًا لاستخراج الروابط التشعبية.
---

## استخراج الروابط من ملف PDF

يوضح هذا المثال كيف يتم التجول عبر جميع تعليقات الروابط على الصفحة الأولى من ملف PDF باستخدام Aspose.PDF للبايثون. يقوم بتصفية التعليقات لتحديد تلك من نوع LinkAnnotation، ويحولها بأمان، ثم يطبع مؤشر الصفحة وموقعها المستطيلي على الصفحة.

يمكن استخدام ذلك للتصحيح، التحليل، أو التحديثات الآلية لتعليقات الروابط الحالية في ملف PDF.

1. تحميل مستند PDF. استخدم ap.Document(path_infile) لفتح الملف.
1. الوصول إلى التعليقات على الصفحة الأولى. استخدم document.pages[1].annotations لاسترجاع جميع التعليقات.
1. تصفية فقط لأنواع LinkAnnotation. تحقق من الخاصية annotation_type لكل تعليق.
1. تحويل ومعالجة LinkAnnotations. استخدم is_assignable() و cast() لضمان وصول آمن إلى خصائص LinkAnnotation.
1. طباعة تفاصيل التعليق. عرض مؤشر الصفحة والمستطيل (الموقع) لكل رابط.

```python

    import aspose.pdf as ap
    from os import path

    # Construct full path for the input PDF file
    path_infile = path.join(self.dataDir, infile)

    # (Optional) You can construct the output file path if needed later
    # path_outfile = path.join(self.dataDir, outfile)

    # Load the PDF document
    document = ap.Document(path_infile)

    # Retrieve all annotations from the first page and filter only LinkAnnotations
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    # Iterate over each link annotation
    for la in link_annotations:
        # Check if the annotation is a LinkAnnotation (type-safe check)
        if is_assignable(la, ap.annotations.LinkAnnotation):
            # Safely cast the annotation to LinkAnnotation type
            annotation = cast(ap.annotations.LinkAnnotation, la)
            
            # Print annotation location and page index
            print(f"Page: {annotation.page_index}, location: {annotation.rect}")
            print(annotation.page_index)
```

## استخراج الروابط التشعبية من ملف PDF

يوضح هذا الكود كيفية استخراج جميع كائنات LinkAnnotation من الصفحة الأولى لمستند PDF باستخدام Aspose.PDF للبايثون، ثم تحديد تلك التي تحتوي على GoToURIAction. بالنسبة لكل رابط من هذا النوع، يطبع مؤشر الصفحة وURI الهدف.

هذا مفيد لمهام مثل:

- تدقيق الروابط الخارجية في PDF
- استخراج عناوين الوثائق أو روابط الدعم
- اكتشاف الروابط المعطلة أو القديمة

1. تحميل مستند PDF. افتح الملف باستخدام ap.Document.
1. الحصول على جميع تعليقات الروابط من الصفحة الأولى. تصفية التعليقات لتشمل فقط تلك التي نوعها AnnotationType.LINK.
1. التحقق من النوع وتحويله إلى LinkAnnotation. تأكد من أن كل تعليق هو فعلاً LinkAnnotation قبل الوصول إلى خصائصه.
1. فحص نوع فعل الرابط. تصفية الروابط التي تستخدم GoToURIAction (أي الروابط إلى عناوين ويب).
1. استخراج وطباعة الـ URI ومؤشر الصفحة. استخدم .uri للحصول على الرابط الخارجي و .page_index للسياق.

```python

    import aspose.pdf as ap
    from os import path

    # Construct the full path for the input PDF file
    path_infile = path.join(self.dataDir, infile)

    # Optional: construct output file path if needed
    # path_outfile = path.join(self.dataDir, outfile)

    # Load the input PDF document
    document = ap.Document(path_infile)

    # Retrieve all annotations from the first page and filter only link annotations
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.LINK
    ]

    # Iterate through filtered link annotations
    for la in link_annotations:
        # Check if the annotation is a LinkAnnotation (safe type check)
        if is_assignable(la, ap.annotations.LinkAnnotation):
            # Cast the annotation to LinkAnnotation to access link-specific properties
            annotation = cast(ap.annotations.LinkAnnotation, la)

            # Check if the link's action is of type GoToURIAction (external web link)
            if is_assignable(annotation.action, ap.annotations.GoToURIAction):
                # Cast the action to GoToURIAction to access the URI property
                action = cast(ap.annotations.GoToURIAction, annotation.action)

                # Print the page number and the link's URI
                print(f"Page {annotation.page_index}, URI: {action.uri}")
```
