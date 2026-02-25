---
title: إنشاء PDF معقد
linktitle: إنشاء PDF معقد
type: docs
weight: 30
url: /ar/python-net/complex-pdf-example/
description: يسمح لك Aspose.PDF للبايثون عبر .NET بإنشاء مستندات أكثر تعقيدًا تحتوي على صور، قطع نصية، وجداول في مستند واحد.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إنشاء PDF معقد باستخدام بايثون
Abstract: يوسع هذا المقال عملية إنشاء PDF الأساسية المعروضة في مثال "Hello, World" من خلال توضيح كيفية إنشاء مستند PDF أكثر تعقيدًا باستخدام بايثون و Aspose.PDF. تم تطوير المستند المثال لشركة خيالية تقدم خدمات العبّارات للركاب ويشمل صورة، قطعتين نصيتين (عنوان وفقرة)، وجدول. تتضمن العملية عدة خطوات - إنشاء كائن `Document` لإنشاء PDF فارغ، إضافة `Page`، ثم إدراج `Image` في الصفحة. يتم إنشاء `TextFragment` للعنوان باستخدام خط Arial بحجم 24pt وتوسيط، ثم يتم إضافته إلى فقرات الصفحة. يتم إضافة `TextFragment` ثاني للوصف، باستخدام خط Times New Roman بحجم 14pt ومحاذاة إلى اليسار. بعد ذلك، يتم إنشاء جدول وتنسيقه بأعمدة بعروض محددة، حدود، وتباعد. يتضمن الجدول صفًا رئيسيًا بخلايا مميزة والعديد من صفوف البيانات التي يتم إنشاؤها بالتكرار
---

أظهر مثال [Hello, World](/pdf/python-net/hello-world-example/) خطوات بسيطة لإنشاء مستند PDF باستخدام بايثون و Aspose.PDF. في هذا المقال، سنستعرض إنشاء مستند أكثر تعقيدًا باستخدام Aspose.PDF للبايثون. كمثال، سنأخذ مستندًا من شركة خيالية تشغل خدمات العبّارات للركاب. سيحتوي مستندنا على صورة، قطعتين نصيتين (عنوان وفقرة)، وجدول.

إذا أنشأنا مستندًا من الصفر، يجب أن نتبع خطوات معينة:

1. إنشاء كائن [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). في هذه الخطوة سننشئ مستند PDF فارغًا مع بعض البيانات الوصفية ولكن بدون صفحات.
1. إضافة [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) إلى كائن المستند. وبالتالي، سيحتوي مستندنا الآن على صفحة واحدة.
1. إضافة [Image](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/) إلى الصفحة.
1. إنشاء [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) للعنوان. للعنوان سنستخدم خط Arial بحجم 24pt وتوسيط.
1. إضافة العنوان إلى [الفقرات](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) في الصفحة.
1. إنشاء [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) للوصف. للوصف سنستخدم خط Arial بحجم 24pt وتوسيط.
1. إضافة (الوصف) إلى فقرات الصفحة.
1. إنشاء وتنسيق جدول. ضبط عرض الأعمدة، الحدود، التباعد، والخط.
1. إضافة (الجدول) إلى [الفقرات](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) في الصفحة.
1. حفظ المستند "Complex.pdf".

```python

from datetime import timedelta
import aspose.pdf as ap

def run_complex(self):

    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()

    # Add image
    imageFileName = self.data_dir + "logo.png"
    page.add_image(imageFileName, ap.Rectangle(20, 730, 120, 830, True))

    # Add Header
    header = ap.text.TextFragment("New ferry routes in Fall 2029")
    header.text_state.font = ap.text.FontRepository.find_font("Arial")
    header.text_state.font_size = 24
    header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    header.position = ap.text.Position(130, 720)
    page.paragraphs.add(header)

    # Add description
    descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. \
    Ferry service is operating at half capacity and on a reduced schedule. Expect lineups."
    description = ap.text.TextFragment(descriptionText)
    description.text_state.font = ap.text.FontRepository.find_font(
        "Times New Roman"
    )
    description.text_state.font_size = 14
    description.horizontal_alignment = ap.HorizontalAlignment.LEFT
    page.paragraphs.add(description)

    # Add table
    table = ap.Table()

    table.column_widths = "200"
    table.border = ap.BorderInfo(
        ap.BorderSide.BOX, 1.0, ap.Color.dark_slate_gray
    )
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.BOX, 0.5, ap.Color.black
    )
    table.default_cell_padding = ap.MarginInfo(4.5, 4.5, 4.5, 4.5)
    table.margin.bottom = 10
    table.default_cell_text_state.font = ap.text.FontRepository.find_font(
        "Helvetica"
    )

    headerRow = table.rows.add()
    headerRow.cells.add("Departs City")
    headerRow.cells.add("Departs Island")

    i = 0
    while i < headerRow.cells.count:
        headerRow.cells[i].background_color = ap.Color.gray
        headerRow.cells[i].default_cell_text_state.foreground_color = (
            ap.Color.white_smoke
        )
        i += 1

    time = timedelta(hours=6, minutes=0)
    incTime = timedelta(hours=0, minutes=30)

    i = 0
    while i < 10:
        dataRow = table.rows.add()
        dataRow.cells.add(str(time))
        time = time.__add__(incTime)
        dataRow.cells.add(str(time))
        i += 1

    page.paragraphs.add(table)

    document.save(self.data_dir + "Complex.pdf")
```

