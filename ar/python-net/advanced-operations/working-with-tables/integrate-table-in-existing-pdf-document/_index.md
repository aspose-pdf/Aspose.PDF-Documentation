---
title: دمج جداول PDF مع مصادر البيانات في Python
linktitle: جدول الدمج
type: docs
weight: 30
url: /ar/python-net/integrate-table/
description: تعرف على كيفية دمج جداول PDF مع مصادر البيانات مثل قواعد البيانات والباندا DataFrames في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: دمج جداول PDF مع قواعد البيانات وإطارات البيانات باستخدام Python
Abstract: توضح هذه المقالة كيفية دمج جداول PDF مع مصادر البيانات الخارجية باستخدام Aspose.PDF لـ Python عبر .NET. تعرف على كيفية إنشاء جداول PDF من الباندا DataFrames والمصادر المهيكلة الأخرى، وإدراجها في المستندات، والتحكم في تدفق الجدول عند العرض عبر صفحات PDF في Python.
---

## قم بإنشاء ملف PDF من داتافريم

ال `create_pdf_from_dataframe` تقوم الوظيفة بإنشاء ملف PDF جديد وإدراج جدول تم إنشاؤه من إطار بيانات الباندا. يُعد هذا الأسلوب مفيدًا للإبلاغ عن عمليات سير العمل حيث توجد بياناتك بالفعل في شكل جدول.

تقوم الوظيفة بالخطوات التالية:

1. قم بإنشاء مستند PDF فارغ باستخدام `ap.Document()`.
1. أضف صفحة إلى المستند.
1. قم بتحويل DataFrame إلى جدول Aspose.PDF عن طريق الاتصال `create_table_from_dataframe(df, max_rows)`.
1. أضف الجدول إلى الصفحة باستخدام `page.paragraphs.add(table)`.
1. احفظ ملف PDF إلى مسار الإخراج.

```python
from os import path
import sys

import pandas as pd
import aspose.pdf as ap
from config import set_license, initialize_data_dir

def create_pdf_from_dataframe(
    outfile: str, df: pd.DataFrame, max_rows: int = 20
) -> None:
    # Create new PDF document
    document = ap.Document()
    page = document.pages.add()

    table = create_table_from_dataframe(df, max_rows)

    # Add table object to first page of input document
    page.paragraphs.add(table)
    document.save(outfile)
```

## إنشاء جدول من داتافريم

ال `create_table_from_dataframe` تقوم الدالة بتحويل داتافريم إلى Aspose.PDF `Table` كائن يمكنك إضافته إلى أي صفحة.

وهي تقوم بما يلي:

1. قم بإنشاء ملف فارغ `ap.Table()` مثال.
1. قم بتعيين حدود الجدول والخلايا للتنسيق المتسق.
1. أضف صف رأس باستخدام أسماء أعمدة DataFrame.
1. إضافة صفوف بيانات من `df.head(max_rows)`.
1. قم بإرجاع كائن الجدول المأهول.

```python
from os import path
import sys

import pandas as pd
import aspose.pdf as ap
from config import set_license, initialize_data_dir

def create_table_from_dataframe(df: pd.DataFrame, max_rows: int = 20) -> ap.Table:
    """Create an Aspose.PDF table from a pandas DataFrame."""
    # Initializes a new instance of the Table
    table = ap.Table()
    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1, ap.Color.light_gray)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.BOTTOM, 1, ap.Color.light_gray
    )

    # Add header row with column names
    header_row = table.rows.add()
    header_row.is_row_broken = False  # Prevent header row from being split across pages
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

## موضوعات الجدول ذات الصلة

- [العمل مع الجداول في PDF باستخدام Python](/pdf/ar/python-net/working-with-tables/)
- [إضافة جداول إلى PDF باستخدام Python](/pdf/ar/python-net/adding-tables/)
- [استخراج الجداول من مستندات PDF](/pdf/ar/python-net/extracting-table/)
- [معالجة الجداول في ملفات PDF الموجودة](/pdf/ar/python-net/manipulating-tables/)