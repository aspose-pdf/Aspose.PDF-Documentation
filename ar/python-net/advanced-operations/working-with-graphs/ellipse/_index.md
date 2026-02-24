---
title: إضافة كائن إهليلج إلى ملف PDF
linktitle: إضافة إهليلج
type: docs
weight: 60
url: /ar/python-net/add-ellipse/
description: تشرح هذه المقالة كيفية إنشاء كائن إهليلج في ملف PDF الخاص بك باستخدام Aspose.PDF للبايثون عبر .NET.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة كائن إهليلج إلى PDF باستخدام بايثون
Abstract: المقالة توفر دليلًا شاملاً حول كيفية استخدام Aspose.PDF للبايثون عبر .NET لإضافة وتخصيص كائنات إهليلج داخل مستندات PDF. يشرح العملية الخاصة بإنشاء وتعديل الإهليلجات، بما في ذلك تعيين أبعادها وألوانها ومواقعها باستخدام وحدة الرسم. يوضح كيفية رسم الإهليلجات على صفحة PDF، مظهرًا القدرة على التحكم في مظهرها وموقعها. يتضمن المثال تعيين خصائص الحدود وإضافة إهليلجات متعددة إلى رسم بياني. يوضح كيفية ملء الإهليلجات بألوان محددة، مقدماً مثالًا حيث يتم ملء إهليلجين بألوان مختلفة وإضافتهما إلى مستند PDF. يشرح كيفية إدراج نص داخل كائنات الإهليلج باستخدام خاصية النص في كائن الرسم. المثال المقدم يظهر كيفية تعيين خصائص الخط وإضافة النص إلى
---

## إضافة كائن إهليلج

يدعم Aspose.PDF للبايثون عبر .NET إضافة كائنات [إهليلج](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/ellipse/) إلى مستندات PDF. كما يقدم ميزة ملء كائن الإهليلج بلون معين.

يوضح هذا المثال كيفية رسم وتخصيص الإهليلجات برمجيًا داخل مستند PDF باستخدام Aspose.PDF للبايثون عبر .NET. من خلال الاستفادة من وحدة الرسم، يمكن للمطورين إنشاء عناصر رسومية معقدة مع تحكم دقيق في مظهرها وموقعها. هذه القدرة أساسية للتطبيقات التي تتطلب إنشاء محتوى رسومي ديناميكي داخل ملفات PDF، مثل المخططات التقنية، والرسوم البيانية، أو الرسوم التوضيحية المخصصة.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add a page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 400)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create first ellipse with specified coordinates and radii
    ellipse1 = drawing.Ellipse(150, 100, 120, 60)
    ellipse1.graph_info.color = ap.Color.green_yellow
    ellipse1.text = ap.TextFragment("Ellipse")

    # Add first ellipse to graph
    graph.shapes.add(ellipse1)

    # Create second ellipse with different dimensions and color
    ellipse2 = drawing.Ellipse(50, 50, 18, 300)
    ellipse2.graph_info.color = ap.Color.dark_red

    # Add second ellipse to graph
    graph.shapes.add(ellipse2)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)

```

![إضافة إهليلج](ellipse.png)

## إنشاء كائن إهليلج ممتلئ

يظهر المقتطف البرمجي التالي كيفية إضافة كائن [إهليلج](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/ellipse/) مملوء باللون.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add a page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 400)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create first ellipse and set its fill color
    ellipse1 = drawing.Ellipse(100, 100, 120, 180)
    ellipse1.graph_info.fill_color = ap.Color.green_yellow

    # Add first ellipse to graph
    graph.shapes.add(ellipse1)

    # Create second ellipse and set its fill color
    ellipse2 = drawing.Ellipse(200, 150, 180, 120)
    ellipse2.graph_info.fill_color = ap.Color.dark_red

    # Add second ellipse to graph
    graph.shapes.add(ellipse2)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

![إهليلج ممتلئ](fill_ellipse.png)

## إضافة نص داخل الإهليلج

يدعم Aspose.PDF للبايثون عبر .NET إضافة نص داخل كائن الرسم البياني. توفر خاصية النص لكائن الرسم البياني خيار تعيين النص لكائن الرسم البياني. يوضح المقتطف البرمجي التالي كيفية إضافة نص داخل كائن إهليلج.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Create Graph instance
    graph = drawing.Graph(400, 400)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    text_fragment = ap.text.TextFragment("Ellipse")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Helvetica")
    text_fragment.text_state.font_size = 24

    ellipse1 = ap.drawing.Ellipse(100, 100, 120, 180)
    ellipse1.graph_info.fill_color = ap.Color.green_yellow
    ellipse1.text = text_fragment
    graph.shapes.append(ellipse1)

    ellipse2 = ap.drawing.Ellipse(200, 150, 180, 120)
    ellipse2.graph_info.fill_color = ap.Color.dark_red
    ellipse2.text = text_fragment
    graph.shapes.append(ellipse2)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF file
    document.save(path_outfile)
```

![نص داخل الإهليلج](text_ellipse.png)

