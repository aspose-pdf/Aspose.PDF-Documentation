---
title: إضافة كائن مستطيل إلى ملف PDF
linktitle: إضافة مستطيل
type: docs
weight: 50
url: /ar/python-net/add-rectangle/
description: توضح هذه المقالة كيفية إنشاء كائن مستطيل في ملف PDF الخاص بك باستخدام Aspose.PDF للغة Python عبر .NET.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة كائن مستطيل إلى PDF باستخدام Python
Abstract: توفر المقالة دليلًا شاملًا حول كيفية إضافة وتعديل كائنات المستطيل في مستندات PDF باستخدام Aspose.PDF للغة Python عبر .NET. تفصِّل العملية لإنشاء مستطيل وإدراجه في مستند PDF، بما في ذلك ضبط الحدود وتعبئته بألوان صلبة أو تدرجات لونية. تشمل المقالة تعليمات خطوة بخطوة مع مقتطفات شفرة توضح إنشاء مستند PDF، وإضافة صفحات، وإدراج كائنات مستطيل بخصائص بصرية مختلفة، مثل التعبئة بألوان صلبة، والتعبئة بتدرجات لونية، والشفافية باستخدام قنوات ألفا. بالإضافة إلى ذلك، تشرح كيفية التحكم في ترتيب Z لكائنات المستطيل لإدارة ترتيب عرضها عندما يتم إضافة أشكال متعددة إلى نفس ملف PDF. يدعم كل قسم بأمثلة بصرية لتوضيح ناتج مقتطفات الشفرة.
---

## إضافة كائن مستطيل

يدعم Aspose.PDF للغة Python عبر .NET ميزة إضافة كائنات رسم (مثل الرسم، الخط، المستطيل، إلخ) إلى مستندات PDF. كما يمكنك إضافة كائن [مستطيل](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) حيث توفر أيضًا إمكانية تعبئة كائن المستطيل.

أولاً، دعنا نلقي نظرة على إمكانية إنشاء كائن مستطيل.

اتبع الخطوات التالية:

1. إنشاء [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) PDF جديد.
1. إضافة [صفحة](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) إلى مجموعة الصفحات في ملف PDF.
1. إضافة [جزء نصي](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) إلى مجموعة الفقرات في مثيل الصفحة.
1. إنشاء مثيل [رسم](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/).
1. تعيين حد لـ [كائن رسم](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/).
1. إضافة كائن [مستطيل](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) إلى مجموعة الأشكال في كائن الرسم.
1. إضافة كائن رسم إلى مجموعة الفقرات في مثيل الصفحة.
1. إضافة [جزء نصي](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) إلى مجموعة الفقرات في مثيل الصفحة.
1. ثم احفظ ملف PDF الخاص بك

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()
    text_fragment = ap.text.TextFragment("Rectangle")

    # Add Text fragment to paragraphs collection of page instance
    page.paragraphs.add(text_fragment)

    # Create Graph instance
    graph = drawing.Graph(400, 300)

    # Add graph object to paragraphs collection of page instance
    page.paragraphs.add(graph)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)
    graph.border = border_info

    # Create Rectangle instance
    rect = drawing.Rectangle(20, 20, 350, 250)

    # Add rectangle object to shape collection of Graph object
    graph.shapes.append(rect)

    # Add Text fragment to paragraphs collection of page instance
    page.paragraphs.add(text_fragment)

    # Save PDF file
    document.save(path_outfile)
```

![إنشاء مستطيل](create_rectangle.png)

## إنشاء كائن مستطيل مملوء

يوفر Aspose.PDF للغة Python عبر .NET أيضًا ميزة تعبئة كائن المستطيل بلون معين.

تُظهر مقتطف الشفرة التالي كيفية إضافة كائن [مستطيل](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) مملوء باللون.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add a page
    page = document.pages.add()

    # Create Graph instance
    graph = drawing.Graph(100, 400)

    # Add graph object to the paragraphs collection of the page instance
    page.paragraphs.add(graph)

    # Create Rectangle instance with specified dimensions
    rect = drawing.Rectangle(100, 100, 200, 120)

    # Specify fill color for the Rectangle object
    rect.graph_info.fill_color = ap.Color.red

    # Add rectangle object to the shapes collection of the Graph object
    graph.shapes.add(rect)

    # Save PDF document
    document.save(path_outfile)
```

ألق نظرة على نتيجة المستطيل المملوء بلون صلب:

![المستطيل المملوء](fill_rectangle.png)

## إضافة رسم بملئ متدرج

يدعم Aspose.PDF للغة Python عبر .NET ميزة إضافة كائنات رسم إلى مستندات PDF وأحيانًا يتطلب تعبئة كائنات الرسم بلون متدرج.

تُظهر مقتطف الشفرة التالي كيفية إضافة كائن [مستطيل](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) مملوء بلون متدرج.

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

    # Add graph object to paragraphs collection of page instance
    page.paragraphs.add(graph)

    # Create Rectangle instance
    rect = drawing.Rectangle(0, 0, 300, 300)

    # Specify fill color for Graph object
    gradient_color = ap.Color()
    gradient_settings = drawing.GradientAxialShading(ap.Color.red, ap.Color.blue)
    gradient_settings.start = ap.Point(0, 0)
    gradient_settings.end = ap.Point(350, 350)
    gradient_color.pattern_color_space = gradient_settings
    rect.graph_info.fill_color = gradient_color

    # Add rectangle object to shape collection of Graph object
    graph.shapes.append(rect)

    # Save PDF file
    document.save(output_file)
```

![مستطيل متدرج](gradient.png)

## إنشاء مستطيل مع قناة لون ألفا

يدعم Aspose.PDF للغة Python .NET تعبئة كائن المستطيل بلون معين. يمكن لكائن المستطيل أيضًا أن يحتوي على قناة لون ألفا لإعطاء مظهر شفاف. تُظهر مقتطف الشفرة التالي كيفية إضافة كائن [مستطيل](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) مع قناة لون ألفا.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Create Graph instance
    graph = drawing.Graph(100, 400)

    # Add graph object to paragraphs collection of page instance
    page.paragraphs.add(graph)

    # Create Rectangle instance
    rect = drawing.Rectangle(100, 100, 200, 120)

    # Specify fill color for Graph object
    rect.graph_info.fill_color = ap.Color.from_argb(128, 244, 180, 0)

    # Add rectangle object to shape collection of Graph object
    graph.shapes.append(rect)

    # Create second rectangle object
    rect1 = drawing.Rectangle(200, 150, 200, 100)
    rect1.graph_info.fill_color = ap.Color.from_argb(160, 120, 0, 120)
    graph.shapes.append(rect1)

    # Save PDF file
    document.save(output_file)
```

![لون قناة ألفا للمستطيل](rectangle_color.png)

## التحكم بترتيب Z للأشكال

يدعم Aspose.PDF للغة .NET ميزة إضافة كائنات رسم (مثل الرسم، الخط، المستطيل، إلخ) إلى مستندات PDF. عند إضافة أكثر من نسخة من نفس الكائن داخل ملف PDF، يمكننا التحكم في عرضها عن طريق تحديد ترتيب Z. يُستخدم ترتيب Z أيضًا عندما نحتاج إلى عرض الكائنات فوق بعضها البعض.

تُظهر مقتطف الشفرة التالي الخطوات لعرض كائنات [مستطيل](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) فوق بعضها البعض.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Set size of PDF page
    page.set_page_size(375, 300)

    # Set left margin for page object as 0
    page.page_info.margin.left = 0

    # Set top margin of page object as 0
    page.page_info.margin.top = 0

    # Create a new rectangle with Color as Red, Z-Order as 0 and certain dimensions
    add_rectangle(page, 50, 40, 60, 40, ap.Color.red, 2)

    # Create a new rectangle with Color as Blue, Z-Order as 0 and certain dimensions
    add_rectangle_to_page(page, 20, 20, 30, 30, ap.Color.blue, 1)

    # Create a new rectangle with Color as Green, Z-Order as 0 and certain dimensions
    add_rectangle_to_page(page, 40, 40, 60, 30, ap.Color.green, 0)

    # Save resultant PDF file
    document.save(output_file)
```

![التحكم بترتيب Z](control.png)
