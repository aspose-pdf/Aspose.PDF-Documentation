---
title: التعليقات التوضيحية التفاعلية باستخدام Python
linktitle: التعليقات التوضيحية التفاعلية
type: docs
weight: 60
url: /ar/python-net/interactive-annotations/
description: تعرف على كيفية إضافة التعليقات التوضيحية للروابط وقراءتها وحذفها، وكيفية إنشاء أزرار التنقل والطباعة في مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: اعمل مع التعليقات التوضيحية التفاعلية وأزرار PDF في Python.
Abstract: تشرح هذه المقالة كيفية التعامل مع التعليقات التوضيحية التفاعلية في ملفات PDF باستخدام Aspose.PDF لـ Python عبر .NET. ويغطي إضافة التعليقات التوضيحية للرابط، وقراءة مناطق الارتباط الحالية، وحذف التعليقات التوضيحية للرابط، وإنشاء أزرار التنقل في الصفحة، وإضافة زر طباعة إلى مستند PDF.
---

توضح هذه المقالة كيفية التعامل مع التعليقات التوضيحية التفاعلية في مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET.

يوضح البرنامج النصي النموذجي العديد من عمليات سير العمل الشائعة:

- إضافة تعليق توضيحي للرابط إلى نص موجود
- احصل على مستطيلات التعليقات التوضيحية للرابط من صفحة
- حذف التعليقات التوضيحية للرابط
- إنشاء أزرار التنقل
- إنشاء زر طباعة

## التعليق التوضيحي للرابط

### إضافة تعليق توضيحي للرابط

يبحث هذا المثال في الصفحة الأولى عن جزء النص `"file"` ويضع تعليقًا توضيحيًا للرابط قابل للنقر فوق منطقة النص المطابقة. عندما ينقر المستخدم على التعليق التوضيحي، يفتح PDF عنوان الويب المحدد.

#### قم بتحميل المستند وابحث عن النص الهدف

قم بإنشاء `Document` الكائن والاستخدام `TextFragmentAbsorber` للبحث عن النص الذي سيصبح تفاعليًا.

```python
document = ap.Document(infile)
text_fragment_absorber = ap.text.TextFragmentAbsorber("file")

document.pages[1].accept(text_fragment_absorber)
phone_number_fragment = text_fragment_absorber.text_fragments[1]
```

#### قم بإنشاء التعليق التوضيحي للرابط

قم ببناء `LinkAnnotation` باستخدام مستطيل جزء النص المطابق وتعيين إجراء URI له.

```python
link_annotation = ap.annotations.LinkAnnotation(
    document.pages[1], phone_number_fragment.rectangle
)
link_annotation.action = ap.annotations.GoToURIAction("https://www.aspose.com")
```

#### أضف التعليق التوضيحي واحفظ ملف PDF

قم بإلحاق التعليق التوضيحي بالصفحة وحفظ الملف المحدث.

```python
document.pages[1].annotations.append(link_annotation)
document.save(outfile)
```

#### مثال كامل

```python
def link_add(infile, outfile):
    document = ap.Document(infile)
    text_fragment_absorber = ap.text.TextFragmentAbsorber("file")

    document.pages[1].accept(text_fragment_absorber)
    phone_number_fragment = text_fragment_absorber.text_fragments[1]

    link_annotation = ap.annotations.LinkAnnotation(
        document.pages[1], phone_number_fragment.rectangle
    )
    link_annotation.action = ap.annotations.GoToURIAction("https://www.aspose.com")

    document.pages[1].annotations.append(link_annotation)
    document.save(outfile)
```

### احصل على تعليق توضيحي للرابط

لفحص الروابط التفاعلية الموجودة، قم بتصفية مجموعة التعليقات التوضيحية في الصفحة الأولى واحتفظ فقط بالعناصر التي يكون نوعها `LINK`. تقوم العينة بعد ذلك بطباعة المستطيل لكل تعليق توضيحي مطابق.

#### قم بتحميل ملف PDF وجمع التعليقات التوضيحية للرابط

```python
document = ap.Document(infile)
link_annotations = [
    a
    for a in document.pages[1].annotations
    if (a.annotation_type == ap.annotations.AnnotationType.LINK)
]
```

#### اقرأ مستطيلات التعليقات التوضيحية

قم بتكرار التعليقات التوضيحية التي تمت تصفيتها وقم بطباعة إحداثيات كل منطقة ارتباط.

```python
for link_annotation in link_annotations:
    print(link_annotation.rect)
```

#### مثال كامل

```python
def link_get(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for link_annotation in link_annotations:
        print(link_annotation.rect)
```

### حذف التعليق التوضيحي للرابط

يزيل سير العمل هذا جميع التعليقات التوضيحية للروابط من الصفحة الأولى ويحفظ ملف PDF الذي تم تنظيفه كملف جديد.

#### ابحث عن التعليقات التوضيحية للرابط لإزالتها

```python
document = ap.Document(infile)
link_annotations = [
    a
    for a in document.pages[1].annotations
    if (a.annotation_type == ap.annotations.AnnotationType.LINK)
]
```

#### احذف كل تعليق توضيحي للرابط

```python
for link_annotation in link_annotations:
    document.pages[1].annotations.delete(link_annotation)
```

#### احفظ المستند المحدث

```python
document.save(outfile)
```

#### مثال كامل

```python
def link_delete(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for link_annotation in link_annotations:
        document.pages[1].annotations.delete(link_annotation)

    document.save(outfile)
```

## التعليق التوضيحي للويدجت

### إضافة زر التنقل

تعد أزرار التنقل مفيدة في ملفات PDF متعددة الصفحات عندما تريد أن يتنقل القراء بين الصفحات دون استخدام واجهة العارض. تضيف هذه العينة `Previous Page` و `Next Page` أزرار لكل صفحة.

#### تعريف إعدادات الأزرار

قم بتخزين تسميات الأزرار والمواضع والإجراءات المحددة مسبقًا في قائمة تكوين بسيطة.

```python
button_config = [
    ("Previous Page", 120.0, ap.annotations.PredefinedAction.PREV_PAGE),
    ("Next Page", 230.0, ap.annotations.PredefinedAction.NEXT_PAGE),
]
```

#### قم بتحميل ملف PDF وتأكد من وجود صفحات متعددة

يفتح النموذج المستند المصدر ويضيف صفحة أخرى بحيث تحتوي إجراءات التنقل على صفحتين على الأقل للعمل بهما.

```python
document = ap.Document(infile)
document.pages.add()
```

#### قم بإنشاء الأزرار في كل صفحة

لكل صفحة، قم بإنشاء ملف `ButtonField`، قم بتعيين النص والألوان الخاصة به، وقم بتعيين إجراء تنقل محدد مسبقًا، ثم قم بإضافته إلى النموذج.

```python
for page in document.pages:
    for name, x_pos, action in button_config:
        rect = ap.Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
        button = ap.forms.ButtonField(page, rect)
        button.partial_name = name
        button.value = name
        button.characteristics.border = ap.Color.red.to_rgb()
        button.characteristics.background = ap.Color.orange.to_rgb()
        button.actions.on_release_mouse_btn = ap.annotations.NamedAction(action)
        document.form.add(button)
```

#### احفظ النتيجة

```python
document.save(outfile)
```

#### مثال كامل

```python
def navigation_buttons_add(infile, outfile):
    button_config = [
        ("Previous Page", 120.0, ap.annotations.PredefinedAction.PREV_PAGE),
        ("Next Page", 230.0, ap.annotations.PredefinedAction.NEXT_PAGE),
    ]

    document = ap.Document(infile)
    document.pages.add()

    for page in document.pages:
        for name, x_pos, action in button_config:
            rect = ap.Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
            button = ap.forms.ButtonField(page, rect)
            button.partial_name = name
            button.value = name
            button.characteristics.border = ap.Color.red.to_rgb()
            button.characteristics.background = ap.Color.orange.to_rgb()
            button.actions.on_release_mouse_btn = ap.annotations.NamedAction(action)
            document.form.add(button)

    document.save(outfile)
```

### إضافة زر طباعة

يقوم هذا المثال بإنشاء ملف PDF جديد من صفحة واحدة ووضع زر طباعة بالقرب من أعلى الصفحة. يؤدي النقر فوق الزر إلى تشغيل إجراء الطباعة المحدد مسبقًا في عارض PDF متوافق.

#### قم بإنشاء ملف PDF جديد وإضافة صفحة

```python
document = ap.Document()
page = document.pages.add()
```

#### إنشاء الزر وتكوينه

حدد مستطيل الزر، وقم بإنشاء `ButtonField`، قم بتعيين التسمية التوضيحية الخاصة به، ثم قم بإرفاق إجراء الطباعة.

```python
rect = ap.Rectangle(72, 748, 164, 768, True)

print_button = ap.forms.ButtonField(page, rect)
print_button.alternate_name = "Print current document"
print_button.color = ap.Color.black
print_button.partial_name = "printBtn1"
print_button.value = "Print Document"
print_button.actions.on_release_mouse_btn = ap.annotations.NamedAction(
    ap.annotations.PredefinedAction.FILE_PRINT
)
```

#### تعيين أنماط الحدود والخلفية

يحدد النموذج حدًا صلبًا ويطبق ألوانًا مخصصة لجعل الزر مرئيًا في المستند.

```python
border = ap.annotations.Border(print_button)
border.style = ap.annotations.BorderStyle.SOLID
border.width = 2
print_button.border = border

print_button.characteristics.border = ap.Color.blue.to_rgb()
print_button.characteristics.background = ap.Color.light_blue.to_rgb()
```

#### أضف الزر واحفظ ملف PDF

```python
document.form.add(print_button)
document.save(outfile)
```

#### مثال كامل

```python
def print_button_add(infile, outfile):
    document = ap.Document()
    page = document.pages.add()

    rect = ap.Rectangle(72, 748, 164, 768, True)

    print_button = ap.forms.ButtonField(page, rect)
    print_button.alternate_name = "Print current document"
    print_button.color = ap.Color.black
    print_button.partial_name = "printBtn1"
    print_button.value = "Print Document"
    print_button.actions.on_release_mouse_btn = ap.annotations.NamedAction(
        ap.annotations.PredefinedAction.FILE_PRINT
    )

    border = ap.annotations.Border(print_button)
    border.style = ap.annotations.BorderStyle.SOLID
    border.width = 2
    print_button.border = border

    print_button.characteristics.border = ap.Color.blue.to_rgb()
    print_button.characteristics.background = ap.Color.light_blue.to_rgb()

    document.form.add(print_button)
    document.save(outfile)
```

## موضوعات ذات صلة

- [استيراد التعليقات التوضيحية وتصديرها](/python-net/import-export-annotations/)
- [التعليقات التوضيحية للتوصيف](/python-net/markup-annotations/)
- [التعليقات التوضيحية لوسائل الإعلام](/python-net/media-annotations/)
- [التعليقات التوضيحية للأمان](/python-net/security-annotations/)
- [التعليقات التوضيحية للشكل](/python-net/shape-annotations/)
- [التعليقات التوضيحية المستندة إلى النص](/python-net/text-based-annotations/)
- [التعليقات التوضيحية للعلامة المائية](/python-net/watermark-annotations/)
