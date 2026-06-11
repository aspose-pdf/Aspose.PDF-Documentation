---
title: إضافة جداول إلى PDF في Python
linktitle: إضافة جداول
type: docs
weight: 10
url: /ar/python-net/adding-tables/
description: تعرف على كيفية إضافة الجداول وتكوينها في مستندات PDF الموجودة في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة وتنسيق الجداول في مستندات PDF باستخدام Python
Abstract: توضح هذه المقالة كيفية إضافة الجداول وتكوينها في مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET. ويغطي إنشاء الجدول، والحدود، والهوامش، والحشو، وامتدادات الصفوف والأعمدة، وسلوك الملاءمة التلقائية، ومعالجة عرض الجدول، وإدراج الصور في الخلايا، والتحكم في العرض عبر الصفحات.
---

تعد إضافة الجداول إلى مستندات PDF الحالية مطلبًا شائعًا لعرض البيانات والمحتوى المنظم وإعداد التقارير. **Aspose.pdf لـ Python عبر .NET** يوفر واجهة برمجة تطبيقات عملية لإدراج الجداول وتنسيقها في ملفات PDF الحالية.

يقدم هذا الدليل أمثلة خطوة بخطوة لإنشاء الجدول وتغيير حجم الأعمدة والحدود والصفوف والخلايا وحفظ المستند المعدل. كما يغطي أيضًا الخيارات المتقدمة مثل حدود الخلايا والهوامش والحشو وإعدادات الملاءمة التلقائية لحجم الجدول الديناميكي.

استخدم هذه الصفحة عندما تحتاج إلى إضافة جداول جديدة إلى ملفات PDF الحالية والتحكم في سلوك التخطيط الخاص بها في Python.

## إنشاء جداول أساسية

### إنشاء جدول

يوضح هذا المثال كيفية إنشاء جدول في مستند PDF بحدود وصفوف متعددة.

1. قم بإنشاء مستند PDF جديد.
1. يضيف صفحة فارغة إلى المستند.
1. قم بتهيئة الجدول.
1. قم بتعيين حدود الجدول الإجمالية.
1. قم بتعيين الحدود للخلايا الفردية.
1. أضف الصفوف والخلايا.
1. أدخل الجدول في الصفحة.
1. احفظ ملف PDF إلى المسار المحدد.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def create_table(outfile: str) -> None:
    # Create new PDF document
    document = ap.Document()
    page = document.pages.add()
    # Initializes a new instance of the Table
    table = ap.Table()
    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 5, ap.Color.light_gray)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 5, ap.Color.light_gray)
    # Create a loop to add 10 rows
    for row_count in range(10):
        # Add row to table
        row = table.rows.add()
        # Add table cells
        row.cells.add("Column (" + str(row_count) + ", 1)")
        row.cells.add("Column (" + str(row_count) + ", 2)")
        row.cells.add("Column (" + str(row_count) + ", 3)")
    # Add table object to first page of input document
    page.paragraphs.add(table)

    # Save updated document containing table object
    document.save(outfile)
```

### إضافة صور إلى خلايا الجدول

يوضح مقتطف الشفرة هذا كيفية إدراج الصور في خلايا الجدول في مستند PDF.

1. قم بإنشاء مستند PDF جديد.
1. قم بتهيئة الجدول.
1. قم بتعيين عرض الأعمدة بالنقاط.
1. تتم إضافة جزء نصي إلى الخلية الأولى.
1. تتم إضافة مثيل 'ap.image () 'إلى الخلية الثانية.
1. قم بتعيين المسار إلى ملف الصورة باستخدام 'img.file'.
1. يتحكم «img.fix_width» و «img.fix_height» في حجم الصورة داخل الخلية.
1. أدخل الجدول في صفحة PDF.
1. احفظ ملف PDF.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def add_image(image: str, outfile: str) -> None:
    # Instantiate Document object
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    table = ap.Table()
    # Set width for table cells
    table.column_widths = "200 100"

    # Create row object and add it to table instance
    row = table.rows.add()
    # Create cell object and add it to row instance
    cell = row.cells.add()
    # Add textfragment to paragraphs collection of cell object
    cell.paragraphs.add(ap.text.TextFragment(image))
    # Create an image instance
    img = ap.Image()
    # Set image type as SVG
    # Path for source file
    img.file = image
    # Set width for image instance
    img.fix_width = 50
    # Set height for image instance
    img.fix_height = 50
    # Add another cell to row object
    cell = row.cells.add()
    # Add SVG image to paragraphs collection of recently added cell instance
    cell.paragraphs.add(img)

    # Add table to paragraphs collection of page object
    page.paragraphs.add(table)
    # Save PDF file
    document.save(outfile)
```

يمكنك إضافة صور SVG إلى خلايا الجدول في مستند PDF:

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def add_svg_image(images: list[str], outfile: str) -> None:
    # Instantiate Document object
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    table = ap.Table()
    # Set width for table cells
    table.column_widths = "200 100"
    for image in images:
        # Create row object and add it to table instance
        row = table.rows.add()
        # Create cell object and add it to row instance
        cell = row.cells.add()
        # Add textfragment to paragraphs collection of cell object
        cell.paragraphs.add(ap.text.TextFragment(image))
        # Create an image instance
        img = ap.Image()
        # Set image type as SVG
        img.file_type = ap.ImageFileType.SVG
        # Path for source file
        img.file = image
        # Set width for image instance
        img.fix_width = 50
        # Set height for image instance
        img.fix_height = 50
        # Add another cell to row object
        cell = row.cells.add()
        # Add SVG image to paragraphs collection of recently added cell instance
        cell.paragraphs.add(img)

    # Add table to paragraphs collection of page object
    page.paragraphs.add(table)
    # Save PDF file
    document.save(outfile)
```

### ColSpan وrowSpan في الجداول

يوضح هذا المثال كيفية دمج خلايا الجدول رأسيًا وأفقيًا لإنشاء تخطيطات جدول معقدة.

1. قم بتعيين حدود الجدول الإجمالية.
1. قم بتعيين حدود الخلايا الافتراضية.
1. ادمج خليتين أفقيًا في خلية واحدة.
1. ادمج الخلية عموديًا عبر صفين.
1. يقوم الصف 5 بحساب امتداد الصفوف عن طريق تخطي العمود المدمج.
1. أدخل الجدول في الصفحة.
1. احفظ ملف PDF.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def add_rowspan_or_colspan(outfile: str) -> None:
    # Create new PDF document
    document = ap.Document()
    page = document.pages.add()

    # Initializes a new instance of the Table
    table = ap.Table()
    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.black)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.black)
    # Add 1st row to table
    row1 = table.rows.add()
    for cell_count in range(1, 5):
        # Add table cells
        row1.cells.add("Test 1" + str(cell_count))

    # Add 2nd row to table
    row2 = table.rows.add()
    row2.cells.add("Test 2 1")
    cell = row2.cells.add("Test 2 2")
    cell.col_span = 2
    row2.cells.add("Test 2 4")

    # Add 3rd row to table
    row3 = table.rows.add()
    row3.cells.add("Test 3 1")
    row3.cells.add("Test 3 2")
    row3.cells.add("Test 3 3")
    row3.cells.add("Test 3 4")

    # Add 4th row to table
    row4 = table.rows.add()
    row4.cells.add("Test 4 1")
    cell = row4.cells.add("Test 4 2")
    cell.row_span = 2
    row4.cells.add("Test 4 3")
    row4.cells.add("Test 4 4")

    # Add 5th row to table
    row5 = table.rows.add()
    row5.cells.add("Test 5 1")
    row5.cells.add("Test 5 3")
    row5.cells.add("Test 5 4")

    # Add table object to first page of input document
    page.paragraphs.add(table)
    # Save updated document containing table object
    document.save(outfile)
```

![عرض كولسبان وروسبان التجريبي](colspan_rowspan.png)

### تطبيق الحدود على الجداول والخلايا

يوضح هذا المثال كيفية تعيين حشوة الخلايا وهوامش الجدول والتحكم في التفاف الكلمات للنص في خلايا الجدول.

1. قم بتعيين عرض الأعمدة.
1. حدد حدود الجدول والخلايا.
1. قم بتعيين الحشو داخل الخلايا لتباعد متناسق.
1. قم بتطبيق الحشو على جميع الخلايا افتراضيًا.
1. إضافة نص والتحكم في التغليف.
1. أضف الصفوف والخلايا.
1. احفظ ملف PDF.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def add_borders(outfile: str) -> None:
    # Create new PDF document
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    tab1 = ap.Table()
    # Add the table in paragraphs collection of the desired section
    page.paragraphs.add(tab1)
    # Set with column widths of the table
    tab1.column_widths = "50 50 50"
    # Set default cell border using BorderInfo object
    tab1.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)
    # Set table border using another customized BorderInfo object
    tab1.border = ap.BorderInfo(ap.BorderSide.ALL, 1)
    # Create MarginInfo object and set its left, bottom, right and top margins
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5
    # Set the default cell padding to the MarginInfo object
    tab1.default_cell_padding = margin
    # Create rows in the table and then cells in the rows
    row1 = tab1.rows.add()
    row1.cells.add("col1")
    row1.cells.add("col2")
    row1.cells.add()
    text = ap.text.TextFragment("col3 with large text string")
    row1.cells[2].paragraphs.add(text)
    row1.cells[2].is_word_wrapped = False
    row2 = tab1.rows.add()
    row2.cells.add("item1")
    row2.cells.add("item2")
    row2.cells.add("item3")
    # Save updated document containing table object
    document.save(outfile)
```

![الهامش والحدود في جدول PDF](margin-border.png)

## تخطيط الجدول والتحجيم

### تركيب تلقائي للأعمدة والصفوف

يوضح مقتطف الشفرة هذا كيفية ضبط عرض أعمدة الجدول تلقائيًا لتناسب الصفحة.
يرجى ملاحظة أنه في المعلمة table.column_widths = «50 50 50" - نقاطه. ولكن يمكنك أيضًا تحديد سنتيمترات (سم) أو بوصة أو%.

1. قم بتعيين عرض الأعمدة الأولي.
1. يضبط الأعمدة تلقائيًا لتناسب عرض الصفحة.
1. حدد حدود الخلايا والجدول.
1. يستخدم 'table.default_cell_padding' 'marginInfo () 'للتباعد المتسق داخل الخلايا.
1. أضف صفوفًا باستخدام 'table.rows.add () '، وأضف الخلايا باستخدام 'row.cells.add ()'.
1. احفظ ملف PDF.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def auto_fit(outfile: str) -> None:
    # Create new PDF document
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    table = ap.Table()

    page.paragraphs.add(table)

    table.column_widths = "50 50 50"
    table.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_WINDOW

    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)

    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1)

    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5

    table.default_cell_padding = margin

    row1 = table.rows.add()
    row1.cells.add("col1")
    row1.cells.add("col2")
    row1.cells.add("col3")
    row2 = table.rows.add()
    row2.cells.add("item1")
    row2.cells.add("item2")
    row2.cells.add("item3")

    document.save(outfile)
```

### إنشاء جداول PDF معقدة مع الخلايا المدمجة والأعمدة المتكررة

قم بإنشاء جدول متقدم في PDF باستخدام Python و Aspose.PDF. وهي تتضمن خلايا رأس مدمجة وخلفيات ملونة وأعمدة متكررة ومجموعة بيانات منظمة كبيرة. تم تكوين الجدول للتعامل مع الفواصل الرأسية والتخطيطات المعقدة للمستندات ذات نمط التقرير.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def add_table_hide_borders(outfile: str) -> None:
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Instantiate a table object that will be nested inside outerTable that will break inside the same page
    table = ap.Table()
    table.broken = ap.TableBroken.VERTICAL
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL)
    table.repeating_columns_count = 2
    page.paragraphs.add(table)

    # Add header Row
    row = table.rows.add()
    cell = row.cells.add("header 1")
    cell.col_span = 2
    cell.background_color = ap.Color.light_gray
    row.cells.add("header 3")

    cell2 = row.cells.add("header 4")
    cell2.col_span = 2
    cell2.background_color = ap.Color.light_blue
    row.cells.add("header 6")

    cell3 = row.cells.add("header 7")
    cell3.col_span = 2
    cell3.background_color = ap.Color.light_green
    cell4 = row.cells.add("header 9")

    cell4.col_span = 3
    cell4.background_color = ap.Color.light_coral
    row.cells.add("header 12")
    row.cells.add("header 13")
    row.cells.add("header 14")
    row.cells.add("header 15")
    row.cells.add("header 16")
    row.cells.add("header 17")

    row_counter = 0
    while row_counter < 3:
        # Create rows in the table and then cells in the rows
        row1 = table.rows.add()
        row1.cells.add("col " + str(row_counter) + ", 1")
        row1.cells.add("col " + str(row_counter) + ", 2")
        row1.cells.add("col " + str(row_counter) + ", 3")
        row1.cells.add("col " + str(row_counter) + ", 4")
        row1.cells.add("col " + str(row_counter) + ", 5")
        row1.cells.add("col " + str(row_counter) + ", 6")
        row1.cells.add("col " + str(row_counter) + ", 7")
        row1.cells.add("col " + str(row_counter) + ", 8")
        row1.cells.add("col " + str(row_counter) + ", 9")
        row1.cells.add("col " + str(row_counter) + ", 10")
        row1.cells.add("col " + str(row_counter) + ", 11")
        row1.cells.add("col " + str(row_counter) + ", 12")
        row1.cells.add("col " + str(row_counter) + ", 13")
        row1.cells.add("col " + str(row_counter) + ", 14")
        row1.cells.add("col " + str(row_counter) + ", 15")
        row1.cells.add("col " + str(row_counter) + ", 16")
        row1.cells.add("col " + str(row_counter) + ", 17")
        row_counter += 1

    document.save(outfile)
```

![الحدود والهوامش والحشو](set-border-style-margins-and-padding-of-table_1.png)

### زوايا طاولة التصميم

يوضح Aspose.PDF لـ Python عبر .NET كيفية تطبيق الزوايا الدائرية على الجدول وتخصيص نصف قطر الحدود.

1. قم بإنشاء مثيل جدول جديد.
1. قم بتهيئة الحدود لجميع الأطراف.
1. اضبط نصف قطر الزاوية.
1. قم بتطبيق نمط الزاوية المستديرة.
1. أضف الصفوف والخلايا.
1. أدخل الجدول في صفحة PDF مع «page.paragrahs.add (جدول)».
1. احفظ مستند PDF.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def create_table_with_round_corner(outfile: str) -> None:
    # Create new PDF document
    document = ap.Document()
    page = document.pages.add()

    # Create a table
    table = ap.Table()

    # Create a blank BorderInfo object
    b_info = ap.BorderInfo(ap.BorderSide.ALL)

    # Set the border a rounded border where radius of round is 15
    b_info.rounded_border_radius = 15

    # Set the table corner style as Round
    table.corner_style = ap.BorderCornerStyle.ROUND

    # Set the table border information
    table.border = b_info

    # Create a loop to add 10 rows
    for row_count in range(0, 10):
        # Add row to table
        row = table.rows.add()
        # Add table cells
        row.cells.add("Column (" + str(row_count) + ", 1)")
        row.cells.add("Column (" + str(row_count) + ", 2)")
        row.cells.add("Column (" + str(row_count) + ", 3)")

    # Add table object to first page of input document
    page.paragraphs.add(table)
    # Save updated document containing table object
    document.save(outfile)
```

## إضافة محتوى إلى الجداول

### استخدام أجزاء HTML في الخلايا

يوضح هذا المثال كيفية إدراج محتوى بتنسيق HTML في خلايا الجدول.

1. حدد حدود الجدول والخلايا.
1. إضافة محتوى HTML.
1. إضافة صفوف. تضيف الحلقة صفوفًا متعددة بمحتوى بتنسيق HTML في كل خلية.
1. أدخل الجدول في صفحة PDF مع «page.paragrahs.add (جدول)».
1. احفظ مستند PDF.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def add_html_fragments(outfile: str) -> None:
    # Instantiate Document object
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    table = ap.Table()

    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.light_gray)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.ALL, 0.5, ap.Color.light_gray
    )
    # Create a loop to add 10 rows
    row_count = 1
    while row_count < 10:
        # Add row to table
        row = table.rows.add()
        # Add table cells
        cell = row.cells.add()
        cell.paragraphs.add(
            ap.HtmlFragment(f"Column <strong>({row_count}, 1)</strong>")
        )

        cell = row.cells.add()
        cell.paragraphs.add(
            ap.HtmlFragment(f"Column <span style='color:red'>({row_count}, 2)</span>")
        )

        cell = row.cells.add()
        cell.paragraphs.add(
            ap.HtmlFragment(
                f"Column <span style='text-decoration: underline'>({row_count}, 3)</span>"
            )
        )
        row_count += 1

    # Add table object to first page of input document
    page.paragraphs.add(table)
    # Save updated document containing table object
    document.save(outfile)
```

### استخدام أجزاء LaTeX في الخلايا

يوضح هذا المثال كيفية إدراج محتوى بتنسيق Latex في خلايا الجدول للتعبيرات الرياضية أو النمطية.

1. حدد حدود الجدول والخلايا.
1. أضف محتوى LaTeX.
1. إضافة صفوف. تضيف الحلقة صفوفًا متعددة بمحتوى بتنسيق Latex في كل خلية.
1. أدخل الجدول في صفحة PDF مع «page.paragrahs.add (جدول)».
1. احفظ مستند PDF.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def add_latex_fragments(outfile: str) -> None:
    # Instantiate Document object
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    table = ap.Table()

    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.light_gray)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.ALL, 0.5, ap.Color.light_gray
    )
    # Create a loop to add 10 rows
    row_count = 1
    while row_count < 10:
        # Add row to table
        row = table.rows.add()
        # Add table cells
        cell = row.cells.add()
        cell.paragraphs.add(ap.LatexFragment(f"Column $\\mathbf{{({row_count}, 1)}}$"))

        cell = row.cells.add()
        cell.paragraphs.add(
            ap.LatexFragment(f"Column $\\textcolor{{red}}{{({row_count}, 2)}}$")
        )

        cell = row.cells.add()
        cell.paragraphs.add(
            ap.LatexFragment(f"Column $\\underline{{({row_count}, 3)}}$")
        )
        row_count += 1

    # Add table object to first page of input document
    page.paragraphs.add(table)
    # Save updated document containing table object
    document.save(outfile)
```

## ميزات الجدول المتقدمة

### إدراج فواصل الصفحات التلقائية في جدول PDF

قم بإنشاء جدول كبير في PDF باستخدام Python و Aspose.PDF، مع فواصل صفحات تلقائية بعد عدد محدد من الصفوف. يقوم بإنشاء جدول متعدد الصفوف وتطبيق الحدود وفرض الصفوف المحددة على البدء في صفحة جديدة للتحكم بشكل أفضل في التخطيط.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def insert_page_break(outfile: str) -> None:
    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Create table instance
    table = ap.Table()

    # Set border style for table
    table.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)

    # Set default border style for table with border color as Red
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)

    # Specify table columns width
    table.column_widths = "100 100"

    # Create a loop to add 200 rows for table
    for counter in range(201):
        row = ap.Row()
        table.rows.add(row)

        cell1 = ap.Cell()
        cell1.paragraphs.add(ap.text.TextFragment(f"Cell {counter}, 0"))
        row.cells.add(cell1)

        cell2 = ap.Cell()
        cell2.paragraphs.add(ap.text.TextFragment(f"Cell {counter}, 1"))
        row.cells.add(cell2)

        # When 10 rows are added, render new row in new page
        if counter % 10 == 0 and counter != 0:
            row.is_in_new_page = True

    # Add table to paragraphs collection of PDF file
    page.paragraphs.add(table)

    # Save PDF document
    document.save(outfile)
```

### تكرار صفوف رأس الصفحة على صفحات متعددة

يوضح هذا المثال كيفية إنشاء جدول يمتد على صفحات متعددة مع إبقاء صفوف العناوين مرئية في كل صفحة.

1. قم بتهيئة الجدول.
1. كرر صفوف الرأس بما في ذلك الخط والحجم واللون.
1. قم بتعيين عرض الأعمدة وتطبيق الحدود على الجدول.
1. إضافة صفوف رأس الصفحة.
1. أضف العديد من صفوف البيانات لفرض الجدول عبر صفحات متعددة.
1. أدخل الجدول في صفحة PDF مع «page.paragrahs.add (جدول)».
1. احفظ مستند PDF.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def add_repeating_rows(outfile: str) -> None:
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Instantiate a table object
    table = ap.Table()

    # Set the table to break across pages
    table.broken = ap.TableBroken.VERTICAL

    # Set number of repeating header rows
    table.repeating_rows_count = 2

    text_state = ap.text.TextState()
    text_state.font_size = 12
    text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_state.foreground_color = ap.Color.red
    table.repeating_rows_style = text_state

    # Set column widths
    table.column_widths = "100 100 100"

    # Set borders
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.black)
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1, ap.Color.black)

    # Add header rows that will repeat on each page
    header_row1 = table.rows.add()
    header_row1.cells.add("Header 1-1")
    header_row1.cells.add("Header 1-2")
    header_row1.cells.add("Header 1-3")

    # Set background color for header rows
    for cell in header_row1.cells:
        cell.background_color = ap.Color.light_gray

    header_row2 = table.rows.add()
    header_row2.cells.add("Header 2-1")
    header_row2.cells.add("Header 2-2")
    header_row2.cells.add("Header 2-3")

    for cell in header_row2.cells:
        cell.background_color = ap.Color.light_blue

    # Add many data rows to force table across multiple pages
    for i in range(1, 101):
        row = table.rows.add()
        row.cells.add(f"Data {i}-1")
        row.cells.add(f"Data {i}-2")
        row.cells.add(f"Data {i}-3")

    # Add table to page
    page.paragraphs.add(table)

    # Save document
    document.save(outfile)
```

### الأعمدة المتكررة

تقوم الدالة «add_repeating_columns» بإنشاء مستند PDF بجدول يحتوي على أعمدة متكررة. يقوم بإعداد جدول محدد وإضافة الرؤوس وملء صفوف البيانات وحفظ ملف PDF الذي تم إنشاؤه في الموقع المحدد. سيؤدي تعيين هذه الخاصية إلى تقسيم الجدول إلى الصفحة التالية حسب العمود وتكرار عدد الأعمدة المحدد في بداية الصفحة التالية.

1. يقوم بتهيئة مستند PDF جديد.
1. يضيف صفحة بأبعاد مخصصة.
1. تعيين نمط حدود الجدول.
1. قم بتهيئة الجدول.
1. أضف جدولًا إلى صفحة PDF.
1. إضافة صف رأس الصفحة.
1. إضافة صفوف بيانات.
1. احفظ مستند PDF.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def add_repeating_columns(outfile: str) -> None:
    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()
    page.set_page_size(ap.PageSize.a5.height, ap.PageSize.a5.width)

    # Define border
    border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.light_gray)

    # Create table
    table = ap.Table()
    table.broken = ap.TableBroken.VERTICAL_IN_SAME_PAGE
    table.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_CONTENT
    table.repeating_columns_count = 5
    table.border = border
    table.default_cell_border = border

    # Add table to page
    page.paragraphs.add(table)

    # Add header row
    row = table.rows.add()
    for i in range(1, 6):
        cell = row.cells.add(f"header {i}")
        cell.background_color = ap.Color.light_gray

    for i in range(6, 18):
        row.cells.add(f"header {i}")

    # Add data rows
    for row_counter in range(1, 6):
        row = table.rows.add()
        for i in range(1, 6):
            cell = row.cells.add(f"cell {row_counter},{i}")
            cell.background_color = ap.Color.light_gray
        for i in range(6, 18):
            row.cells.add(f"cell {row_counter},{i}")

    # Save PDF document
    document.save(outfile)
```

### قم بإنشاء جدول PDF باستخدام خلايا نصية مستديرة

قم بإنشاء جدول في PDF باستخدام Python و Aspose.PDF مع تدوير النص بزوايا مختلفة داخل كل خلية. وهي مفيدة للرؤوس الرأسية والتخطيطات الإبداعية والجداول المدمجة وتنسيق التقارير المخصصة.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def rotated_text_table(outfile: str) -> None:
    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Initializes a new instance of the Table
    table = ap.Table()
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, Color.black)
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, Color.black)

    # Add 1st row to table
    row1 = table.rows.add()
    row1.min_row_height = 200

    for cell_count in range(4):
        # Add table cells
        cell = row1.cells.add()

        tf = ap.text.TextFragment(f"Cell 1 {cell_count - 1}")
        tf.text_state.rotation = 90 * cell_count
        tf.horizontal_alignment = HorizontalAlignment.CENTER

        cell.paragraphs.add(tf)

    # Add table object to first page of input document
    page.paragraphs.add(table)

    # Save result
    document.save(outfile)
```

## موضوعات الجدول ذات الصلة

- [العمل مع الجداول في PDF باستخدام Python](/pdf/ar/python-net/working-with-tables/)
- [استخراج الجداول من مستندات PDF](/pdf/ar/python-net/extracting-table/)
- [دمج جداول PDF مع مصادر البيانات](/pdf/ar/python-net/integrate-table/)
- [معالجة الجداول في ملفات PDF الموجودة](/pdf/ar/python-net/manipulating-tables/)
