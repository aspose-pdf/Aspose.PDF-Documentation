---
title: إضافة أشكال بيضاوية إلى PDF في Python
linktitle: إضافة شكل بيضاوي
type: docs
weight: 60
url: /ar/python-net/add-ellipse/
description: تعرف على كيفية رسم الأشكال البيضاوية وتعبئتها وتسميتها في ملفات PDF في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: ارسم الأشكال البيضاوية في ملفات PDF باستخدام Python
Abstract: توضح هذه المقالة كيفية إضافة أشكال بيضاوية إلى مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET. وهي تغطي الأشكال البيضاوية المحددة والأشكال البيضاوية المملوءة وإضافة نص داخل كائنات القطع الناقص.
---

## إضافة كائن بيضاوي

Aspose.PDF لبيثون عبر .NET يتيح لك إضافة [الشكل البيضاوي](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/ellipse/) الأشكال إلى صفحات PDF باستخدام [رسم بياني](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) فئة. يمكنك رسم الخطوط العريضة للقطع الناقص وتطبيق ألوان التعبئة ووضع النص داخل كائنات القطع الناقص.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_ellipse(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    ellipse1 = drawing.Ellipse(150, 100, 120, 60)
    ellipse1.graph_info.color = ap.Color.green_yellow
    ellipse1.text = ap.text.TextFragment("Ellipse")
    graph.shapes.add(ellipse1)

    ellipse2 = drawing.Ellipse(50, 50, 18, 300)
    ellipse2.graph_info.color = ap.Color.dark_red
    graph.shapes.add(ellipse2)

    page.paragraphs.add(graph)
    document.save(outfile)
```

![إضافة شكل بيضاوي](ellipse.png)

## إنشاء كائن بيضاوي معبأ

يعرض مقتطف الشفرة التالي كيفية إضافة [الشكل البيضاوي](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/ellipse/) كائن مليء بالألوان.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def create_ellipse_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    ellipse1 = drawing.Ellipse(100, 100, 120, 180)
    ellipse1.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(ellipse1)

    ellipse2 = drawing.Ellipse(200, 150, 180, 120)
    ellipse2.graph_info.fill_color = ap.Color.dark_red
    graph.shapes.add(ellipse2)

    page.paragraphs.add(graph)
    document.save(outfile)
```

![شكل بيضاوي محشو](fill_ellipse.png)

## إضافة نص داخل الشكل البيضاوي

يتيح لك Aspose.PDF لـ Python عبر .NET أيضًا وضع نص داخل كائنات الشكل. يضيف المثال التالي نصًا إلى الأشكال البيضاوية.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_text_inside_ellipse(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    text_fragment = ap.text.TextFragment("Ellipse")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Helvetica")
    text_fragment.text_state.font_size = 24

    ellipse1 = ap.drawing.Ellipse(100, 100, 120, 180)
    ellipse1.graph_info.fill_color = ap.Color.green_yellow
    ellipse1.text = text_fragment
    graph.shapes.add(ellipse1)

    ellipse2 = ap.drawing.Ellipse(200, 150, 180, 120)
    ellipse2.graph_info.fill_color = ap.Color.dark_red
    ellipse2.text = text_fragment
    graph.shapes.add(ellipse2)

    page.paragraphs.add(graph)
    document.save(outfile)
```

![نص داخل الشكل البيضاوي](text_ellipse.png)

## موضوعات الرسم البياني ذات الصلة

- [العمل مع الرسوم البيانية PDF في بايثون](/pdf/ar/python-net/working-with-graphs/)
- [أضف أشكال الدوائر إلى PDF في Python](/pdf/ar/python-net/add-circle/)
- [أضف أشكال المنحنيات إلى PDF في Python](/pdf/ar/python-net/add-curve/)
- [إضافة أشكال مستطيلة إلى PDF في Python](/pdf/ar/python-net/add-rectangle/)
