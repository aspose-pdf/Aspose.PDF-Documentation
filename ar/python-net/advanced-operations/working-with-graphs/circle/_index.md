---
title: إضافة عنصر دائرة إلى ملف PDF
linktitle: إضافة دائرة
type: docs
weight: 20
url: /ar/python-net/add-circle/
description: تشرح هذه المقالة كيفية إنشاء عنصر دائرة في ملف PDF الخاص بك باستخدام Aspose.PDF للبايثون عبر .NET.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة عنصر دائرة إلى PDF باستخدام بايثون
Abstract: توفر المقالة دليلًا حول استخدام Aspose.PDF للبايثون عبر .NET لإنشاء عناصر دائرة داخل مستندات PDF. تشرح عملية إضافة رسومات دائرة محددة ومملوءة، وتبرز كيف يمكن أن تكون مخططات الدائرة أداة مفيدة لعرض البيانات عبر فئات متعددة عندما تمثل البيانات كلًا كاملاً. تتضمن المقالة تعليمات خطوة بخطوة لإنشاء نسخة `Document`، وإعداد كائن `Drawing` بأبعاد محددة، وتطبيق حد، وإضافة كائن `Graph` إلى صفحة PDF. تُظهر أمثلة الشيفرة رسم دائرة بسيطة ودائرة مملوءة، مع تعليمات مفصلة حول ضبط الألوان وإضافة نص إلى الدائرة. كما تُعرض النتائج البصرية لهذه العمليات، مظهرة قدرات Aspose.PDF في تحسين محتوى PDF بعناصر رسومية ديناميكية.
---

## إضافة عنصر دائرة

مثل مخططات الأعمدة، يمكن استخدام مخططات الدائرة لعرض البيانات في عدد من الفئات المنفصلة. ومع ذلك، لا يمكن استخدام مخططات الدائرة إلا عندما تتوفر لديك بيانات لجميع الفئات التي تشكل الكل. لذا دعونا نلقي نظرة على إضافة عنصر [دائرة](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/circle/) باستخدام Aspose.PDF للبايثون .NET.

يوضح هذا المثال كيفية رسم دائرة برمجيًا داخل مستند PDF باستخدام Aspose.PDF للبايثون عبر .NET. من خلال الاستفادة من وحدة الرسم، يمكن للمطورين إنشاء عناصر رسومية معقدة مع تحكم دقيق في مظهرها وموقعها. هذه القدرة أساسية للتطبيقات التي تتطلب إنشاء محتوى رسومي ديناميكي داخل ملفات PDF، مثل المخططات التقنية، الرسوم البيانية، أو الرسومات المخصصة.

اتبع الخطوات التالية:

1. إنشاء نسخة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. إنشاء [Drawing object](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) بأبعاد معينة.
1. تعيين [border](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) لكائن Drawing.
1. إضافة كائن [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) إلى مجموعة الفقرات في الصفحة.
1. حفظ ملف PDF الخاص بنا.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 200)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create a circle with the specified coordinates and radius
    circle = drawing.Circle(100, 100, 40)

    # Set the circle's color
    circle.graph_info = drawing.GraphInfo()
    circle.graph_info.color = ap.Color.green_yellow

    # Add the circle to the graph shapes
    graph.shapes.add(circle)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

ستظهر الدائرة المرسومة كالتالي:

![رسم دائرة](drawing_circle.png)

## إنشاء عنصر دائرة مملوء

يوضح هذا المثال كيفية إضافة عنصر دائرة مملوء باللون.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 200)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create a filled circle
    circle = drawing.Circle(100, 100, 40)
    circle.graph_info = drawing.GraphInfo()
    circle.graph_info.color = ap.Color.green_yellow
    circle.graph_info.fill_color = ap.Color.green
    circle.text = ap.text.TextFragment("Circle")

    # Add the circle to the graph shapes
    graph.shapes.add(circle)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

دعونا نرى نتيجة إضافة دائرة مملوءة:

![دائرة مملوءة](filled_circle.png)


