---
title: إضافة أشكال خطية إلى PDF في Python
linktitle: إضافة سطر
type: docs
weight: 40
url: /ar/python-net/add-line/
description: تعرف على كيفية رسم أشكال الخطوط والخطوط المصممة في ملفات PDF في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: ارسم أشكال الخطوط في ملفات PDF باستخدام Python
Abstract: توضح هذه المقالة كيفية إضافة أشكال الخطوط إلى مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET. وهي تغطي إنشاء الخطوط الأساسية وتكوين أنماط الخطوط المتقطعة ورسم الخطوط عبر الصفحة.
---

## إضافة كائن سطر

Aspose.PDF لبيثون عبر .NET يتيح لك إضافة [خط](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) الأشكال إلى صفحات PDF باستخدام [رسم بياني](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) فئة. يمكنك التحكم في لون الخط ونمط لوحة القيادة والموضع.

اتبع الخطوات أدناه:

1. ابتكر [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) مثال.
1. إنشاء كائن رسم بياني
1. أضِف [رسم بياني](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) الاعتراض على مجموعة الفقرات من الصفحة.
1. إنشاء الخط وتكوينه
1. أضف [خط](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) إلى الرسم البياني
1. احفظ ملف PDF الخاص بنا.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing


def add_line(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(100, 400)
    page.paragraphs.add(graph)

    line = drawing.Line([100, 100, 200, 100])
    line.graph_info.dash_array = [0, 1, 0]
    line.graph_info.dash_phase = 1
    graph.shapes.add(line)

    document.save(outfile)
```

![إضافة سطر](add_line.png)

## كيفية إضافة خط متقطع إلى مستند PDF الخاص بك

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_dotted_dashed_line(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(100, 400)
    page.paragraphs.add(graph)

    line = drawing.Line([100, 100, 200, 100])
    line.graph_info.color = ap.Color.red
    line.graph_info.dash_array = [0, 1, 0]
    line.graph_info.dash_phase = 1
    graph.shapes.add(line)

    document.save(outfile)
```

نتيجة إضافة خط متقطع منقط:

![خط متقطع](dash_line.png)

## ارسم خطًا عبر الصفحة

يمكنك أيضًا رسم خطوط عبر الصفحة لتشكيل تقاطع.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def draw_line_across_page(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    page.page_info.margin.left = 0
    page.page_info.margin.right = 0
    page.page_info.margin.bottom = 0
    page.page_info.margin.top = 0

    graph = drawing.Graph(page.page_info.width, page.page_info.height)
    line = drawing.Line([page.rect.llx, 0, page.page_info.width, page.rect.ury])
    graph.shapes.add(line)
    line2 = drawing.Line([0, page.rect.ury, page.page_info.width, page.rect.llx])
    graph.shapes.add(line2)
    page.paragraphs.add(graph)

    document.save(outfile)
```

![خط الرسم](draw_line.png)

## موضوعات الرسم البياني ذات الصلة

- [العمل مع الرسوم البيانية PDF في بايثون](/pdf/ar/python-net/working-with-graphs/)
- [أضف أشكال المنحنيات إلى PDF في Python](/pdf/ar/python-net/add-curve/)
- [إضافة أشكال مستطيلة إلى PDF في Python](/pdf/ar/python-net/add-rectangle/)
- [تحقق من حدود الشكل في رسوم PDF باستخدام Python](/pdf/ar/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/)
