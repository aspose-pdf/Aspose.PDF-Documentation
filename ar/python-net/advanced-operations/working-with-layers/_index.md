---
title: العمل مع طبقات PDF باستخدام Python
linktitle: العمل مع طبقات PDF
type: docs
weight: 50
url: /ar/python-net/working-with-pdf-layers/
description: تعرف على كيفية إضافة طبقات PDF وقفلها واستخراجها وتسويتها ودمجها في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إدارة طبقات PDF باستخدام بايثون
Abstract: تشرح هذه المقالة كيفية العمل مع طبقات PDF (مجموعات المحتوى الاختيارية) باستخدام Aspose.PDF لـ Python عبر .NET. تعرف على كيفية إضافة الطبقات، وتأمين رؤية الطبقة، واستخراج محتوى الطبقة، وتسوية المحتوى ذي الطبقات، ودمج الطبقات في طبقة واحدة.
---

تتيح لك طبقات PDF، والتي تسمى أيضًا مجموعات المحتوى الاختيارية (OCGs)، تنظيم المحتوى في مجموعات مرئية منفصلة يمكن عرضها أو إخفاؤها في برامج عرض PDF المتوافقة. في Aspose.PDF، يتم إنشاء عمليات الطبقة حول [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) API.

باستخدام Aspose.PDF لبيثون عبر .NET، يمكنك:

- أضف طبقات متعددة إلى الصفحة.
- قم بقفل الطبقات وفتحها للتحكم في سلوك الرؤية.
- استخرج الطبقات إلى ملفات أو تدفقات منفصلة.
- قم بتسوية المحتوى ذي الطبقات في الصفحة.
- دمج طبقات متعددة في طبقة واحدة.

## إضافة طبقات إلى PDF

يقوم هذا المثال بإنشاء PDF بثلاث طبقات. يستخدم [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)، يضيف [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)، ويلحق [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) الكائنات على تلك الصفحة.

1. قم بإنشاء ملف جديد [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) وأضف [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. قم بإنشاء وإضافة الطبقة الحمراء.
1. قم بإنشاء وإضافة الطبقة الخضراء.
1. قم بإنشاء وإضافة الطبقة الزرقاء.
1. احفظ مستند PDF.

سيحتوي ملف PDF الناتج على ثلاث طبقات منفصلة: خط أحمر وخط أخضر وخط أزرق. يمكن تشغيل كل منها أو إيقاف تشغيلها في قارئات PDF التي تدعم المحتوى متعدد الطبقات.

```python
import aspose.pdf as ap

def add_layers(outfile: str) -> None:
    document = ap.Document()
    page = document.pages.add()

    # Red layer
    layer = ap.Layer("oc1", "Red Line")
    layer.contents.append(ap.operators.SetRGBColorStroke(1, 0, 0))
    layer.contents.append(ap.operators.MoveTo(500, 700))
    layer.contents.append(ap.operators.LineTo(400, 700))
    layer.contents.append(ap.operators.Stroke())
    page.layers.append(layer)

    # Green layer
    layer = ap.Layer("oc2", "Green Line")
    layer.contents.append(ap.operators.SetRGBColorStroke(0, 1, 0))
    layer.contents.append(ap.operators.MoveTo(500, 750))
    layer.contents.append(ap.operators.LineTo(400, 750))
    layer.contents.append(ap.operators.Stroke())
    page.layers.append(layer)

    # Blue layer
    layer = ap.Layer("oc3", "Blue Line")
    layer.contents.append(ap.operators.SetRGBColorStroke(0, 0, 1))
    layer.contents.append(ap.operators.MoveTo(500, 800))
    layer.contents.append(ap.operators.LineTo(400, 800))
    layer.contents.append(ap.operators.Stroke())
    page.layers.append(layer)

    document.save(outfile)
    print(f"Layers added successfully. File saved at {outfile}")
```

## قفل طبقة PDF

يفتح هذا المثال ملف PDF، ويغلق طبقة معينة في الصفحة الأولى، ويحفظ الملف المحدث.

يمنع قفل الطبقة المستخدمين من تغيير حالة رؤية تلك الطبقة في برامج عرض PDF المدعومة. يتم الوصول إلى الطبقات من صفحة وإدارتها من خلال مجموعة طبقات الصفحة.

الأساليب والخصائص المتاحة:

- [`Layer.lock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods) يقفل الطبقة.
- [`Layer.unlock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods) يفتح الطبقة.
- [`Layer.locked`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#properties) تقوم بإرجاع حالة القفل الحالية.

1. افتح وثيقة PDF.
1. قم بالوصول إلى الصفحة الأولى من PDF.
1. تحقق مما إذا كانت الصفحة تحتوي على طبقات.
1. احصل على الطبقة الأولى وقفلها.
1. احفظ ملف PDF المحدث.

إذا كان PDF يحتوي على طبقات، فسيتم تأمين الطبقة الأولى، مما يضمن عدم تغيير حالة الرؤية من قبل المستخدم. في حالة عدم العثور على طبقات، تتم طباعة رسالة بدلاً من ذلك.

```python
import aspose.pdf as ap

def lock_layer(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    page = document.pages[1]

    if len(page.layers) > 0:
        layer = page.layers[0]
        layer.lock()
        document.save(outfile)
        print(f"Layer locked successfully. File saved at {outfile}")
    else:
        print("No layers found in the document.")
```

## استخراج عناصر طبقة PDF

يستخدم هذا المثال Aspose.PDF لـ Python عبر مكتبة.NET لاستخراج الطبقات الفردية من الصفحة الأولى من مستند PDF وحفظ كل طبقة كملف PDF منفصل باستخدام [`Layer.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods).

لإنشاء PDF جديد من طبقة، يمكن استخدام مقتطف الشفرة التالي:

1. قم بتحميل ملف PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. الوصول إلى الطبقات في الصفحة من 1 إلى [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. تحقق من وجود الطبقات.
1. قم بالتكرار من خلال الطبقات وحفظ كل منها.

```python
import aspose.pdf as ap

def extract_layers(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    layers = document.pages[1].layers

    if len(layers) == 0:
        print("No layers found in the document.")
        return

    index = 1
    for layer in layers:
        output_file = outfile.replace(".pdf", f"{index}.pdf")
        layer.save(output_file)
        print(f"Layer {index} saved to {output_file}")
        index += 1
```

من الممكن استخراج عناصر طبقة PDF وحفظها في دفق ملفات PDF جديد:

```python
from io import FileIO
import aspose.pdf as ap

def extract_layers_stream(infile: str, outfile: str) -> None:
    document = ap.Document(infile)

    if len(document.pages[1].layers) == 0:
        print("No layers found in the document.")
        return

    layer = document.pages[1].layers[0]

    with FileIO(outfile, "wb") as output_layer:
        layer.save(output_layer)
    print(f"Layer extracted to stream: {outfile}")
```

## قم بتسوية ملف PDF ذي الطبقات

يستخدم هذا البرنامج النصي Aspose.PDF لـ Python عبر .NET لتسوية جميع الطبقات في الصفحة الأولى من مستند PDF. تعمل التسوية على دمج المحتوى المرئي لكل طبقة في طبقة واحدة موحدة، مما يسهل الطباعة أو المشاركة أو الأرشفة دون فقدان الدقة المرئية أو البيانات الخاصة بالطبقة. يتم تنفيذ العملية مع [`Layer.flatten()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods).

1. قم بتحميل وثيقة PDF.
1. طبقات الوصول في الصفحة 1.
1. تحقق من وجود الطبقات.
1. قم بتسطيح كل طبقة بـ `layer.flatten(True)`.
1. احفظ المستند المعدل.

```python
import aspose.pdf as ap

def flatten_layers(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    layers = document.pages[1].layers

    if len(layers) == 0:
        print("No layers found in the document.")
        return

    for layer in layers:
        layer.flatten(True)

    document.save(outfile)
    print(f"Layers flattened successfully. File saved at {outfile}")
```

## دمج جميع الطبقات في PDF في واحدة

يستخدم مقتطف الشفرة هذا Aspose.PDF لدمج جميع الطبقات في الصفحة الأولى من PDF في طبقة موحدة باسم مخصص باستخدام [`Page.merge_layers()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods).

1. قم بتحميل وثيقة PDF.
1. قم بالوصول إلى الصفحة 1 واسترجع طبقاتها.
1. تحقق من وجود الطبقات.
1. حدد اسم طبقة جديدة.
1. ادمج الطبقات في طبقة واحدة.
1. احفظ المستند.

```python
import aspose.pdf as ap

def merge_layers(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    page = document.pages[1]

    if len(page.layers) == 0:
        print("No layers found in the document.")
        return

    new_layer_name = "LayerNew"
    page.merge_layers(new_layer_name)
    document.save(outfile)
    print(f"Layers merged successfully. File saved at {outfile}")
```

## موضوعات الطبقة ذات الصلة

- [العمل مع صفحات PDF في بايثون](/pdf/ar/python-net/working-with-pages/)
- [العمل مع الجداول في PDF باستخدام Python](/pdf/ar/python-net/working-with-tables/)
- [إضافة صفحات PDF في بايثون](/pdf/ar/python-net/add-pages/)
