---
title: إضافة أشكال القوس إلى PDF في Python
linktitle: إضافة قوس
type: docs
weight: 10
url: /ar/python-net/add-arc/
description: تعرف على كيفية رسم الأشكال القوسية وتعبئتها في ملفات PDF في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: ارسم أشكال القوس في ملفات PDF باستخدام Python
Abstract: توضح هذه المقالة كيفية إضافة أشكال القوس إلى مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET. وهي تغطي إنشاء أقواس محددة ورسم مقاطع القوس المملوءة وإضافتها إلى حاوية الرسم البياني.
---

## إضافة كائن قوس

Aspose.PDF لبيثون عبر .NET يتيح لك إضافة [قوس](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/arc/) الأشكال إلى صفحات PDF باستخدام [رسم بياني](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) فئة. يمكنك رسم الأقواس المحددة ومقاطع القوس المملوءة للمخططات والرسوم التوضيحية الفنية.

اتبع الخطوات أدناه:

1. ابتكر [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) مثال.
1. ابتكر [كائن الرسم البياني](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) بأبعاد معينة.
1. مجموعة [الحدود](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) لكائن الرسم البياني.
1. قم بإنشاء كائن قوس مطابق.
1. أضف هذا الكائن إلى مجموعة الأشكال في كائن الرسم البياني.
1. أضِف [رسم بياني](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) الاعتراض على مجموعة الفقرات من الصفحة.
1. احفظ ملف PDF الخاص بنا.

يعرض مقتطف الشفرة التالي كيفية إضافة [قوس](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/arc/) كائن.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_arc(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    arc1 = drawing.Arc(100, 100, 95, 0, 90)
    arc1.graph_info.color = ap.Color.green_yellow
    graph.shapes.add(arc1)

    arc2 = drawing.Arc(100, 100, 90, 70, 180)
    arc2.graph_info.color = ap.Color.dark_blue
    graph.shapes.add(arc2)

    arc3 = drawing.Arc(100, 100, 85, 120, 210)
    arc3.graph_info.color = ap.Color.red
    graph.shapes.add(arc3)

    page.paragraphs.add(graph)
    document.save(outfile)
```

## إنشاء كائن القوس المملوء

يوضح هذا المثال كيفية إضافة مقطع قوس مليء بالألوان.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_arc_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    arc = drawing.Arc(100, 100, 95, 0, 90)

    arc.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(arc)

    line = drawing.Line([195, 100, 100, 100, 100, 195])
    line.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(line)

    page.paragraphs.add(graph)
    document.save(outfile)
```

نتيجة إضافة قوس مملوء:

![قوس مملوء](filled_arc.png)

## موضوعات الرسم البياني ذات الصلة

- [العمل مع الرسوم البيانية PDF في بايثون](/pdf/ar/python-net/working-with-graphs/)
- [أضف أشكال الدوائر إلى PDF في Python](/pdf/ar/python-net/add-circle/)
- [أضف أشكال المنحنيات إلى PDF في Python](/pdf/ar/python-net/add-curve/)
- [أضف أشكال الخطوط إلى PDF في Python](/pdf/ar/python-net/add-line/)