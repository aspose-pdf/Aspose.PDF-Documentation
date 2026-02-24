---
title: تعديل الجداول في ملف PDF موجود
linktitle: تعديل الجداول
type: docs
weight: 40
url: /ar/python-net/manipulating-tables/
description: تعلم كيفية التعامل مع الجداول في ملفات PDF الموجودة باستخدام Aspose.PDF للغة بايثون عبر .NET، مما يوفر مرونة في تعديل المستند.
lastmod: "2025-09-27"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## تعديل الجداول في ملف PDF موجود

يظهر Aspose.PDF للبايثون كيفية تعديل محتوى خلية محددة داخل جدول في مستند PDF. يستخدم فئة TableAbsorber لتحديد موقع الجداول في الصفحة الأولى، ويصل إلى جزء نصي معين داخل الخلية الأولى من الجدول الأول، ويحدّث نصه، ثم يحفظ ملف PDF المعدل إلى ملف جديد.

1. افتح ملف PDF باستخدام 'ap.Document()'.
1. أنشئ كائن TableAbsorber لاكتشاف الجداول في ملف PDF.
1. يستدعي absorber.visit() للعثور على جميع الجداول في الصفحة الأولى.
1. الوصول إلى جزء نصي محدد:
- يستخرج الجدول الأول.
- يحصل على الصف الأول من الجدول.
- يحدد الجزء النصي الثاني داخل الخلية.
1. تعديل النص.
1. احفظ ملف PDF المحدّث.
1. يطبع تأكيد حفظ الملف.

```python

    import aspose.pdf as ap
    from os import path

    # Define file names and data directory
    data_dir = "."  # or specify your data directory
    infile = "input.pdf"   # replace with your input PDF file name
    outfile = "output.pdf" # replace with your desired output PDF file name

    # Open PDF document
    path_infile = path.join(data_dir, infile)
    path_outfile = path.join(data_dir, outfile)
    document = ap.Document(path_infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    # Get access to first table on page, their first cell and text fragments in it
    fragment = absorber.table_list[0].row_list[0].cell_list[0].text_fragments[1]

    # Change text of the first text fragment in the cell
    fragment.text = "hi world"

    # Save PDF document

    document.save(path_outfile)
    print(f"File saved at: {path_outfile}")
```

## استبدال الجدول القديم بجدول جديد في مستند PDF

يسمح Aspose.PDF باستبدال جدول موجود في ملف PDF بجدول جديد. يفتح مقطع الشيفرة ملف PDF، يحدد الجدول الأول في الصفحة الأولى باستخدام TableAbsorber، ينشئ جدولًا جديدًا بأعمدة ذات عرض مخصص ومحتوى، ثم يستبدل الجدول الأصلي بالجدول الجديد. أخيرًا، يحفظ ملف PDF المحدّث إلى ملف جديد.

يظهر كيف يمكن تعديل بنية الجدول ومحتواه في ملف PDF دون تعديل باقي المستند.

```python

    import aspose.pdf as ap
    from os import path

    # Open PDF document
    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)
    document = ap.Document(path_infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    # Get first table on the page
    table = absorber.table_list[0]

    # Create new table
    new_table = ap.Table()
    new_table.column_widths = "100 100 100"
    new_table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 1.0)

    row = new_table.rows.add()
    row.cells.add("Col 1")
    row.cells.add("Col 2")
    row.cells.add("Col 3")
    row = new_table.rows.add()
    row.cells.add("Col 12")
    row.cells.add("Col 22")
    row.cells.add("Col 32")

    # Replace the table with new one
    absorber.replace(document.pages[1], table, new_table)

    # Save PDF document
    document.save(path_outfile)
    print(f"File saved at: {path_outfile}")
```
