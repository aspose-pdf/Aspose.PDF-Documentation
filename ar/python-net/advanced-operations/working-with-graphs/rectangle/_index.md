---
title: إضافة أشكال مستطيلة إلى PDF في Python
linktitle: إضافة مستطيل
type: docs
weight: 50
url: /ar/python-net/add-rectangle/
description: تعرف على كيفية رسم الأشكال المستطيلة وتعبئتها في ملفات PDF في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: ارسم أشكال المستطيل في ملفات PDF باستخدام Python
Abstract: توضح هذه المقالة كيفية إضافة أشكال مستطيلة إلى مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET. وهي تغطي المستطيلات المحددة والحشوات الصلبة والمتدرجة وشفافية ألفا والتحكم بالترتيب Z.
---

## إضافة كائن مستطيل

Aspose.PDF لبيثون عبر .NET يتيح لك إضافة [المستطيل](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) الأشكال إلى صفحات PDF من خلال [رسم بياني](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) فئة. يمكنك رسم مستطيلات مخططة وتطبيق حشوات صلبة أو متدرجة أو شفافة.

اتبع الخطوات أدناه:

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. أضِف [صفحة](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) إلى مجموعة صفحات من ملف PDF.
1. أضِف [جزء من النص](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/) إلى مجموعة فقرات مثيل الصفحة.
1. ابتكر [رسم بياني](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) مثال.
1. تعيين الحدود لـ [كائن الرسم البياني](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/).
1. أضِف [المستطيل](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) كائن إلى مجموعة أشكال من كائن الرسم البياني.
1. أضف كائن رسم بياني إلى مجموعة فقرات مثيل الصفحة.
1. أضِف [جزء من النص](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/) إلى مجموعة فقرات مثيل الصفحة.
1. واحفظ ملف PDF الخاص بك

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_rectangle(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    text_fragment = ap.text.TextFragment("Rectangle")
    page.paragraphs.add(text_fragment)

    graph = drawing.Graph(400, 300)
    page.paragraphs.add(graph)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)

    rect = drawing.Rectangle(20, 20, 350, 250)
    graph.shapes.add(rect)
    page.paragraphs.add(text_fragment)

    document.save(outfile)
```

![إنشاء مستطيل](create_rectangle.png)

## إنشاء كائن مستطيل معبأ

يوفر Aspose.PDF لـ Python عبر .NET أيضًا ميزة ملء كائن مستطيل بلون معين.

يعرض مقتطف الشفرة التالي كيفية إضافة [المستطيل](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) كائن مليء بالألوان.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def create_rectangle_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(100, 400)
    page.paragraphs.add(graph)

    rect = drawing.Rectangle(100, 100, 200, 120)
    rect.graph_info.fill_color = ap.Color.red
    graph.shapes.add(rect)

    document.save(outfile)
```

نتيجة المستطيل المملوء بلون صلب:

![مستطيل معبأ](fill_rectangle.png)

## إضافة رسم باستخدام تعبئة متدرجة

يدعم Aspose.PDF لـ Python عبر .NET ميزة إضافة كائنات الرسم البياني إلى مستندات PDF وأحيانًا يكون مطلوبًا ملء كائنات الرسم البياني باستخدام Gradient Color.

يعرض مقتطف الشفرة التالي كيفية إضافة [المستطيل](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) كائن مملوء بلون متدرج.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_drawing_with_gradient_fill(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    page.paragraphs.add(graph)

    rect = drawing.Rectangle(0, 0, 300, 300)
    gradient_color = ap.Color()
    gradient_settings = drawing.GradientAxialShading(ap.Color.red, ap.Color.blue)
    gradient_settings.start = ap.Point(0, 0)
    gradient_settings.end = ap.Point(350, 350)
    gradient_color.pattern_color_space = gradient_settings
    rect.graph_info.fill_color = gradient_color
    graph.shapes.add(rect)

    document.save(outfile)
```

![مستطيل متدرج](gradient.png)

## إنشاء مستطيل باستخدام قناة ألوان ألفا

يدعم Aspose.PDF لـ Python عبر .NET أيضًا الشفافية من خلال قناة ألوان ألفا.

يعرض مقتطف الشفرة التالي كيفية إضافة [المستطيل](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) كائن بقيم ألفا.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def create_rectangle_with_alpha_color_channel(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(100, 400)
    page.paragraphs.add(graph)

    rect = drawing.Rectangle(100, 100, 200, 120)
    rect.graph_info.fill_color = ap.Color.from_argb(128, 244, 180, 0)
    graph.shapes.add(rect)

    rect1 = drawing.Rectangle(200, 150, 200, 100)
    rect1.graph_info.fill_color = ap.Color.from_argb(160, 120, 0, 120)
    graph.shapes.add(rect1)

    document.save(outfile)
```

![لون قناة ألفا المستطيل](rectangle_color.png)

## التحكم في ترتيب الأشكال Z

يدعم Aspose.PDF لـ .NET ميزة إضافة كائنات الرسم البياني (على سبيل المثال الرسم البياني والخط والمستطيل وما إلى ذلك) إلى مستندات PDF. عند إضافة أكثر من مثيل لنفس الكائن داخل ملف PDF، يمكننا التحكم في عرضها من خلال تحديد Z-Order. يتم استخدام Z-Order أيضًا عندما نحتاج إلى عرض الكائنات فوق بعضها البعض.

يعرض مقتطف الشفرة التالي خطوات العرض [المستطيل](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) الكائنات فوق بعضها البعض.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing


def _add_rectangle_to_page(
    page: ap.Page,
    x: float,
    y: float,
    width: float,
    height: float,
    color: ap.Color,
    zindex: int,
):
    graph = drawing.Graph(width, height)
    graph.is_change_position = False
    graph.left = x
    graph.top = y
    rect = drawing.Rectangle(0, 0, width, height)
    rect.graph_info.fill_color = color
    rect.graph_info.color = color
    graph.shapes.add(rect)
    graph.z_index = zindex
    page.paragraphs.add(graph)


def control_z_order_of_rectangle(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(375, 300)
    page.page_info.margin.left = 0
    page.page_info.margin.top = 0

    _add_rectangle_to_page(page, 50, 40, 60, 40, ap.Color.red, 2)
    _add_rectangle_to_page(page, 20, 20, 30, 30, ap.Color.blue, 1)
    _add_rectangle_to_page(page, 40, 40, 60, 30, ap.Color.green, 0)

    document.save(outfile)
```

![التحكم في أمر Z](control.png)

## موضوعات الرسم البياني ذات الصلة

- [العمل مع الرسوم البيانية PDF في بايثون](/pdf/ar/python-net/working-with-graphs/)
- [تحقق من حدود الشكل في رسوم PDF باستخدام Python](/pdf/ar/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/)
- [أضف أشكال الخطوط إلى PDF في Python](/pdf/ar/python-net/add-line/)
- [أضف الأشكال البيضاوية إلى PDF في Python](/pdf/ar/python-net/add-ellipse/)