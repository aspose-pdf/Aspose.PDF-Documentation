---
title: العمل مع طبقات PDF باستخدام بايثون
linktitle: العمل مع طبقات PDF
type: docs
weight: 50
url: /ar/python-net/work-with-pdf-layers/
description: تشرح هذه المقالة كيفية قفل طبقة PDF، استخراج عناصر طبقة PDF، تسطيح PDF متعدد الطبقات، ودمج جميع الطبقات داخل PDF في طبقة واحدة.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية إدارة وقفل واستخراج وتسطيح ودمج طبقات PDF باستخدام بايثون
Abstract: تشرح هذه المقالة كيفية العمل مع طبقات PDF في بايثون باستخدام Aspose.PDF لـ .NET، بما في ذلك قفل الطبقات، استخراج عناصر الطبقة، تسطيح ملفات PDF متعددة الطبقات، ودمج الطبقات.
---

تسمح طبقات PDF للمستند باحتواء مجموعات متعددة من المحتوى يمكن إظهارها أو إخفاؤها بشكل انتقائي. قد تشمل كل طبقة نصًا أو صورًا أو رسومات، ويمكن للمستخدمين تشغيلها أو إيقافها حسب الحاجة. تكون الطبقات مفيدة بشكل خاص في المستندات المعقدة حيث يجب تنظيم المحتوى أو فصله. تستخدم الأمثلة أدناه واجهات برمجة التطبيقات [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) و[`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) وتتعامل مع كائنات [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) عبر مجموعة `layers` الخاصة بالصفحة.

## قفل طبقة PDF

مع Aspose.PDF لبايثون عبر .NET يمكنك فتح ملف PDF (انظر [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/))، قفل طبقة معينة [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) في الصفحة الأولى [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)، وحفظ المستند مع التغييرات.

الطرق والخاصية المتوفرة على كائن [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/):

- `layer.lock()` – قفل الطبقة. (انظر [`Layer.lock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods))
- `layer.unlock()` – فتح قفل الطبقة. (انظر [`Layer.unlock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods))
- `layer.locked` – يُعيد الحالة الحالية للقفل. (انظر [`Layer.locked`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#properties))

1. افتح مستند PDF (انظر [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. استرجع الصفحة الأولى باستخدام مجموعة [`Pages`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) للمستند (انظر [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)).
1. اختر الـ[`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) لقفلها من `page.layers`.
1. استدعِ `layer.lock()` لمنع المستخدمين من تغيير رؤية الطبقة.
1. احفظ المستند المحدث باستخدام [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

import aspose.pdf as ap

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

يتيح لك Aspose.PDF استخراج كل [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) من [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) وحفظه كملف PDF منفصل.

لإنشاء PDF جديد من طبقة، يمكن استخدام مقتطف الشيفرة التالي (يتم الوصول إلى مجموعة `layers` عبر `Page.layers`):

```python

import aspose.pdf as ap

def save_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers

        # Save each layer to a new PDF with a unique filename
        for i, layer in enumerate(layers):
            layer.save(f"{path_outfile}_layer_{i}.pdf")
```

يمكنك أيضًا حفظ الطبقات إلى تدفق:

```python

import aspose.pdf as ap
import io

def save_layers_to_stream(path_infile):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers
        streams = []
        for layer in layers:
            layer_stream = io.BytesIO()
            layer.save(layer_stream)
            layer_stream.seek(0)
            streams.append(layer_stream)
        return streams
```

## تسطيح PDF متعدد الطبقات

التسطيح يجعل الـ[`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) دائمًا على الصفحة، ويزيل وظيفة التبديل.

```python

import aspose.pdf as ap

def flatten_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        # Flatten each layer
        for layer in page.layers:
            layer.flatten(cleanup_content_stream=True)

        document.save(path_outfile)
```

المعامل `cleanup_content_stream` يتحكم فيما إذا كانت علامات مجموعة المحتوى الاختيارية (OCG) تُزال. ضبطه على `False` يسرّع عملية التسطيح. راجع طريقة [`Layer.flatten()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods) للمزيد من التفاصيل.

## دمج جميع الطبقات داخل PDF في طبقة واحدة

يمكنك دمج جميع الطبقات (أو طبقات محددة) في طبقة جديدة واحدة [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) (واجهة دمج الطبقات موجودة في كائن [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)).

الطرق على كائن [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/):

- `page.merge_layers(new_layer_name)` — دمج جميع الطبقات في اسم طبقة جديد (انظر [`Page.MergeLayers()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods)).
- `page.merge_layers(new_layer_name, new_optional_content_group_id)` — دمج باستخدام معرّف مجموعة محتوى اختياري مخصص (انظر [`Page.MergeLayers()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods)).

```python

import aspose.pdf as ap

def merge_layers(path_infile, path_outfile, new_layer_name, optional_group_id=None):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        if optional_group_id:
            page.merge_layers(new_layer_name, optional_group_id)
        else:
            page.merge_layers(new_layer_name)

        document.save(path_outfile)
```
