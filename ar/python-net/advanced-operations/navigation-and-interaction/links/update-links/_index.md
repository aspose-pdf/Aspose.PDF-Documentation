---
title: تحديث الروابط في PDF باستخدام بايثون
linktitle: تحديث الروابط
type: docs
weight: 20
url: /ar/python-net/update-links/
description: تحديث الروابط في PDF برمجيًا. هذا الدليل يوضح كيفية تحديث الروابط في PDF باستخدام لغة بايثون.
lastmod: "2025-07-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية تحديث الروابط في PDF
Abstract: دليل Aspose.PDF للبايثون عبر .NET حول تحديث الروابط يشرح للمطورين عملية تعديل سلوك الروابط التشعبية داخل مستندات PDF باستخدام بايثون. يوضح كيفية تغيير وجهات الروابط لتشير إلى صفحات معينة أو مواقع ويب خارجية أو حتى ملفات PDF أخرى. يغطي الوثائق أيضًا كيفية تعديل مظهر تعليقات الروابط، بما في ذلك لون النص، ويوفر أمثلة شفرة عملية لكل سيناريو. سواء كنت تصحح عناوين URL قديمة أو تعزز التنقل، يوفر هذا المورد نهجًا واضحًا وفعّالًا لإدارة الروابط برمجيًا.
---

## تحديث لون نص LinkAnnotation

يوضح هذا المثال كيفية اكتشاف جميع تعليقات الروابط في الصفحة الأولى من ملف PDF باستخدام Aspose.PDF للبايثون، ثم تمييز النص القريب من كل رابط بتغيير لون الخط إلى الأحمر. يستخدم TextFragmentAbsorber مع مساحة موسعة قليلاً حول كل مستطيل رابط للعثور على النص المجاور وتعديله.

يمكن استخدام ذلك لـ:

- وضع علامة مرئية على الروابط في المستند
- تحسين إمكانية الوصول من خلال إبراز المحتوى المرتبط
- معالجة ملفات PDF مسبقًا قبل المراجعة أو التصدير

بالنسبة لكل من تعليقات الروابط هذه، يستخرج البرنامج الحدود المستطيلة لها ويوسع تلك المنطقة قليلًا لتشمل النص المجاور، مما يسمح بتحديد بصري أوسع. ثم يطبق TextFragmentAbsorber على هذه المنطقة الموسعة لاستخراج أي قطع نصية موجودة داخلها. يتم تعديل هذه القطاعات الملتقطة بتغيير لون الخط إلى الأحمر، مما يضع علامة فعّالة على النص المحيط للتأكيد والمراجعة. بعد تطبيق جميع هذه التحديثات، يتم حفظ المستند المعدل إلى مسار الإخراج، مع الحفاظ على التعليقات المميّزة ونصها المرتبط.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Load the input PDF document
    document = ap.Document(path_infile)

    # Filter all link annotations on the first page
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.LINK
    ]

    # Loop through each link annotation found
    for la in link_annotations:
        # Create a text absorber for extracting text fragments
        ta = ap.text.TextFragmentAbsorber()

        # Get the rectangle area of the annotation
        rect = la.rect

        # Expand the rectangle slightly to catch text near the link
        rect.llx -= 2  # Lower-left x
        rect.lly -= 2  # Lower-left y
        rect.urx += 2  # Upper-right x
        rect.ury += 2  # Upper-right y

        # Restrict text search to the adjusted rectangle
        ta.text_search_options = ap.text.TextSearchOptions(rect)

        # Apply the absorber to the first page
        ta.visit(document.pages[1])

        # Iterate through found text fragments and change their color to red
        for textFragment in ta.text_fragments:
            textFragment.text_state.foreground_color = ap.Color.red

    # Save the updated PDF document to the output path
    document.save(path_outfile)
```

## تحديث الحدود

يركز البرنامج على الصفحة الأولى من المستند ويستبعد جميع التعليقات، مختارًا فقط تلك التي من نوع LINK — والتي عادةً ما تمثل عناصر تفاعلية، مثل الروابط التشعبية أو أدوات التنقل. لكل من هذه التعليقات، يقوم الكود بتحويلها إلى نوع LinkAnnotation ويحدّث خاصية اللون إلى الأحمر، مما يميّزها بصريًا لتبرز عن باقي المحتوى. بعد تعديل جميع تعليقات الروابط، يتم حفظ المستند المحدث إلى موقع الإخراج المحدد، مع الحفاظ على النمط الجديد.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Load the PDF document
    document = ap.Document(path_infile)

    # Get all annotations of type LINK on the first page
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    # Loop through each link annotation and change its color to red
    for la in link_annotations:
        link_annotation = cast(ap.annotations.LinkAnnotation, la)
        link_annotation.color = ap.Color.red  # Highlight the link in red

    # Save the modified PDF to the output path
    document.save(path_outfile)
```    

## تحديث الوجهة على الويب

بعد إعداد المسارات، يتم تحميل المستند الأصلي باستخدام مكتبة Aspose.PDF، مما يجعل محتواه متاحًا للتعديل. ثم يركز البرنامج على الصفحة الأولى من المستند، مستبعدًا جميع التعليقات ومختارًا فقط تلك التي من نوع الرابط، والتي عادةً ما تمثل مناطق قابلة للنقر أو روابط تشعبية. لتجنب أخطاء النوع وضمان التعامل الآمن، يتم التحقق من كل تعليق باستخدام is_assignable ثم تحويله إلى النوع المناسب LinkAnnotation. إذا كان الرابط مرتبطًا بـ GoToURIAction، أي أنه يشير إلى عنوان ويب، يقوم البرنامج بتحديث هذا الـ URI لتوجيه المستخدمين إلى "https://www.google.com". أخيرًا، بعد تطبيق جميع التغييرات المطلوبة، يتم حفظ المستند المعدل إلى مسار الإخراج المحدد.

```python

    import aspose.pdf as ap
    from os import path

path_infile = path.join(self.dataDir, infile)
path_outfile = path.join(self.dataDir, outfile)

# Load the PDF document
document = ap.Document(path_infile)

# Find all LINK annotations on the first page
link_annotations = [
    a
    for a in document.pages[1].annotations
    if (a.annotation_type == ap.annotations.AnnotationType.LINK)
]

# Loop through annotations and replace target URI
for la in link_annotations:
    # Ensure the annotation is a LinkAnnotation
    if is_assignable(la, ap.annotations.LinkAnnotation):
        annotation = cast(ap.annotations.LinkAnnotation, la)
        
        # Check if the action is of type GoToURIAction
        if is_assignable(annotation.action, ap.annotations.GoToURIAction):
            action = cast(ap.annotations.GoToURIAction, annotation.action)
            
            # Replace the existing URI with Google
            action.uri = "https://www.google.com"

# Save the modified document to output path
document.save(path_outfile)
```
