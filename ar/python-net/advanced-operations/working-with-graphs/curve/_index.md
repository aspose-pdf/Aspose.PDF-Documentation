---
title: إضافة كائن منحنى إلى ملف PDF
linktitle: إضافة منحنى
type: docs
weight: 30
url: /ar/python-net/add-curve/
description: تشرح هذه المقالة كيفية إنشاء كائن منحنى في ملف PDF باستخدام Aspose.PDF للبايثون عبر .NET.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة كائن منحنى إلى PDF باستخدام بايثون
Abstract: تناقش المقالة تنفيذ منحنيات الرسم البياني في مستندات PDF باستخدام مكتبة Aspose.PDF للبايثون عبر .NET. تقدم مفهوم منحنى الرسم البياني، وهو اتحاد للخطوط الإسقاطية، وتفصل خطوات إنشاء كل من المنحنيات البسيرة البسيطة والمملوءة برموز بيزيه برمجيًا. توفر المقالة إرشادات خطوة بخطوة وقطوع شفرة لرسم المنحنيات داخل PDF، مع إبراز التلاعب بالعناصر الرسومية باستخدام وحدة الرسم في Aspose.PDF. تشمل العملية إنشاء نسخة `Document`، وتعريف كائن `Drawing` بأبعاد محددة، وتعيين الحدود، وإضافة كائن `Graph` إلى صفحة PDF. تُظهر النتائج البصرية لهذه الأمثلة البرمجية من خلال صور توضح المنحنيات الناتجة. تستكشف المقالة أيضًا إنشاء كائنات منحنى مملوءة، موضحة كيفية ضبط ألوان التعبئة للمنحنيات، وهو أمر حاسم لتوليد محتوى رسومي ديناميكي مثل المخططات التقنية، والرسوم البيانية، أو الرسومات التوضيحية المخصصة في PDF.
---

## إضافة كائن منحنى

الرسم البياني [منحنى](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/curve/) هو اتحاد متصل للخطوط الإسقاطية، كل خط يلتقي بثلاثة أخرى في نقاط مزدوجة عادية.

في هذه المقالة، سوف نستكشف منحنيات الرسم البياني البسيطة، ومنحنيات مملوءة، التي يمكنك إنشاؤها في مستند PDF الخاص بك.

يوضح هذا المثال كيفية رسم منحنى بيزيه برمجيًا داخل مستند PDF باستخدام Aspose.PDF للبايثون عبر .NET. من خلال الاستفادة من وحدة الرسم، يمكن للمطورين إنشاء عناصر رسومية معقدة مع تحكم دقيق في مظهرها وموقعها. هذه القدرة أساسية للتطبيقات التي تتطلب إنشاء محتوى رسومي ديناميكي داخل ملفات PDF، مثل المخططات التقنية، الرسوم البيانية، أو الرسوم التوضيحية المخصصة.

اتبع الخطوات أدناه:

1. إنشاء [المستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) instance.
1. إنشاء [كائن الرسم](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) بأبعاد معينة.
1. ضبط [الحدود](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) لكائن الرسم.
1. إضافة كائن [رسم بياني](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) إلى مجموعة الفقرات في الصفحة.
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

    # Create a curve and set its properties
    curve1 = drawing.Curve([10, 10, 50, 60, 70, 10, 100, 120])
    curve1.graph_info = drawing.GraphInfo()
    curve1.graph_info.color = ap.Color.green_yellow

    # Add the curve to the graph shapes
    graph.shapes.add(curve1)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

الصورة التالية توضح النتيجة التي تم تنفيذها باستخدام مقتطف الشيفرة الخاص بنا:

![رسم المنحنى](drawing_curve.png)

## إنشاء كائن منحنى مملوء

يظهر هذا المثال كيفية إضافة كائن منحنى مملوء باللون.

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

    # Create a curve and set fill color
    curve1 = drawing.Curve([10, 10, 50, 60, 70, 10, 100, 120])
    curve1.graph_info = drawing.GraphInfo()
    curve1.graph_info.fill_color = ap.Color.green_yellow

    # Add the curve to the graph shapes
    graph.shapes.add(curve1)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

انظر إلى نتيجة إضافة منحنى مملوء:

![منحنى مملوء](filled_curve.png)

