---
title: إنشاء ملف PDF معقد
linktitle: إنشاء ملف PDF معقد
type: docs
weight: 30
url: /ar/python-net/complex-pdf-example/
description: Aspose.PDF لـ Python عبر .NET يسمح لك بإنشاء مستندات أكثر تعقيدًا تحتوي على صور وأجزاء نصية وجداول في مستند واحد.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بإنشاء ملف PDF معقد باستخدام Python
Abstract: تتوسع هذه المقالة في عملية إنشاء PDF الأساسية الموضحة في مثال «Hello, World» من خلال توضيح كيفية إنشاء مستند PDF أكثر تعقيدًا باستخدام Python و Aspose.PDF. تم تطوير المستند النموذجي لشركة وهمية لخدمات عبّارات الركاب ويتضمن صورة وجزئين نصيين (رأس وفقرة) وجدولًا. تتضمن العملية عدة خطوات - إنشاء كائن «مستند» لإنشاء ملف PDF فارغ، وإضافة «صفحة»، ثم إدراج «صورة» في الصفحة. يتم إنشاء «TextFragment» للرأس باستخدام خط Arial بحجم 24 نقطة ومحاذاة مركزية، والتي تتم إضافتها بعد ذلك إلى فقرات الصفحة. تمت إضافة «TextFragment» ثانية للوصف، باستخدام خط Times New Roman بحجم 14 نقطة مع المحاذاة اليسرى. بعد ذلك، يتم إنشاء جدول وتنسيقه بعرض أعمدة وحدود وحشو محدد. يتضمن الجدول صف رأس يحتوي على خلايا مميزة وصفوف بيانات متعددة تم إنشاؤها عن طريق التكرار
---

ال [مرحبًا بالعالم](/pdf/ar/python-net/hello-world-example/) أظهر المثال خطوات بسيطة لإنشاء مستند PDF باستخدام Python و Aspose.PDF. في هذه المقالة، سنلقي نظرة على إنشاء مستند أكثر تعقيدًا باستخدام Aspose.PDF لـ Python. على سبيل المثال، سنأخذ مستندًا من شركة وهمية تدير خدمات عبّارات الركاب. سوف تحتوي وثيقتنا على صورة وشظيتين نصيتين (رأس وفقرة) وجدول.

إذا قمنا بإنشاء مستند من البداية، فنحن بحاجة إلى اتباع خطوات معينة:

1. قم بإنشاء مثيل [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) كائن. في هذه الخطوة، سننشئ مستند PDF فارغًا مع بعض البيانات الوصفية ولكن بدون صفحات.
1. إضافة [صفحة](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) إلى كائن المستند. لذلك، ستحتوي وثيقتنا الآن على صفحة واحدة.
1. إضافة [صورة](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/) إلى الصفحة.
1. قم بإنشاء [جزء من النص](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) لرأس الصفحة. بالنسبة للرأس، سنستخدم خط Arial بحجم الخط 24pt والمحاذاة المركزية.
1. إضافة رأس إلى الصفحة [فقرات](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties).
1. قم بإنشاء [جزء من النص](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) للحصول على وصف. بالنسبة للوصف، سنستخدم خط Arial بحجم الخط 24pt والمحاذاة المركزية.
1. أضف وصفًا إلى فقرات الصفحة.
1. جدول الإنشاء والتصميم. قم بتعيين عرض العمود والحدود والحشو والخط.
1. إضافة جدول إلى الصفحة [فقرات](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties).
1. احفظ مستندًا "Complex.pdf».

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
    description.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    description.text_state.font_size = 14
    description.horizontal_alignment = ap.HorizontalAlignment.LEFT
    page.paragraphs.add(description)

    # Add table
    table = ap.Table()

    table.column_widths = "200"
    table.border = ap.BorderInfo(ap.BorderSide.BOX, 1.0, ap.Color.dark_slate_gray)
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.BOX, 0.5, ap.Color.black)
    table.default_cell_padding = ap.MarginInfo(4.5, 4.5, 4.5, 4.5)
    table.margin.bottom = 10
    table.default_cell_text_state.font = ap.text.FontRepository.find_font("Helvetica")

    headerRow = table.rows.add()
    headerRow.cells.add("Departs City")
    headerRow.cells.add("Departs Island")

    i = 0
    while i < headerRow.cells.count:
        headerRow.cells[i].background_color = ap.Color.gray
        headerRow.cells[
            i
        ].default_cell_text_state.foreground_color = ap.Color.white_smoke
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
