---
title: إنشاء ملف PDF معقد
linktitle: إنشاء ملف PDF معقد
type: docs
weight: 30
url: /ar/python-net/complex-pdf-example/
description: يتيح لك Aspose.PDF لـ Python عبر .NET إنشاء مستندات أكثر تعقيدًا تحتوي على صور وقطع نصية وجداول في مستند واحد.
lastmod: "2022-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

أظهر مثال [Hello, World](/pdf/ar/python-net/hello-world-example/) خطوات بسيطة لإنشاء مستند PDF باستخدام Python و Aspose.PDF. في هذه المقالة، سنلقي نظرة على كيفية إنشاء مستند أكثر تعقيدًا باستخدام Aspose.PDF لـ Python. كمثال، سنأخذ مستندًا من شركة خيالية تدير خدمات عبّارات الركاب. سيحتوي مستندنا على صورة، وقطعتين نصيتين (عنوان وفقرة)، وجدول.

إذا قمنا بإنشاء مستند من البداية، نحتاج إلى اتباع خطوات معينة:

1. إنشاء كائن [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). في هذه الخطوة سنقوم بإنشاء وثيقة PDF فارغة مع بعض البيانات الوصفية ولكن بدون صفحات.
1. إضافة [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) إلى كائن الوثيقة. الآن ستحتوي وثيقتنا على صفحة واحدة.
1. إضافة [Image](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/) إلى الصفحة.
1. إنشاء [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) للرأس. للرأس سنستخدم خط Arial بحجم 24pt ومحاذاة في المنتصف.
1. إضافة الرأس إلى [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) الصفحة.
1. إنشاء [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) للوصف. للوصف سنستخدم خط Arial بحجم 24pt ومحاذاة في المنتصف.
1. إضافة (الوصف) إلى فقرات الصفحة.
1. إنشاء جدول، إضافة خصائص الجدول.

1. إضافة (جدول) إلى [الصفحة](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties).
1. حفظ المستند "Complex.pdf".

```python

    import aspose.pdf as ap

    # تهيئة كائن المستند
    document = ap.Document()
    # إضافة صفحة
    page = document.pages.add()

    # إضافة صورة
    page.add_image(image_file, ap.Rectangle(20, 730, 120, 830, True))

    # إضافة عنوان
    header = ap.text.TextFragment("مسارات العبارات الجديدة في خريف 2020")
    header.text_state.font = ap.text.FontRepository.find_font("Arial")
    header.text_state.font_size = 24
    header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    header.position = ap.text.Position(130, 720)
    page.paragraphs.add(header)

    # إضافة وصف
    descriptionText = "يجب على الزوار شراء التذاكر عبر الإنترنت ويقتصر عدد التذاكر على 5,000 يوميًا. \
    تعمل خدمة العبارات بنصف السعة وعلى جدول زمني مخفض. توقع الاصطفاف."
    description = ap.text.TextFragment(descriptionText)
    description.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    description.text_state.font_size = 14
    description.horizontal_alignment = ap.HorizontalAlignment.LEFT
    page.paragraphs.add(description)

    # إضافة جدول
    table = ap.Table()

    table.column_widths = "200"
    table.border = ap.BorderInfo(ap.BorderSide.BOX, 1.0, ap.Color.dark_slate_gray)
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.BOX, 0.5, ap.Color.black)
    table.default_cell_padding = ap.MarginInfo(4.5, 4.5, 4.5, 4.5)
    table.margin.bottom = 10
    table.default_cell_text_state.font = ap.text.FontRepository.find_font("Helvetica")

    headerRow = table.rows.add()
    headerRow.cells.add("يغادر المدينة")
    headerRow.cells.add("يغادر الجزيرة")

    i = 0
    while i < headerRow.cells.count:
        headerRow.cells[i].background_color = ap.Color.gray
        headerRow.cells[i].default_cell_text_state.foreground_color = ap.Color.white_smoke
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

    document.save(output_pdf)
```