---
title: العمل مع طبقات PDF باستخدام Python
linktitle: العمل مع طبقات PDF
type: docs
weight: 50
url: /ar/python-net/working-with-pdf-layers/
description: المهمة التالية تشرح كيفية قفل طبقة PDF، استخراج عناصر طبقة PDF، تسطيح PDF متعدد الطبقات، ودمج جميع الطبقات داخل PDF في طبقة واحدة.
lastmod: "2025-11-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: التعامل مع طبقات PDF
Abstract: يوفر هذا الدليل نظرة شاملة حول كيفية إدارة ومعالجة طبقات PDF باستخدام مكتبة Aspose.PDF للـ Python عبر .NET. طبقات PDF—المعروفة أيضًا بمجموعات المحتوى الاختياري (OCGs)—تمكن من تنظيم المحتوى في مكونات بصرية منفصلة يمكن تشغيلها أو إيقافها.
---

طبقات PDF وسيلة قوية لتنظيم وعرض المحتوى بمرونة داخل ملف PDF واحد، مما يسمح للمستخدمين بإظهار أو إخفاء أجزاء مختلفة حسب احتياجاتهم.

مع **Aspose.PDF for Python via .NET**، يمكنك:

- قفل/فتح قفل الطبقات للتحكم في الرؤية.
- استخراج الطبقات إلى ملفات أو تدفقات منفصلة.
- تسطيح الطبقات لجعلها دائمة.
- دمج الطبقات في طبقة موحدة واحدة.

## إضافة طبقات إلى PDF

يوضح هذا المثال كيفية إنشاء وإضافة طبقات متعددة إلى مستند PDF باستخدام Aspose.PDF للـ Python عبر .NET. كل طبقة تحتوي على محتوى رسومي منفصل، مثل الخطوط الملونة، والتي يمكن تشغيلها أو إيقافها في عارضات PDF التي تدعم الطبقات.

1. إنشاء مستند PDF جديد وإضافة صفحة.
1. إنشاء وإضافة الطبقة الحمراء.
1. إنشاء وإضافة الطبقة الخضراء.
1. إنشاء وإضافة الطبقة الزرقاء.
1. حفظ مستند PDF.

سيتضمن الـ PDF الناتج ثلاث طبقات منفصلة: خط أحمر، خط أخضر، وخط أزرق. يمكن تشغيل كل منها أو إيقافه في قارئات PDF التي تدعم المحتوى المتعدد الطبقات.

```python

import aspose.pdf as ap
from os import path

def add_colored_layers(outfile: str, data_dir: str) -> None:
    """
    Creates a PDF with three layers (Red, Green, Blue lines).
    
    Args:
        outfile (str): Name of the output PDF file.
        data_dir (str): Directory path to save the file.
    """
    path_outfile = path.join(data_dir, outfile)

    try:
        # Create a new PDF document and add a blank page
        document = ap.Document()
        page = document.pages.add()

        # Helper function to add a colored line layer
        def add_layer(layer_id: str, layer_name: str, color: tuple, y_position: int):
            layer = ap.Layer(layer_id, layer_name)
            layer.contents.append(ap.operators.SetRGBColorStroke(*color))
            layer.contents.append(ap.operators.MoveTo(500, y_position))
            layer.contents.append(ap.operators.LineTo(400, y_position))
            layer.contents.append(ap.operators.Stroke())
            page.layers.append(layer)

        # Add Red, Green, and Blue layers
        add_layer("oc1", "Red Line", (1, 0, 0), 700)
        add_layer("oc2", "Green Line", (0, 1, 0), 750)
        add_layer("oc3", "Blue Line", (0, 0, 1), 800)

        # Save the document
        document.save(path_outfile)
        print(f"\nLayers added successfully.\nFile saved at: {path_outfile}")

    except Exception as e:
        print(f"Error adding layers: {e}")
```

## قفل طبقة PDF

مع Aspose.PDF للـ Python عبر .NET يمكنك فتح ملف PDF، قفل طبقة معينة في الصفحة الأولى، وحفظ المستند مع التغييرات.

يوضح هذا المثال كيفية قفل طبقة (مجموعة محتوى اختياري، OCG) في مستند PDF باستخدام Aspose.PDF للـ Python عبر .NET. القفل يمنع المستخدمين من تغيير رؤية الطبقة في عارض PDF، مما يضمن أن يبقى المحتوى مرئيًا دائمًا (أو مخفيًا) وفقًا لتعريف المستند.

الطرق والخصائص المتاحة:

- layer.lock() – يقفل الطبقة.
- layer.unlock() – يفتح قفل الطبقة.
- layer.locked – يُرجع حالة القفل الحالية.

1. فتح مستند PDF.
1. الوصول إلى الصفحة الأولى من PDF.
1. التحقق مما إذا كانت الصفحة تحتوي على طبقات.
1. الحصول على الطبقة الأولى وقفلها.
1. حفظ الـ PDF المحدّث.

إذا كان الـ PDF يحتوي على طبقات، سيتم قفل الطبقة الأولى، مما يضمن عدم إمكانية تغيير حالة رؤيتها من قبل المستخدم. إذا لم توجد طبقات، سيتم طباعة رسالة بدلاً من ذلك.

```python

import aspose.pdf as ap
from os import path

def lock_layer(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        page = document.pages[1]
        layer = page.layers[0]

        # Lock the layer
        layer.lock()

        # Save updated PDF
        document.save(path_outfile)
```

## استخراج عناصر طبقة PDF

يستخدم هذا المثال مكتبة Aspose.PDF للـ Python عبر .NET لاستخراج طبقات فردية من الصفحة الأولى لمستند PDF وحفظ كل طبقة كملف PDF منفصل.

لإنشاء PDF جديد من طبقة، يمكن استخدام المقتطف البرمجي التالي:

1. تحميل مستند PDF. يتم تحميل ملف PDF المدخل إلى كائن Aspose.PDF.Document.
1. الوصول إلى الطبقات في الصفحة 1. يسترجع البرنامج جميع الطبقات من الصفحة الأولى باستخدام document.pages[1].layers.
1. التحقق من وجود طبقات. إذا لم تُعثر على طبقات، يتم طباعة رسالة وتخرج الدالة.
1. التكرار وحفظ كل طبقة.

```python

import aspose.pdf as ap
from os import path

def save_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers

        # Save each layer to a new PDF
        for layer in layers:
            layer.save(path_outfile)
```

يمكن استخراج عناصر طبقة PDF وحفظها في تدفق ملف PDF جديد:

```python

import aspose.pdf as ap
from os import path

def save_layers_to_stream(path_infile, output_stream):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers
        for layer in layers:
            layer.save(output_stream)
```

## تسطيح PDF متعدد الطبقات

يستخدم هذا البرنامج النصي Aspose.PDF للـ Python عبر .NET لتسطيح جميع الطبقات في الصفحة الأولى من مستند PDF. يقوم التسطيح بدمج المحتوى البصري لكل طبقة في طبقة موحدة واحدة، مما يجعل من الأسهل طباعة أو مشاركة أو حفظ الأرشيف دون فقدان الدقة البصرية أو بيانات الطبقة المحددة.

1. تحميل مستند PDF. يتم تحميل ملف PDF المدخل في كائن Aspose.PDF.Document.
1. الوصول إلى الطبقات في الصفحة 1. يقوم السكريبت باستخراج جميع الطبقات من الصفحة الأولى باستخدام document.pages[1].layers.
1. التحقق من وجود الطبقة. إذا لم يتم العثور على طبقات، يتم طباعة رسالة وتخرج الدالة.
1. تسطيح كل طبقة. يتم تسطيح كل طبقة باستخدام layer.flatten(True)، مما يدمج محتواها في الصفحة.
1. حفظ المستند المعدل.

```python

import aspose.pdf as ap
from os import path

def flatten_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        if not page.layers:
            print("No layers found in the document.")
            return
        # Flatten each layer
        for layer in page.layers:
            layer.flatten(cleanup_content_stream=True)

        document.save(path_outfile)
```

## دمج جميع الطبقات داخل PDF في طبقة واحدة

يستخدم هذا المقتطف من الشيفرة Aspose.PDF لدمج جميع الطبقات في الصفحة الأولى من ملف PDF في طبقة موحدة واحدة باسم مخصص.

1. تحميل مستند PDF. يتم تحميل ملف PDF في كائن Aspose.PDF.Document.
1. الوصول إلى الصفحة والطبقات الخاصة بها. يتم اختيار الصفحة الأولى واستخراج طبقاتها.
1. التحقق من وجود الطبقات. إذا لم توجد طبقات، يتم طباعة رسالة وتخرج العملية.
1. تحديد اسم الطبقة الجديدة. يتم تحديد اسم طبقة جديد ("LayerNew") للنتيجة المدمجة.
1. دمج الطبقات. إذا تم توفير معرف مجموعة محتوى اختياري، يتم استخدامه في الدمج. وإلا، يتم دمج الطبقات باستخدام الاسم الجديد فقط.
1. حفظ المستند

```python

import aspose.pdf as ap
from os import path

def merge_layers(path_infile, path_outfile, new_layer_name, optional_group_id=None):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        if optional_group_id:
            page.merge_layers(new_layer_name, optional_group_id)
        else:
            page.merge_layers(new_layer_name)

        document.save(path_outfile)
```
