---
title: إضافة أشكال منحنية إلى PDF في Python
linktitle: إضافة منحنى
type: docs
weight: 30
url: /ar/python-net/add-curve/
description: تعرف على كيفية رسم الأشكال المنحنية وتعبئتها في ملفات PDF في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: ارسم أشكال المنحنيات في ملفات PDF باستخدام Python
Abstract: توضح هذه المقالة كيفية إضافة أشكال منحنية إلى مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET. وهي تغطي إنشاء منحنيات محددة وملء كائنات المنحنيات وعرض مسارات المنحنيات المخصصة في حاوية الرسم البياني.
---

## إضافة كائن منحنى

Aspose.PDF لبيثون عبر .NET يتيح لك إضافة [منحنى](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/curve/) الأشكال إلى صفحات PDF من خلال [رسم بياني](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) فئة.

توضح هذه المقالة كيفية إنشاء كل من المنحنيات المحددة والمملوءة.

اتبع الخطوات أدناه:

1. ابتكر [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) مثال.
1. ابتكر [كائن الرسم البياني](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) بأبعاد معينة.
1. مجموعة [الحدود](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) لكائن الرسم البياني.
1. أضِف [رسم بياني](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) الاعتراض على مجموعة الفقرات من الصفحة.
1. احفظ ملف PDF الخاص بنا.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_curve(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 200)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    curve1 = drawing.Curve([10, 10, 50, 60, 70, 10, 100, 120])
    curve1.graph_info.color = ap.Color.green_yellow
    graph.shapes.add(curve1)

    page.paragraphs.add(graph)
    document.save(outfile)
```

تعرض الصورة التالية النتيجة التي تم تنفيذها باستخدام مقتطف الشفرة الخاص بنا:

![منحنى الرسم](drawing_curve.png)

## إنشاء كائن منحنى معبأ

يوضح هذا المثال كيفية إضافة كائن Curve المليء بالألوان.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing


def add_curve_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 200)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    curve1 = drawing.Curve([10, 10, 50, 60, 70, 10, 100, 120])
    curve1.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(curve1)

    page.paragraphs.add(graph)
    document.save(outfile)
```

نتيجة إضافة منحنى معبأ:

![منحنى معبأ](filled_curve.png)

## موضوعات الرسم البياني ذات الصلة

- [العمل مع الرسوم البيانية PDF في بايثون](/pdf/ar/python-net/working-with-graphs/)
- [أضف أشكال القوس إلى PDF في Python](/pdf/ar/python-net/add-arc/)
- [أضف أشكال الخطوط إلى PDF في Python](/pdf/ar/python-net/add-line/)
- [أضف الأشكال البيضاوية إلى PDF في Python](/pdf/ar/python-net/add-ellipse/)