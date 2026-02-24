---
title: تحقق من حدود الشكل في مجموعة الأشكال باستخدام بايثون
type: docs
weight: 70
url: /ar/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/
description: تعلم كيفية التحقق من حدود الشكل عند إدراجه في مجموعة الأشكال لضمان أنه يتناسب مع الحاوية الأم.
lastmod: "2025-05-14"
draft: false
TechArticle: true
AlternativeHeadline: دليل للتحقق من حدود الشكل في مجموعة الأشكال
Abstract: تقدم هذه المقالة دليلاً شاملاً حول الاستفادة من ميزة فحص الحدود في مجموعة الأشكال، خاصةً داخل مستندات PDF باستخدام بايثون. تُعدّ هذه الميزة أساسية لضمان أن العناصر الرسومية، مثل الأشكال، تتناسب بشكل مناسب مع الحاويات الأم. يمكن تكوينها لإلقاء استثناء إذا تجاوز المكوّن حدود الحاوية، مما يضمن معالجة أخطاء قوية. يشرح الدليل خطوات إنشاء مستند PDF جديد، إضافة صفحة، وإنشاء عنصر رسومي (شكل مستطيل) داخل كائن رسم بياني. تُوفر تعليمات مفصلة لإنشاء كائن `Document`، إضافة `Page`، وإنشاء كائن `Graph`. يصف إعداد شكل `Rectangle` وتكوين `BoundsCheckMode` إلى `THROW_EXCEPTION_IF_DOES_NOT_FIT`، مما يضمن إلقاء استثناء إذا لم يتناسب الشكل مع الأبعاد المحددة للرسم البياني. يتم توضيح العملية بمثال كود بايثون باستخدام مكتبة Aspose.PDF، مع إبراز التنفيذ العملي لهذه الميزات.
---

توفر هذه المقالة دليلًا مفصلاً حول استخدام ميزة فحص الحدود في مجموعة الأشكال. تضمن هذه الميزة أن العناصر تتناسب مع الحاوية الأم ويمكن تكوينها لإلقاء استثناء إذا لم يتناسب المكوّن.

1. إنشاء PDF جديد [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. إضافة صفحة
1. إنشاء [رسم بياني](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/)
1. إنشاء شكل مستطيل
1. وضع فحص الحدود
1. إضافة الـ[مستطيل](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) إلى الرسم البياني

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Create a Graph object with specified dimensions
    graph = ap.drawing.Graph(100, 100)
    graph.top = 10
    graph.left = 15
    graph.border = ap.BorderInfo(ap.BorderSide.BOX, 1, ap.Color.black)
    page.paragraphs.add(graph)

    # Create a shape object(for example, Rectangle) with specified dimensions
    rect = drawing.Rectangle(-1, 0, 50, 50)
    rect.graph_info.fill_color = ap.Color.tomato

    # Set the BoundsCheck mode to THROW_EXCEPTION_IF_DOES_NOT_FIT
    graph.shapes.update_bounds_check_mode(ap.BoundsCheckMode.THROW_EXCEPTION_IF_DOES_NOT_FIT)

    # Add the rectangle to the graph
    graph.shapes.add(rect)
```            
