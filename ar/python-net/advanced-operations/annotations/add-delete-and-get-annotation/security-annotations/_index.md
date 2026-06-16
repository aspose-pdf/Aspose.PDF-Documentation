---
title: التعليقات التوضيحية للأمان باستخدام Python
linktitle: التعليقات التوضيحية للأمان
type: docs
weight: 75
url: /ar/python-net/security-annotations/
description: تعرف على كيفية وضع علامة على النص للتنقيح وتطبيق التعليقات التوضيحية وتنقيح مناطق الصور في ملفات PDF باستخدام Aspose.PDF لـ Python عبر .NET.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بتنقيح محتوى PDF الحساس في Python باستخدام التعليقات التوضيحية للأمان.
Abstract: توضح هذه المقالة كيفية التعامل مع التعليقات التوضيحية للأمان في مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET. وهي تغطي وضع علامات على النص المطابق بتعليقات التنقيح، وتطبيق التنقيحات بشكل دائم، وتنقيح مناطق الصورة المحددة بناءً على مستطيلات موضع الصورة المكتشفة.
---

توضح هذه المقالة كيفية استخدام التعليقات التوضيحية للأمان في مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET.

يوضح البرنامج النصي النموذجي ثلاث عمليات سير عمل شائعة للتنقيح:

- ضع علامة على أجزاء النص مع التعليقات التوضيحية للتنقيح
- تطبيق التعليقات التوضيحية الحالية للتنقيح بشكل دائم
- تنقيح منطقة الصورة المكتشفة على الصفحة

## وضع علامة على تنقيح النص

يبحث سير العمل هذا عن النص المطابق في المستند ويضع التعليقات التوضيحية للتنقيح فوق كل مباراة. لا يزيل المحتوى بعد؛ يقوم فقط بوضع علامة على النص لتنقيحه لاحقًا.

### افتح ملف PDF وابحث عن النص الهدف

قم بإنشاء `TextFragmentAbsorber` لمصطلح البحث وتمكين خيارات البحث عن النص العادي قبل مسح جميع الصفحات.

```python
document = ap.Document(infile)
text_fragment_absorber = ap.text.TextFragmentAbsorber(search_term)

text_search_options = ap.text.TextSearchOptions(True)
text_fragment_absorber.text_search_options = text_search_options
document.pages.accept(text_fragment_absorber)
```

### إنشاء تعليقات توضيحية للتنقيح لكل مباراة

لكل جزء من النص المطابق، قم بإنشاء ملف `RedactionAnnotation` باستخدام مستطيل الجزء وتكوين مظهره المرئي.

```python
for text_fragment in text_fragment_absorber.text_fragments:
    page = text_fragment.page
    annotation_rectangle = text_fragment.rectangle
    redaction_annotation = ap.annotations.RedactionAnnotation(
        page, annotation_rectangle
    )
    redaction_annotation.fill_color = ap.Color.gray
    redaction_annotation.border_color = ap.Color.red
    redaction_annotation.color = ap.Color.white
    redaction_annotation.overlay_text = "REDACTED"
    redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
    redaction_annotation.repeat = True
    page.annotations.add(redaction_annotation, True)
```

### احفظ ملف PDF المحدد

```python
document.save(outfile)
```

### مثال كامل

```python
def mark_text_redaction(infile, outfile, search_term):
    document = ap.Document(infile)
    text_fragment_absorber = ap.text.TextFragmentAbsorber(search_term)

    text_search_options = ap.text.TextSearchOptions(True)
    text_fragment_absorber.text_search_options = text_search_options
    document.pages.accept(text_fragment_absorber)

    for text_fragment in text_fragment_absorber.text_fragments:
        page = text_fragment.page
        annotation_rectangle = text_fragment.rectangle
        redaction_annotation = ap.annotations.RedactionAnnotation(
            page, annotation_rectangle
        )
        redaction_annotation.fill_color = ap.Color.gray
        redaction_annotation.border_color = ap.Color.red
        redaction_annotation.color = ap.Color.white
        redaction_annotation.overlay_text = "REDACTED"
        redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
        redaction_annotation.repeat = True
        page.annotations.add(redaction_annotation, True)

    document.save(outfile)
```



## تطبيق التنقيح

بعد إضافة التعليقات التوضيحية للتنقيح، يقوم سير العمل هذا بتطبيقها بشكل دائم على الصفحة الأولى. بمجرد التطبيق، تتم إزالة المحتوى الأصلي من إخراج المستند.

### قم بتحميل ملف PDF وجمع التعليقات التوضيحية للتنقيح

```python
document = ap.Document(infile)
redaction_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.REDACTION
]
```

### قم بتطبيق كل تعليق توضيحي للتنقيح

يتحقق النموذج من إمكانية التعامل مع كل تعليق توضيحي كملف `RedactionAnnotation` قبل الاتصال `redact()`.

```python
for redaction_annotation in redaction_annotations:
    if is_assignable(redaction_annotation, ap.annotations.RedactionAnnotation):
        cast(ap.annotations.RedactionAnnotation, redaction_annotation).redact()
```

### احفظ ملف PDF المنقح

```python
document.save(outfile)
```

### مثال كامل

```python
def apply_redaction(infile, outfile):
    document = ap.Document(infile)
    redaction_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.REDACTION
    ]

    for redaction_annotation in redaction_annotations:
        if is_assignable(redaction_annotation, ap.annotations.RedactionAnnotation):
            cast(ap.annotations.RedactionAnnotation, redaction_annotation).redact()

    document.save(outfile)
```



## منطقة التنقيح

يقوم هذا المثال بتنقيح منطقة الصورة المكتشفة بدلاً من النص. يقوم بمسح الصفحة بحثًا عن مواضع الصور، ويحدد مستطيلًا واحدًا للموضع، ويضيف تعليقًا توضيحيًا على تلك المنطقة.

### افتح ملف PDF واكتشف مواضع الصور

استخدم `ImagePlacementAbsorber` للعثور على مواضع الصور في الصفحة الأولى.

```python
document = ap.Document(infile)

image_placement_absorber = ap.ImagePlacementAbsorber()
page = document.pages[1]
page.accept(image_placement_absorber)
```

### قم بإنشاء تعليق توضيحي للتنقيح لمنطقة الصورة المحددة

تستخدم العينة موضع الصورة الثالث المكتشف وتطبق نفس نمط التنقيح المستخدم في مثال وضع العلامات النصية.

```python
target_rect = image_placement_absorber.image_placements[2].rectangle
redaction_annotation = ap.annotations.RedactionAnnotation(page, target_rect)
redaction_annotation.fill_color = ap.Color.gray
redaction_annotation.border_color = ap.Color.red
redaction_annotation.color = ap.Color.white
redaction_annotation.overlay_text = "REDACTED"
redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
redaction_annotation.repeat = True
```

### أضف التعليق التوضيحي واحفظ ملف PDF

```python
page.annotations.add(redaction_annotation, True)
document.save(outfile)
```

### مثال كامل

```python
def redact_area(infile, outfile):
    document = ap.Document(infile)

    image_placement_absorber = ap.ImagePlacementAbsorber()
    page = document.pages[1]
    page.accept(image_placement_absorber)

    target_rect = image_placement_absorber.image_placements[2].rectangle
    redaction_annotation = ap.annotations.RedactionAnnotation(page, target_rect)
    redaction_annotation.fill_color = ap.Color.gray
    redaction_annotation.border_color = ap.Color.red
    redaction_annotation.color = ap.Color.white
    redaction_annotation.overlay_text = "REDACTED"
    redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
    redaction_annotation.repeat = True

    page.annotations.add(redaction_annotation, True)
    document.save(outfile)
```

## موضوعات ذات صلة

- [استيراد التعليقات التوضيحية وتصديرها](/python-net/import-export-annotations/)
- [التعليقات التوضيحية التفاعلية](/python-net/interactive-annotations/)
- [التعليقات التوضيحية للتوصيف](/python-net/markup-annotations/)
- [التعليقات التوضيحية لوسائل الإعلام](/python-net/media-annotations/)
- [التعليقات التوضيحية للشكل](/python-net/shape-annotations/)
- [التعليقات التوضيحية المستندة إلى النص](/python-net/text-based-annotations/)
- [التعليقات التوضيحية للعلامة المائية](/python-net/watermark-annotations/)
