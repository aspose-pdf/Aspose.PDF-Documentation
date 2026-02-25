---
title: إضافة كائن خط إلى ملف PDF
linktitle: إضافة خط
type: docs
weight: 40
url: /ar/python-net/add-line/
description: تشرح هذه المقالة كيفية إنشاء كائن خط في ملف PDF الخاص بك باستخدام Aspose.PDF للبايثون عبر .NET.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة كائن خط إلى PDF باستخدام بايثون
Abstract: تناقش المقالة كيفية إضافة كائنات خط إلى مستند PDF باستخدام Aspose.PDF للبايثون عبر .NET. تشرح عملية إنشاء مثيل `Document` وإضافة كائن `Graph` إلى PDF. توفر المقالة خطوات مفصلة لإنشاء وتكوين كائن `Line`، بما في ذلك تحديد نمط الخط المتقطع ولونه. تشمل مقاطع شفرة توضح كيفية إضافة خط بسيط، وخط منقط ومشطر، وكيفية رسم خطوط عبر الصفحة لتشكيل نمط صليب. كل قسم يصاحبه تمثيل بصري للـ PDF الناتج. يعتبر هذا الدليل مصدرًا عمليًا للمطورين الذين يرغبون في تحسين مستندات PDF الخاصة بهم باستخدام العناصر الرسومية عبر Aspose.PDF.
---

## إضافة كائن خط

يدعم Aspose.PDF للبايثون عبر .NET إمكانية إضافة كائنات رسومية (مثل الرسوم، الخط، المستطيل إلخ) إلى مستندات PDF. كما يمكنك إضافة كائن [Line](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) حيث يمكنك أيضًا تحديد نمط الخط المتقطع، اللون، وتنسيقات أخرى لعنصر الخط.

اتبع الخطوات أدناه:

1. إنشاء مثيل [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) .
1. إنشاء كائن Graph
1. إضافة كائن [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) إلى مجموعة الفقرات في الصفحة.
1. إنشاء وتكوين الخط
1. إضافة [Line](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) إلى الـ Graph
1. حفظ ملف PDF الخاص بنا.

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
    line = drawing.Line([100, 100, 200, 100])

    # Specify fill color for Graph object
    line.graph_info.dash_array = [0, 1, 0]
    line.graph_info.dash_phase = 1

    # Add rectangle object to shape collection of Graph object
    graph.shapes.append(line)

    # Save PDF file
    document.save(path_outfile)
```

![Add Line](add_line.png)

## كيفية إضافة خط منقط ومشطر إلى مستند PDF الخاص بك

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
    line = drawing.Line([100, 100, 200, 100])

    # Set color for Line object
    line.graph_info.color = ap.Color.red

    # Specify fill color for Graph object
    line.graph_info.dash_array = [0, 1, 0]
    line.graph_info.dash_phase = 1

    # Add rectangle object to shape collection of Graph object
    graph.shapes.append(line)

    # Save PDF file
    document.save(path_outfile)
```

دعونا نتحقق من النتيجة:

![Dashed Line](dash_line.png)

## رسم خط عبر الصفحة

يمكننا أيضًا استخدام كائن الخط لرسم صليب يبدأ من الزاوية اليسرى السفلية إلى الزاوية اليمنى العلوية ومن الزاوية اليسرى العليا إلى الزاوية اليمنى السفلية.

يرجى إلقاء نظرة على مقطع الشفرة التالي لتحقيق هذا المتطلب.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Set page margin on all sides as 0
    page.page_info.margin.left = 0
    page.page_info.margin.right = 0
    page.page_info.margin.bottom = 0
    page.page_info.margin.top = 0

    # Create Graph object with Width and Height equal to page dimensions
    graph = drawing.Graph(page.page_info.width, page.page_info.height)

    # Create first line object starting from Lower-Left to Top-Right corner of page
    line = drawing.Line([page.rect.llx, 0, page.page_info.width, page.rect.ury])

    # Add line to shape collection of Graph object
    graph.shapes.append(line)

    # Draw line from Top-Left corner of page to Bottom-Right corner of page
    line2 = drawing.Line([0, page.rect.ury, page.page_info.width, page.rect.llx])

    # Add line to shape collection of Graph object
    graph.shapes.append(line2)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF file
    document.save(path_outfile)
```

![Drawing Line](draw_line.png)


