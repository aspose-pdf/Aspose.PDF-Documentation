---
title: دمج الجدول مع مصادر البيانات PDF
linktitle: دمج الجدول
type: docs
weight: 30
url: /ar/python-net/integrate-table/
description: توضح هذه المقالة كيفية دمج جداول PDF. دمج الجدول مع قاعدة البيانات وتحديد ما إذا كان الجدول سيفصل في الصفحة الحالية.
lastmod: "2025-09-17"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## إنشاء PDF من DataFrame

الدالة 'create_pdf_from_dataframe' تأخذ DataFrame وتحوّلها إلى جدول داخل PDF جديد. تنشئ مستند PDF جديد، تضيف صفحة، تولد جدولًا من DataFrame (باستخدام طريقة مساعدة)، وتحفظ النتيجة في مسار الملف المحدد. وليس ذلك فحسب، بل هو سهل جدًا.

1. يقوم بتهيئة مستند PDF فارغ باستخدام 'ap.Document()'.
1. الدالة 'self.create_table_from_dataframe(df, max_rows)' تحول DataFrame إلى كائن جدول Aspose.PDF.
1. إدراج الجدول في صفحة PDF. يضيف الجدول المُولد إلى محتوى الصفحة الأولى (page.paragraphs.add(table)).
1. حفظ مستند PDF.

```python

from os import path
import pandas as pd
import aspose.pdf as ap

# Example DataFrame
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Paris", "London"]
})

max_rows = 3  # Number of rows to include in the table
path_outfile = "output.pdf"

# Define the function to create a table from DataFrame
def create_table_from_dataframe(df, max_rows):
    table = ap.Table()
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1, ap.Color.light_gray)
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.BOTTOM, 1, ap.Color.light_gray
    )
    # Add header row with column names
    header_row = table.rows.add()
    header_row.is_row_broken = False
    for column_name in df.columns:
        cell = header_row.cells.add(str(column_name))
        cell.background_color = ap.Color.light_gray
    # Add data rows
    for row_data in df.head(max_rows).itertuples(index=False):
        row = table.rows.add()
        for value in row_data:
            row.cells.add(str(value))
    return table

# Load source PDF document
document = ap.Document()
page = document.pages.add()

table = create_table_from_dataframe(df, max_rows)

# Add table object to first page of input document
page.paragraphs.add(table)
document.save(path_outfile)
```

## إنشاء جدول من DataFrame

يقوم هذا الكود بتحويل DataFrame إلى كائن جدول Aspose.PDF. يقوم بإعداد حدود الجدول، يضيف صفًا رأسياً بأسماء الأعمدة، ويملأ الجدول بأول max_rows صفًا من DataFrame. يمكن بعد ذلك إضافة الجدول الناتج إلى مستند PDF.

1. ينشئ كائن 'ap.Table()' فارغ.
1. ضبط حد الجدول.
1. ضبط حد الخلية الافتراضي.
1. إضافة صف الرأس.
1. إضافة صفوف البيانات.
1. إرجاع الجدول.

```python

    from os import path
    import pandas as pd
    import aspose.pdf as ap

    
    table = ap.Table()  # Initializes a new instance of the Table
    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1, ap.Color.light_gray)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.BOTTOM, 1, ap.Color.light_gray
    )

    # Add header row with column names
    header_row = table.rows.add()
    header_row.is_row_broken = (
        False  # Prevent header row from being split across pages
    )
    for column_name in df.columns:
        cell = header_row.cells.add(str(column_name))
        cell.background_color = ap.Color.light_gray

    # Add data rows
    for row_data in df.head(max_rows).itertuples(index=False):
        row = table.rows.add()
        for value in row_data:
            row.cells.add(str(value))

    return table
```
