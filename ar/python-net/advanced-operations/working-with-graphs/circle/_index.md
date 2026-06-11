---
title: أضف أشكال الدائرة إلى PDF في Python
linktitle: إضافة دائرة
type: docs
weight: 20
url: /ar/python-net/add-circle/
description: تعرف على كيفية رسم أشكال الدوائر وتعبئتها في ملفات PDF في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: ارسم أشكال الدوائر في ملفات PDF باستخدام Python
Abstract: توضح هذه المقالة كيفية إضافة أشكال الدوائر إلى مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET. وهي تغطي إنشاء دوائر محددة وملء الدوائر بالألوان ووضع النص داخل كائنات الدائرة.
---

## إضافة كائن الدائرة

Aspose.PDF لبيثون عبر .NET يتيح لك إضافة [دائرة](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/circle/) الأشكال إلى صفحات PDF من خلال [رسم بياني](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) فئة. استخدم الدوائر للرسوم التخطيطية والتعليقات التوضيحية والعناصر المرئية البسيطة.

اتبع الخطوات أدناه:

1. ابتكر [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) مثال.
1. ابتكر [كائن الرسم البياني](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) بأبعاد معينة.
1. مجموعة [الحدود](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) لكائن الرسم البياني.
1. أضِف [رسم بياني](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) الاعتراض على مجموعة الفقرات من الصفحة.
1. احفظ ملف PDF الخاص بنا.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_circle(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 200)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    circle = drawing.Circle(100, 100, 40)
    circle.graph_info.color = ap.Color.green_yellow
    graph.shapes.add(circle)

    page.paragraphs.add(graph)
    document.save(outfile)
```

ستبدو دائرتنا المرسومة كما يلي:

![دائرة الرسم](drawing_circle.png)

## إنشاء كائن الدائرة المملوءة

يوضح هذا المثال كيفية إضافة دائرة وتعبئتها بالألوان.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_circle_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 200)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    circle = drawing.Circle(100, 100, 40)
    circle.graph_info.color = ap.Color.green_yellow
    circle.graph_info.fill_color = ap.Color.green
    circle.text = ap.text.TextFragment("Circle")
    graph.shapes.add(circle)

    page.paragraphs.add(graph)
    document.save(outfile)
```

نتيجة إضافة دائرة مملوءة:

![دائرة مملوءة](filled_circle.png)

## موضوعات الرسم البياني ذات الصلة

- [العمل مع الرسوم البيانية PDF في بايثون](/pdf/ar/python-net/working-with-graphs/)
- [أضف أشكال القوس إلى PDF في Python](/pdf/ar/python-net/add-arc/)
- [أضف الأشكال البيضاوية إلى PDF في Python](/pdf/ar/python-net/add-ellipse/)
- [إضافة أشكال مستطيلة إلى PDF في Python](/pdf/ar/python-net/add-rectangle/)