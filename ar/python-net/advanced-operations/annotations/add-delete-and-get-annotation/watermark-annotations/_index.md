---
title: التعليقات التوضيحية للعلامة المائية باستخدام Python
linktitle: التعليقات التوضيحية للعلامة المائية
type: docs
weight: 70
url: /ar/python-net/watermark-annotations/
description: تعرف على كيفية إضافة التعليقات التوضيحية للعلامة المائية وفحصها وحذفها في مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: اعمل مع التعليقات التوضيحية للعلامة المائية في ملفات PDF باستخدام Python.
Abstract: تشرح هذه المقالة كيفية إنشاء التعليقات التوضيحية للعلامة المائية وقراءتها وإزالتها في مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET. ويغطي إضافة تعليق توضيحي للعلامة المائية النصية مع حالة النص المخصصة والتعتيم، وفحص التعليقات التوضيحية للعلامة المائية الحالية، وحذف التعليقات التوضيحية للعلامة المائية من صفحة PDF.
---

توضح هذه المقالة كيفية التعامل مع التعليقات التوضيحية للعلامة المائية في مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET.

يوضح البرنامج النصي النموذجي ثلاث عمليات سير عمل شائعة:

- إضافة تعليق توضيحي للعلامة المائية
- احصل على مستطيلات التعليقات التوضيحية للعلامة المائية
- حذف التعليقات التوضيحية للعلامة المائية

## إضافة تعليق توضيحي للعلامة المائية

يضيف هذا المثال تعليقًا توضيحيًا للعلامة المائية إلى الصفحة الأولى من مستند PDF. تستخدم العلامة المائية حالة نصية للتحكم في إعدادات الخط وتطبق عتامة مخصصة لمظهر شبه شفاف.

### افتح ملف PDF واحصل على الصفحة المستهدفة

```python
document = ap.Document(infile)
page = document.pages[1]
```

### قم بإنشاء التعليق التوضيحي للعلامة المائية

حدد مستطيل التعليقات التوضيحية وألحقه بمجموعة التعليقات التوضيحية للصفحة.

```python
watermark_annotation = ap.annotations.WatermarkAnnotation(
    page,
    ap.Rectangle(100, 100, 400, 200, True),
)

page.annotations.append(watermark_annotation)
```

### تكوين مظهر النص

قم بإنشاء `TextState` كائن للتحكم في لون النص وحجم الخط وعائلة الخط.

```python
text_state = ap.text.TextState()
text_state.foreground_color = ap.Color.blue
text_state.font_size = 25
text_state.font = ap.text.FontRepository.find_font("Arial")
```

### تعيين العتامة ونص العلامة المائية

يستخدم النموذج عتامة بنسبة 50٪ ويكتب ثلاثة أسطر نصية في التعليق التوضيحي للعلامة المائية.

```python
watermark_annotation.opacity = 0.5
watermark_annotation.set_text_and_state(["HELLO", "Line 1", "Line 2"], text_state)
```

### احفظ ملف PDF

```python
document.save(outfile)
```

### مثال كامل

```python
def watermark_add(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    watermark_annotation = ap.annotations.WatermarkAnnotation(
        page,
        ap.Rectangle(100, 100, 400, 200, True),
    )

    page.annotations.append(watermark_annotation)

    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.blue
    text_state.font_size = 25
    text_state.font = ap.text.FontRepository.find_font("Arial")

    watermark_annotation.opacity = 0.5
    watermark_annotation.set_text_and_state(["HELLO", "Line 1", "Line 2"], text_state)

    document.save(outfile)
```

## احصل على تعليق توضيحي للعلامة المائية

لفحص التعليقات التوضيحية للعلامة المائية الحالية، قم بتصفية التعليقات التوضيحية للصفحة الأولى بواسطة `WATERMARK` اكتب واطبع المستطيلات الخاصة بهم.

### قم بتحميل المستند وجمع التعليقات التوضيحية للعلامة المائية

```python
document = ap.Document(infile)
watermark_annotations = [
    a
    for a in document.pages[1].annotations
    if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
]
```

### اطبع مستطيلات التعليقات التوضيحية

```python
for watermark_annotation in watermark_annotations:
    print(watermark_annotation.rect)
```

### مثال كامل

```python
def watermark_get(infile, outfile):
    document = ap.Document(infile)
    watermark_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
    ]

    for watermark_annotation in watermark_annotations:
        print(watermark_annotation.rect)
```

## حذف التعليق التوضيحي للعلامة المائية

يزيل سير العمل هذا جميع التعليقات التوضيحية للعلامة المائية من الصفحة الأولى ويحفظ ملف PDF المحدث.

### ابحث عن التعليقات التوضيحية للعلامة المائية لإزالتها

```python
document = ap.Document(infile)
watermark_annotations = [
    a
    for a in document.pages[1].annotations
    if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
]
```

### احذف التعليقات التوضيحية واحفظ ملف PDF

```python
for watermark_annotation in watermark_annotations:
    document.pages[1].annotations.delete(watermark_annotation)

document.save(outfile)
```

### مثال كامل

```python
def watermark_delete(infile, outfile):
    document = ap.Document(infile)
    watermark_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
    ]

    for watermark_annotation in watermark_annotations:
        document.pages[1].annotations.delete(watermark_annotation)

    document.save(outfile)
```

## موضوعات ذات صلة

- [استيراد التعليقات التوضيحية وتصديرها](/python-net/import-export-annotations/)
- [التعليقات التوضيحية التفاعلية](/python-net/interactive-annotations/)
- [التعليقات التوضيحية للتوصيف](/python-net/markup-annotations/)
- [التعليقات التوضيحية لوسائل الإعلام](/python-net/media-annotations/)
- [التعليقات التوضيحية للأمان](/python-net/security-annotations/)
- [التعليقات التوضيحية للشكل](/python-net/shape-annotations/)
- [التعليقات التوضيحية المستندة إلى النص](/python-net/text-based-annotations/)
